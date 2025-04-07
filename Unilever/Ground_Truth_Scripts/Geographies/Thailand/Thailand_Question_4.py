import pandas as pd
import os
import logging

def Que_4():
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
        region_satisfaction_avg = {}

        # Sheets: North, South, Central
        region_names = [list(data_dict.keys())[i] for i in [3, 5, 6]]

        for name in region_names:
            df = data_dict[name]
            filtered_df = df[df["CLUSTER"] == "End-to-End Convenience"]

            # Just in case formatting issues exist
            filtered_df.loc[:, "How satisfied people are with how they are currently solving the Need/PP "] = (
                filtered_df["How satisfied people are with how they are currently solving the Need/PP "]
            )

            avg_satisfaction = filtered_df["How satisfied people are with how they are currently solving the Need/PP "].mean()
            region_satisfaction_avg[name] = avg_satisfaction
            logging.info(f"{name}: {avg_satisfaction}")

        df = pd.DataFrame(list(region_satisfaction_avg.items()), columns=["Region", "Average Satisfaction"])

        print("Region-wise Average Satisfaction for 'End-to-End Convenience':")
        print(df)
        logging.info(f"\n{df}")

        return df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
