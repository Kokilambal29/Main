import pandas as pd
import os
import logging

def Que_10():
    # Define Excel file path
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
        combined_df = combined_df.sort_values(by="% of people for whom the PP/Need applies", ascending=False)
        top_5 = combined_df.head(5)

        top_needs = []
        for need, penetration in zip(top_5["PAIN POINT/ NEED STATEMENT"], top_5["% of people for whom the PP/Need applies"]):
            top_needs.append({"Need": need, "Penetration": penetration})
            logging.info(f"Need: {need}, Penetration: {penetration}")

        df = pd.DataFrame(top_needs)

        print("Top 5 high incidence needs:")
        print(df)
        logging.info(f"\n{df}")

        return df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
