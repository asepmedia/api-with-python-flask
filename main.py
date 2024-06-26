from flask import Flask
from routes.blueprint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()
