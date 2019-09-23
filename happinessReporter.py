# Drew Meyers

import csv
import sqlite3
from CLI import *
import os

def main():
    keep_alive = True
    while keep_alive:
        #Do stuff

        keep_alive = CLI_continue_program()
        menu_selec = CLI_create_menu()
        if not CLI_exit_check(menu_selec):
            CLI_Handler(menu_selec)
        else:
            keep_alive = False


def CLI_Handler(option):
    option = upper(option)
    OPTIONS_DICT = {'A': CLI_add_year(), 'B': CLI_search(), 'C': CLI_edit(),
    'D': CLI_delete(), 'EXIT': '',  'H': CLI_help_screen(), 'M': CLI_create_menu(),
    'S': CLI_samples()}

    if option in OPTIONS_DICT:
        cli_response = OPTIONS_DICT[option] #returns a list with [0] being next instruction, [1] data

    def continue_program():
    answer = 'default'
    while answer != 'y' and answer != 'n':
        if answer != 'default': # if the answer is not defualt they are going through loop again and give them hint
            print('Your response could not be understood. Please respond "Yes" or "No"')

        answer = input("Would you like to submit another query? (yes/no): ")
        if answer:
            answer = answer[0].lower()

    return answer == 'y'


#Requires a csv file name as a string
#Fills database with values in the csv file. No headers or it will give weird results
#No return value. Table name is RankTable

def insertYearData(fileName):
    f = open(fileName)
    openFile = csv.reader(f)
    
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS RankTable('Country','rank','SD','Positive affect','Negative Affect','Social Support','Freedom','Corruption','Generosity','GDP per Capita','Life Expectancy','Year')""")
    param = """INSERT INTO 'RankTable' VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"""
    
    
    for row in csvFile:
        cur.execute(param,row)
        con.commit()

    cur.execute("SELECT Country FROM RankTable")
    result= cur.fetchall()
    con.close()


#Requires a csv file name as a string
#Fills database with values in the csv file. No headers or it will give weird results
#No return value. Table name is GeneralData

def insertCountryData(fileName):
    f = open(fileName)
    openFile = csv.reader(f)
    param = """INSERT INTO 'GeneralData' VALUES(?,?,?);"""
    
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS GeneralData('Country','reigon','Languages')""")
    
    
    
    for row in csv_f:
        cur.execute(param,row)
        con.commit()
    
    cur.execute("SELECT Languages FROM GeneralData")
    con.close()


main()
