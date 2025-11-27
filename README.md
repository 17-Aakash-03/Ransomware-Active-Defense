Real-time Active Defense System Against Ransomware

 Project Overview

This is a proactive cybersecurity defense system designed to detect and block ransomware attacks in real-time. Unlike traditional antiviruses that rely on signatures, this system monitors file system behavior and uses "honeypots" (decoy files) to identify malicious encryption attempts.

 Key Features

Honeypot Traps: Deploys decoy files in strategic locations. If these files are modified, the system instantly flags it as an attack.

Real-time Monitoring: Continuously watches file system events (Read/Write/Modify).

Automated Response: Immediately kills the suspicious process to prevent further data loss.

Entropy Analysis: Analyzes file entropy to detect encryption (randomness) in file structures.

🛠️ Tech Stack

Language: Python

Libraries: watchdog (for monitoring), psutil (for process management), scikit-learn (for ML models), tkinter (for the UI).

Operating System: Windows / Linux compatible.

 How to Run

Clone the repository:

git clone [https://github.com/17-Aakash-03/Ransomware-Active-Defense.git](https://github.com/17-Aakash-03/Ransomware-Active-Defense.git)


Navigate to the project folder:

cd ActiveDefence_project


Install dependencies (if listed in a requirements file) or manually install needed libraries:

pip install watchdog psutil pandas scikit-learn


Run the main script:

python main.py


Disclaimer

This tool is for educational and defensive purposes only. Do not use this code to develop malware.
