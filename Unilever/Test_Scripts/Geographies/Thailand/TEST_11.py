import pandas as pd
import sys
import logging
import os
from datetime import datetime

# Setup log directory
today = datetime.today().strftime('%Y-%m-%d')
log_dir = os.path.join("/Users/apple/Downloads/Automation/Unilever/Logs", today)
os.makedirs(log_dir, exist_ok=True)

# Log file setup
timestamp_str = datetime.now().strftime('%H-%M-%S')
log_filename = f"Unilever_Thailand_TEST_011_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Add path for GT script import
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

try:
    import Thailand_Question_11
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

# Run GT function
GT_df = Thailand_Question_11.Que_11()
print("Test Function Output:\n", GT_df)

# Shutdown logging
logging.shutdown()
