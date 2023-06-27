import os
import json
import pandas as pd

def aggregated_transcation_state():
    
    aggr_trans_st_path = r"D:\Phonepe Pulse\clone\data\aggregated\transaction\country\india\state"
    aggr_trans_st_dir = os.listdir(aggr_trans_st_path)
    
    aggr_trans_dict = {
                        'state':[],
                        'year':[],
                        'quater':[],
                        'transacion_type':[],
                        'transacion_count':[],
                        'transacion_amount':[]
                      }

    for state in aggr_trans_st_dir:
            state_path = f"{aggr_trans_st_path}\\{state}\\"
            state_years = os.listdir(state_path)
            for year in state_years:
                state_year_path = f"{state_path}{year}\\"
                json_files = os.listdir(state_year_path)
                for json_file in json_files:
                    json_file_path = state_year_path + json_file
                    read_json= open(json_file_path, 'r')
                    load_json = json.load(read_json)
                    
                    try:
                        for data in load_json['data']['transactionData']:
                            name = data['name']
                            count = data['paymentInstruments'][0]['count']
                            amount = data['paymentInstruments'][0]['amount']
                            aggr_trans_dict['transacion_type'].append(name.replace('-', '').lower())
                            aggr_trans_dict['transacion_count'].append(count)
                            aggr_trans_dict['transacion_amount'].append(amount)
                            aggr_trans_dict['state'].append(state.replace('-', ' '))
                            aggr_trans_dict['year'].append(year)
                            aggr_trans_dict['quater'].append('q'+ json_file.strip('.json'))
                            
                    except Exception as e:
                        print(f"Problem occured while extracting: {str(e)}")

    aggr_trans_df = pd.DataFrame(aggr_trans_dict)
    return aggr_trans_df

def aggregated_user_state():
    
    aggr_usr_st_path = r"D:\Phonepe Pulse\clone\data\aggregated\user\country\india\state"
    aggr_usr_st_dir = os.listdir(aggr_usr_st_path)
    
    aggr_user_dict = {
                        'state': [], 
                        'year': [], 
                        'quater': [], 
                        'brand': [],
                        'brand_count': [], 
                        'brand_percentage': []
                    }
    
    for state in aggr_usr_st_dir:
            state_path = f"{aggr_usr_st_path}\\{state}\\"
            state_years = os.listdir(state_path)
            for year in state_years:
                state_year_path = f"{state_path}{year}\\"
                json_files = os.listdir(state_year_path)
                for json_file in json_files:
                    json_file_path = state_year_path + json_file
                    read_json= open(json_file_path, 'r')
                    load_json = json.load(read_json)
                    
                    try:
                        for data in load_json['data']['usersByDevice']:
                            brand = data['brand']
                            count = data['count']
                            percentage = data['percentage']
                            aggr_user_dict['brand'].append(brand.lower())
                            aggr_user_dict['brand_count'].append(count)
                            aggr_user_dict['brand_percentage'].append(percentage)
                            aggr_user_dict['state'].append(state.replace('-', ' '))
                            aggr_user_dict['year'].append(year)
                            aggr_user_dict['quater'].append('q'+ json_file.strip('.json'))
                            
                    except Exception as e:
                        pass
                        
    aggr_usr_df = pd.DataFrame(aggr_user_dict)
    return aggr_usr_df

def map_transcation_state():
    
    map_trans_st_path = r"D:\Phonepe Pulse\clone\data\map\transaction\hover\country\india\state"
    map_trans_st_dir = os.listdir(map_trans_st_path)
    
    map_trans_dict = {
                        'state': [], 
                        'year': [], 
                        'quater': [], 
                        'district': [],
                        'transaction_count': [], 
                        'transaction_amount': []
                    }

    for state in map_trans_st_dir:
                state_path = f"{map_trans_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)

                        try:
                            for data in load_json['data']["hoverDataList"]:
                                district = data['name']
                                count = data['metric'][0]['count']
                                amount = data['metric'][0]['amount']
                                map_trans_dict['district'].append(district
                                                                  .replace('district', '')
                                                                  .replace('nicobars', 'nicobar')
                                                                 )
                                map_trans_dict['transaction_count'].append(count)
                                map_trans_dict['transaction_amount'].append(amount)
                                map_trans_dict['state'].append(state.replace('-', ' '))
                                map_trans_dict['year'].append(year)
                                map_trans_dict['quater'].append('q'+ json_file.strip('.json'))

                        except Exception as e:
                            pass
                
    map_trans_df = pd.DataFrame(map_trans_dict)
    return map_trans_df

def map_user_state():
    
    map_usr_st_path = r"D:\Phonepe Pulse\clone\data\map\user\hover\country\india\state"
    map_usr_st_dir = os.listdir(map_usr_st_path)
    
    map_user_dict = {
                        'state': [], 
                        'year': [], 
                        'quater': [], 
                        'district': [],
                        'registered_user': [], 
                        'app_opening': []
                    }
    
    for state in map_usr_st_dir:
                state_path = f"{map_usr_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)
                        
                        try:
                            for data in load_json['data']["hoverData"]:
                                district = data
                                registered_user =  load_json['data']["hoverData"][data]["registeredUsers"]
                                app_opening = load_json['data']["hoverData"][data]["appOpens"]
                                map_user_dict['district'].append(district
                                                                  .replace('district', '')
                                                                  .replace('nicobars', 'nicobar')
                                                                )
                                map_user_dict['registered_user'].append(registered_user)
                                map_user_dict['app_opening'].append(app_opening)
                                map_user_dict['state'].append(state.replace('-', ' '))
                                map_user_dict['year'].append(year)
                                map_user_dict['quater'].append('q'+ json_file.strip('.json'))
                        
                        except Exception as e:
                            pass
                            
    map_usr_df = pd.DataFrame(map_user_dict)
    return map_usr_df  

