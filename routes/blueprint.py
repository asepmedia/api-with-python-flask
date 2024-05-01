from flask import Blueprint
import modules.user.route as user
import modules.portfolio.route as portfolio

blueprint = Blueprint('v1', __name__)

blueprint.register_blueprint(user.blueprint, url_prefix='/users')
blueprint.register_blueprint(portfolio.blueprint, url_prefix='/portfolios')