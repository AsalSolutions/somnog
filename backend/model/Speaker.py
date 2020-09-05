from db import db, mm
# **Speaker Schema:**
# `(id,firstname,lastname,photo,description, company,job_title,description,social_acount)`


class Speaker(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    companyName = db.Column(db.String(140), nullable=True)
    jobTitle = db.Column(db.String(120), nullable=True)
    speaker_photo = db.Column(db.String(100), nullable=True,default="default.png")
    socialAccount = db.Column(db.String(200), nullable=True)
    workshop = db.relationship('Workshop',
        backref=db.backref('workshop', lazy=True))

    def __repr__(self):
        return f"Speaker {self.firstName} {self.lastName}" 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class SpeakerModelSchema(mm.Schema):
    class Meta:
        fields = ('_id', 'firstName', 'lastName', 'email', 'phone',
                  'description', 'companyName', 'jobTitle', 'Photo', 'socialAccount')


# Create DB
# db.create_all()
# # Insert Spearker
# speaker_1 = Speaker(firstName="Hassan", lastName="Abdisamad",
#                     email="hassan@example.com", jobTitle="Machine Developer")
# db.session.add(speaker_1)
# db.session.commit()

# speaker = Speaker.query.all()
