import click


@click.group(short_help="salted_template CLI.")
def salted_template():
    """salted_template CLI.
    """
    pass


@salted_template.command()
@click.argument("name", default="salted_template")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [salted_template]
