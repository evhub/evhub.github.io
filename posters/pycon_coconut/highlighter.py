from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import LatexFormatter

lexer = get_lexer_by_name("coconut")
formatter = LatexFormatter(full=True)
with open("coconut_examples.coco", "r") as code_file:
    code = code_file.read()
    highlighted = highlight(code, lexer, formatter)
with open("coconut_examples.tex", "w") as out_file:
    out_file.write(highlighted)
