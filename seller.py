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


@seller_bp.route("/sellers/login", methods=["POST"])
def seller_login():
    data = request.get_json()
    email = data.get()
    password = data.get()
    response = supabase.auth.sign_in_with_password(
    {
        "email": email,
        "password": password,
    }
)
    ...


@seller_bp.route("/sellers/signup", methods=["POST"])
def seller_signup():

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    response = supabase.auth.sign_up(
    {
        "email": email,
        "password": password,
    }
)
    ...

