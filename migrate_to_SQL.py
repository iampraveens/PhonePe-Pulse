import mysql.connector as mysql
from mysql.connector import Error
from extraction import *

def create_aggregated_transcation():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS aggregated_transcation')

        cursor.execute('''CREATE TABLE IF NOT EXISTS aggregated_transcation(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            transacion_type   VARCHAR(255),
                                            transacion_count  INT,
                                            transacion_amount FLOAT(50,3))'''
                      )

        query = '''
                INSERT INTO aggregated_transcation (state, year, quater, transacion_type, transacion_count, transacion_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        aggregated_transcation = aggregated_transcation_state()

        for _, row in aggregated_transcation.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
def create_aggregated_user():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS aggregated_user')

        cursor.execute('''CREATE TABLE IF NOT EXISTS aggregated_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            brand             VARCHAR(255),
                                            brand_count       INT,
                                            brand_percentage  FLOAT)'''
                      )

        query = '''
                INSERT INTO aggregated_user (state, year, quater, brand, brand_count, brand_percentage)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        aggregated_user = aggregated_user_state()

        for _, row in aggregated_user.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
def create_map_transcation():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS map_transcation')

        cursor.execute('''CREATE TABLE IF NOT EXISTS map_transcation(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            district          VARCHAR(255),
                                            transacion_count  INT,
                                            transacion_amount DECIMAL(20,5))'''
                      )

        query = '''
                INSERT INTO map_transcation (state, year, quater, district, transacion_count, transacion_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        map_transcation = map_transcation_state()

        for _, row in map_transcation.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
def create_map_user():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS map_user')

        cursor.execute('''CREATE TABLE IF NOT EXISTS map_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            district          VARCHAR(255),
                                            registered_user   INT,
                                            app_opening       INT)'''
                      )

        query = '''
                INSERT INTO map_user (state, year, quater, district, registered_user, app_opening)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        map_user = map_user_state()

        for _, row in map_user.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
            
def create_top_transcation():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS top_transcation')

        cursor.execute('''CREATE TABLE IF NOT EXISTS top_transcation(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            district          VARCHAR(255),
                                            transacion_count  INT,
                                            transacion_amount FLOAT(50,3))'''
                      )

        query = '''
                INSERT INTO top_transcation (state, year, quater, district, transacion_count, transacion_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        top_transcation = top_transcation_state()

        for _, row in top_transcation.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
def create_top_user():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS top_user')

        cursor.execute('''CREATE TABLE IF NOT EXISTS top_user(
                                            state             VARCHAR(255),
                                            year              INT,
                                            quater            VARCHAR(255),
                                            district          VARCHAR(255),
                                            registered_user   INT)'''
                      )

        query = '''
                INSERT INTO top_user (state, year, quater, district, registered_user)
                VALUES (%s, %s, %s, %s, %s)

                '''
        top_user = top_user_state()

        for _, row in top_user.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
            
def create_top_transcation_pincode():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS top_transcation_pincode')

        cursor.execute('''CREATE TABLE IF NOT EXISTS top_transcation_pincode(
                                            state             VARCHAR(255),
                                            pincode           INT,
                                            year              INT,
                                            quater            VARCHAR(255),
                                            transacion_count  INT,
                                            transacion_amount FLOAT(50,3))'''
                      )

        query = '''
                INSERT INTO top_transcation_pincode (state, pincode, year, quater, transacion_count, transacion_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

                '''
        top_transcation_pincode = top_transcation_state_pincode()

        for _, row in top_transcation_pincode.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
def create_top_user_pincode():
    
    try:
        connection = mysql.connect(
                            host = 'localhost',
                            database = 'phonepe_pulse',
                            user = 'root',
                            password = '#Praveenvishnu17'
                        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print('MySQL connected successfully!')
        
        cursor.execute('DROP TABLE IF EXISTS top_user_pincode')

        cursor.execute('''CREATE TABLE IF NOT EXISTS top_user_pincode(
                                            state             VARCHAR(255),
                                            pincode           INT,
                                            year              INT,
                                            quater            VARCHAR(255),
                                            registered_user   INT)'''
                      )

        query = '''
                INSERT INTO top_user_pincode (state, pincode, year, quater, registered_user)
                VALUES (%s, %s, %s, %s, %s)

                '''
        top_user_pincode = top_user_state_pincode()

        for _, row in top_user_pincode.iterrows():
            values = tuple(row)
            cursor.execute(query, values)
            connection.commit()
            
    except Error as e:
        print(f'Error occured: {str(e)}')
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed.')
            
