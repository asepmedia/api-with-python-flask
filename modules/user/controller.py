import flask
import modules.user.model as model


def index():
    users = []

    for user in model.find():
        users.append(model.to_json(user))

    return flask.jsonify({
        "status": 200,
        "data": users,
    })


def show(user_id):
    row = model.first(user_id)

    if row is None:
        return flask.jsonify({
            "message": "User not found",
        }), 400

    return flask.jsonify({
        "status": 200,
        "data": model.to_json(row),
    })
