from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)

# Production-ready configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///myjournal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Fix for Render's PostgreSQL URL format (if using PostgreSQL)
if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgres://'):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgres://', 'postgresql://', 1)

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    entries = db.relationship('JournalEntry', backref='author', lazy=True)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists!', 'error')
        return redirect(url_for('home'))
    
    # Create new user
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(name=name, email=email, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    flash('Account created successfully! Please login.', 'success')
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Invalid email or password!', 'error')
        return redirect(url_for('home'))
    
    session['user_id'] = user.id
    session['user_name'] = user.name
    flash(f'Welcome back, {user.name}!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('home'))
    
    user = User.query.get(session['user_id'])
    entries = JournalEntry.query.filter_by(user_id=user.id).order_by(JournalEntry.created_at.desc()).all()
    return render_template('dashboard.html', user=user, entries=entries)

@app.route('/create-entry', methods=['GET', 'POST'])
def create_entry():
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        new_entry = JournalEntry(title=title, content=content, user_id=session['user_id'])
        db.session.add(new_entry)
        db.session.commit()
        
        flash('Journal entry created successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_entry.html')

@app.route('/entry/<int:entry_id>')
def view_entry(entry_id):
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('home'))
    
    entry = JournalEntry.query.get_or_404(entry_id)
    
    # Check if entry belongs to current user
    if entry.user_id != session['user_id']:
        flash('Access denied!', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('view_entry.html', entry=entry)

@app.route('/edit-entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('home'))
    
    entry = JournalEntry.query.get_or_404(entry_id)
    
    # Check if entry belongs to current user
    if entry.user_id != session['user_id']:
        flash('Access denied!', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        entry.title = request.form.get('title')
        entry.content = request.form.get('content')
        db.session.commit()
        
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('view_entry', entry_id=entry.id))
    
    return render_template('edit_entry.html', entry=entry)

@app.route('/delete-entry/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    if 'user_id' not in session:
        flash('Please login first!', 'error')
        return redirect(url_for('home'))
    
    entry = JournalEntry.query.get_or_404(entry_id)
    
    # Check if entry belongs to current user
    if entry.user_id != session['user_id']:
        flash('Access denied!', 'error')
        return redirect(url_for('dashboard'))
    
    db.session.delete(entry)
    db.session.commit()
    
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Use environment variables for port (required for deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)