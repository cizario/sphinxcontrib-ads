VERSION = (1, 0, 0, 'dev2')
__version__ = '.'.join(map(str, VERSION))

from .directives import AdsDirective
from .events import config_inited, update_templates_path, html_page_context
from .nodes import AdsNode


def setup(app):
    app.add_config_value('ads', None, True)
    app.add_node(AdsNode, html=(AdsNode.visit, AdsNode.depart))
    app.add_directive('ads', AdsDirective)
    app.connect('config-inited', config_inited, 500)
    app.connect('config-inited', update_templates_path, 700)
    app.connect('html-page-context', html_page_context)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
