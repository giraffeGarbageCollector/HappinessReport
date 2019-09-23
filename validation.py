import sqlite3


con = sqlite3.connect('happy.db')
user_input = input("Input from user: ")
splited_input = user_input.split()

def check_table_name(splited_input):
    for i in range (1,len(splited_input)+1):
        params = str(i)
        # query = "SELECT * FROM projects where id=?"
        query = "SELECT ? FROM projects"
        cursor = con.execute(query,params)
        result = cursor.fetchone()
        # print(result)
        if result == None:
            return False
        else:
            print(1)

if (check_table_name(splited_input)==False):
    print("no passed")
else:
    print("passed")

def check_each_name(splited_input):
    if check_table_name(user_input)!=False:
        if "country" in splited_input():
            if "happy" in splited_input:
                if "most" in splited_input:
                    if "2015" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2015 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2015 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2016" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2016 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2016 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2017" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2017 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2017 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2018" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2018 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2018 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2018" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2019 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2019 ORDER BY happy DESC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                if "least" in splited_input:
                    if "2015" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2015 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2015 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2016" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2016 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2016 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2017" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2017 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2017 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2018" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2018 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2018 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
                    elif "2018" in splited_input:
                        if "number" in splited_input:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2019 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchall()
                            number_result = result[2] # 2 should be replaced with a number that user inputs
                            # print(result)
                            if number_result == None:
                                return False
                        else:
                            query = "SELECT country,happy,year FROM GeneralData AND RankTable WHERE year=2019 ORDER BY happy ASC"
                            cursor = con.execute(query)
                            result = cursor.fetchone()
                            # print(result)
                            if result == None:
                                return False
            elif "supportive" in splited_input:
            elif "free" in splited_input:
            elif "corrupt" in splited_input:
            elif "generous" in splited_input:
            elif "wealthy" in splited_input:
            elif "healthy" in splited_input:
            else:
                return False


        if "language" in splited_input():
            if "happy" in splited_input:
            elif "supportive" in splited_input:
            elif "free" in splited_input:
            elif "corrupt" in splited_input:
            elif "generous" in splited_input:
            elif "wealthy" in splited_input:
            elif "healthy" in splited_input:
            else:
                return False
        if "region" in splited_input():
            if "happy" in splited_input:
            elif "supportive" in splited_input:
            elif "free" in splited_input:
            elif "corrupt" in splited_input:
            elif "generous" in splited_input:
            elif "wealthy" in splited_input:
            elif "healthy" in splited_input:
            else:
                return False

if check_each_name(splited_input)!= False:
    # if it's not false, means it's true and then following should be output functions













