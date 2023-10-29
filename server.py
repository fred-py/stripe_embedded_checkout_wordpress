#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, redirect, request

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51O1iMbL0FB5xAf6Hkyy6S5iT8Fj6IaaY0IeT9EXAfYMZfpxoRvSvV2Qcm4fdSYzskRrL0pmHhJVP45IIVVEplIjZ00bBPePPOH'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

#YOUR_DOMAIN = 'http://localhost:4242'
YOUR_DOMAIN = 'https://unitedpropertyservices.au/wheelie-bin-clean/'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            ui_mode='embedded',
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1O3BbfL0FB5xAf6HRP3sV5H8',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            return_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)

    return jsonify(clientSecret=session.client_secret)


@app.route('/session-status', methods=['GET'])
def session_status():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

    return jsonify(status=session.status, customer_email=session.customer_details.email)


if __name__ == '__main__':
    app.run(debug=True, port=4242)