from flask import (Blueprint, render_template)

main_page = Blueprint('main_page', 'main_page')


@main_page.route("/", methods=['GET'])
def index():

    return render_template('index.html')


'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

This route located in ../resources/tweet.py
'''
