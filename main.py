from flask import Flask
from flask_cors import CORS
from buyer import buyer_bp
from seller import seller_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(buyer_bp, url_prefix="/buyer")
app.register_blueprint(seller_bp, url_prefix="/seller")

if __name__ == "__main__":
    app.run(debug=True)