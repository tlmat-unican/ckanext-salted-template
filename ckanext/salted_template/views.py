from flask import Blueprint


salted_template = Blueprint(
    "salted_template", __name__)


def page():
    return "Hello, salted_template!"


salted_template.add_url_rule(
    "/salted_template/page", view_func=page)


def get_blueprints():
    return [salted_template]
