from docutils.parsers.rst import Directive, directives

from .nodes import AdsNode


class AdsDirective(Directive):
    """Ads ".. ads::" rst directive."""

    def run(self):

        ads = self.state.document.settings.env.config.ads

        return [AdsNode(ads=ads)]
