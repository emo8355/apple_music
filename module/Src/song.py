from .. import db


class Song(db.Model):
    __tablename__ = "song"
    __id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(999), unique=False, nullable=False)
    img = db.Column(db.String(
        999), default="https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/512/unknown-icon.png", unique=False, nullable=True)
    name = db.Column(db.String(80), default="unknown",
                     unique=False, nullable=True)
    genre = db.Column(db.String(80), default="unknown",
                      unique=False, nullable=True)
    author_id = db.Column(db.String(80), default="unknown",
                          unique=False, nullable=True)
    author = db.Column(db.String(80), default="unknown",
                       unique=False, nullable=True)
    album = db.Column(db.String(80), default="n/a")
    duration = db.Column(db.String(25), default="0:0",
                         unique=False, nullable=True)
    lyrics = db.Column(db.String(888888), default="unknown",
                       unique=False, nullable=True)
    year = db.Column(db.Integer, default=9999, unique=False, nullable=True)
    like = db.Column(db.Integer, default=0, unique=False, nullable=True)

    # def __repr__(self):
    #     return '<song %r>' % self.__id
