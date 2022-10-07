"""  Models class file for Brand, Discount_Code, User and User_Discount_Code """


from ast import Str
from doctest import FAIL_FAST
from flask import Flask
from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'loyality.db')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# ------- App CLI commands


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')


@app.cli.command('db_seed')
def db_seed():
    # sample brands data
    apple = Brand(name='Apple', discount_seed=0)
    amazon = Brand(name='Amazon', discount_seed=10)
    google = Brand(name='Google', discount_seed=0)
    db.session.add(apple)
    db.session.add(amazon)
    db.session.add(google)

    # sample users data
    sara = User(name='Sara', email='sara@mail.com', password='Sara&123$')
    john = User(name='John Doe', email='jdoe@mail.com', password='J!*doe')
    db.session.add(sara)
    db.session.add(john)

    db.session.commit()
    print('Database seeded!')

# ----------- Classes


class Brand(db.Model):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    discount_seed = Column(Integer, default=0)

    def __repr__(self):
        return f'Brand {self.name}'


class Discount_Code(db.Model):
    __tablename__ = 'discount_codes'
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, nullable=False)
    discount_code = Column(String, nullable=False)
    status = Column(Integer, default=0)  # 0 = unused, 1 = used


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String)


class User_Discount_Code(db.Model):
    __tablename__ = 'user_discount_code'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    brand_id = Column(Integer)
    discount_code = Column(String)
    valid_till = Column(DateTime)

# -------- schema to serialize


class BrandSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'discount_seed')


brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)


class DiscountCodeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'brand_id', 'discount_code', 'status')


discount_code_schema = DiscountCodeSchema()
discount_codes_schema = DiscountCodeSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)
