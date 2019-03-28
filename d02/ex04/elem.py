#! /usr/bin/python3

class Text(str):

    def __str__(self):
        out = super().__str__()
        out = out.replace('"', '&quot;')
        out = out.replace('<', '&lt;') 
        out = out.replace('>', '&gt;') 
        out = out.replace('\n', '\n<br />\n') 
        return (out)

class Elem():
    def __init__(self, tag="div", attr={}, content=None, tag_type="double"):
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if content != None and type(content) == str:
             raise Elem.ValidationError()
        self.add_content(content)
    
    class ValidationError(Exception):
        def __init__(self):
            super().__init__("This content is neither a Text nor an Elem.")

    def check_content(self, content):
        if not isinstance(content, Elem) and not isinstance(content, Text) and not isinstance(content, list):
            return (False)

        if isinstance(content, list):
            for elem in content:
                if not isinstance(elem, Text) and not isinstance(elem, Elem):
                    return (False)
        return (True)

    def print_begin_tag(self):
        out = "<{}".format(self.tag)
        for attr, attr_value in self.attr.items():
            out += " {}=\"{}\"".format(attr, attr_value)
        if self.tag_type == "simple":
            out += " />"
        else:
            out += ">"
        return (out)
    
    def print_end_tag(self):
        if self.tag_type == "double":
            return("</{}>".format(self.tag))
        return("")

    def add_content(self, content):
        if not content:
            return
        if not self.check_content(content):
            raise self.ValidationError()
        if isinstance(content, Elem):
            self.content.append(content)
        if isinstance(content, list):
            for elem in content:
                if elem != Text(''):
                    self.content.append(elem)
        if isinstance(content, Text) and len(content) > 0:
            self.content.append(content) 

    def print_content(self):
        if self.content is None:
            return
        out = ""
        len_content = len(self.content)
        idx = 0
        for elem in self.content:
            if type(elem) != Text:
                out += "\n  "
                out += elem.__str__().replace("\n", "\n  ")
                if idx == len_content - 1 :
                    out += "\n"
            else:
                out += "\n  "
                out += str(elem)
                if idx == len_content - 1 :
                    out += "\n"
            idx += 1
        return (out)

    def __str__(self):
        out = self.print_begin_tag()
        out += self.print_content()
        out += self.print_end_tag()
        return (out)

def main():
    html = Elem(
     tag='html',
      content=[Elem(tag='head', 
       content=Elem(tag='title',
            content=Text('"Hello ground!"'))),
      Elem(tag='body',
        content=[Elem(tag='h1',
          content=Text('"Oh no, not again!"')), 
        Elem(tag='img', tag_type='simple', attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])
    print(html)

if __name__ == '__main__':
    main()