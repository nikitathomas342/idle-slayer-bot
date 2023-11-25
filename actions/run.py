import time
import keyboard
from datetime import datetime, timedelta
from utils import find_img_center_on_screen, click_by_point

check_chest_hunt_in = 100
click_boost_in = 5


def check_termination_key():
    if keyboard.is_pressed("Esc"):
        return True
    return False


def start_check_hunt_action():
    close_btn = find_img_center_on_screen("chest_hunt_close_button.png", 1)
    if close_btn is not None:
        click_by_point(close_btn)
    else:
        return

    print("Starting chest hunt action")

    chest = find_img_center_on_screen("closed_chest.png")
    while chest is not None:
        click_by_point(chest)
        time.sleep(10)
        chest = find_img_center_on_screen("closed_chest.png")

    time.sleep(10)
    close_btn = find_img_center_on_screen("chest_run_close.png")
    click_by_point(close_btn)


def start_run_action(minutes=20):
    print(f"Starting run action for {minutes} minutes.")
    run_until = datetime.now() + timedelta(minutes=minutes)
    boost_btn_center = find_img_center_on_screen("boost.png", 5)
    check_chest_hunt = 0
    click_boost = 0
    while datetime.now() < run_until:
        # Click on empty screen
        if boost_btn_center is not None:
            x, y = boost_btn_center
            click_by_point((x + 100, y))
            time.sleep(80 / 1000)

        # Click boost
        click_boost = click_boost + 1
        if click_boost == click_boost_in and boost_btn_center is not None:
            click_boost = 0
            click_by_point(boost_btn_center)

        check_chest_hunt = check_chest_hunt + 1
        if check_chest_hunt == check_chest_hunt_in:
            check_chest_hunt = 0
            start_check_hunt_action()

        if check_termination_key():
            break
