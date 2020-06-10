from flask import Blueprint, request, jsonify
from models import db, Driver
import bcrypt
import helper_functions

driver_api = Blueprint('driver_api', __name__)


@driver_api.route("/driver", methods=['POST'])
@driver_api.route("/driver/", methods=['POST'])
def create_driver():
    data = request.get_json()
    driver_email = Driver.query.filter_by(email=data['email']).first()
    if driver_email is not None:
        return jsonify({'message': 'Driver email already exists'})

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_customer = helper_functions.populate_driver(data, hashed_password)
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'New  Driver created!'})


@driver_api.route('/driver/id/<public_id>/', methods=['GET'])
def get_one_customer(public_id):
    driver = Driver.query.filter_by(public_id=public_id).first()
    if not driver:
        return jsonify({'message': ' No driver found'})
    else:
        driver_data = helper_functions.allocate_data(driver)
        return jsonify({'driver': driver_data})


@driver_api.route('/driver/', methods=['GET'])
def get_all_drivers():

    drivers = Driver.query.all()
    return jsonify({'drivers': helper_functions.combine_results(drivers)})


@driver_api.route('/driver/keyword/<keyword>/', methods=['GET'])
def get_specified_drivers(keyword):

    drivers = Driver.query.filter(Driver.last_name.like("%" + keyword + "%"))
    return jsonify({'drivers': helper_functions.combine_results(drivers)})


@driver_api.route('/driver/<public_id>/', methods=['DELETE'])
def delete_store(public_id):
    driver = Driver.query.filter_by(public_id=public_id).first()
    if not driver:
        return jsonify({'message': 'Customer not found'})
    else:
        db.session.delete(driver)
        db.session.commit()
        return jsonify({'message': 'Driver deleted'})