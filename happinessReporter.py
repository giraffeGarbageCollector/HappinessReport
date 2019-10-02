import csv
import sqlite3
from typing import List

import Result  # for database interactions

YEAR_MIN, YEAR_MAX = 2015, 2019


def main():
    keep_alive = True  # Main sentinel for program
    while keep_alive:
        menu_selec = CLI_create_menu()  # create a menu every time

        if not CLI_exit_check(menu_selec):  # check before other function calls for exit command
            try:
                option_handler(menu_selec)  # process command and get result string
            except SyntaxError:
                print("Invalid Option. Please Try Again")
        else:
            keep_alive = False  # User did want to exit, setting sentinel

        if not keep_alive:
            print("Thank you for using Happiness Reporter. Have a great day!")


def option_handler(option):
    option = str.upper(option)
    result = None
    options_dict = {'A': CLI_add_year(), 'B': CLI_search(), 'C': CLI_edit(),
                    'D': CLI_delete(), 'EXIT': '', 'H': CLI_help_screen(),
                    'M': CLI_create_menu(), 'S': CLI_samples()}

    if option in options_dict:
        result = options_dict[option]
    else:
        print('Option:', option)
        raise SyntaxError('Invalid Option Selected')

    return result


# Requires a csv file name as a string
# Fills database with values in the csv file. No headers or it will give weird results
# No return value. Table name is RankTable

def insertYearData(fileName):
    f = open(fileName)
    csv_file = csv.reader(f)

    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS RankTable('Country','rank','SD','Positive affect','Negative Affect','Social Support','Freedom','Corruption','Generosity','GDP per Capita','Life Expectancy','Year')""")
    param = """INSERT INTO 'RankTable' VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"""

    for row in csv_file:
        cur.execute(param, row)
        con.commit()

    cur.execute("SELECT Country FROM RankTable")
    result = cur.fetchall()
    con.close()


# Requires a csv file name as a string
# Fills database with values in the csv file. No headers or it will give weird results
# No return value. Table name is GeneralData


def insertCountryData(fileName):
    f = open(fileName)
    csv_file = csv.reader(f)
    param = """INSERT INTO 'GeneralData' VALUES(?,?,?);"""

    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS GeneralData('Country','Reigon','Languages')""")

    for row in csv_file:
        cur.execute(param, row)
        con.commit()

    cur.execute("SELECT Languages FROM GeneralData")
    con.close()


# TODO
# Returns bool for if a query is syntaxtically correct
def validate_query(query_str):
    return False


# TODO
# Updates a country record by id given the field to be updated and the new value
def update_record(id, field, value):
    pass


# TODO
# Remove a db entry given the result object
def remove_record(result):
    pass


# Returns a list of all qualifiers entered. Unvalidated result returned
def __find_qualifiers(search_upper_split):
    found_quals = []
    qualifiers_lst = ['HAPPY', 'SUPPORTIVE', 'FREE', 'CORRUPT',
                      'GENEROUS', 'WEALTHY', 'HEALTHY']
    for qual in qualifiers_lst:
        if qual in search_upper_split:
            found_quals.append(qual)
    return found_quals


# REturns ordering syntax Unvalidated result returned
def __find_rank(search_upper_split):
    found_rank = None
    rank_dict = {'TOP': 'Desc', 'BOTTOM': 'Asc', 'MOST': 'Desc',
                 'LEAST': 'Asc'}  # TODO Make sure that these are the correct sql orderings
    for rank in rank_dict:
        if rank in search_upper_split:
            if found_rank is None:
                found_rank = rank_dict[rank]
            else:
                raise SyntaxError("Too Many Rank Modifiers Found")
    return found_rank


