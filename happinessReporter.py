# Drew Meyers

def main():
    keep_alive = True
    while keep_alive:
        #Do stuff

        keep_alive = continue_program()


def continue_program():
    answer = 'default'
    while answer != 'y' and answer != 'n':
        if answer != 'default': # if the answer is not defualt they are going through loop again and give them hint
            print('Your response could not be understood. Please respond "Yes" or "No"')

        answer = input("Would you like to submit another query? (yes/no): ")
        if answer:
            answer = answer[0].lower()

    return answer == 'y'

