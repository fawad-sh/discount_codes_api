""" Main program for Discount Code Microservice"""
""" Developer: Fawad I Sheikh
    Date: 5-Oct-2022
"""


from db_setup import Brand, Discount_Code, brand_schema, brands_schema, discount_codes_schema, discount_code_schema
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from disc_codes import generate_dc, fetch_dc
import os
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'loyalty.db')
db = SQLAlchemy(app)

#
# ------ Routes Definition ---------
#


@app.route("/")
def index():
    return "Welcome to Discount code microservice API "


@app.route("/brands")
def brands():
    brands_list = Brand.query.all()
    result = brands_schema.dump(brands_list)
    # print(result)
    return jsonify(result)


@app.route("/codes")
def codes():
    brand_id = request.args.get('brand_id')
    if brand_id:
        codes_list = Discount_Code.query.filter_by(brand_id=brand_id)
    else:
        codes_list = Discount_Code.query.all()

    result = discount_codes_schema.dump(codes_list)
    # print(result)
    if not result:
        return jsonify(message='No discount codes found'), 404

    return jsonify(result)


# ----- Generate discount_code  END POINT ----------
@app.route("/generate_disc_codes", methods=['GET', 'POST'])
def generate_disc_codes():
    """Generate discount codes, the endpoint expects two parameters
        brand_code = the brand code for which the codes will be generated
        count = how many discount codes to be generated. It is optional, default value is 10 if nothing is passed. """

    brand_id = request.args.get("brand_id")
    seed = 0

    if not brand_id:
        return jsonify(message='Please pass Brand id, it is required to generate discount codes'), 404

    count = request.args.get("count")
    if not count:
        count = 10
    else:
        """ determine count is a +ve number """
        try:
            count = int(count)
            if count <= 0:
                raise ValueError

        except ValueError:
            return {'message': 'Please send a positive numeric value for count'}, 401

    status = {'message': '', 'code': 0}
    codes = generate_dc(brand_id, count, status)

    if not codes:
        return jsonify(message=f'Codes not generated, please contact customer support. Error - {status["message"]}'), status['code']

    return jsonify(message=f'{count} Discount codes generated for Brand_id = {brand_id} ')


# ----- fetch_discount_code  END POINT ----------
@ app.route("/fetch_discount_code", methods=['GET', 'POST'])
def fetch_disc_code():
    """Fetch discount codes, the endpoint expects two parameters
        brand_id = the brand id for which the discount code will be returned
        user_id = the user_id requesting for discount code. """

    brand_id = request.args.get("brand_id")
    if not brand_id:
        return jsonify(message='Please pass Brand id, it is required to fetch discount code'), 404

    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify(message='Please pass User id, it is required to fetch discount code'), 404

    status = {'message': '', 'code': 0}

    code = fetch_dc(brand_id, user_id, status)
    if not code:
        return jsonify(message=f'Code not fetched, please contact customer support. Error - {status["message"]}'), status['code']

    return jsonify(message=f'{code.discount_code} discount code is fetched for brand id = {brand_id}')


# -
# -
# ------ Main  ---------
if __name__ == "__main__":
    app.run(debug=True)
