from datetime import datetime
from db import db, mm

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workshopTitle = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    startDate = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    endDate = db.Column(db.DateTime, nullable=True,default=datetime.utcnow())
    course_image = db.Column(db.String(20), nullable=False,
                     default="default.png")
    location = db.Column(db.String(80))
    lecturer_id = db.Column(db.Integer, db.ForeignKey('speaker._id'),
        nullable=False)

    def __repr__(self):
        return f"Workshop: {self.workshopTitle} {self.startDate} {self.endDate} {self.course_image}"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class WorkshopModelSchema(mm.Schema):
    class Meta:
        fields = ('id', 'workshopTitle', 'description', 'startDate', 'endDate',
                  'course_image', 'location', 'lecturer_id')


# Create DB
# db.create_all()

