import os
import happinessReporter

CLI_OPTIONS = {"[A]dd Year Data" :  " - Add data to the database [C]RUD",
               "[B]rowse/Search Data": " - Search the database C[R]UD",
               "[C]hange Data": " - Edit database entries CR[U]D",
               "[D]elete an Entry": " - Delete a database entry CRRU[D]",
                "[EXIT] (works everywhere)": " - Exit the program now",
                "[H]elp": " - This menu",
                "[M]enu This Menu": " - Diplay the menu again" ,
               "[S]ample Queries": " - Show sample queries to try",
               }



def CLI_continue_program():
    answer = 'default'

    while answer != 'y' and answer != 'n':
        if answer != 'default':  # if the answer is not default they are going through loop again and give them hint
            print('Your response could not be understood. Please respond "Yes" or "No"')

        answer = input("Would you like to submit another query? (yes/no): ")
        if answer:
            answer = answer[0].lower()

    return answer == 'y'


def CLI_exit_check(command):
    return command == 'EXIT'

def CLI_add_year():
    filename_input = input('Please type file name. Or, type absolute path if not in working directory: ')
    while not (os.path.exists(filename_input) and filename_input.__contains__('.csv')):
        print('Invalid File Name. Please check that the CSV exists as specified and try again.')
        filename_input = input("Please type file name or absolute path if not in working directory: ")

    happinessReporter.insertYearData(filename_input)


def CLI_help_screen():
    help_str = """Welcome To Happiness Reporter\n\n'
                    COMMANDS:\n
                    """
    for key in CLI_OPTIONS:
        help_str += key + CLI_OPTIONS[key]



def CLI_search():
    pass


def CLI_edit():
    pass


def CLI_delete():
    pass


def CLI_samples():
    pass


def CLI_create_menu():
    welcome_prompt = "Welcome to the Happiness Reporter!\n Please select from one of the options below:\n"
    selection = ''
    do_conv = True

    while selection not in CLI_OPTIONS:
        if not do_conv:
            print('Not a valid option')
        else:
            do_conv = False
            print(welcome_prompt)
            for option in CLI_OPTIONS:
                print(option)
            selection = str.upper(input('Command: '))
    return selection
