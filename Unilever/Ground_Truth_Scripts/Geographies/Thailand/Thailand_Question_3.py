import pandas as pd
import os
import logging

def Que_3():
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

        freq_record = {}
        sorted_df = data_dict['Greater Bangkok'].sort_values(
            by="Frequency per year of experienced PP/Need ", ascending=False
        )

        for i in range(5):
            pp = sorted_df.iloc[i]["PAIN POINT/ NEED STATEMENT"]
            freq = sorted_df.iloc[i]["Frequency per year of experienced PP/Need "]
            freq_record[pp] = freq
            logging.info(f"{pp}: {freq}")

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(list(freq_record.items()), columns=["Pain Point", "Frequency"])

        # Print and log nicely
        print("Top 5 Pain Points in Greater Bangkok:")
        print(df)
        logging.info("\nTop 5 Pain Points in Greater Bangkok:\n%s", df.to_string(index=False))

        return df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
