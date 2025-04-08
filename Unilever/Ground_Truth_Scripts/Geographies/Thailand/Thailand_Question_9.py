import pandas as pd
import os
import logging

def Que_9():
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
        LSM_names = list(data_dict.keys())[7:]

        results = []

        for name in LSM_names:
            df = data_dict[name]
            df = df.dropna(subset=["% of people for whom the PP/Need applies"])
            df = df.sort_values(by="% of people for whom the PP/Need applies", ascending=False)
            top_5 = df.head(5)

            for _, row in top_5.iterrows():
                need = row["PAIN POINT/ NEED STATEMENT"]
                penetration = row["% of people for whom the PP/Need applies"]
                results.append({
                    "LSM Group": name,
                    "Pain Point/Need Statement": need,
                    "Penetration (%)": penetration
                })
                logging.info(f"LSM: {name}, Need: {need}, Penetration: {penetration}")

        result_df = pd.DataFrame(results)
        print("Top 5 Pain Points for Each LSM Group by Penetration:\n", result_df)

        return result_df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
