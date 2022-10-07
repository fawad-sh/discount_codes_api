""" Dicount code module """

import db_setup
import datetime

def generate_dc(brand_id, count, status):
    """ Generate discount codes for the passed brand_id """

    # verify that valid brand passed
    brand = verify_brand(brand_id)
    if not brand:
        status['message'] = 'Brand id not found. Please send existing Brand code in your request'
        status['code'] = 404
        return None
    else:
        seed = brand.discount_seed + 1

    codes = []
    for x in range(seed, seed+count):
        c = str(x).zfill(6)

        # debug msg
        # print(f'discount code = {c}')

        dc = db_setup.Discount_Code(
            brand_id=brand.id, discount_code=c, status=0)
        db_setup.db.session.add(dc)
        codes.append(c)

    brand.discount_seed = seed + count - 1

    db_setup.db.session.commit()

    status['message'] = f'{count} Codes successfully generated for {brand.name} '
    status['code'] = 200

    return codes


def fetch_dc(brand_id, user_id, status):
    # verify that valid brand passed
    brand = verify_brand(brand_id)
    if not brand:
        status['message'] = 'Brand id not found. Please send existing Brand id in your request'
        status['code'] = 404
        return None

    user = db_setup.User.query.filter_by(id=user_id).first()
    if not user:
        status['message'] = 'User id not found. Please send existing user in in your request'
        status['code'] = 404
        return None

    code = db_setup.Discount_Code.query.filter_by(
        brand_id=brand_id, status=0).first()

    if not code:
        status['message'] = 'Code not Found.'
        status['code'] = 404
    else:
        # mark discount code as used
        code.status = 1
        # add 30 days validity to discount code
        d = datetime.date.today() + datetime.timedelta(days=30)

        # to notify brand that a user gets the discount code
        user_dc = db_setup.User_Discount_Code(
            brand_id=brand_id, user_id=user_id, discount_code=code.discount_code, valid_till=d)
        db_setup.db.session.add(user_dc)

        db_setup.db.session.commit()

    return code


def verify_brand(brand_id):
    result = db_setup.Brand.query.filter_by(id=brand_id).first()
    return result


if __name__ == '__main__':
    status = {'message': '', 'code': 0}

    print(generate_dc(1, 5, status))
    print(status)
