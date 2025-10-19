import os
import flask
from dotenv import load_dotenv
from supabase import create_client, Client

# Load local .env file (if present)
load_dotenv()

# Expected env vars: SUPABASE_URL and SUPABASE_ANON_KEY
url: str = os.environ.get("SUPABASE_URL")
anon_key: str = os.environ.get("SUPABASE_ANON_KEY") or os.environ.get("SUPABASE_KEY")


app = flask.Flask(__name__)

supabase: Client = create_client(url, anon_key)


@app.route("/buy_dishes", methods=["GET"])
def get_dishes():
    response = (
        supabase.table("DISH")
        .select("*")
        .execute()
    )
    return flask.jsonify(response.data)


@app.route("/add_dishes", methods=["POST"])
# will get user input to add a new dish
def add_dish():
    data = flask.request.get_json()
    dish = data.get("Dish")
    price = data.get("Price")
    response = supabase.table("DISH").insert({"id":7, "Dish": dish,"Price": price}).execute()
    return flask.jsonify(response.data)

if __name__ == "__main__":
    app.run(debug=True)