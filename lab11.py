import sqlite3
import base64
import webbrowser
import os


def createConnection(dbFileName):
    cre_conn = None
    try:
        is_exist = os.path.exists(dbFileName)
        if is_exist:
            cre_conn = sqlite3.connect(dbFileName)
        else:
            raise Exception('Database file not found')
    except Exception as ex:
        print(ex)
    return cre_conn


def main():
    try:
        # connection to sqlite3
        with createConnection('week11.db') as conn:
            # user input prompt
            while True:
                user_input = input('Please a number between 1 and 24 to open browser(to quit enter q):')
                if user_input.isdigit():
                    input_id = int(user_input)
                    if 0 < input_id < 25:
                        sql = f"SELECT * FROM Lab10 WHERE id={input_id}"
                        cursor = conn.cursor()
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        encoded_link_utf = data[1]
                        covert_link = base64.b64decode(encoded_link_utf).decode('utf-8')
                        webbrowser.open(covert_link)
                        user_city_name = input(f"Please enter a city name [Current:{data[2]}]:")
                        user_country_name = input(f"Please enter a country name [Current:{data[3]}]:")
                        sql = f"UPDATE Lab10 SET City='{user_city_name}', Country='{user_country_name}' WHERE id={user_input}"
                        cur = conn.cursor()
                        cur.execute(sql)
                        conn.commit()
                        print("Your record is updated!")
                    else:
                        print("The number you entered is not between 1 and 24")
                else:
                    if user_input == 'q' or user_input == 'Q':
                        print("Thank you")
                        break
                    else:
                        print("It is not an expected value!")
    except Exception as ex:
        # Error message
        print(ex)


# The __name__ variable (two underscores before and after)
# is a special Python variable.
# It gets its value depending on how we execute the containing script.
if __name__ == '__main__':
    main()