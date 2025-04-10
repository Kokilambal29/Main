import pandas as pd
import os
import logging

def Que_6():
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
        unique_pp = combined_df['PAIN POINT/ NEED STATEMENT'].dropna().unique()

        sorted_pp_dict = {}
        for pp in unique_pp:
            pp_df = combined_df[combined_df['PAIN POINT/ NEED STATEMENT'] == pp]
            avg = pp_df['How satisfied people are with how they are currently solving the Need/PP '].mean()
            sorted_pp_dict[pp] = avg

        sorted_pp_df = pd.DataFrame(
            sorted_pp_dict.items(),
            columns=["PAIN POINT/ NEED STATEMENT", "How satisfied people are with how they are currently solving the Need/PP "]
        )

        sorted_pp_df = sorted_pp_df.sort_values(
            by="How satisfied people are with how they are currently solving the Need/PP ",
            ascending=True
        )

        top_5 = sorted_pp_df.head(5)

        logging.info("Top 5 Pain Points with Lowest Satisfaction:")
        logging.info(f"\n{top_5}")

        print("Top 5 Pain Points with Lowest Satisfaction:")
        print(top_5)

        return top_5
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
        return pd.DataFrame()
