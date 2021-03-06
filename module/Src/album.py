from .. import db
from .album_songs import Album_Songs


class Album(db.Model):
    __tablename__ = "album"
    __id = db.Column(db.Integer, primary_key=True)
    cover_img = db.Column(db.String(
        999), default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Vinyl_record.svg/1200px-Vinyl_record.svg.png", unique=False, nullable=True)
    name = db.Column(db.String(80), default="unknown",
                     unique=False, nullable=True)
    author = db.Column(db.String(80), default="unknown",
                       unique=False, nullable=True)
    genre = db.Column(db.String(80), default="unknown",
                      unique=False, nullable=True)
    year = db.Column(db.String(20), default="dd mm yyyy",
                     unique=False, nullable=True)
    like = db.Column(db.Integer, default=0, unique=False, nullable=True)
    # song can have many albums and albums can have many songs
    Song_list = db.relationship(
        "Song", secondary=Album_Songs, backref=db.backref("song_list", lazy='dynamic'))

    # def __repr__(self):
    #     return '<Album {}>'.format(f"Album id: {self.id} Album name: {self.name}")
