import ckan.plugins.toolkit as tk


def salted_template_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "salted_template_required": salted_template_required,
    }
