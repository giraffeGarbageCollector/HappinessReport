#TODO
#Returns the search results of a validated search string. If no results, return the empty array
def search(validated_search_str):
    parsed = validated_search_str.split()
    if (isinstance(parsed[0], int)==True):
        rank = parsed[0]
        order = parsed[1]
        qualifier = parsed[2]
        noun = parsed[3]
        year = parsed[4]
        
        if (order == "most"):
            order = "ASC"
        elif (order == "least"):
            order = "DESC"
        
        con = sqlite3.connect("CountryData.db")
        cur = con.cursor()
        if (noun == "country"):
            cur.execute("SELECT Country,rank,SD,Positive affect,Negative Affect,Social Support,Freedom,Corruption,Generosity,GDP per Capita,Life Expectancy FROM RankTable WHERE Year IN ("+year+") AND "+noun+" FROM RankTable ORDER BY "+qualifier+" "+order+" LIMIT "+rank)
    
    results = []
    return results
