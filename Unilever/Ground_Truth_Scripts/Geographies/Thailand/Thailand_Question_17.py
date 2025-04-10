import pandas as pd
import os
import logging

def Que_17():
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
        urban_rural_df = statistics_df['Urban_Rural']

        urban_row = urban_rural_df[urban_rural_df['Category'] == 'URBAN']
        rural_row = urban_rural_df[urban_rural_df['Category'] == 'RURAL']

        urban_total = int(urban_row['Total'].values[0])
        rural_total = int(rural_row['Total'].values[0])

        total_respondents = {
            'Urban': urban_total,
            'Rural': rural_total
        }

        print("\nUrban vs Rural Respondents:")
        print(total_respondents)
        logging.info(f"Urban: {urban_total}, Rural: {rural_total}")

        result_df = pd.DataFrame(list(total_respondents.items()), columns=["Region Type", "Total Respondents"])
        return result_df

    else:
        print("File does not exist:", statistics_datatable_filepath)
        logging.error(f"File does not exist: {statistics_datatable_filepath}")
        return pd.DataFrame()
