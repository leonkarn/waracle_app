from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    yumFactor = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'comment': self.comment,
            'imageUrl': self.imageUrl,
            'yumFactor': self.yumFactor
        }
