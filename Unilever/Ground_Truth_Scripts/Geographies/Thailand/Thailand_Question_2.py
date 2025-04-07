import pandas as pd
import os
import logging
import matplotlib.pyplot as plt

def Que_2():
    # Path to the Excel file (relative to this script)
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
        LSM_wise_avg = {}

        # Sheets from index 7 onward are LSM-wise
        LSM_names = list(data_dict.keys())[7:]

        for name in LSM_names:
            df = data_dict[name]
            filtered_df = df[df["CLUSTER"] == "Enhanced Cleaning"]
            filtered_df.loc[:, "Importance/Relevance of the Need/PP for people"] = pd.to_numeric(
                filtered_df["Importance/Relevance of the Need/PP for people"], errors='coerce'
            )

            avg_value = filtered_df["Importance/Relevance of the Need/PP for people"].mean()
            LSM_wise_avg[name] = avg_value
            logging.info(f"{name}: {avg_value}")

        df = pd.DataFrame(list(LSM_wise_avg.items()), columns=["LSM Group", "Average Importance/Relevance"])

        # Print and log
        print("LSM-wise Averages:")
        print(df)
        logging.info(f"\n{df}")

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(LSM_wise_avg.keys(), LSM_wise_avg.values(), color='skyblue')
        plt.xlabel("LSM Group")
        plt.ylabel("Average Importance/Relevance")
        plt.title("LSM-wise Average Importance for 'Enhanced Cleaning'")
        plt.tight_layout()

        # Save the plot
        plot_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Logs', 'LSM_plot.png')
        plt.savefig(plot_path)
        logging.info(f"Plot saved to {plot_path}")
        plt.show()

        return df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")
