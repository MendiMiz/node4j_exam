from flask import Blueprint, request, jsonify

from service.call_register_service import register_call
from service.data_normalization import extract_normalized_devices

phone_blueprint = Blueprint("phone_calls", __name__)

@phone_blueprint.route("/", methods=['POST'])
def get_calls():
   res = register_call(request.json)
   print(res)
   return jsonify({ }), 200

