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

@app.route('/ti_webhook_cp', methods = ['POST'])
def ti_webhook_cp():
    """Renders the webhook receiver for course purchased page."""
    return render_template(
        'TI_webhook_cp.html',
        title='Webhook',
        year=datetime.now().year,
        message='Your application description page.'
        ti_webhook = request.get_json()
    )

