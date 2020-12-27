"""
BÖTE GAME DESIGNER

"""
from control import Control
import config
from states import splash
from states import mainmenu


def main():
    """Add states to control here."""
    run_it = Control(config.title)
    state_dict = {"SPLASH": splash.Splash(),
                  "MAINMENU":  mainmenu.MainMenu(),
                  "GAME":  splash.Splash(),
                  }
    run_it.setup_states(state_dict, "SPLASH")
    run_it.main()
