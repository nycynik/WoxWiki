from flask import jsonify
from oxnote import app, db
from oxnote.models import Page, Tag
from flask import redirect, url_for, flash, request, render_template

@app.route('/')
def index():
    """
    Lists all pages in the wiki
    """
    pages = Page.query.all()
    jt = lambda x: [k.name for k in x]
    return jsonify([(x.title, jt(x.tags)) for x in pages])

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Adds a new page
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag_list = request.form.getlist('tags[]')
        existing_tags = Tag.query.all()

        page = Page(title=title, content=content)
        db.session.flush([page])
        for tag in tag_list:
            for t in existing_tags:
                if tag == t.name:
                    page.tags.append(t)
            else:
                t = Tag(name=tag)
                db.session.add(t)
                page.tags.append(t)

        db.session.add(page)
        db.session.commit()
        flash('Page sucessfully added', 'success')
        return redirect(url_for('index'))

    # Display the form
    return render_template('add.html')

