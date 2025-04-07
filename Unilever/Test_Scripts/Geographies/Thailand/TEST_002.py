import pandas as pd
import sys
import logging
import os
from datetime import datetime

# Step 1: Get current date
today = datetime.today().strftime('%Y-%m-%d')

# Step 2: Create logs folder
log_dir = os.path.join("/Users/apple/Downloads/Automation/Unilever/Logs", today)
os.makedirs(log_dir, exist_ok=True)

# Step 3: Log filename with timestamp
timestamp_str = datetime.now().strftime('%H-%M-%S')
log_filename = f"Unilever_Thailand_TEST_002_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Step 4: Set up logging
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Load the ground truth script
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

try:
    import Thailand_Question_2
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

# STEP-1 Run Ground Truth Script
GT_df = Thailand_Question_2.Que_2()
print("Test Function Output:\n", GT_df)

# STEP-2 placeholder

logging.shutdown()
