import pandas as pd
import os
import logging

def Que_7():
    # Excel file path
    exceldata_filepath = os.path.join(
        os.path.dirname(__file__), '..', '..', '..',
        'Dataset', 'Geographies', 'Thailand', 'Coloured',
        '22-019734_Pain_Points Library_TH_v2_ICUO.xlsx'
    )
    exceldata_filepath = os.path.abspath(exceldata_filepath)

    print("Checking file at:", exceldata_filepath)
    logging.info(f"Checking file at: {exceldata_filepath}")

    if os.path.exists(exceldata_filepath):
        data_dict = pd.read_excel(exceldata_filepath, sheet_name=None, skiprows=3, header=0)
        combined_df = data_dict['All Pain Points Library- MAIN']

        # Compute unmet needs
        combined_df['Unmet_Needs'] = (
            combined_df["Importance/Relevance of the Need/PP for people"] -
            combined_df["How satisfied people are with how they are currently solving the Need/PP "]
        )

        combined_df = combined_df.sort_values(by='Unmet_Needs', ascending=False)
        top_5 = combined_df.head(5)

        result_df = top_5[[
            'PAIN POINT/ NEED STATEMENT',
            'Importance/Relevance of the Need/PP for people',
            'How satisfied people are with how they are currently solving the Need/PP ',
            'Unmet_Needs'
        ]]

        result_df.columns = ['Pain Point/Need Statement', 'Importance', 'Satisfaction', 'Unmet Score']

        print("Top 5 Unmet Needs:")
        print(result_df)
        logging.info("\nTop 5 Unmet Needs:\n%s", result_df)

        return result_df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
