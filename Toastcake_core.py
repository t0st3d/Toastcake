import re

def parse_logs(log_data):
    """Processes log data using regex for anomaly detection."""
    patterns = {
        "error": r"ERROR: (.+)",  # Captures error messages
        "warning": r"WARNING: (.+)",  # Captures warnings
        "command": r"\[(\w+)\]: (.+)",  # Captures command-like patterns
    }
    
    findings = {}
    
    for key, pattern in patterns.items():
        matches = re.findall(pattern, log_data)
        if matches:
            findings[key] = matches
    
    return findings

def chat_response(user_input):
    """Handles user input and returns an appropriate response."""
    responses = {
        "hello": "Hey there! How can I assist you?",
        "status": "Toastcake is running optimally.",
        "exit": "Shutting down..."
    }
    
    for key, response in responses.items():
        if re.search(rf"\b{key}\b", user_input, re.IGNORECASE):
            return response
    
    return "I'm still learning. Can you rephrase that?"

def test_function():
    """Returns a confirmation that Toastcake Core is loaded."""
    return "✅ Toastcake Core Loaded!"
