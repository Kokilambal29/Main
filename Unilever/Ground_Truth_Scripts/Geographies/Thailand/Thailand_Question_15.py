import pandas as pd
import os
import logging
import matplotlib.pyplot as plt

def Que_15():
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

        for i in range(2, len(regions_df.columns)):
            pain_points = regions_df.columns[i]
            value = int(regions_df.iloc[2, i])
            regions_tot_respondents[pain_points] = value
            logging.info(f"Pain Point: {pain_points}, Total Respondents: {value}")

        table_df = pd.DataFrame(list(regions_tot_respondents.items()), columns=["Pain points", "Total Respondents"])
        print("\nDistribution of Pain Points in Greater Bangkok:")
        print(table_df.to_string(index=False))

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(regions_tot_respondents.keys(), regions_tot_respondents.values(), color='skyblue')
        plt.xlabel("Pain points", fontsize=12)
        plt.ylabel("Total Respondents", fontsize=12)
        plt.title("Total Respondents Across Regions", fontsize=14)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()

        # Save the plot
        plot_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Logs', 'PainPoints_Distribution_GreaterBangkok.png')
        plt.savefig(plot_path)
        logging.info(f"Plot saved to {plot_path}")
        plt.show()

        return table_df

    else:
        print("File does not exist:", statistics_datatable_filepath)
        logging.error(f"File does not exist: {statistics_datatable_filepath}")
        return pd.DataFrame()
