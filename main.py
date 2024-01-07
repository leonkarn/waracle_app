from flask import request, jsonify
from swagger import swaggerui_blueprint, SWAGGER_URL
from models import db, app, Cake

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/cakes', methods=['GET', 'POST'])
def total_cakes():
    if request.method == 'GET':
        cakes = Cake.query.all()
        return jsonify([cake.to_dict() for cake in cakes])

    elif request.method == 'POST':
        data = request.json
        cake = Cake(name=data['name'], comment=data['comment'], image_url=data['image_url'],
                    yum_factor=data['yum_factor'])
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
