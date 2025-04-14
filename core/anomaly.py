
import random
def detect():
    chance = random.randint(1, 10)
    if chance == 1:
        return "Suspicious activity detected."
    return "No anomaly detected."
