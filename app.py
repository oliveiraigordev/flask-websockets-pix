from flask import Flask
from repository.database import db
from repository.socketio import socketio
from routes.payment import payment_bp
from models.payment import Payment


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(payment_bp)

db.init_app(app)
socketio.init_app(app)


if __name__ == '__main__':
    socketio.run(app, debug=True)
