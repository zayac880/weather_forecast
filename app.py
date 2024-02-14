from flask import Flask
from routes.routes import update_balance_route

app = Flask(__name__)


@app.route('/update_balance', methods=['POST'])
def update_balance():
    return update_balance_route()


if __name__ == '__main__':
    app.run(debug=True)
