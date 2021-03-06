"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact 2',
        year=datetime.now().year,
        message='Your contact page.'
    )
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/ti_webhook_cp', methods = ['GET','POST'])
def ti_webhook_cp():
    """Renders the webhook receiver for course purchased page."""
    if request.method == 'POST':
        ti_webhook2 = request.get_json(force=True)
    else:
        ti_webhook2 = "No webhook received"
    return render_template(
        'TI_webhook_cp.html',
        title='Webhook',
        year=datetime.now().year,
        message='Your application description page.',
        ti_webhook = ti_webhook2
    )

