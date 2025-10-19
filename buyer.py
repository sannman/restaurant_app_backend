from flask import Blueprint, jsonify
from secret import supabase 


buyer_bp = Blueprint("buyer", __name__)

@buyer_bp.route("/dishes", methods=["GET"])
def get_dishes():
    response = supabase.table("DISH").select("*").execute()
    return jsonify(response.data)
