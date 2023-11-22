"""Utilities functions"""
import os
import pyautogui

from config import MAX_RETRIES


def get_img(file_name):
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "assets", file_name)
    return img_path


def find_img_center_on_screen(img_path, retries=MAX_RETRIES) -> pyautogui.Point | None:
    while retries != 0:
        try:
            window_location = None
            try:
                window_location = pyautogui.locateCenterOnScreen(get_img(img_path))
                retries = MAX_RETRIES
            except KeyboardInterrupt:
                break
            except:
                retries = retries - 1
                window_location = None
            if window_location is not None:
                return window_location
        except KeyboardInterrupt:
            break
    return None


def find_all_img_locations_on_screen(img_path, retries=MAX_RETRIES):
    while retries != 0:
        try:
            window_location = None
            try:
                window_location = pyautogui.locateAllOnScreen(get_img(img_path))
                retries = MAX_RETRIES
            except KeyboardInterrupt:
                break
            except:
                retries = retries - 1
                window_location = None
            if window_location is not None:
                return window_location
        except KeyboardInterrupt:
            break
    return None


def click_by_point(point):
    x, y = point
    pyautogui.click((x / 2, y / 2))
