import os
from extraction import *

def save_dataframe_as_csv(dataframe, folder_path, file_name):
    csv_file_path = os.path.join(folder_path, f"{file_name}.csv")
    dataframe.to_csv(csv_file_path, index=False)
    
def save_all_dataframes_as_csv():
    
    directory_path = r"D:\Phonepe Pulse"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    folder_name = "miscellaneous"
    folder_path = os.path.join(directory_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    save_dataframe_as_csv(aggregated_transcation_state(), folder_path, "aggregated_transcation_state")
    save_dataframe_as_csv(aggregated_user_state(), folder_path, "aggregated_user_state")
    save_dataframe_as_csv(map_transcation_state(), folder_path, "map_transcation_state")
    save_dataframe_as_csv(map_user_state(), folder_path, "map_user_state")
    save_dataframe_as_csv(top_transcation_state(), folder_path, "top_transcation_state")
    save_dataframe_as_csv(top_user_state(), folder_path, "top_user_state")
    save_dataframe_as_csv(top_transcation_state_pincode(), folder_path, "top_transcation_state_pincode")
    save_dataframe_as_csv(top_user_state_pincode(), folder_path, "top_user_state_pincode")
    
save_all_dataframes_as_csv()

