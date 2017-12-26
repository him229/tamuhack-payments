# coding: utf-8
"""
TAMUhack Stripe Payments
"""
import os
import stripe
from flask import Flask, request, session
from flask import render_template, Response, redirect, send_from_directory

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret')

stripe_pub_key = os.environ['STRIPE_PUB_KEY']
stripe.api_key = os.environ['STRIPE_SECRET_KEY']


@app.route('/')
def index():
    amount = request.args.get('amount', 0)
    rep_name = request.args.get('rep_name', '')
    company_name = request.args.get('company_name', '')
    try:
        amount = int(amount)
    except:
        amount = 0

    session['rep_name'] = rep_name
    session['company_name'] = company_name
    session['amount'] = amount

    return render_template(
        'index.html',
        key=stripe_pub_key,
        amount=amount,
        rep_name=rep_name,
        company_name=company_name,
        stripe_pub_key=stripe_pub_key
    )


@app.route('/charge', methods=['GET', 'POST'])
def charge():
    if request.method == 'GET':
        return redirect('/')
    email = request.form['stripeEmail']
    token = request.form['stripeToken']
    reason = "%s - %s" % (session['company_name'], session['rep_name'])
    amount = int(session['amount']) * 100
    stripe.Charge.create(
        receipt_email=email,
        source=token,
        currency='usd',
        amount=amount,
        description=reason,
    )
    return render_template('success.html')


@app.route('/robots.txt')
def robots():
    text = 'User-Agent: *\nDisallow: /\n'
    return Response(text, mimetype='text/plain')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        app.root_path, 'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )