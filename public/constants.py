from public.data import Features, Feature 

init_state_features = all_features = Features([
    Feature(
        "Simplified Cognition", False, "simplified_cognition", "Enjoy a smoother learning curve and faster development process with simplified cognitive load. With intuitive APIs, clear documentation, and well-structured code patterns, you can focus on building your application logic instead of struggling with complex framework internals.",
        """
from zenaura.ui import img, h1

def Image(src, alt, width, height):
    return img(src=src, alt=alt, width=width, height=height)
    
def Header1(text):
    return h1(text)
""", idx=0
    ),
    Feature(
        "Intuitive UI Building", False, "intuitive_ui_building", "Craft beautiful and user-friendly interfaces effortlessly using a declarative syntax and a rich set of pre-built UI components. This approach simplifies UI development, enhances readability, and promotes consistency throughout your application.",
        """
from zenaura.client.component import Component
from zenaura.client.page import Page
from zenaura.ui import div, h1, h2, img, a, ul, li

def NavItem(href, text):
    return li(a(href=href, text=text))

def NavList(items):
    return ul(items)
    
class Header(Component):
    def render(self):
        return div(
            h1("Zenaura v0.15.0"),
            nav(
                ul(
                    NavItem("#", "Learn"),
                    NavItem("#", "API Reference"),
                )
            )
        )
        
top_bar = Header()
landing_page = Page([top_bar])
""", idx=1
    ),
    Feature(
        "Stateful Components",
        False,
        "components", 
        "Empower your application with the ability to manage dynamic content that reacts to user interactions and internal state changes. Stateful components can store data, update their appearance based on user action, making them essential for building interactive and responsive user interfaces.", 
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from zenaura.ui import div, h1, button

class Counter(Component):
    def __init__(self):
        self.count = 0

    @mutator
    async def increment(self, event) -> None:
        self.count += 1
        self.mutate()

    @mutator
    async def decrement(self, event) -> None:
        self.count -= 1
        self.mutate()

    def render(self):
        return div(
            h1(f"Count: {self.count}"),
            button("Increment", on_click=self.increment),
            button("Decrement", on_click=self.decrement)
        )
""", idx=2
    ),
    Feature(
        "Pages",
        False,
        "pages", 
        "Structure your application as a collection of distinct pages, each representing a different view or section. This approach enhances user navigation and allows you to organize your components and UI elements logically, improving the overall user experience.",
        """
from zenaura.client.app import Route, App
from zenaura.client.page import Page
from zenaura.client.component import Component
from zenaura.ui import div, h1

class Counter(Component):
    def render(self):
        return div(h1("Counter Page"))

counter = Counter()
counters_page = Page([counter])

app = App()
app.add_route(Route(
    title="Counter",
    path="/counter",
    page=counters_page
))

app.run()
""", idx=3
    ),
    Feature(
        "Server-Side Rendering (SSR)",
        False,
        "server_side_rendering", 
        "Leverage the power of server-side rendering to generate HTML on the server before sending it to the client. SSR can significantly improve initial page load times, enhance SEO (Search Engine Optimization) by making your content more accessible to search engines, and provide a smoother user experience, especially on slower connections or devices.",
        """
from flask import Flask
from zenaura.server import ZenauraServer
from zenaura.client.page import Page
from zenaura.client.component import Component
from zenaura.ui import div, h1

app = Flask(__name__, static_folder="public")

class Counter(Component):
    def render(self):
        return div(h1("Counter SSR Page"))

counter = Counter()
counters_page = Page([counter])

@app.route('/ssr')
def ssr():    
    return ZenauraServer.hydrate_page(counters_page)
    
if __name__ == "__main__":
    app.run()
""", idx=4
    ),
    Feature(
        "Asynchronous Virtual DOM",
        False,
        "asynchronous_virtual_dom", 
        "Optimize your application's UI updates by employing an asynchronous virtual DOM. This technique allows the framework to intelligently track changes in your component data and update only the necessary parts of the real DOM, minimizing unnecessary re-renders and leading to a more performant and responsive user interface.",
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from zenaura.ui import div, button

class NonBlockingVirtualDom(Component):
    @mutator
    async def non_blocking_updates1(self, event) -> None:
        self.mutate()

    @mutator
    async def non_blocking_updates2(self, event) -> None:
        self.mutate()

    def render(self):
        return div(
            button("Update 1", on_click=self.non_blocking_updates1),
            button("Update 2", on_click=self.non_blocking_updates2)
        )
""", idx=5
    ),
    Feature(
        "Built-in Client Router", False, "built_in_router", "Enable seamless navigation within your application using a built-in router. Routers handle the mapping of URLs to specific components or pages, allowing users to move between different sections of your application without requiring full page reloads, resulting in a smoother and more engaging user experience.",
        """
from zenaura.client.app import Route, App
from zenaura.client.page import Page
from zenaura.client.component import Component
from zenaura.ui import div, h1

class Counter(Component):
    def render(self):
        return div(h1("Counter Page"))

counter = Counter()
counters_page = Page([counter])

app = App()
app.add_route(Route(
    title="Counter",
    path="/counter",
    page=counters_page
))

app.run()
""", idx=6
    ),
    Feature(
        "Signals", False, "signals", "Simplify the management of application state and facilitate communication between components by using signals. Signals provide a reactive way to propagate data changes throughout your application, allowing components to react to updates and stay in sync without complex manual event handling.",
        """
from zenaura.client.observer import Subject, Observer

GlobalCounterSubject = Subject()
GlobalCounterSubject.state = {"counter": 1}

class GlobalCounterObserver1(Observer):
    def update(self, value):
        if value > 4:
            print("counter value > 4")

observer1 = GlobalCounterObserver1()
GlobalCounterSubject.attach(observer1)
""", idx=7
    ),
    Feature(
        "Dependency Injection (DI)", False, "dependency_injection", "Streamline the management of dependencies between components using dependency injection. DI makes your code more modular, testable, and maintainable by allowing components to declare their dependencies explicitly and receive them from an external injector, promoting loose coupling and flexibility.",
        """
from zenaura.client.component import Component
from zenaura.ui import div

class DependencyInjection(Component):
    def __init__(self, dependencies):
        self.api = dependencies["api"]
    
    def render(self):
        return div(f"API Endpoint: {self.api}")

di = DependencyInjection({"api": "https://api.com/v1"})
""", idx=8
    ),
    Feature(
        "Lifecycle Methods", False, "lifecycle_methods", "Gain fine-grained control over the behavior of your components at different stages of their existence. Lifecycle methods, such as `attached`, `on_mutation`, and `on_settled`, allow you to execute code when a component is created, before it updates, or after it updates in the DOM, enabling you to perform tasks like fetching data, initializing state, and cleaning up resources.",
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from zenaura.ui import div

class Lifecycles(Component):
    @mutator
    async def attached(self):
        # Fetch data or initialize state when the component mounts
        pass

    async def on_mutation(self):
        # Perform actions before the component updates
        pass

    async def on_settled(self):
        # Perform actions after the component updates
        pass

    def render(self):
        return div("Lifecycle Methods Example")
""", idx=9
    ),
])