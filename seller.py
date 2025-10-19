from flask import Blueprint, request, jsonify
from secret import supabase  # import client from secrets

seller_bp = Blueprint("seller", __name__)

@seller_bp.route("/dishes", methods=["POST"])
def add_dish():
    data = request.get_json()
    dish = data.get("Dish")
    price = data.get("Price")
    response = supabase.table("DISH").insert({"Dish": dish, "Price": price}).execute()
    return jsonify(response.data)