import pandas as pd
import os
import logging

def Que_5():
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

        # Use the relevant sheet
        combined_df = data_dict['All Pain Points Library- MAIN']
        combined_df = combined_df.sort_values(by="Importance/Relevance of the Need/PP for people", ascending=False)
        top_3 = combined_df.head(3)

        priority_needs = []
        for need, relevance in zip(top_3["PAIN POINT/ NEED STATEMENT"], top_3["Importance/Relevance of the Need/PP for people"]):
            priority_needs.append({"Need": need, "Relevance": relevance})
            logging.info(f"Need: {need}, Relevance: {relevance}")

        df = pd.DataFrame(priority_needs)

        print("Top 3 priority needs:")
        print(df)
        logging.info(f"\n{df}")

        return df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
