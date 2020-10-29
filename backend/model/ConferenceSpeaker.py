from datetime import datetime
from db import db, mm


class ConferenceSpeaker(db.Model):
    __tablename__ = "speakers"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    instituion = db.Column(db.String(140), nullable=True)
    title = db.Column(db.String(120), nullable=True)
    photo = db.Column(db.String(100), nullable=True,default="default.png")
    website = db.Column(db.String(200), nullable=True)
    # This should later be moved on its own model for db normalization
    topic = db.Column(db.String(140), nullable=True)
    authors = db.Column(db.String(140), nullable=True)
    summary = db.Column(db.String(140), nullable=True)
    submittedDate= db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    session = db.relationship('ConferenceSession',
        backref=db.backref('Speaker', lazy=True))

    def __repr__(self):
        return f"ConferenceSession {self.firstName} {self.lastName}" 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class ConferenceSpeakerSchema(mm.Schema):
    class Meta:
        fields = ('id', 'firstName', 'lastName', 'email', 'phone',
                  'description', 'institution', 'title', 'photo', 'website')



