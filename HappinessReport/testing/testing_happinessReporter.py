import happinessReporter


def main_testing():
    errors = 0

    errors += continue_program_tester()

    print('Errors Found:', errors)


def continue_program_tester():
    section_errors = 0

    #Test Yes
    print('TESTING: Please type \'yes\'')
    test1 = continue_program()
    if not test1:
        section_errors += 1
        print('TESTING: Failed detecting a yes for program continue function')

    #Test No
    print('TESTING: Please type \'no\'')
    test2 = continue_program()
    if test2:
        section_errors += 1
        print('TESTING: Failed detecting a no for program continue function')

    # Test Nothing
    print('TESTING: Please type nothing at all. Then \'no\'')
    test3 = continue_program()
    if test3:
        section_errors += 1
        print('TESTING: Failed handling no answer')


    #Test Garbage
    print('TESTING: Please type garbage. Then \'no\'')
    test4 = continue_program()
    if test4:
        section_errors += 1
        print('TESTING: Failed detecting a no for program continue function')

    return section_errors



main_testing()
