from oxnote import db

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True) # ADD: lowercase/slug checking
    content = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

    @property
    def seralized(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self._serialize_tags
        }

    @property
    def _serialize_tags(self):
        tag_list = [tag.seralized for tag in self.tags]
        tag_list.sort(key=lambda x: x['name'])
        return tag_list


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)

    @property
    def seralized(self):
        return {
            'id': self.id,
            'name': self.name
        }
