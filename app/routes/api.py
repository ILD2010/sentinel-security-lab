from flask import Blueprint, jsonify

from app.utils.system_info import get_system_info


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/system")
def system_status():

    system_info = get_system_info()

    return jsonify(system_info)