from flask import Flask

from routes.phone_calls_routes import phone_blueprint

app = Flask(__name__)

app.register_blueprint(phone_blueprint, url_prefix="/api/phone_tracker")

if __name__ == '__main__':
    app.run(debug=True)