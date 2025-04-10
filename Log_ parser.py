import re
import os
import time

LOG_FILE = "logs/toastcake.log"
ANOMALY_THRESHOLD = 100

def parse_logs():
    error_count = {}
    with open(LOG_FILE, "r") as file:
        for line in file:
            match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (ERROR|WARNING) \| (.+)", line)
            if match:
                timestamp, level, message = match.groups()
                error_count[message] = error_count.get(message, 0) + 1
                if error_count[message] > ANOMALY_THRESHOLD:
                    print(f"⚠️ Anomaly Detected: '{message}' occurred {error_count[message]} times!")

                    # Attempt auto-fix
                    auto_fix(message)

    print("--- Monitoring logs again in 10 seconds ---")
    time.sleep(10)
    parse_logs()

def auto_fix(error_message):
    if "Failed to load module" in error_message:
        print("🔧 Attempting to reload module...")
        os.system("python -m toastcake_core --reload")
    elif "Low battery" in error_message:
        print("🔋 Alert: Consider connecting to power.")
    else:
        print("❌ No fix available.")

parse_logs()
