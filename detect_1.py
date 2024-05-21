import subprocess
import time
import os

def is_hdmi_disconnected():
    try:
        xrandr_output = subprocess.check_output("xrandr", shell=True).decode("utf-8")
        return "disconnected" in xrandr_output
    except subprocess.CalledProcessError:
        return False

def terminate():
    subprocess.run(["python3", "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/cleanup.py"])
    subprocess.run(["sudo", "su"])

if __name__ == "__main__":
    while True:
        if not is_hdmi_disconnected():
            terminate()
            break
        time.sleep(2)# check every 2 seconds
#        print("........")