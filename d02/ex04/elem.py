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
    def __init__(self, tag="div", attr={}, content="", tag_type="double"):
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type
    
    def __str__(self):
        out = "<{}".format(self.tag)
        for attr, attr_value in self.attr.items():
            out += " {}=\"{}\"".format(attr, attr_value)
        if self.tag_type == "double":
            out += ">"
            if self.content:
                out += self.content
            out += "</{}>".format(self.tag)
        else:
            out += " />"
        return (out)


def main():
    elem = Elem(tag="div", attr={"toto":"tata"}, content="toto", tag_type="double")
    test = Elem('div', {}, None, 'double')
    print(test)

if __name__ == '__main__':
    main()