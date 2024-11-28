from flask import Blueprint, request, jsonify

from repository.device_repo import get_device_by_method, get_device_with_better_connection
from service.call_register_service import register_call
from service.data_normalization import extract_normalized_devices

phone_blueprint = Blueprint("phone_calls", __name__)

@phone_blueprint.route("/", methods=['POST'])
def get_calls():
   res = register_call(request.json)
   return jsonify(res), 200

@phone_blueprint.route("/calls_by_method/Bluetooth", methods=['GET'])
def get_calls_by_method():
   res = get_device_by_method("Bluetooth")
   return jsonify(res.value_or(None)), 200

@phone_blueprint.route("/better_connection", methods=['GET'])
def get_calls_with_better_connection():
   res = get_device_with_better_connection(-60)
   return jsonify(res.value_or(None)), 200


