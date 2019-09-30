import sqlite3
dic=["least","most","happy","supportive","free","corrupt","generous","wealthy","healthy","country","language","region","2015","2016","2017","2018","2019"]
adj=["happy","supportive","free","corrupt","generous","wealthy","healthy"]
non=["country","language","region"]
year=["2015","2016","2017","2018","2019"]

con = sqlite3.connect('data.db')
user_input = input("Input from user: ")
splited_input = user_input.split()

def validate(splited_input):
    if splited_input[0].isdigit():
        print (splited_input[0])
        print (splited_input[1])
        if splited_input[1] !="most" and splited_input[1] != "least":
            # print("error1")
            return False
        else:
            if splited_input[2] not in adj:
                # print("error2")
                return False
            else:
                if splited_input[3] not in non:
                    # print("error3")
                    return False
                else:
                    if len(splited_input) == 5:
                        if splited_input[4] not in year:
                            print("error4")
                            return False
                        else:
                            return True
                    elif len(splited_input) > 5:
                        return False
                    else:
                        return True
    elif splited_input[0] =="most" or splited_input[0] =="least":
        if splited_input[1] not in adj:
            # print("error11")
            return False
        else:
            if splited_input[2] not in non:
                # print("error22")
                return False
            else:
                if len(splited_input) == 4:
                    if splited_input[3] not in year:
                        # print("error33")
                        return False
                    else:
                        return True
                elif len(splited_input) > 4:
                    return False
                else:
                    return True
    else:
        return False

if validate(splited_input)==False:
    print("user input is invalid")
if validate(splited_input)==True:
    print("you are all good")