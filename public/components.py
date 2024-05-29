import asyncio 
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.presentational import * 
from public.constants import init_state_features
from zenaura.client.dom import zenaura_dom

class Header(Component):
    def render(self):
        return Builder("header").with_child(
            Builder("nav").with_children(
                NavList([
                Image("./public/logo.png", "zenaura", "40", "40", "navbarLogo"),
                NavItem("#", "Learn"),
                NavItem("#", "API Reference"),
                ])
            ).build()
        ).build()
    

class IntroSection(Component):
    def render(self):
        return Section([
            Div("introHeaders", [
                Header1("The Python Library For"),
                Header1("Building Modern Web User Interface")
            ]),
            Button("intro-btn-1", "Start Creating"),
            Button("intro-btn-2", "API Reference")
        ], "intro")
    
class Footer(Component):
    def render(self):
        return Builder("footer").with_text("Zenaura@2024").build()
    
class DropDown(Component):
    def __init__(self):
        super().__init__()
        self.state = init_state_features
        self.instance_name = "features_drop_down"

    async def toggle(self, event):
        active = 0
        for idx, feature in enumerate(self.state.features):
            feature.active = False
            if feature.name == event.target.name:
                active = idx

        self.state.features[active].active = True
        await self.animate_transition(active)

    async def animate_transition(self, active):
        for idx, feature in enumerate(self.state.features):
            feature_class = 'codeWrapper'
            if idx == active:
                feature_class += ' codeWrapper-enter'
            else:
                feature_class += ' codeWrapper-exit'
            
            feature.class_name = feature_class
            self.state.features[idx] = feature
        
        # Re-render component to apply enter classes
        await zenaura_dom.render(self)

        # Wait for the transition to complete (800ms)
        await asyncio.sleep(0.8)

        # Update classes to their final state
        for idx, feature in enumerate(self.state.features):
            if idx == active:
                feature.class_name = 'codeWrapper codeWrapper-enter-active'
            else:
                feature.class_name = 'codeWrapper codeWrapper-exit-active'

            self.state.features[idx] = feature
        
        # Re-render component to apply the final classes
        await zenaura_dom.render(self)

    async def attached(self):
        await asyncio.sleep(0.8)
        await zenaura_dom.render(self)
        self.state.features[0].active = True
        await self.animate_transition(0)



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
                            feature.active,
                            feature.class_name
                        ) for feature in self.state.features 
                    ])
                ])
            ])
        ], "features")