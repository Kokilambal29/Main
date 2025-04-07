import pandas as pd
import os


def Que_1():

    exceldata_filepath = r'D:\Automation\Unilever\Dataset\Geographies\Thailand\Coloured\22-019734_Pain_Points Library_TH_v2_ICUO.xlsx'
    if os.path.exists(exceldata_filepath):
        data_dict = pd.read_excel(exceldata_filepath, sheet_name=None, skiprows=3, header=0)
        region_avg = {}
        
        region_names = list(data_dict.keys())[2:7]

        for name in region_names:
            df = data_dict[name]
            filtered_df = df[df["CLUSTER"] == "Proactive Care "]
            filtered_df.loc[:, "% of people for whom the PP/Need applies"] = filtered_df["% of people for whom the PP/Need applies"].astype(str).str.rstrip("%").astype(float)

            region_avg[name] = float(filtered_df["% of people for whom the PP/Need applies"].mean())

        df = pd.DataFrame(list(region_avg.items()), columns=['Region', 'Value'])
        print(df)
        return df
    else:
        print("File does not exist:", exceldata_filepath)

