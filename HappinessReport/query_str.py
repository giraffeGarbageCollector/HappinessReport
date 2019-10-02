def validate_query(query_str):
    qualifiers_lst = ['HAPPY', 'SUPPORTIVE', 'FREE', 'CORRUPT', 'GENEROUS', 'WEALTHY', 'HEALTHY']
    noun_lst = ['COUNTRY', 'LANGUAGE', 'REGION']
    year_lst = ["2015", "2016", "2017", "2018", "2019"]
    rank_lst = ['TOP', 'Bottom', 'MOST', 'LEAST']

    splited_input = query_str.split()
    ## 2 most happy country region 2015
    if splited_input[0].isdigit():
        if splited_input[1] not in rank_lst:
            return False
        else:
            if splited_input[2] not in qualifiers_lst:
                return False
            else:
                if splited_input[3] not in noun_lst:
                    return False
                else:
                    ## length 4 , 5, 6
                    if len(splited_input) == 4:
                        if splited_input[3] in noun_lst:
                            return True
                        else:
                            return False
                    elif len(splited_input) == 5:
                        if splited_input[4] not in noun_lst:
                            if splited_input[4] not in year_lst:
                                return False
                            else:
                                return True
                        elif (splited_input[4] in noun_lst) and (splited_input[4]!=splited_input[3]):
                            return True
                        else:
                            return False
                    elif len(splited_input) == 6:
                        if splited_input[4] not in noun_lst:
                            return False
                        elif splited_input[4] == splited_input[3]:
                            return False
                        elif splited_input[5] not in year_lst:
                            return False
                        else:
                            return True
    ## most happy country region 2015
    elif splited_input[0] in rank_lst:
        if splited_input[1] not in qualifiers_lst:
            return False
        else:
            if splited_input[2] not in noun_lst:
                return False
            else:
                # length 3, 4, 5
                if len(splited_input) == 3:
                    if splited_input[2] in noun_lst:
                        return True
                    else:
                        return False
                elif len(splited_input) == 4:
                    if splited_input[3] not in noun_lst:
                        if splited_input[3] not in year_lst:
                            return False
                        else:
                            return True
                    elif (splited_input[3] in noun_lst) and (splited_input[3]!=splited_input[2]):
                            return True
                    else:
                        return False
                elif len(splited_input) == 5:
                    if splited_input[3] not in noun_lst:
                        return False
                    elif splited_input[3] == splited_input[2]:
                        return False
                    if splited_input[4] not in year_lst:
                        return False
                    else:
                        return True

    else:
        return False