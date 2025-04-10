import pandas as pd
import os
import logging
import matplotlib.pyplot as plt
from datetime import datetime

def Que_8():
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

        region_sustainability_avg = {}
        region_names = list(data_dict.keys())[2:7]  # Adjust index as needed

        for name in region_names:
            df = data_dict[name]
            filtered_df = df[df["CLUSTER"] == "Sustainability"]
            filtered_df.loc[:, "Importance/Relevance of the Need/PP for people"] = pd.to_numeric(
                filtered_df["Importance/Relevance of the Need/PP for people"], errors='coerce'
            )
            avg_importance = filtered_df["Importance/Relevance of the Need/PP for people"].mean()
            region_sustainability_avg[name] = avg_importance
            logging.info(f"{name}: {avg_importance}")

        result_df = pd.DataFrame(
            list(region_sustainability_avg.items()),
            columns=["Region", "Average Importance"]
        )

        print("Region-wise Average Importance for Sustainability:")
        print(result_df)
        logging.info(f"\n{result_df}")

        # Save the plot
        today = datetime.today().strftime('%Y-%m-%d')
        timestamp = datetime.now().strftime('%H-%M-%S')
        log_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Logs', today)
        os.makedirs(log_dir, exist_ok=True)
        plot_path = os.path.join(log_dir, f"Thailand_Question_8_Sustainability_{timestamp}.png")

        plt.figure(figsize=(10, 6))
        plt.bar(region_sustainability_avg.keys(), region_sustainability_avg.values(), color='seagreen')
        plt.xlabel("Regions")
        plt.ylabel("Average Importance/Relevance Index")
        plt.title("Region-wise Average Importance for Sustainability")
        plt.tight_layout()
        plt.savefig(plot_path)
        logging.info(f"Plot saved to {plot_path}")
        plt.show()

        return result_df
    else:
        print("File does not exist:", exceldata_filepath)
        logging.error(f"File does not exist: {exceldata_filepath}")

