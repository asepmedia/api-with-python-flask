import flask
import modules.portfolio.model as model


def index():
    users = []

    for user in model.find():
        users.append(model.to_json(user))

    return flask.jsonify({
        "status": 200,
        "data": users,
    })


def show(portfolio_id):
    row = model.first(portfolio_id)

    if row is None:
        return flask.jsonify({
            "message": "Portfolio not found",
        }), 400

    return flask.jsonify({
        "status": 200,
        "data": model.to_json(row),
    })

