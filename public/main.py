from zenaura.client.app import Route, App
from zenaura.client.page import Page
from public.routes import ClientRoutes
from public.components import (
    Header, 
    IntroSection, 
    DropDown, 
    Footer,
    GameOfLife
)
import asyncio

# Instantiate components
header = Header()
intro_section = IntroSection()

features_drop_down = DropDown()
footer = Footer()

gameOfLife = GameOfLife([])
# App and routing
router = App()
home_page = Page([header, intro_section, features_drop_down, gameOfLife, footer])

router.add_route(Route(
    title="Developer-Focused | Zenaura",
    path=ClientRoutes.home.value,
    page=home_page
))

router.navigate("/zenaura-landing-page/")

# Run the application
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(router.handle_location())

