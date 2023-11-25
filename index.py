"Project's main point"

import pyautogui
from actions.run import start_run_action
from actions.ascension import start_ascension_action
from utils import find_img_center_on_screen, click_by_point


def main():
    "Script starting point"
    initial_location = pyautogui.position()

    active_window = find_img_center_on_screen("active_window.png", 5)
    if active_window is None:
        inactive_window = find_img_center_on_screen("inactive_window.png")
        if inactive_window is None:
            print("Game window is not open.")
            return
        click_by_point(inactive_window)

    start_ascension_action()
    start_run_action(20)

    pyautogui.moveTo(initial_location)


if __name__ == "__main__":
    main()
