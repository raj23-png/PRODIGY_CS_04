import threading
import time
import os

# File to store the logged keystrokes
log_file = "key_log.txt"

# Keylogger function
def keylogger():
    print("Press 'ESC' to stop logging.")
    keys = []
    while True:
        try:
            key = input()
            keys.append(key)
            if key == 'esc':
                break
            with open(log_file, "a") as file:
                file.write(f"{key}\n")
        except KeyboardInterrupt:
            break

    # Write all keys to file at the end
    with open(log_file, "a") as file:
        for key in keys:
            file.write(f"{key}\n")

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=keylogger)
keylogger_thread.start()

# Let the keylogger run for a specified duration
time.sleep(30)  # Example duration: 30 seconds
os._exit(0)

