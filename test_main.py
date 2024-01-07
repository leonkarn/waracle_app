import unittest
from main import app, db
from models import Cake


class CakeAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            cake1 = Cake(name='Chocolate Cake', comment='Rich and delicious',
                         image_url='http://cakes.com/chocolate.jpg', yum_factor=5)
            cake2 = Cake(name='Vanilla Cake', comment='Light and fluffy', image_url='http://cakes.com/vanilla.jpg',
                         yum_factor=4)
            db.session.add(cake1)
            db.session.add(cake2)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_cakes(self):
        response = self.app.get('/cakes')
        self.assertEqual(response.status_code, 200)

    def test_add_cake(self):
        cake_data = {
            'name': 'Test Cake',
            'comment': 'A test cake',
            'image_url': 'http://example.com/test_cake.jpg',
            'yum_factor': 4
        }
        response = self.app.post('/cakes', json=cake_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Cake', str(response.data))

    def test_delete_cake(self):
        cake = Cake(name='Delete Me', comment='Delete this cake', image_url='http://example.com/delete_cake.jpg',
                    yum_factor=3)
        db.session.add(cake)
        db.session.commit()

        response = self.app.delete(f'/cakes/{cake.id}')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/cakes')
        self.assertNotIn('Delete Me', str(response.data))
