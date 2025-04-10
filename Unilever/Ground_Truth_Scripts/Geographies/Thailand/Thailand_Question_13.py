import pandas as pd
import os
import logging

def Que_13():
    # Statistics file path
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

        # Extract gender counts from the "Respondent gender" sheet
        genders_df = statistics_df['Respondent gender']
        male = genders_df.loc[2, 'Total']
        female = genders_df.loc[3, 'Total']

        # Log and print results
        print(f"Male Surveyed: {male}\nFemale Surveyed: {female}")
        logging.info(f"Male Surveyed: {male}\nFemale Surveyed: {female}")

        # Return result as DataFrame
        result_df = pd.DataFrame({
            'Gender': ['Male', 'Female'],
            'Count': [male, female]
        })
        return result_df

    else:
        print("File does not exist:", statistics_datatable_filepath)
        logging.error(f"File does not exist: {statistics_datatable_filepath}")
        return pd.DataFrame()
