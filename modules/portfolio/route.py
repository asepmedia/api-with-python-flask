from flask import Blueprint
import modules.portfolio.controller as controller

blueprint = Blueprint('portfolio', __name__)

blueprint.route('/', methods=['GET'])(controller.index)
blueprint.route('/<int:portfolio_id>', methods=['GET'])(controller.show)
