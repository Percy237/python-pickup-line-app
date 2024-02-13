import schedule
import time
import subprocess


# Function to execute the backup script
def execute_backup():
    print("Executing backup...")
    subprocess.run(["python", "backup.py"])


schedule.every().day.at("02:00").do(execute_backup)

while True:
    schedule.run_pending()
    time.sleep(60)
