from woxwiki import db

page_tags = db.Table('page_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)


page_categories = db.Table('page_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True) # ADD: lowercase/slug checking
    content = db.Column(db.Text)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    tags = db.relationship('Tag', secondary=page_tags,
        backref=db.backref('pages', lazy='dynamic'))
    categories = db.relationship('Category', secondary=page_categories,
        backref=db.backref('pages', lazy='dynamic'))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date_created': self.date_created,
            'date_modified': self.date_modified,
            'tags': self._serialize_tags,
            'categories': self._serialize_categories,
        }

    @property
    def _serialize_tags(self):
        tag_list = [tag.serialized for tag in self.tags]
        tag_list.sort(key=lambda x: x['name'])
        return tag_list

    @property
    def _serialize_categories(self):
        category_list = [category.serialized for category in self.categories]
        category_list.sort(key=lambda x: x['name'])
        return category_list


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]))

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent': self._serialize_parent
        }

    @property
    def _serialize_parent(self):
        return self.parent.serialized
