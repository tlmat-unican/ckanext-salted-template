
def salted_template_hello():
    return "Hello, salted_template!"


def get_helpers():
    return {
        "salted_template_hello": salted_template_hello,
    }
