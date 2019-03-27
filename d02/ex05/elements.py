#! /usr/bin/python3

from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="html", content=content, attr=attr)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag="body", content=content)

class Head(Elem):
    def __init__(self, content=None):
        print(content, type(content))
        super().__init__(tag="head", content=content)

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag="title", content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="meta", content=content, attr=attr, tag_type="simple")

class Table(Elem):
    def __init__(self, content=None):
        super().__init__(tag="table", content=content)

class Th(Elem):
    def __init__(self, content=None):
        super().__init__(tag="th", content=content)

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(tag="tr", content=content)

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(tag="td", content=content)

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(tag="ul", content=content)

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(tag="ol", content=content)

class Li(Elem):
    def __init__(self, content=None):
        super().__init__(tag="li", content=content)

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag="h1", content=content)

class H2(Elem):
    def __init__(self, content=None):
        super().__init__(tag="h2", content=content)

class P(Elem):
    def __init__(self, content=None):
        super().__init__(tag="p", content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="div", content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=None):
        super().__init__(tag="span", content=content)

class Hr(Elem):
    def __init__(self, content=None):
        super().__init__(tag="hr", content=content, tag_type="simple")

class Br(Elem):
    def __init__(self, content=None):
        super().__init__(tag="br", content=content, tag_type="simple")

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag="img", content=content, attr=attr, tag_type="simple")

def simple_tests():
    assert (str(Html(Text("Content")))) == '<html>\n  Content\n</html>'
    assert (str(Html(Text("Content"), {'lang': "en"}))) == '<html lang="en">\n  Content\n</html>'
    assert (str(Head(Text("Content")))) == '<head>\n  Content\n</head>'
    assert (str(Body(Text("Content")))) == '<body>\n  Content\n</body>'
    assert (str(Title(Text("Content")))) == '<title>\n  Content\n</title>'
    assert (str(Table(Text("")))) == '<table></table>'
    assert (str(Th(Text()))) == '<th></th>'
    assert (str(Tr())) == '<tr></tr>'
    assert (str(Td())) == '<td></td>'
    assert (str(Ul())) == '<ul></ul>'
    assert (str(Ol())) == '<ol></ol>'
    assert (str(Li())) == '<li></li>'
    assert (str(H1())) == '<h1></h1>'
    assert (str(H2())) == '<h2></h2>'
    assert (str(P())) == '<p></p>'
    assert (str(Div(attr={'style': "color: blue;"}))) == '<div style="color: blue;"></div>'
    assert (str(Span())) == '<span></span>'
    assert (str(Meta(attr={'charset': 'utf-8'}))) == '<meta charset="utf-8" />'
    assert (str(Img(attr={'src': 'image.png', 'title': 'fake'}))) == '<img src="image.png" title="fake" />'
    assert (str(Hr())) == '<hr />'
    assert (str(Br())) == '<br />'
    print("Simple tests: OK")

def main():
    simple_tests()
    html = Html([
        Head(
            Title(Text('"hello ground!"'))
        ),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ]),
    ])
    print(html)

if __name__ == '__main__':
    main()