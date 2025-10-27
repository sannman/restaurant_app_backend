from flask import Blueprint, jsonify , request
from secret import supabase 


dishes_bp = Blueprint("dishes", __name__)

@dishes_bp.route("/dishes", methods=["GET"])
def get_dishes():
    response = supabase.table("DISH").select("*").execute()
    return jsonify(response.data)

@dishes_bp.route("/dishes/search", methods=["GET"])
def search_dishes():
    query  = request.get_json()
    search = query.get("query")
    response = supabase.table("dish").select("*").like("dish", search).execute()
    print(response.data)
    return jsonify(response.data)

