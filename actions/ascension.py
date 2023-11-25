import pyautogui
import time
from utils import find_img_center_on_screen, click_by_point


def collect():
    collect_button = find_img_center_on_screen("minion_claim_reward.png")
    while collect_button is not None:
        click_by_point(collect_button)
        click_by_point(collect_button)
        time.sleep(5)
        collect_button = find_img_center_on_screen("minion_claim_reward.png")

    return None


def start_minion_collect_action():
    print("Starting minion collect action")
    minion_tab = find_img_center_on_screen("ascension_minion_tab.png", 10)
    click_by_point(minion_tab)

    collect()
    pyautogui.scroll(20)
    collect()

    return


def start_ascension_action():
    print("Starting ascention action")

    ascension_button = find_img_center_on_screen("ascension_button.png")
    click_by_point(ascension_button)

    start_minion_collect_action()

    ascension_close_button = find_img_center_on_screen("ascension_close_button.png", 10)
    click_by_point(ascension_close_button)
