import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd


def total_transactions(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT transaction_type, sum(transaction_amount) AS transaction_amount 
                FROM aggregated_transaction 
                WHERE year = %s 
                AND quater = %s 
                GROUP BY transaction_type
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['transaction type', 
                                           'transaction amount']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
def top_state_transactions_amount(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, SUM(transaction_amount) AS top_states
                FROM top_transaction
                WHERE year = %s
                AND quater = %s
                GROUP BY state 
                ORDER BY top_states DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state', 
                                           'transaction amount']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_state_transactions_count(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, SUM(transaction_count) AS top_states
                FROM top_transaction
                WHERE year = %s
                AND quater = %s
                GROUP BY state 
                ORDER BY top_states DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state', 
                                           'transaction count']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
def top_district_transactions_amount(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT district, SUM(transaction_amount) AS top_district_amount
                FROM map_transaction
                WHERE year = %s
                AND quater = %s
                GROUP BY district 
                ORDER BY top_district_amount DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['district', 
                                           'transaction amount']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_district_transactions_count(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT district, SUM(transaction_count) AS top_district_count
                FROM map_transaction
                WHERE year = %s
                AND quater = %s
                GROUP BY district 
                ORDER BY top_district_count DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['district', 
                                           'transaction count']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_pincode_transactions_amount(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT pincode, SUM(transaction_amount) AS top_pincode_amount
                FROM top_transaction_pincode
                WHERE year = %s
                AND quater = %s
                GROUP BY pincode 
                ORDER BY top_pincode_amount DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['pincode', 
                                           'transaction amount']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_pincode_transactions_count(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT pincode, SUM(transaction_count) AS top_pincode_count
                FROM top_transaction_pincode
                WHERE year = %s
                AND quater = %s
                GROUP BY pincode 
                ORDER BY top_pincode_count DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['pincode', 
                                           'transaction count']).reset_index(drop=True)
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
def user_brand_count(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT brand, SUM(brand_count) AS user_count
                FROM aggregated_user
                WHERE year = %s
                AND quater = %s
                GROUP BY brand
                ORDER BY user_count DESC
                LIMIT 10;

                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['brand', 
                                           'user count'])
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def user_brand_count_state(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, brand, SUM(brand_count) AS state_user_count
                FROM aggregated_user
                WHERE year = %s
                AND quater = %s
                GROUP BY state, brand
                ORDER BY state_user_count DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state',
                                           'brand', 
                                           'user count'])
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_user_state(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, SUM(registered_user) AS user_count_state
                FROM top_user
                WHERE year = %s
                AND quater = %s
                GROUP BY state
                ORDER BY user_count_state DESC
                LIMIT 10;
    
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state',
                                           'user count'])
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_user_district(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT district, SUM(registered_user) AS user_count_state
                FROM top_user
                WHERE year = %s
                AND quater = %s
                GROUP BY district
                ORDER BY user_count_state DESC
                LIMIT 10;
    
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['district',
                                           'user count'])
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
def top_user_pincode(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, pincode, SUM(registered_user) AS user_count_pincode
                FROM top_user_pincode
                WHERE year = %s
                AND quater = %s
                GROUP BY state, pincode
                ORDER BY user_count_pincode DESC
                LIMIT 10;
    
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['state',
                                           'pincode',
                                           'user count'])
        df.index += 1

        return df
    
    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
