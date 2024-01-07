from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.schema import CheckConstraint

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("user")}:{os.getenv("password")}@db:5432/{os.getenv("db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cake(db.Model):
    __tablename__ = 'cakes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    yum_factor = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('yum_factor >= 1 AND yum_factor <= 5', name='check_yum_factor'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'comment': self.comment,
            'image_url': self.image_url,
            'yum_factor': self.yum_factor
        }
