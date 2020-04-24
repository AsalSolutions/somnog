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
    photo = db.Column(db.String(100), nullable=True)
    socialAccount = db.Column(db.String(200), nullable=True)

    def __init__(self, firstName, lastName, email,
                 phone, description, companyName, jobTitle, photo, socialAccount):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.description = description
        self.companyName = companyName
        self.jobTitle = jobTitle
        self.photo = photo
        self.socialAccount = socialAccount

    @classmethod
    def save(cls, self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def update(cls, self):
        db.session.commit()


class SpeakerSchema(mm.Schema):
    class Meta:
        fields = ('_id', 'firstName', 'lastName', 'email', 'phone',
                  'description', 'companyName', 'jobTitle', 'Photo', 'socialAccount')


# Create DB
db.create_all()
# # Insert Spearker
# speaker_1 = Speaker(firstName="Hassan", lastName="Abdisamad",
#                     email="hassan@example.com", jobTitle="Machine Developer")
# db.session.add(speaker_1)
# db.session.commit()

# speaker = Speaker.query.all()
