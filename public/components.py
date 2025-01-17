import asyncio 
import random
from zenaura.client.component import Component, Reuseable
from zenaura.client.mutator import mutator, mutates
from public.presentational import * 
from public.constants import init_state_features
from zenaura.client.dom import zenaura_dom
from dataclasses import dataclass
from zenaura.client.tags.builder import Builder
from zenaura.web.utils import window
from zenaura.client.dispatcher import dispatcher
class Header(Component):
    def render(self):
        return Div("navbar", [
            Div("left", [
                Image("./public/logo.png", "zenaura", "55", "55", "navbarLogo"),
                NavItemText("https://araldhafeeri.github.io/Zenaura/", "Docs"),
                NavItemText("https://araldhafeeri.github.io/Zenaura/", "APIs"),
            ]),
            Div("center", [
                NavItemIcon("https://www.linkedin.com/company/102984598/admin/feed/posts/",  Image("./public/linkedin.png", "zenaura", "33", "33", "socialIcons")),
                NavItemIcon("mailto:ar.aldhafeeri11@gmail.com",  Image("./public/gmail.png", "zenaura", "33", "33", "socialIcons")),
                NavItemIcon("https://github.com/ARAldhafeeri/Zenaura",  Image("./public/github.png", "zenaura", "33", "33", "socialIcons")),
            ]),
            Div("right", [
               Paragraph("v0.15.23")
            ])
        ])
        
class IntroSection(Component):

    def docs(self, event):
        window.open("https://araldhafeeri.github.io/Zenaura/")
    def render(self):
        return Section([
            Div("introHeaders", [
                Header1("The Python Library For"),
                Header1("Building Modern Web User Interface")
            ]),
            Button("intro-btn-1", "Start Creating", "intro_section.docs.1"),
            Button("intro-btn-2", "API Reference", "intro_section.docs.2")
        ], "intro")
    
class Footer(Component):
    def render(self):
        return Builder("footer").with_text("Zenaura@2025").build()
    
class DropDown(Component):
    def __init__(self):
        super().__init__()
        self.state = init_state_features
        self.instance_name = "features_drop_down"
        self.active = self.state.features[0]
        self.previous = self.state.features[1]

    def toggle(self,event):
        curr_name = event.target.name
        def find_previous(x):
            if x.active == True:
                return x

        
        def find_by_name(x):
            nonlocal curr_name
            if x.name == curr_name:
                return x
    
        self.previous = next(filter(find_previous, self.state.features))
        self.active = next(filter(find_by_name, self.state.features))
        if self.active.idx == self.previous.idx:
            return # do nothing
        self.state.features[self.active.idx].active = True
        self.state.features[self.previous.idx].active = False
        self.animate_transition()

    def animate_transition(self):
  
        self.previous.class_name = 'codeWrapper codeWrapper-exit'
        self.active.class_name = 'codeWrapper codeWrapper-enter'
        self.state.features[self.active.idx] = self.active
        self.state.features[self.previous.idx] = self.previous

        # Re-render component to apply enter classes
        dispatcher.dispatch(zenaura_dom.render, self)


        self.active.class_name = 'codeWrapper codeWrapper-enter-active'
        self.previous.class_name = 'codeWrapper codeWrapper-exit-active'
        self.state.features[self.active.idx] = self.active
        self.state.features[self.previous.idx] = self.previous

        # Re-render component to apply the final classes
        dispatcher.dispatch(zenaura_dom.render, self)
    
    @mutator
    async def attached(self):
        self.state.features[0].active = True
        self.animate_transition()



    def render(self):
        return Section([
            Div('container', [
                Div('examplesPara', [
                    Header1("Components-Based User Interfaces"),
                    Paragraph("""
                        Zenaura empowers developers to craft user interfaces entirely
                        using Python. With Zenaura, they can effortlessly 
                        decompose their code into modular components, 
                        define pages mapped to routes, all within an 
                        Object-oriented paradigm. 
                        This approach enhances maintainability, scalability, 
                        and performance, offering a seamless development experience.
                    """)
                ]),
               
            ]),
             Div('row', [
                    Div('column sticky', [
                        ExapandableContentButton(
                            Button('expand-btn', feature.title, f"features.toggle.{idx}", feature.name),
                            feature.description,
                            feature.active,
                        ) for idx, feature in enumerate(self.state.features)
                    ]),
                    Div("column", [
                     ExpandableContent(
                            feature.code_example, 
                            feature.active,
                            feature.class_name
                        ) for feature in self.state.features 
                    ])
                ])
        ], "features")
    
@dataclass
class Cell:
    alive: bool
    generation: int = 0

class GameOfLifeState:
    grid: list[Cell]  # Flattened grid of cells
    generations: int
    running: bool
    live_cells: list[Cell]  # Store live cells as a separate list

