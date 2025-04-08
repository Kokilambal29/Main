import pandas as pd
import os
import logging
import matplotlib.pyplot as plt

def Que_14():
    # Excel file path
    statistics_datatable_filepath = os.path.join(
        os.path.dirname(__file__), '..', '..', '..',
        'Dataset', 'Geographies', 'Thailand', 'Colourless',
        '2201972801_Pain_Points_TH_V2_BAN_1_NoSigTest_unw_1_processed.xlsx'
    )
    statistics_datatable_filepath = os.path.abspath(statistics_datatable_filepath)

    print("Checking file at:", statistics_datatable_filepath)
    logging.info(f"Checking file at: {statistics_datatable_filepath}")

    if os.path.exists(statistics_datatable_filepath):
        statistics_df = pd.read_excel(statistics_datatable_filepath, sheet_name=None)
        regions_df = statistics_df['Respondent region']
        regions_tot_respondents = {}

        for i in range(2, len(regions_df)):
            region = regions_df.iloc[i, 0]
            total_respondents = regions_df.loc[i, 'Total']
            regions_tot_respondents[region] = total_respondents
            logging.info(f"Region: {region}, Total Respondents: {total_respondents}")

        print("\nTotal Respondents by Region:")
        print(regions_tot_respondents)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(regions_tot_respondents.keys(), regions_tot_respondents.values(), color='skyblue')
        plt.xlabel("Regions")
        plt.ylabel("Total respondents")
        plt.title("Total respondents across regions")
        plt.tight_layout()

        # Save the plot
        plot_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Logs', 'Respondents_by_Region_Plot.png')
        plt.savefig(plot_path)
        logging.info(f"Plot saved to {plot_path}")
        plt.show()

        # Convert dict to DataFrame
        df_result = pd.DataFrame(list(regions_tot_respondents.items()), columns=['Region', 'Total Respondents'])
        return df_result

    else:
        print("File does not exist:", statistics_datatable_filepath)
        logging.error(f"File does not exist: {statistics_datatable_filepath}")
        return pd.DataFrame()
