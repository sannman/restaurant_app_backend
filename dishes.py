from flask import Blueprint, jsonify , request
from secret import supabase 
from seller import get_seller_by_id

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

@dishes_bp.route("/add/dishes", methods=["POST"])
def add_dish():
    data = request.get_json()
    print("Received data:", data)
    dish = data.get("dish")
    price = data.get("price")
    email = data.get("email")
    seller = get_seller_by_id(email)
    if not seller:
        return jsonify({"error": "Seller not found."}), 404
    if seller["role_id"] != 1:
        return jsonify({"error": "Only sellers can add dishes."}), 403
    if seller["role_id"] == 1:
        dish_data = {
            
            "dish": dish,
            "price": price,
            "user_id": seller["id"],
            "role_id": seller["role_id"]
        }
        print("Dish data " , dish_data)
        supabase.table("dish").insert(dish_data).execute()
        return jsonify(f"Dish added name : {dish} , price : {price}"), 201
