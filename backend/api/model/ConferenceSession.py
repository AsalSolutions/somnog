import datetime
from db import db, mm


class ConferenceSession(db.Model):
    __tablename__ = "conference_session"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    startTime = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    endTime = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    photo = db.Column(db.String(100), nullable=True,default="default.png")
    speaker_id = db.Column(db.Integer, db.ForeignKey('speakers.id'),
        nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('speakers.id'),
        nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('speakers.id'),
        nullable=False)

    def __repr__(self):
        return f"ConferenceSession {self.title}" 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class ConferenceSessionSchema(mm.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'startTime', 'endTime',
                  'photo', 'speaker_id', 'tag_id', 'location_id')



