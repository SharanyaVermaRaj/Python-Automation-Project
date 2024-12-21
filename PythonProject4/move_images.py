import os
import shutil
import glob
import logging
from logging import exception

logging.basicConfig(filename="file_automation_log.txt",level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info("Started")
def check_folder_exists(folder_path):
    """Check if a folder exists.If not ,log an error."""
    if not os.path.isdir(folder_path):
        logging.error(f"Folder {folder_path} does not exist")
        raise FileNotFoundError(f"Folder {folder_path} does not exist")
    else:
        logging.info(f"Folder {folder_path} exists")

source_folder = os.path.expanduser("~/Downloads")
destination_folder = os.path.expanduser("~/Desktop/Presentation Images")

try:
    check_folder_exists(source_folder)
    check_folder_exists(destination_folder)

    images = glob.glob(os.path.join(source_folder, "*.jpg")) + glob.glob(os.path.join(source_folder,"*.jpeg")) + glob.glob(os.path.join(source_folder,"*.png"))
    for image in images:
        try:
            shutil.move(image, destination_folder)
            logging.info(f"Moving {image} to {destination_folder}")
        except Exception as e:
            logging.error(f"Failed to move {image} to {destination_folder}")

except FileNotFoundError as e:
    logging.error(str(e))
except Exception() as e:
    logging.error(f"An unexpected error occurred: {str(e)}")



print("Done")


