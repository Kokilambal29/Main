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
log_filename = f"Unilever_Thailand_TEST_14_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Step 4: Set up logging
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Step 5: Load the ground truth script
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

try:
    import Thailand_Question_14
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

# Step 6: Run Ground Truth Script
GT_df = Thailand_Question_14.Que_14()
print("Test Function Output:\n", GT_df)

# Step 7: Log the DataFrame output
logging.info("Test Function Output:\n" + GT_df.to_string(index=False))

# Step 8: Shutdown logging
logging.shutdown()
