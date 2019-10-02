def validate_query(query_str):
    qualifiers_lst = ['HAPPY', 'SUPPORTIVE', 'FREE', 'CORRUPT', 'GENEROUS', 'WEALTHY', 'HEALTHY']
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
                if splited_input[3] !="COUNTRY":
                    return False
                else:
                    # 2 most happy country
                    if len(splited_input) == 4:
                        if splited_input[3] == "COUNTRY":
                            return True
                        else:
                            return False
                    # 2 most happy country 2015
                    elif len(splited_input) == 5:
                        if splited_input[4] != "COUNTRY":
                            if splited_input[4] in year_lst:
                                return True
                            else:
                                return False
                        else:
                            return False
                    # 2 most happy country in region
                    # 2 most happy country language speaking
                    elif len(splited_input) == 6:
                        if splited_input[4] != "IN" and splited_input[4] != "LANGUAGE":
                            return False
                        else:
                            if splited_input[4] == "IN":
                                if splited_input[5] == "REGION":
                                    return True
                                else:
                                    return False
                            elif splited_input[4] == "LANGUAGE":
                                if splited_input[5] == "SPEAKING":
                                    return True
                                else:
                                    return False
                    # 2 most happy country in region 2015
                    # 2 most happy country language speaking 2015
                    elif len(splited_input) == 7:
                        if splited_input[4] != "IN" and splited_input[4] != "LANGUAGE":
                            return False
                        else:
                            if splited_input[4] == "IN":
                                if splited_input[5] == "REGION":
                                    if splited_input[6] in year_lst:
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            elif splited_input[4] == "LANGUAGE":
                                if splited_input[5] == "SPEAKING":
                                    if splited_input[6] in year_lst:
                                        return True
                                    else:
                                        return False
                                else:
                                    return False


    ################################ most happy country region 2015 ############################
    elif splited_input[0] in rank_lst:
        if splited_input[1] not in qualifiers_lst:
            return False
        else:
            if splited_input[2] != "COUNTRY":
                return False
            else:
                # length 3, 4, 5
                if len(splited_input) == 3:
                    if splited_input[2] == "COUNTRY":
                        return True
                    else:
                        return False
                # 2 most happy country 2015
                elif len(splited_input) == 4:
                    if splited_input[3] != "COUNTRY":
                        if splited_input[3] in year_lst:
                            return True
                        else:
                            return False
                    else:
                        return False
                # 2 most happy country in region
                # 2 most happy country language speaking
                elif len(splited_input) == 5:
                    if splited_input[3] != "IN" and splited_input[3] != "LANGUAGE":
                        return False
                    else:
                        if splited_input[3] == "IN":
                            if splited_input[4] == "REGION":
                                return True
                            else:
                                return False
                        elif splited_input[3] == "LANGUAGE":
                            if splited_input[4] == "SPEAKING":
                                return True
                            else:
                                return False
                # 2 most happy country in region 2015
                # 2 most happy country language speaking 2015
                elif len(splited_input) == 6:
                    if splited_input[3] != "IN" and splited_input[3] != "LANGUAGE":
                        return False
                    else:
                        if splited_input[3] == "IN":
                            if splited_input[4] == "REGION":
                                if splited_input[5] in year_lst:
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        elif splited_input[3] == "LANGUAGE":
                            if splited_input[4] == "SPEAKING":
                                if splited_input[5] in year_lst:
                                    return True
                                else:
                                    return False
                            else:
                                return False

    else:
        return False
