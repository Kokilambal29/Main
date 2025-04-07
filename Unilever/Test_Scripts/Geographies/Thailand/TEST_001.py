import pandas as pd
import sys
import logging
import os
from datetime import datetime

# Step 1: Get current date as a string
today = datetime.today().strftime('%Y-%m-%d')

# Step 2: Create a folder with today's date if it doesn't exist
log_dir = os.path.join(r"D:\Automation\Unilever\Logs", today)
os.makedirs(log_dir, exist_ok=True)

# Step 3: Define the full log file path
timestamp_str = datetime.now().strftime('%H-%M-%S')
log_filename = f"Unilever_Thailand_TEST_001_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Step 4: Set up logging to write to that file
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Get the absolute path of the script directory
script_dir = r"D:\Automation\Unilever\Ground_Truth_Scripts\Geographies\Thailand"

if script_dir:
    sys.path.insert(0, script_dir)
    try:
        import Thailand_Question_1
    except ModuleNotFoundError:
        print(f"Module not found in {script_dir}")
else:
    print("Environment variable THAILAND_SCRIPT_PATH is not set.")


#STEP-1 Calling the Ground Truth Scripts

GT_df = Thailand_Question_1.Que_1()
print("Test Function", GT_df)


#STEP-2 Calling the Model Scripts


logging.shutdown()
