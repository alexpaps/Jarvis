def CalculateThePercentages():
    from fb import FootballPercantageCalculation
    FootballPercantageCalculation()

def BettingOddsIntoList():
    read = open("BettingOdds.txt","r")
    Lista = []
    ListInList = []
    counter = 0

    for line in read:
        if counter == 0:
            Lista.append(line)
            counter += 1
        elif 1<=counter<=3:
            Lista.append(line)
            counter += 1
            if counter == 4:
                ListInList.append(Lista)
                counter = 0
                Lista = []
    
    read.close()

    return ListInList

def BestBettingOpportunities():
    from fb import FootballPercantageCalculation
        
    Write = open("TopBetsOfTheWeek.txt","w")
    GameList = FootballPercantageCalculation()
    OddsList = BettingOddsIntoList()

    for List in GameList:
        if float(List[1]) > 45:
            for Item in OddsList:
                if List[0] == Item[0]:
                    if float(Item[1]) > float(List[4]):
                        Write.write("{} : 1 with odd {}({})\n".format(List[0].strip(),Item[1].strip(),round(List[4],2)))
                        break
        elif float(List[3]) > 45:
            for Item in OddsList:
                if List[0] == Item[0]:
                    if float(Item[3]) > float(List[6]):
                        Write.write("{} : 2 with odd {}({})\n".format(List[0].strip(),Item[3].strip(),round(List[6],2)))
                        break

    Write.close()


