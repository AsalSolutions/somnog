from db import db, mm
# **Speaker Schema:**
# `(id,firstname,lastname,photo,description, company,job_title,description,social_acount)`


class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    company_name = db.Column(db.String(140), nullable=True)
    job_title = db.Column(db.String(120), nullable=True)
    speaker_photo = db.Column(
        db.String(100), default="default.png")
    website = db.Column(db.String(200))
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
        fields = ('id', 'first_name', 'last_name', 'email', 'phone',
                  'description', 'company_name', 'job_title', 'speaker_Photo', 'website')
