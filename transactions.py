import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def transactions(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='yourpassword', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT 
                    SUM(map_transaction.transaction_count) AS total_transaction_count,
                    SUM(map_transaction.transaction_amount) AS total_transaction_amount,
                    AVG(map_transaction.transaction_amount/map_transaction.transaction_count) AS average_transaction_amount
                FROM
                    map_transaction
                WHERE
                    map_transaction.year = %s
                    AND map_transaction.quater = %s
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['All PhonePe transactions', 
                                           'Total payment value', 
                                           'Avg. transaction value']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def transactions_categories(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='yourpassword', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT
                SUM(CASE WHEN transaction_type = 'recharge & bill payments' THEN transaction_count ELSE 0 END) AS recharge_bill_payments,
                SUM(CASE WHEN transaction_type = 'peertopeer payments' THEN transaction_count ELSE 0 END) AS peertopeer_payments,
                SUM(CASE WHEN transaction_type = 'merchant payments' THEN transaction_count ELSE 0 END) AS merchan_payments,
                SUM(CASE WHEN transaction_type = 'financial services' THEN transaction_count ELSE 0 END) AS financial_services,
                SUM(CASE WHEN transaction_type = 'others' THEN transaction_count ELSE 0 END) AS others
                FROM
                aggregated_transaction
                WHERE
                transaction_type IN ('recharge & bill payments', 'peertopeer payments', 'merchant payments', 'financial services', 'others')
                AND year = %s
                AND quater = %s;
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Recharge & bill payments', 
                                           'Peer-to-peer payments', 
                                           'Merchant payments',
                                           'Financial Services',
                                           'Others']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def transactions_top_state(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='yourpassword', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT state, SUM(transaction_count) AS total_transaction_count
                FROM aggregated_transaction
                WHERE year = %s
                AND quater = %s
                GROUP BY state
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['State',
                                           'Total transaction count']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        
        
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def transactions_top_district(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='yourpassword', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT district, SUM(transaction_count) AS total_transaction_count
                FROM top_transaction
                WHERE year = %s 
                AND quater = %s
                GROUP BY district
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['District',
                                           'Total transaction count']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
        

import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

def transactions_top_pincode(year, quater):
    try:
        connection = mysql.connect(user='root', 
                                   password='yourpassword', 
                                   host='localhost', 
                                   database='phonepe_pulse'
                                )
        cursor = connection.cursor()

        query = '''
                SELECT pincode , SUM(transaction_count) AS total_transaction_count
                FROM top_transaction_pincode
                WHERE year = %s 
                AND quater = %s
                GROUP BY pincode
                ORDER BY total_transaction_count DESC
                LIMIT 10;
                
                '''
        cursor.execute(query, (year, quater))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        df = pd.DataFrame(result, columns=['Pincode',
                                           'Total transaction count']).reset_index(drop=True)
        df.index += 1

        return df

    except Error as e:
        print(f"Error occurred while connecting to MySQL: {str(e)}")
