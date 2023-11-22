from utils import (
    find_img_center_on_screen,
    click_by_point,
    find_all_img_locations_on_screen,
)
from datetime import datetime, timedelta
import time
import random
import pyautogui

check_chest_hunt_in = 100
click_boost_in = 20


def start_check_hunt_action():
    print("Starting chest hunt action.")
    close_btn = find_img_center_on_screen("chest_hunt_close_button.png", 5)
    if close_btn is not None:
        click_by_point(close_btn)

    chests = find_all_img_locations_on_screen("closed_chest.png")
    while chests is not None:
        print(chests)
        chest_locations = list(chests)
        random_chest = random.choice(chest_locations)
        random_chest_center = pyautogui.center(random_chest)
        click_by_point(random_chest_center)
        time.sleep(1)
        chests = find_all_img_locations_on_screen("closed_chest.png")

    return


def start_run_action(minutes=20):
    print(f"Starting run action for {minutes} minutes.")
    run_until = datetime.now() + timedelta(minutes=minutes)
    boost_btn_center = find_img_center_on_screen("boost.png", 5)
    check_chest_hunt = 0
    click_boost = 0
    print(boost_btn_center)
    while datetime.now() < run_until:
        # Click on empty screen
        if boost_btn_center is not None:
            x, y = boost_btn_center
            click_by_point((x + 100, y))
            time.sleep(80 / 1000)

        # Click boost
        click_boost = click_boost + 1
        if click_boost == click_boost_in and boost_btn_center is not None:
            click_by_point(boost_btn_center)

        check_chest_hunt = check_chest_hunt + 1
        if check_chest_hunt == check_chest_hunt_in:
            check_chest_hunt = 0
            start_check_hunt_action()
