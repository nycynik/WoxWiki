import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class MetaParseException(Exception):
    pass


class HighlightRenderer(mistune.Renderer):
    """
    Using pygments on code blocks.
    """
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class Marker:
    """
    Takes in text, and marks it up.
    """

    def __init__(self):
        self.renderer = HighlightRenderer()
        self.markdown = mistune.Markdown(renderer=self.renderer)

    def to_html(self, text):
        marked = self.markdown(text)
        return marked
