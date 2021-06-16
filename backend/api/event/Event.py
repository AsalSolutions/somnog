from datetime import datetime
from api import db, mm

# id :1
# name : 'SOMNOG 5 Event'
# startDate : 15 July
# EndDate : 20 July
# workshopTracks_id :
# ConferenceId :
# location:id
# price : 40


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), unique=True,
                     nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    # address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
    #                        nullable=False)
    # address = db.relationship('Address',
    #                           backref=db.backref('events', lazy=True))

    # workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'),
    #                         nullable=False)
    # workshop = db.relationship('Workshop',
    #                            backref=db.backref('event', lazy=True))
    # conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'),
    #                           nullable=False)
    # conference = db.relationship('Conference',
    #                              backref=db.backref('event', lazy=True))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #! Delete All
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': f'{num_rows_deleted} row(s) deleted'}
        except:
            return {'message': 'Something went wrong'}

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_event_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def __repr__(self):
        return(f"{__class__.__name__} {self.name}")


class EventSchema(mm.Schema):
    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date',
                  'price', 'created_date', 'updated_date')
