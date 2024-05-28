from public.data import Features, Feature 
init_state_features = all_features = Features([
    Feature(
        "Stateful Components",
        True,
        "components", 
        "Empower your application with the ability to manage dynamic content that reacts to user interactions and internal state changes. Stateful components can store data, update their appearance, and trigger actions based on events, making them essential for building interactive and responsive user interfaces.", 
        """
# Counter Component
class Counter(Component):
    def __init__(self):
        super().__init__()
        self.count = 0  # Initial state

    def increment(self):
        self.count += 1

    def view(self):
        return Div("counter", [
            Button("Increment", on_click=self.increment),
            Text(f"Count:")
        ])
"""),
    Feature(
        "Pages",
        False,
        "pages", 
        "Structure your application as a collection of distinct pages, each representing a different view or section. This approach enhances user navigation and allows you to organize your components and UI elements logically, improving the overall user experience.",
         """
# Router Configuration
router = Router([
    ("/", HomePage),
    ("/about", AboutPage),
    ("/contact", ContactPage)
])
"""
        ),
    Feature(
        "Server-Side Rendering (SSR)",
        False,
        "server_side_rendering", 
        "Leverage the power of server-side rendering to generate HTML on the server before sending it to the client. SSR can significantly improve initial page load times, enhance SEO (Search Engine Optimization) by making your content more accessible to search engines, and provide a smoother user experience, especially on slower connections or devices.",
        """
# Server-Side Rendering with a Framework (Example with Flask)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {"title": "My Website", "content": "Welcome to my SSR-powered website!"}
    return render_template("index.html", **data)
"""
        ),
    Feature(
        "Asynchronous Virtual DOM",
        False,
        "asynchronous_virtual_dom", 
        "Optimize your application's UI updates by employing an asynchronous virtual DOM. This technique allows the framework to intelligently track changes in your component data and update only the necessary parts of the real DOM, minimizing unnecessary re-renders and leading to a more performant and responsive user interface.",
        """
# Simplified Virtual DOM Diffing (Conceptual)
def update_dom(old_node, new_node):
    if old_node.type != new_node.type:
        # Replace the entire node
        old_node.replace_with(new_node)
    else:
        # Update attributes
        for attr, value in new_node.attributes.items():
            old_node.set_attribute(attr, value)
        # Recursively update children
        for i in range(len(new_node.children)):
            update_dom(old_node.children[i], new_node.children[i])
"""
        ),
    Feature(
        "Built-in Router", False, "built_in_router", "Enable seamless navigation within your application using a built-in router. Routers handle the mapping of URLs to specific components or pages, allowing users to move between different sections of your application without requiring full page reloads, resulting in a smoother and more engaging user experience.",
        """
# Navigation with a Built-in Router
def navigate_to_about():
    router.push("/about")  # Navigate to the about page

Button("Go to About", on_click=navigate_to_about)
"""
        ),
    Feature(
        "Signals", False, "signals", "Simplify the management of application state and facilitate communication between components by using signals. Signals provide a reactive way to propagate data changes throughout your application, allowing components to react to updates and stay in sync without complex manual event handling.",
        """
# Signal Usage
user_logged_in = Signal()

def on_login_success(user_data):
    user_logged_in.emit(user_data)  # Notify other components

user_logged_in.connect(update_profile_component)  # Listen for login event
"""
        ),
    Feature(
        "Dependency Injection (DI)", False, "dependency_injection", "Streamline the management of dependencies between components using dependency injection. DI makes your code more modular, testable, and maintainable by allowing components to declare their dependencies explicitly and receive them from an external injector, promoting loose coupling and flexibility.",
         """
# Dependency Injection (Conceptual)
class MyComponent:
    def __init__(self, api_client: ApiClient):  # Inject the dependency
        self.api_client = api_client

    def fetch_data(self):
        return self.api_client.get_data()
"""
        ),
    Feature(
        "Lifecycle Methods", False, "lifecycle_methods", "Gain fine-grained control over the behavior of your components at different stages of their existence. Lifecycle methods, such as `onMount`, `onUpdate`, and `onUnmount`, allow you to execute code when a component is created, updated, or removed from the DOM, enabling you to perform tasks like fetching data, initializing state, and cleaning up resources.",
        """
# Lifecycle Methods
class MyComponent(Component):
    def on_mount(self):
        # Fetch initial data, set up event listeners, etc.
        pass

    def on_update(self, previous_props):
        # Handle changes in component properties
        pass

    def on_unmount(self):
        # Clean up resources (timers, event listeners)
        pass
"""
        ),
    Feature(
        "Simplified Cognition", False, "simplified_cognition", "Enjoy a smoother learning curve and faster development process with simplified cognitive load. With intuitive APIs, clear documentation, and well-structured code patterns, you can focus on building your application logic instead of struggling with complex framework internals.",
         """
# Simplified Syntax for Creating UI Elements
Div("container", [
    H1("Welcome to my app"),
    Button("Click me")
])
"""
        ),
    Feature(
        "Intuitive UI Building", False, "intuitive_ui_building", "Craft beautiful and user-friendly interfaces effortlessly using a declarative syntax and a rich set of pre-built UI components. This approach simplifies UI development, enhances readability, and promotes consistency throughout your application.",
        """
# Declarative UI Definition
class MyPage(Component):
    def view(self):
        return Div("page-content", [
            H1("Page Title"),
            P("Some paragraph text."),
            # ... other UI elements
        ])
"""
        )
])