# Returns a list with odd entries the noun syntax and the even index the value. Unvalidated result returned
# i.e. list = ['Country', 'United States', ....]
def __find_nouns(search_upper_split):
    found_nouns = []
    noun_lst = ['SPEAKING', 'IN']  # Language and Region
    for i in range(len(noun_lst)):
        if noun_lst[i] in search_upper_split:
            found_nouns.append(noun_lst[i])
    #            found_nouns.append(noun_lst[i+1]) #TODO Needs validation that it is grabbing noun
    return found_nouns


# Returns the search rresult limit (ex show 5: limit =5) and a list with all year(s) requested. Unvalidated result returned
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


# Returns the search results of a validated search string. If no results, return the empty array
def search(search_str):
    results = []
    if validate_query(search_str):
        sql_query = "SELECT * FROM RankTable WHERE "
        descending_order = True
        search_list_split = search_str.upper().split()
        try:
            search_limit, years = __find_numbers_years(search_list_split)
            qualifiers = __find_qualifiers(search_list_split)
            nouns = __find_nouns(search_list_split)
            rank = __find_rank(search_list_split)

            # TODO Validate all of these parts
            # TODO Validate all of these parts

            if years:
                for year in years:
                    sql_query += "`Year` == " + year + " OR "
                sql_query = sql_query.rsplit(' ', 1)[0]  # Remove the last "OR" from the sql query
            sql_query += " ORDER BY "
            if qualifiers:
                for qual in qualifiers:
                    pass  ##TODO add qualifiers to query

            if rank:
                sql_query += rank + ' '
            if search_limit:
                sql_query += " LIMIT " + search_limit
            if nouns:
                if nouns == "IN":
                    noun = search_list_split[search_list_split.len()]
                    sql_query += "INNER JOIN GeneralData ON RankTable.country = GeneralTable WHERE GeneralData.region = " + noun
                elif nouns == "SPEAKING":
                    noun = search_list_split[search_list_split.len() - 1]
                    sql_query += "INNER JOIN GeneralData ON RankTable.country = GeneralTable WHERE GeneralData.language LIKE " + noun

            con = sqlite3.connect(":memory:")
            cur = con.cursor()
            cur.execute(sql_query)



        except SyntaxError:
            print("There was an Error in your search. Please check it and try again")

    return results


def search_one(validated_search_str):
    results = search(validated_search_str)
    return results[0]


# Returns if the result object exists in the database
def entry_exists(result):
    return len(search(result)) > 0


## OLD py

import os
import time

MENU = "MENU"
ESCAPE = "EXIT"
CLI_OPTIONS = {"[A]dd Year Data" :  " - Add data to the database [C]RUD",
               "[B]rowse/Search Data": " - Search the database C[R]UD",
               "[C]hange Data": " - Edit database entries CR[U]D",
               "[D]elete an Entry": " - Delete a database entry CRRU[D]",
                ESCAPE + " (works everywhere)": " - Exit the program now",
                "[H]elp": " - This menu",
                "[M]enu This Menu": " - Diplay the menu again" ,
               "[S]ample Queries": " - Show sample queries to try",
               }

CLI_OPTIONS_LETTERS = [command[1] for command in CLI_OPTIONS.keys()]


def CLI_exit_check(command):
    return command.upper() == 'EXIT'

def CLI_add_year():
    filename_input = input('Please type file name. Or, type absolute path if not in working directory: ')
    while not (os.path.exists(filename_input) and filename_input.__contains__('.csv')):
        print('Invalid File Name. Please check that the CSV exists as specified and try again.')
        filename_input = input("Please type file name or absolute path if not in working directory: ")

    insertYearData(filename_input)


def CLI_help_screen():
    help_str = """Welcome To Happiness Reporter\n\n'
                    ABOUT:\n
                    \tFrom the Report (https://worldhappiness.report/):\n
                    \t\t"The World Happiness Report is a landmark survey of the state of global happiness that ranks\n
                    \t\t156 countries by how happy their citizens perceive themselves to be. This year’s World \n
                    \t\tHappiness Report focuses on happiness and the community: how happiness has evolved over \n
                    \t\tthe past dozen years, with a focus on the technologies, social norms, conflicts and government \n
                    \t\tpolicies that have driven those changes."\n\n
                    COMMANDS:\n
                    """
    for key in CLI_OPTIONS:
        help_str += key + CLI_OPTIONS[key] + "\n"

    help_str += """
                \nSYNTAX:\n
                All commands are in CAPITALS.\n
                *finish*
                """ # TODO: Finish the syntax
    print(help_str)



