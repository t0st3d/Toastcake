...m.termux/files/home/toastcake/toastcake.py
import log_parser
import time
import toastcake_core

if __name__ == "__main__":
    print("🔍 Toastcake Log Monitor Running...")

    last_log_size = 0  # Track changes in file size

    while True:
        with open("toastcake.log", "r") as log_file:
            log_data = log_file.read()

        if len(log_data) > last_log_size:  # Only pro>
            log_parser.parse_logs(log_data)
            last_log_size = len(log_data)
            print("✅ Log updated, checking for anoma>

        # Clear old logs (keep last 100 lines)
        with open("toastcake.log", "r") as log_file:
            lines = log_file.readlines()

        with open("toastcake.log", "w") as log_file:
            log_file.writelines(lines[-100:])  # Keep>

        print("⏳ Waiting 10 seconds before the next >
        time.sleep(10)  # Slow down the loop
time.sleep(10)  # Slow down the loop

def chat_response(user_input):
    responses = {
        "hello": "Hey there! How can I help?",
        "how are you": "I'm running at full efficienc>
        "what is toastcake": "Toastcake is a personal>
        "exit": "Goodbye!"
    }
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm still learning. Can you rephrase that>

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Toastcake:", chat_response(user_input))

