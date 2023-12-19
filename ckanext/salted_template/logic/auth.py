import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def salted_template_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "salted_template_get_sum": salted_template_get_sum,
    }
