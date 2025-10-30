from flask import Blueprint, request, jsonify
from secret import supabase  # import client from secrets

seller_bp = Blueprint("seller", __name__)

@seller_bp.route("/sellers/login", methods=["POST"])
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
            "session": response.session.access_token,
            "user_id": response.user.id

        }

    return jsonify({"user": user_data})


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

    #data to send in public.user to link (buyer/seller)
    data_seller = {
        "id" : response.user.id,
        "email": email,
        "role_id": 1, # user id == 1 is seller , 2 == buyer
    }
    supabase.table("users").insert(data_seller).execute()
    user_data = {
            "email": getattr(response.user, "email", None),
            "session": getattr(getattr(response, "session", None), "access_token", None),
            "user_id": getattr(response.user, "id", None)

        }
    

    return jsonify({"user": user_data}), 201



def get_seller_by_id(email):
    response = supabase.table("users").select("*").eq("role_id", 1).eq("email", email).execute()
    if response.data:
        print(response.data)
        return response.data[0]
    
    return None





