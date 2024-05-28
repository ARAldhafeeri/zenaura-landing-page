from zenaura.client.tags.builder import Builder
from zenaura.client.component import Component
from zenaura.client.tags.node import Node, Attribute

def NavItem(href, text):
    return Builder('li').with_child(
        Builder('a').with_attribute('href', href).with_text(text).build()
    ).build()

def NavList(items):
    return Node("ul", children=items)
 
def Image(src, alt):
    return Builder("img").with_attributes(
        src=src,
        alt=alt
    ).build()

def Header2(text):
    return Builder('h2').with_text(text).build()

def Header1(text):
    return Builder('h1').with_text(text).build()

def Section(children, class_name="intro"):
    section = Builder('section').with_attribute('class', class_name).build()
    section.children = children
    return section

class Header(Component):
    def render(self):
        return Builder("header").with_child(
            Builder("nav").with_children(
                Node(text="v0.9.93-alpha"), 
                NavList([
                NavItem("#", "Learn"),
                NavItem("#", "API Reference"),
                ])
            ).build()
        ).build()



# features menu
    
def Header1(text):
    return Builder('h1').with_text(text).build()

def Paragraph(text, class_name=None):
    builder = Builder('p').with_text(text)
    if class_name:
        builder = builder.with_attribute('class', class_name)
    return builder.build()

def Div(class_name, children):
    div = Builder('div').with_attribute('class', class_name).build()
    div.children = children
    return div

def Button(class_name, text, onclick_handler=None, name=None):
    builder = Builder('button').with_attribute('class', class_name).with_text(text)
    if onclick_handler:
        builder = builder.with_attribute('py-click', onclick_handler)
    if name:
        builder = builder.with_attribute("name", name)
    return builder.build()

def ExapandableContentButton(btn, content, is_visible):
    style = 'display: none;' if not is_visible else 'display: block;'
    active = "controlsActive" if is_visible else "controls"
    content = Paragraph(content, "featureParagraph")
    content.attributes.append(Attribute('style', style))
    return Div(active, [
        btn,
        content
        
    ])

def CodeBlock(code):
    return Builder('pre').with_child(Builder('code').with_attribute("class", "language-python").with_text(code).build()).build()

def Tabs(tabs):
    return Div('tabs', [Button('tab-btn', tab) for tab in tabs])

def DocumentationButton():
    return Button('documentation-btn', 'Documentation')


def TableRow(content):
    return Div('row', [Div('cell', content)])

def Table(rows):
    return Div('table row', rows)

def ExpandableContent( code, is_visible):
    style = 'display: none;' if not is_visible else 'display: block;'
    content = Div('expandable-content', [
        Div('code-section ', [
            CodeBlock(code)
        ])
    ])
    content.attributes.append(Attribute('style', style))
    return content