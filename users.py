import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def users(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT 
                SUM(registered_user) as total_user_count,
                SUM(app_opening) as total_appopening_count
                FROM map_user
                WHERE year = %s
                AND quater = %s;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Registered PhonePe users',
                                           'PhonePe app opens']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def users_top_state(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT
                state,
                SUM(registered_user) AS total_registered_users
                FROM map_user
                WHERE year = %s
                AND quater = %s
                GROUP BY state
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['State',
                                           'Total registered users']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
    
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def users_top_district(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT
                district,
                SUM(registered_user) AS total_registered_users
                FROM top_user
                WHERE year = %s
                AND quater = %s
                GROUP BY district
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['District',
                                           'Total registered users']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def users_top_pincode(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='#Praveenvishnu17', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT
                pincode,
                SUM(registered_user) AS total_registered_users
                FROM top_user_pincode
                WHERE year = %s
                AND quater = %s
                GROUP BY pincode
                ORDER BY total_registered_users DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Pincode',
                                           'Total registered users']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")