def CLI_search():
    q_input = ''
    while "EXIT" not in q_input.upper():
        print("\nType \"EXIT\" to go back to main menu")
        q_input = input("Search:")
        if validate_query(q_input):
            results = search(q_input)
        else:
            print("Sorry, the syntax you used was incorrect")

        #Print Results
        print("RESULTS:\n")
        for result in results:
            __print_result(result)


def __print_result(result):
    print("Country:", result.get_country, "Rank:", result.get_rank(),
          "Happiness Score:", result.get_score(), "GDP:", result.get_gdp(),
          "ID:", result.get_id())

def __edit_result(result):
    while ESCAPE not in usr_in.upper():
        print("Here is the data for", result.get_country())
        print(result.list_values())

        usr_in = input("What Would You Like To Change? (Type \"exit\" to go back to edit menu): ")
        field_in = usr_in.upper()
        if not CLI_exit_check(field_in) and result.is_valid_field(field_in.lower()):
            value_in = input("New Value: ")

            if not CLI_exit_check(value_in):
                print("New Value:", value_in)
                valid_in = input("Is This Correct? y/n")

                if valid_in.upper() == 'Y':
                    print("Updating Record", end="")
                    update_record(result.get_id(), field_in, value_in)

                else:
                    print("Not Updating Record", end="")

                for i in range(3):
                    print(".", end="")
                    time.sleep(.3)
                print("Record for ", result.get_country(), ":\n", result.list_values(), sep='')

            else:
                print("Invalid Field")



def CLI_edit():
    cli_input = ''
    while MENU not in cli_input.upper():
        print("Type \"menu\" to go back to main menu")
        cli_input = input("ID of entry to edit")
        if entry_exists(cli_input):
            entry = search("ID " , cli_input)
            __print_result(entry)
            __edit_result(entry)
        else:
            print("Sorry, We could not find entry with that ID")


def CLI_delete():
    cli_input = ''
    while MENU not in cli_input.upper():
        print("Type \"menu\" to go back to main menu")
        cli_input = input("ID of entry to delete")
        entry = search_one("ID " + cli_input)
        if entry:
            print("Is This Right?")
            __print_result(entry)
            cli_input = input("Confimation to DELETE, permanently,", entry.get_Country,
                              "\n with ID", entry.get_ID, "(case sensitive) Y/N:")
            if cli_input in 'Y':
                print("Deleting Record", end="")
                remove_record(entry)
            else:
                print("Not Deleting Record", end="")

            for i in range(3):
                print(".", end="")
                time.sleep(.3)
        else:
            print("Sorry, We could not find entry with that ID")


def CLI_samples():
    sample_str = """
                    Sample:
                    MOST HAPPT COUNTRY
                    2 MOST HEALTHY SPANISH COUNTRIES
                    LEAST CORRUPT REGION 2016
                    COUNTRIES            
                    """

    print(sample_str)



def CLI_create_menu():
    welcome_prompt = "Welcome to the Happiness Reporter!\n Please select from one of the options below:\n"
    selection = ''
    do_loop_conversion = True

    while selection not in CLI_OPTIONS_LETTERS or len(selection) > 1:
        if not do_loop_conversion:
            print('Not a valid option')
        else:
            do_loop_conversion = False
            print(welcome_prompt)

        print("To exit, type\" ", ESCAPE.lower(), "\"")
        for option in CLI_OPTIONS:
            print(option)
        selection = str.upper(input('Command: '))
    return selection



main()
