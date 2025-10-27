from flask import Blueprint, jsonify , request
from secret import supabase 


buyer_bp = Blueprint("buyer", __name__)

@buyer_bp.route("/buyers/login", methods=["POST"])
def seller_login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    user_data = {
            "email": response.user.email,
            "password": password
        }
    return jsonify({"user": user_data})


@buyer_bp.route("/buyers/signup", methods=["POST"])
def buyer_signup():

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    response = supabase.auth.sign_up(
    {
        "email": email,
        "password": password,
    }
    )
    user_data = {
            "email": response.user.email,
            "password": password
        }
    return jsonify({"user": user_data})



@buyer_bp.route("/dishes", methods=["GET"])
def get_dishes():
    response = supabase.table("DISH").select("*").execute()
    return jsonify(response.data)

@buyer_bp.route("/dishes/search", methods=["GET"])
def search_dishes():
    query  = request.get_json()
    search = query.get("query")
    response = supabase.table("dish").select("*").like("dish", search).execute()
    print(response.data)
    return jsonify(response.data)