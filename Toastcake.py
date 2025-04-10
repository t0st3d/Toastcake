import log_parser
import time
import toastcake_core
import os
from threading import Thread
from flask import Flask

TEST_MODE = os.getenv("TOASTCAKE_TEST", "false").lower() == "true"

if TEST_MODE:
    print("🚀 Running in Test Mode. No real data will be affected!")

LOG_FILE = "toastcake.log"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Toastcake Web Interface</h1><p>System is running...</p>"

def run_web_interface():
    app.run(host="0.0.0.0", port=5000, debug=False)  # Accessible over local network

def monitor_logs():
    print("🔍 Toastcake Log Monitor Running...")

    last_log_size = 0  # Track changes in file size

    try:
        while True:
            with open(LOG_FILE, "r") as log_file:
                log_data = log_file.read()

            if len(log_data) > last_log_size:  # Only process new logs
                log_parser.parse_logs(log_data)
                last_log_size = len(log_data)
                print("✅ Log updated, checking for anomalies...")

            # Clear old logs (keep last 100 lines)
            with open(LOG_FILE, "r") as log_file:
                lines = log_file.readlines()

            with open(LOG_FILE, "w") as log_file:
                log_file.writelines(lines[-100:])  # Keep last 100 lines

            print("⏳ Waiting 10 seconds before the next check...")
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n🛑 Log monitoring stopped by user.")

def chat_response(user_input):
    responses = {
        "hello": "Hey there! How can I help?",
        "how are you": "I'm running at full efficiency!",
        "what is toastcake": "Toastcake is a personal AI designed for monitoring and assistance.",
        "exit": "Goodbye!"
    }
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm still learning. Can you rephrase that?"

def chat_loop():
    print("💬 Toastcake Chat Mode. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        print("Toastcake:", chat_response(user_input))

if __name__ == "__main__":
    # Start log monitoring in a separate thread
    log_thread = Thread(target=monitor_logs, daemon=True)
    log_thread.start()

    # Start web interface in a separate thread
    web_thread = Thread(target=run_web_interface, daemon=True)
    web_thread.start()

    # Start chatbot interaction
    chat_loop()
