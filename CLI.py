CLI_OPTIONS = ["[A]dd Year Data", "[B]rowse/Search Data", "[C]hange Data",
           "[D]elete an Entry", "[EXIT] (works everywhere)", "[H]elp", "[M]enu This Menu",
           "[S]ample Queries"]

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
            selection = upper(input('Command: '))
    return selection

def CLI_continue_program():
    answer = 'default'
    while answer != 'y' and answer != 'n':
        if answer != 'default': # if the answer is not defualt they are going through loop again and give them hint
            print('Your response could not be understood. Please respond "Yes" or "No"')

        answer = input("Would you like to submit another query? (yes/no): ")
        if answer:
            answer = answer[0].lower()

    return answer == 'y'

def CLI_exit_check(command):
    return command == 'EXIT'

def CLI_help_screen():

def CLI_add_year():
    filename_input = input('Please type file name or absolute path if not in working directory: ')
    while os.path.exists(filename_input):
        print('Invalid File Name. Please check that the CSV exists as specified and try again.')
        filename_input = input("Please type file name or absolute path if not in working directory: ")

    insertYearData(filename_input)

def CLI_search():
    pass

def CLI_edit():
    pass

def CLI_delete():
    pass

def CLI_samples():
    pass

