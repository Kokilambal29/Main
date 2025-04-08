import pandas as pd
import sys
import logging
import os
from datetime import datetime

# Log directory setup
today = datetime.today().strftime('%Y-%m-%d')
log_dir = os.path.join("/Users/apple/Downloads/Automation/Unilever/Logs", today)
os.makedirs(log_dir, exist_ok=True)

# Log file
timestamp_str = datetime.now().strftime('%H-%M-%S')
log_filename = f"Unilever_Thailand_TEST_15_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Setup logging
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Import Ground Truth function
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

try:
    import Thailand_Question_15
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

# Run function and capture DataFrame
GT_df = Thailand_Question_15.Que_15()
print("Test Function Output:\n", GT_df)

# Log the DataFrame output
logging.info("Test Function Output:\n" + GT_df.to_string(index=False))

# Shutdown logging
logging.shutdown()
