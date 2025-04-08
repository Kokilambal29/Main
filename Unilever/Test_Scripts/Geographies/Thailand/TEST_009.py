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
log_filename = f"Unilever_Thailand_TEST_009_{today}_{timestamp_str}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Add Ground Truth Script path
script_dir = "/Users/apple/Downloads/Automation/Unilever/Ground_Truth_Scripts/Geographies/Thailand"
sys.path.insert(0, script_dir)

# Import and run the GT function
try:
    import Thailand_Question_9
except ModuleNotFoundError:
    print(f"Module not found in {script_dir}")
    logging.error(f"Module not found in {script_dir}")
    sys.exit(1)

try:
    GT_df = Thailand_Question_9.Que_9()
    print("GT Output for Question 10:\n", GT_df)
    logging.info(f"\n{GT_df}")
except Exception as e:
    print(f"Error during execution: {str(e)}")
    logging.error(f"Execution Error: {str(e)}")

logging.shutdown()
