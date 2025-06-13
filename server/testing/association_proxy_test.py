from app import app, db
from server.models import Customer, Item, Review


class TestAssociationProxy:
    def setup_method(self):
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_has_association_proxy(self):
        with app.app_context():
            c = Customer()
            i = Item()
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            assert r in c.reviews
