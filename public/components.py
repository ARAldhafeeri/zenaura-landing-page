from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from dataclasses import fields
from public.data import Features
from public.presentational import * 
from public.constants import init_state_features

class IntroSection(Component):
    def render(self):
        return Section([
            Image(src="public/logo.svg", alt="zenaura logo"),
            Header1("The Python library for building modern web UI."),
            Button("intro-btn-1", "Start Creating"),
            Button("intro-btn-2", "API Reference")
        ])
    
class DropDown(Component):
    def __init__(self):
        super().__init__()
        self.state = init_state_features
        self.instance_name = "features_drop_down"
    @mutator
    async def toggle(self, event):
        event.preventDefault()
        for feature in self.state.features:
            # set previous to false 
            if feature.active: 
                feature.active = False
            # set current to true 
            if feature.name == event.target.name:
                feature.active = True 


    def render(self):
        return Section([
            Div('container', [
            Header1("Create modular user interfaces using components"),
                Paragraph("""
                    Zenaura empowers developers to craft user interfaces entirely
                    using Python. With Zenaura, they can effortlessly 
                    decompose their code into modular components, 
                    define pages mapped to routes, all within an 
                    Object-oriented paradigm. 
                    This approach enhances maintainability, scalability, 
                    and performance, offering a seamless development experience.
                """),
                Div('row', [
                    Div('column', [
                    
                        ExapandableContentButton(
                            Button('expand-btn', feature.title, f'{self.instance_name}.toggle', feature.name),
                            feature.description,
                            feature.active,
                        ) for feature in self.state.features
                      
                    ]),
                    Div("column", [
                        ExpandableContent(
                            feature.code_example, 
                            feature.active
                        ) for feature in self.state.features
                    ])
                ])
            ])
        ], "features")