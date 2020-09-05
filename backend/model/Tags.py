from db import db, mm

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True nullable=False)
    
    

    def __repr__(self):
        return f"Tags {self.title}"
       
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
        fields = ('id', 'title')



# db.create_all()

