import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import config

def introduction_title():
  value = toolkit.config.get("ckan.salted_template.introduction_title")
  return value

def custom_css_filename():
  value = toolkit.config.get("ckan.salted_template.custom_css_filename")
  return value


class SaltedTemplatePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic','salted_template')

      # ITemplateHelpers
    def get_helpers(self):
        return {'salted_template_introduction_title': introduction_title(),
            'salted_template_custom_css_filename': custom_css_filename()}


