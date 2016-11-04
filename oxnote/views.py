from flask import jsonify
from oxnote import app, db
from oxnote.models import Page, Tag

@app.route('/')
def index():
    """
    Lists all pages in the wiki
    """
    pages = Page.query.all()
    return jsonify(pages)