def top_transcation_state():
    
    top_trans_st_path = r"D:\Phonepe Pulse\clone\data\top\transaction\country\india\state"
    top_trans_st_dir = os.listdir(top_trans_st_path)
    
    top_trans_dict = {
                        'state': [], 
                        'year': [], 
                        'quater': [], 
                        'district': [],
                        'total_transcation_count': [], 
                        'total_transcation_amount': []
                    }
    
    for state in top_trans_st_dir:
                state_path = f"{top_trans_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)
                        
                        try:
                            districts = load_json['data']['districts']
                            
                            for data in districts:
                                district = data['entityName']
                                count = data['metric']['count']
                                amount = data['metric']['amount']
                                top_trans_dict['district'].append(district
                                                                  .replace('district', '')
                                                                  .replace('nicobars', 'nicobar')
                                                                 )
                                top_trans_dict['total_transcation_count'].append(count)
                                top_trans_dict['total_transcation_amount'].append(amount)
                                top_trans_dict['state'].append(state
                                                                .replace('-', ' '))
                                top_trans_dict['year'].append(year)
                                top_trans_dict['quater'].append('q'+ json_file.strip('.json'))

                        except Exception as e:
                            pass
                                                                  
    top_trans_df = pd.DataFrame(top_trans_dict)
    return top_trans_df

def top_user_state():
    
    top_usr_st_path = r"D:\Phonepe Pulse\clone\data\top\user\country\india\state"
    top_usr_st_dir = os.listdir(top_usr_st_path)
    
    top_user_dict = {
                        'state': [], 
                        'year': [], 
                        'quater': [], 
                        'district': [],
                        'registered_user': []
                    }
    
    for state in top_usr_st_dir:
                state_path = f"{top_usr_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)
                        
                        try:
                            for data in load_json['data']['districts']:
                                district = data['name']
                                registered_user = data['registeredUsers']
                                top_user_dict['district'].append(district
                                                                      .replace('district', '')
                                                                      .replace('nicobars', 'nicobar')
                                                                     )
                                top_user_dict['registered_user'].append(registered_user)
                                top_user_dict['state'].append(state.replace('-', ' '))
                                top_user_dict['year'].append(year)
                                top_user_dict['quater'].append('q'+ json_file.strip('.json'))
                            
                        except Exception as e:
                            pass
                        
    top_user_df = pd.DataFrame(top_user_dict)
    return top_user_df

def top_transcation_state_pincode():
    
    top_trans_st_path = r"D:\Phonepe Pulse\clone\data\top\transaction\country\india\state"
    top_trans_st_dir = os.listdir(top_trans_st_path)
    
    
    top_trans_pin_dict = {
                            'state': [],
                            'pincode': [],
                            'year': [], 
                            'quater': [], 
                            'total_transcation_count': [], 
                            'total_transcation_amount': []
                        }
    
    for state in top_trans_st_dir:
                state_path = f"{top_trans_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)
                        
                        try:
                            pincodes = load_json['data']['pincodes']
                            
                            for data in pincodes:
                                pincode = data['entityName']
                                count = data['metric']['count']
                                amount = data['metric']['amount']
                                top_trans_pin_dict['pincode'].append(pincode)
                                top_trans_pin_dict['total_transcation_count'].append(count)
                                top_trans_pin_dict['total_transcation_amount'].append(amount)
                                top_trans_pin_dict['state'].append(state
                                                                .replace('-', ' '))
                                top_trans_pin_dict['year'].append(year)
                                top_trans_pin_dict['quater'].append('q'+ json_file.strip('.json'))
                                
                        except Exception as e:
                            pass
                        
    top_trans_pin_df = pd.DataFrame(top_trans_pin_dict)
    return top_trans_pin_df

def top_user_state_pincode():
    
    top_usr_st_path = r"D:\Phonepe Pulse\clone\data\top\user\country\india\state"
    top_usr_st_dir = os.listdir(top_usr_st_path)
    
    top_usr_pin_dict = {
                            'state': [],
                            'pincode': [],
                            'year': [], 
                            'quater': [], 
                            'registered_user': []
                        }
    
    for state in top_usr_st_dir:
                state_path = f"{top_usr_st_path}\\{state}\\"
                state_years = os.listdir(state_path)
                for year in state_years:
                    state_year_path = f"{state_path}{year}\\"
                    json_files = os.listdir(state_year_path)
                    for json_file in json_files:
                        json_file_path = state_year_path + json_file
                        read_json= open(json_file_path, 'r')
                        load_json = json.load(read_json)
                        
                        try:
                            pincodes = load_json['data']['pincodes']
                            
                            for data in pincodes:
                                pincode = int(data['name'])
                                registered_user = int(data['registeredUsers'])
                                top_usr_pin_dict['pincode'].append(pincode)
                                top_usr_pin_dict['registered_user'].append(registered_user)
                                top_usr_pin_dict['state'].append(state.replace('-', ' '))
                                top_usr_pin_dict['year'].append(int(year))
                                top_usr_pin_dict['quater'].append('q'+ json_file.strip('.json'))
                                
                        except Exception as e:
                            pass
                        
    top_usr_pin_df = pd.DataFrame(top_usr_pin_dict)
    return top_usr_pin_df
                                
                                
                          
                                                                                                                     

  

                