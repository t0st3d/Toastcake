
import time
from .logger import log_data
from .anomaly import detect
from .chat_commands import parse_command

def run_loop():
    print("[Toastcake] Core AI initialized.")
    while True:
        log_data()
        anomaly = detect()
        if anomaly != "No anomaly detected.":
            print("[Anomaly] Detected:", anomaly)
        time.sleep(5)
