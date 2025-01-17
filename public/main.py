from zenaura.client.app import Route, App
from zenaura.client.page import Page
from public.routes import ClientRoutes
from public.constants import init_state_features
from public.components import (
    Header, 
    IntroSection, 
    DropDown, 
    Footer,
)
from zenaura.client.dispatcher import dispatcher

# Instantiate components
header = Header()
intro_section = IntroSection()

features_drop_down = DropDown()
footer = Footer()


# App and routing
router = App()
home_page = Page([header, intro_section, features_drop_down, footer])

# Dispatcher bindings
dispatcher.bind("intro_section.docs.1", "click", intro_section.docs)
dispatcher.bind("intro_section.docs.2", "click", intro_section.docs)

for i in range(len(init_state_features.features)):
    id = f"features.toggle.{i}"
    dispatcher.bind(id, "click", features_drop_down.toggle)

router.add_route(Route(
    title="Developer-Focused | Zenaura",
    path=ClientRoutes.home.value,
    page=home_page
))

router.run()
dispatcher.dispatch(router.navigate, ClientRoutes.home.value)