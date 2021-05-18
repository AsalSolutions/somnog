from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime
from db import db, mm


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(180), unique=True,
                      nullable=False)
    username = db.Column(db.String(80), unique=True,
                         nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
                        nullable=False)
    role = db.relationship('Role',
                           backref=db.backref('users', lazy=True))
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

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
    # Get user by email     
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_hash(hashed, password):
        return check_password_hash(hashed, password)

    def __repr__(self):
        return(f"{__class__.__name__} {self.username}")


class UserSchema(mm.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'role.name')


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,
                     nullable=False)
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return(f"{__class__.__name__} {self.name}")


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
