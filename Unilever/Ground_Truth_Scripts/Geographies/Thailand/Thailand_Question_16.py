import pandas as pd
import os
import logging

def Que_16():
    # Excel file path
    statistics_datatable_filepath = os.path.join(
        os.path.dirname(__file__), '..', '..', '..',
        'Dataset', 'Geographies', 'Thailand', 'Colourless',
        '2201972801_Pain_Points_TH_V2_BAN_1_NoSigTest_unw_1_processed.xlsx'
    )
    statistics_datatable_filepath = os.path.abspath(statistics_datatable_filepath)

    print("Checking file at:", statistics_datatable_filepath)
    logging.info(f"Checking file at: {statistics_datatable_filepath}")

    if os.path.exists(statistics_datatable_filepath):
        statistics_df = pd.read_excel(statistics_datatable_filepath, sheet_name=None)
        methodsofwashing_df = statistics_df['Method of Washing']

        net_machine_washers_row = methodsofwashing_df[methodsofwashing_df['Category'] == 'NET Machine Washers']
        net_hand_washers_row = methodsofwashing_df[methodsofwashing_df['Category'] == 'NET Hand Washers']

        machine_washers_total = int(net_machine_washers_row['Total'].values[0])
        hand_washers_total = int(net_hand_washers_row['Total'].values[0])

        total_respondents = {
            'Machine washers': machine_washers_total,
            'Hand washers': hand_washers_total
        }

        for category, count in total_respondents.items():
            print(f"{category}: {count}")
            logging.info(f"{category}: {count}")

        df_result = pd.DataFrame(list(total_respondents.items()), columns=["Washing Method", "Total Respondents"])
        return df_result

    else:
        print("File does not exist:", statistics_datatable_filepath)
        logging.error(f"File does not exist: {statistics_datatable_filepath}")
        return pd.DataFrame()
