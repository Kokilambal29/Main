import pandas as pd
import sys
import logging
import os
from datetime import datetime

# Step 1: Get current date as a string
today = datetime.today().strftime('%Y-%m-%d')

# Step 2: Create a folder with today's date if it doesn't exist
log_dir = os.path.join("/Users/apple/Downloads/Automation/Unilever/Logs", today)
os.makedirs(log_dir, exist_ok=True)

# Step 3: Define the full log file path
timestamp_str = datetime.now().strftime('%H-%M-%S')
log_filename = f"Unilever_Thailand_TEST_003_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Step 4: Set up logging to write to that file
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Add the Ground_Truth_Scripts path to sys.path
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

# Try importing and calling the Ground Truth script
try:
    import Thailand_Question_3
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

# STEP-1 Calling the Ground Truth Script
GT_df = Thailand_Question_3.Que_3()
print("Test Function Output:\n", GT_df)

# STEP-2 Placeholder for Model Script (if any)

logging.shutdown()
