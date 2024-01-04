from flask import Flask, request, jsonify
# from models import db, Cake
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cake(db.Model):
    __tablename__ = 'cakes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    yum_factor = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'comment': self.comment,
            'image_url': self.image_url,
            'yum_factor': self.yum_factor
        }


@app.route('/', methods=['GET'])
def main_route():
    return "Hello world"


@app.route('/cakes', methods=['GET'])
def list_cakes():
    cakes = Cake.query.all()
    return jsonify([cake.to_dict() for cake in cakes])


@app.route('/cakes', methods=['POST'])
def add_cake():
    data = request.json
    cake = Cake(name=data['name'], comment=data['comment'], image_url=data['image_url'], yum_factor=data['yum_factor'])
    db.session.add(cake)
    db.session.commit()
    return jsonify(cake.to_dict()), 201


@app.route('/cakes/<int:id>', methods=['DELETE'])
def delete_cake(id):
    cake = Cake.query.get_or_404(id)
    db.session.delete(cake)
    db.session.commit()
    return jsonify({'message': 'Cake deleted'}), 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, host="0.0.0.0")