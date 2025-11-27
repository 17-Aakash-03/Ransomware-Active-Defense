import os
import time

# Configuration
TARGET_FOLDER = "TestFolder"

def encrypt_files():
    print(f"😈 MALWARE STARTED. Targeting: {TARGET_FOLDER}")
    
    # Check if folder exists
    if not os.path.exists(TARGET_FOLDER):
        print("Target folder not found! Create 'TestFolder' first.")
        return

    # List files
    files = os.listdir(TARGET_FOLDER)
    
    for file_name in files:
        file_path = os.path.join(TARGET_FOLDER, file_name)
        
        # Only attack files
        if os.path.isfile(file_path):
            print(f"Encrypting {file_name}...")
            
            # Open file in 'append' mode
            with open(file_path, "a") as f:
                # 1. Write the malicious data
                f.write("\nENCRYPTED_CHUNK_1")
                
                # 2. FORCE Windows to notice the change NOW.
                f.flush()
                os.fsync(f.fileno()) 
                
                # 3. Wait while holding the file open.
                print("   (WAITING 10s - CATCH ME NOW!)")
                time.sleep(10.0) 
            
            # Brief pause before next file
            time.sleep(0.1) 

    print("😈 ATTACK FINISHED.")

if __name__ == "__main__":
    print("WARNING: This will modify files in 'TestFolder'.")
    choice = input("Type 'yes' to start the attack: ")
    
    if choice.lower() == "yes":
        encrypt_files()
