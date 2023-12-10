"""
Author: Eitan Shoshan
Program name: Ex-2.7 functions
Description: the functions that the server use
Date: 10-12-23
"""
import glob
import os
import shutil
import subprocess
import pyautogui
import base64

ERROR_MSG = "an error was found"
SUCCEED_MSG = "done"


def folder_dir(folder_path):
    """
    the function gets the path as a parameter and returns all the files in it
    :param folder_path:
    :return: a list of the files in path
    """
    try:
        folder_path = folder_path + '/*.*'
        file_list = glob.glob(folder_path)
        return file_list
    except:
        return ERROR_MSG


def delete(file_path):
    """
    the function deletes the file from path
    :param file_path:
    :return: done/error message
    """
    try:
        os.remove(file_path)
        return SUCCEED_MSG
    except os.error as err:
        return ERROR_MSG + err


def copy(original, new):
    """
    the function copies the file from original path into new path
    :param original:
    :param new:
    :return: done/error message
    """
    try:
        shutil.copy(original, new)
        return SUCCEED_MSG
    except shutil.Error as err:
        return ERROR_MSG


def execute(path):
    """
    the function executes the app from path
    :param path:
    :return: done/error message
    """
    try:
        subprocess.call(path)
        return SUCCEED_MSG
    except:
        return ERROR_MSG


def screenshot():
    """
    take a screenshot and save it in a pre-defined path
    :return: done/error message
    """
    try:
        image = pyautogui.screenshot()
        image.save("c:/temp/screenshot/screenshot.jpg")
        return SUCCEED_MSG
    except Exception as e:
        print("Exception:", e)
        return ERROR_MSG


def send_photo():
    """
    the function sends the last screenshot the server took to the client
    :return: a string of the bytes of the photo
    """
    try:
        with open("c:/temp/screenshot/screenshot.jpg", 'rb') as file:
            image_bytes = file.read()
        encoded_image = base64.b64encode(image_bytes)
        return encoded_image.decode('utf-8')  # Convert bytes to string for transmission
    except Exception as e:
        return "Error in send_photo: " + str(e)


def process_server_response(response):
    """
    converts the string of bytes to a photo and saves it in a pre-defined path
    :param response:
    :return: nothing
    """
    try:
        if response.startswith("Error"):  # Simple check for error messages
            print(response)
        else:
            image_data = base64.b64decode(response)
            with open('c:/temp/client/received_image.jpg', 'wb') as file:
                file.write(image_data)
    except Exception as e:
        print("Error processing server response: " + str(e))
