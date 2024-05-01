from flask import Blueprint
import modules.user.controller as controller

blueprint = Blueprint('user', __name__)

blueprint.route('/', methods=['GET'])(controller.index)
blueprint.route('/<int:user_id>', methods=['GET'])(controller.show)

