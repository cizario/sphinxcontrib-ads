from docutils.nodes import General, Element


class AdsNode(General, Element):
    """Add node for inline Ads."""

    @staticmethod
    def visit(self, node):

        template = node['ads']['vendor'] + '.html'
        context = {
            'attributes': node['ads']['attributes']
        }

        self.body.append(
            self.builder.templates.render(template, context)
        )

    @staticmethod
    def depart(self, node):
        pass
