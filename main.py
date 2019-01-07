from flask import Flask
from routers.user.user import bp as user_bp
from routers.product.product import bp as product_bp
from models.db import db_session

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

#Connect Router
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)