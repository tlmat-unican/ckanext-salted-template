import ckan.plugins.toolkit as tk
import ckanext.salted_template.logic.schema as schema


@tk.side_effect_free
def salted_template_get_sum(context, data_dict):
    tk.check_access(
        "salted_template_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.salted_template_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'salted_template_get_sum': salted_template_get_sum,
    }
