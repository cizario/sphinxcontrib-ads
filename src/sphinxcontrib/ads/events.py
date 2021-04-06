import os

from .errors import AdsConfigError


def config_inited(app, config):

    ads = config.ads

    if not ads or not isinstance(ads, dict):

        raise AdsConfigError(
            "'ads' object must be properly defined in 'conf.py' file depending on a given vendor."
        )

    else:

        if 'vendor' not in ads.keys() or not ads['vendor']:

            raise AdsConfigError(
                "'vendor' must be defined, supported values: 'carbonads', 'ethicalads'."
            )

        elif ads['vendor'] not in ['carbonads', 'ethicalads']:

            raise AdsConfigError(
                f"'{ads['vendor']}' is not recognized as vendor's value, supported values: 'carbonads' or 'ethicalads'."
            )

        else:

            if 'attributes' not in ads.keys() or not (ads['attributes'] and isinstance(ads['attributes'], dict)):

                raise AdsConfigError(
                    f"{ads['vendor']}: 'attributes' must be properly defined according to the given vendor."
                )

            else:

                if ads['vendor'] == 'carbonads':

                    if 'url' not in ads['attributes'].keys() or not ads['attributes']['url']:
                        raise AdsConfigError(
                            "carbonads: 'url' must be defined."
                        )

                elif ads['vendor'] == 'ethicalads':

                    if 'data-ea-publisher' not in ads['attributes'].keys() or not ads['attributes']['data-ea-publisher']:
                        raise AdsConfigError(
                            "ethicalads: 'data-ea-publisher' must be defined."
                        )

def update_templates_path(app, config):
    templates_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_templates'))
    config.templates_path.append(templates_path)

def html_page_context(app, pagename, templatename, context, doctree):

    def ads():

        ads = app.config.ads

        template = ads['vendor'] + '.html'
        context = {
            'attributes': ads['attributes']
        }

        return app.builder.templates.render(template, context)

    context['ads'] = ads
