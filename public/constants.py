from public.data import Features, Feature 
init_state_features = all_features = Features([
      Feature(
        "Simplified Cognition", False, "simplified_cognition", "Enjoy a smoother learning curve and faster development process with simplified cognitive load. With intuitive APIs, clear documentation, and well-structured code patterns, you can focus on building your application logic instead of struggling with complex framework internals.",
         """
def Image(src, alt, width, height):
    return Builder("img").with_attributes(
        src=src,
        alt=alt,
        width=width,
        height=height
    ).build()
    
def Header1(text):
    return Builder('h1').with_text(text).build()
"""
        ),
    Feature(
        "Intuitive UI Building", False, "intuitive_ui_building", "Craft beautiful and user-friendly interfaces effortlessly using a declarative syntax and a rich set of pre-built UI components. This approach simplifies UI development, enhances readability, and promotes consistency throughout your application.",
        """
from zenaura.client.component import Component
from zenaura.client.page import Page
def NavItem(href, text):
    return Builder('li').with_child(
        Builder('a').with_attribute('href', href).with_text(text).build()
    ).build()

def NavList(items):
    return Node("ul", children=items)
    
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
        
top_bar = Header()
landing_page = Page([top_bar])

"""
        ),
    Feature(
        "Stateful Components",
        False,
        "components", 
        "Empower your application with the ability to manage dynamic content that reacts to user interactions and internal state changes. Stateful components can store data, update their appearance based on user action, making them essential for building interactive and responsive user interfaces.", 
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class Counter(Component):
  def __init__(self):
      self.count = 0

  @mutator
  async def increment(self, event) -> None:
    #increment count and mutates ui
    pass

  @mutator
  async def decrement(self, event) -> None:
    # decrement count mutates ui
    pass


  def render(self) -> Node:
    # ui code
    pass
"""),
    Feature(
        "Pages",
        False,
        "pages", 
        "Structure your application as a collection of distinct pages, each representing a different view or section. This approach enhances user navigation and allows you to organize your components and UI elements logically, improving the overall user experience.",
         """
from zenaura.client.component import Component
from zenaura.client.page import Page
class Counter(Component):
    pass
counter = Counter()
counters_page = Page([counter])
"""
        ),
    Feature(
        "Server-Side Rendering (SSR)",
        False,
        "server_side_rendering", 
        "Leverage the power of server-side rendering to generate HTML on the server before sending it to the client. SSR can significantly improve initial page load times, enhance SEO (Search Engine Optimization) by making your content more accessible to search engines, and provide a smoother user experience, especially on slower connections or devices.",
        """
from flask import Flask
from public.main import counters_page
from zenaura.server import ZenauraServer

app = Flask(__name__,
            static_folder="public"
            )

@app.route('/ssr')
def ssr():    
    # Render the main HTML template with the rendered component
    return ZenauraServer.hydrate_page(counters_page)
    
if __name__ == "__main__":
    app.run()
"""
        ),
    Feature(
        "Asynchronous Virtual DOM",
        False,
        "asynchronous_virtual_dom", 
        "Optimize your application's UI updates by employing an asynchronous virtual DOM. This technique allows the framework to intelligently track changes in your component data and update only the necessary parts of the real DOM, minimizing unnecessary re-renders and leading to a more performant and responsive user interface.",
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class NonBlookingVirtualDom(Component):

  @mutator
  async def non_blocking_updates1(self, event) -> None:
      pass

  @mutator
  async def non_blocking_updates2(self, event) -> None:
	  pass
"""
        ),
    Feature(
        "Built-in Client Router", False, "built_in_router", "Enable seamless navigation within your application using a built-in router. Routers handle the mapping of URLs to specific components or pages, allowing users to move between different sections of your application without requiring full page reloads, resulting in a smoother and more engaging user experience.",
        """
from zenaura.client.app import Route, App 
from zenaura.client.component import Component
from zenaura.client.page import Page

class Counter(Component):
    pass
counter = Counter()
counters_page = Page([counter])

router = App()

router.add_route(Route(
		title="counter",
		path="/counter",
		page=counters_page
))
"""
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
"""
        ),
    Feature(
        "Dependency Injection (DI)", False, "dependency_injection", "Streamline the management of dependencies between components using dependency injection. DI makes your code more modular, testable, and maintainable by allowing components to declare their dependencies explicitly and receive them from an external injector, promoting loose coupling and flexibility.",
         """
from zenaura.client.component import Component

class DependencyInjection(Component):
	def __init__(self, dependencies):
		self.api = dependencies["api"]
	pass # use dependency inside the component
	
di = DependencyInjection({"api": "https://api.com/v1"})
"""
        ),
    Feature(
        "Lifecycle Methods", False, "lifecycle_methods", "Gain fine-grained control over the behavior of your components at different stages of their existence. Lifecycle methods, such as `attached`, `on_mutation`, and `on_settled`, allow you to execute code when a component is created, before it updates, or after it updates in the DOM, enabling you to perform tasks like fetching data, initializing state, and cleaning up resources.",
        """
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class DependencyInjection(Component):
	
	@mutator
	async def attached(self):
		# do something when component mounts
		# fetch data and attach it to component and so on.
		
	async def on_mutation(self):
		# do something before the component mutates and renders
		
	async def on_settled(self):
		# do something when update finish and component renders
"""
        ),
])