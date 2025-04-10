import pandas as pd
import os
import logging

def Que_12():
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
        region_names = list(data_dict.keys())[7:]

        results = []

        for name in region_names:
            df = data_dict[name]
            df = df.sort_values(by='How satisfied people are with how they are currently solving the Need/PP ', ascending=True)
            top_5 = df.head(5)

            for need, satisfaction in zip(top_5["PAIN POINT/ NEED STATEMENT"], top_5["How satisfied people are with how they are currently solving the Need/PP "]):
                print(f"LSM Group: {name}, Need: {need}, Satisfaction: {satisfaction}")
                logging.info(f"LSM Group: {name}, Need: {need}, Satisfaction: {satisfaction}")
                results.append({
                    "LSM Group": name,
                    "Pain Point/Need Statement": need,
                    "Satisfaction": satisfaction
                })

        result_df = pd.DataFrame(results)
        print("\nTop 5 least satisfaction pain points by LSM group:")
        print(result_df)
        logging.info(f"\n{result_df}")

        return result_df

    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
        return pd.DataFrame()
