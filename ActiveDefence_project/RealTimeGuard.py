import time
import sys
import os
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
DIRECTORY_TO_WATCH = "." 
THRESHOLD = 3 
# CHANGED: Increased to 100 seconds so it doesn't forget the count
TIME_WINDOW = 100 

# --- WHITELIST ---
WHITELIST = ["explorer.exe", "notepad.exe", "svchost.exe"]

class ActiveDefenseHandler(FileSystemEventHandler):
    def __init__(self):
        self.modification_count = 0
        self.start_time = time.time()

    def find_and_kill_process(self, file_path):
        print(f"🔍 Hunting for process touching: {file_path}")
        
        for proc in psutil.process_iter(['pid', 'name', 'open_files']):
            try:
                if proc.info['open_files']:
                    for open_file in proc.info['open_files']:
                        if open_file.path == os.path.abspath(file_path):
                            
                            proc_name = proc.info['name']
                            proc_pid = proc.info['pid']

                            if proc_name in WHITELIST:
                                print(f"🛡️ Safe process detected ({proc_name}). Skipping.")
                                return

                            print(f"------------------------------------------------")
                            print(f"⚔️ MALWARE DETECTED: {proc_name} (PID: {proc_pid})")
                            print(f"🚫 TERMINATING PROCESS IMMEDIATELY...")
                            proc.kill() 
                            print(f"✅ Threat Neutralized.")
                            print(f"------------------------------------------------")
                            return

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass 

    def on_modified(self, event):
        if event.is_directory:
            return

        current_time = time.time()
        
        if current_time - self.start_time > TIME_WINDOW:
            self.modification_count = 0
            self.start_time = current_time
        
        self.modification_count += 1
        print(f"[INFO] File modified: {event.src_path}")

        if self.modification_count >= THRESHOLD:
            print("!!! ALERT: High frequency modifications detected !!!")
            self.find_and_kill_process(event.src_path)
            # Do not reset counter immediately to ensure we keep hunting if misses
            # self.modification_count = 0 

if __name__ == "__main__":
    print(f"🛡️ ACTIVE DEFENSE SYSTEM ONLINE")
    print(f"Monitoring: {os.path.abspath(DIRECTORY_TO_WATCH)}")
    
    event_handler = ActiveDefenseHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DIRECTORY_TO_WATCH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
