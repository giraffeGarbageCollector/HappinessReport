import csv
import sqlite3
from typing import List

from CLI import *
import Result # for database interactions

YEAR_MIN = 2015
YEAR_MAX = 2019


def main():
    keep_alive = True #Main sentinel for program
    while keep_alive:
        menu_selec = CLI_create_menu() #create a menu every time

        if not CLI_exit_check(menu_selec): #check before other function calls for exit command
            try:
                option_handler(menu_selec) #process command and get result string
            except SyntaxError:
                print("Invalid Option. Please Try Again")
        else:
            keep_alive = False #User did want to exit, setting sentinel

        if not keep_alive:
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


#TODO
#Returns bool for if a query is syntaxtically correct
def validate_query(query_str):
    return False

#TODO
#Updates a country record by id given the field to be updated and the new value
def update_record(id, field, value):
    pass

#TODO
#Remove a db entry given the result object
def remove_record(result):
    pass


def __find_qualifiers(search_upper_split):
    found_quals = []
    qualifiers_lst = ['HAPPY' , 'SUPPORTIVE', 'FREE', 'CORRUPT',
                       'GENEROUS', 'WEALTHY', 'HEALTHY']
    for qual in qualifiers_lst:
        if qual in search_upper_split:
            found_quals.append(qual)
    return found_quals


def __find_rank(search_upper_split):
    found_rank = None
    rank_lst = ['TOP', 'Bottom', 'MOST', 'LEAST']
    for rank in rank_lst:
        if rank in search_upper_split:
            if found_rank is None:
                found_rank = rank
            else:
                raise SyntaxError("Too Many Rank Modifiers Found")
    return found_rank

def __find_nouns(search_upper_split):
    found_nouns = []
    noun_lst = ['COUNTRY', 'LANGUAGE', 'REGION']
    for i in range(len(noun_lst)):
        if noun_lst[i] in search_upper_split:
            found_nouns.append(noun_lst[i+1]) ##TODO Needs validation that it is grabbing noun
    return found_nouns

def __find_numbers_years(search_upper_split):
    found_years: List[int] = []
    limit = None
    for word in search_upper_split:
        try:
            num = int(word)
            if num < 1000:
                if limit is None:
                    limit = num
            elif YEAR_MIN <= num <= YEAR_MAX:
                found_years.append(num)
            else:
                raise SyntaxError("Invalid Number Found")
        except ValueError:
            pass
    return limit, found_years


#Returns the search results of a validated search string. If no results, return the empty array
def search(search_str):
    results = []
    if validate_query(search_str):
        sql_query = "SELECT * FROM GeneralData WHERE "
        descending_order = True
        search_list_split = search_str.upper().split()
        try:
            search_limit, years = __find_numbers_years(search_list_split)
            qualifiers = __find_qualifiers(search_list_split)
            nouns = __find_nouns(search_list_split)
            rank = __find_rank(search_list_split)

            if years:
                for year in years:
                    sql_query += "Year == " + year + " AND "
            for noun in nouns:
                sql_query += noun
            sql_query += ""
        except SyntaxError:
            print("There was an Error in your search. Please check it and try again")

    return results

def search_one(validated_search_str):
    results = search(validated_search_str)
    return results[0]

#Returns if the result object exists in the database
def entry_exists(result):
    return len(search(result)) > 0

main()
