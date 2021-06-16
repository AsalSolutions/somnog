from db import db, mm


class WorkshopLecturer(db.Model):
    __tablename__ = "lecturers"
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
    isLead = db.Column(db.Boolean, default=False, nullable=False)
    trackName = db.relationship('Workshop',
        backref=db.backref('lecturer', lazy=True))

    def __repr__(self):
        return f"WorkshopLecturer {self.firstName} {self.lastName}" 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class WorkshopLecturerSchema(mm.Schema):
    class Meta:
        fields = ('id', 'firstName', 'lastName', 'email', 'phone',
                  'description', 'institution', 'title', 'photo', 'website')



