import shutil
import os
import datetime

database_path = (
    r"C:\Users\Tsembom Percy\Documents\Dev\Python\Rizz Like Percy\db.sqlite3"
)
backup_location = r"C:\Users\Tsembom Percy\Documents\Dev\Python\Rizz Like Percy\backups"

if not os.path.exists(backup_location):
    os.makedirs(backup_location)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

backup_file = f"backup_{timestamp}.db"

source_file_path = database_path
backup_file_path = os.path.join(backup_location, backup_file)

shutil.copyfile(source_file_path, backup_file_path)

print(f"Backup successful: {backup_file_path}")
