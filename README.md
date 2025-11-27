Real-Time Active Defense System Against Ransomware
About the Project
This project is a Behavioral Active Defense System designed to stop ransomware attacks in their tracks. Unlike traditional antivirus software that relies on "signatures" (databases of known viruses), this system monitors the behavior of files in real-time.
If any process attempts to modify multiple files rapidly (a common ransomware behavior), this system acts as a digital guard: it instantly identifies the malicious process and terminates it before it can encrypt your data.
Problems Solved
This project addresses three critical failures in traditional cybersecurity:
1.	Zero-Day Attacks: Traditional antiviruses cannot stop new, unknown ransomware because they don't have a signature for it yet. This project solves that by ignoring signatures and looking for bad behavior instead.
2.	Latency: Human reaction time is too slow to stop a ransomware attack once it starts. This system reacts autonomously in milliseconds.
3.	Data Loss: By acting instantly, the system limits the damage to just 1 or 2 files before the threat is neutralized, rather than losing the entire hard drive.
How It Works (The Logic)
The system operates on a "Detect → Hunt → Kill" cycle:
1.	Monitor: The system uses the watchdog library to watch a specific directory for "Modified" events.
2.	Analyze: It counts how many files are changed within a short time window (e.g., 3 files in 100ms).
3.	Hunt: If the threshold is breached, it uses psutil to scan all running processes and find which Process ID (PID) is holding those files open.
4.	Kill: It checks if the PID is on a "Whitelist" (like Notepad or Explorer). If not, it issues a kill() command to terminate the process immediately.
Results
•	Reaction Time: The system successfully detects high-frequency file changes within milliseconds.
•	Success Rate: In simulated tests (using a dummy attacker script), the system successfully terminated the attacker process 100% of the time after the 3rd file modification.
•	False Positives: Safe applications (like Notepad) were added to a whitelist to prevent accidental termination.
Tech Stack
•	Language: Python 3.x
•	File Monitoring: watchdog library
•	Process Management: psutil library
•	Environment: Tested on Windows 10 (VirtualBox)
How to Run
Prerequisites: You need Python installed.
1.	Clone the Repository:
2.	git clone [https://github.com/17-Aakash-03/Ransomware-Active-Defense.git](https://github.com/17-Aakash-03/Ransomware-Active-Defense.git)
3.	cd Ransomware-Active-Defense
4.	Install Required Libraries:
5.	pip install watchdog psutil
6.	Run the Guard (The Defense): Open a terminal and run:
7.	python RealTimeGuard.py
The system is now watching your folder.
8.	Run the Simulation (The Attack): Open a separate terminal window and run:
9.	python attacker.py
Follow the prompts to start the dummy attack and watch the Guard stop it!
Disclaimer
This tool is for educational purposes only. The "attacker" script provided here is harmless and only writes text to files to simulate activity. Do not use the concepts in this code to create malicious software.

