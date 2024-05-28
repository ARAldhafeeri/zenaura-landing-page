from zenaura.client.app import Route, App
from zenaura.client.page import Page
from public.routes import ClientRoutes
from public.components import *
import asyncio

# Instantiate components
header = Header()
intro_section = IntroSection()

features_drop_down = DropDown()

# App and routing
router = App()
home_page = Page([header, intro_section, features_drop_down])

router.add_route(Route(
    title="Developer-Focused | Zenaura",
    path=ClientRoutes.home.value,
    page=home_page
))

# Run the application
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(router.handle_location())