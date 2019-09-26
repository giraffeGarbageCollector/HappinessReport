# Drew Meyers

import csv
import sqlite3

from CLI import *
import Result

def main():
    keep_alive = True #Main sentinel for program
    while keep_alive:
        menu_selec = CLI_create_menu() #create a menu every time

        if not CLI_exit_check(menu_selec): #check before other function calls for exit command
            try:
                prnt_str = option_handler(menu_selec) #process command and get result string
            except SyntaxError:
                print("Invalid Option. Please Try Again")
        else:
            keep_alive = False #User did want to exit, setting sentinel
        if keep_alive:
            keep_alive = CLI_continue_program()
        else:
            print("Thank you for using Happiness Reporter. Have a great day!")


def option_handler(option):
    option = str.upper(option)
    options_dict = {'A': CLI_add_year(), 'B': CLI_search(), 'C': CLI_edit(),
                    'D': CLI_delete(), 'EXIT': '',  'H': CLI_help_screen(),
                    'M': CLI_create_menu(), 'S': CLI_samples()}

    if option in options_dict:
        options_dict[option]
    else:
        print('Option:', option)
        raise SyntaxError('Invalid Option Selected')


#Requires a csv file name as a string
#Fills database with values in the csv file. No headers or it will give weird results
#No return value. Table name is RankTable

def insertYearData(fileName):
    f = open(fileName)
    csv_file = csv.reader(f)
    
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS RankTable('Country','rank','SD','Positive affect','Negative Affect','Social Support','Freedom','Corruption','Generosity','GDP per Capita','Life Expectancy','Year')""")
    param = """INSERT INTO 'RankTable' VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"""
    
    
    for row in csv_file:
        cur.execute(param, row)
        con.commit()

    cur.execute("SELECT Country FROM RankTable")
    result= cur.fetchall()
    con.close()


#Requires a csv file name as a string
#Fills database with values in the csv file. No headers or it will give weird results
#No return value. Table name is GeneralData



def insertCountryData(fileName):
    f = open(fileName)
    csv_file = csv.reader(f)
    param = """INSERT INTO 'GeneralData' VALUES(?,?,?);"""
    
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS GeneralData('Country','reigon','Languages')""")
    
    
    
    for row in csv_file:
        cur.execute(param,row)
        con.commit()
    
    cur.execute("SELECT Languages FROM GeneralData")
    con.close()


main()
