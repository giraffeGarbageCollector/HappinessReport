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

CLI_OPTIONS_LETTERS = [command[2] for command in CLI_OPTIONS.keys()]


def CLI_exit_check(command):
    return command.upper() == 'EXIT'

def CLI_add_year():
    filename_input = input('Please type file name. Or, type absolute path if not in working directory: ')
    while not (os.path.exists(filename_input) and filename_input.__contains__('.csv')):
        print('Invalid File Name. Please check that the CSV exists as specified and try again.')
        filename_input = input("Please type file name or absolute path if not in working directory: ")

    happinessReporter.insertYearData(filename_input)


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
        if happinessReporter.validate_query(q_input):
            results = happinessReporter.search(q_input)
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
                    happinessReporter.update_record(result.get_id(), field_in, value_in)

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
        if happinessReporter.entry_exists(cli_input):
            entry = happinessReporter.search("ID " , cli_input)
            __print_result(entry)
            __edit_result(entry)
        else:
            print("Sorry, We could not find entry with that ID")


def CLI_delete():
    cli_input = ''
    while MENU not in cli_input.upper():
        print("Type \"menu\" to go back to main menu")
        cli_input = input("ID of entry to delete")
        entry = happinessReporter.search_one("ID " + cli_input)
        if entry:
            print("Is This Right?")
            __print_result(entry)
            cli_input = input("Confimation to DELETE, permanently,", entry.get_Country,
                              "\n with ID", entry.get_ID, "(case sensitive) Y/N:")
            if cli_input in 'Y':
                print("Deleting Record", end="")
                happinessReporter.remove_record(entry)
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

        print("To exit, type\"", ESCAPE.lower(), "\"")
        for option in CLI_OPTIONS:
            print(option)
        selection = str.upper(input('Command: '))
    return selection

import happinessReporter
