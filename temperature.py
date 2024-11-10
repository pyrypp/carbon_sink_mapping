'''
Use function scoreFromCsv
'''

from math import exp
import json

def tempScore(avg: float, std: float, temp: float) -> float:
    '''
    Don't care about this!!!
    Returs a score for a single datapoint of surface temperature corresponding how well the plant likes the temperature.
    '''
    value = exp(-((temp+273.15-avg) ** 2)/(2 * std ** 2))
    return value

def tempScoreAvg(avg: float, diff: float, temps: list[float]) -> float:
    '''
    Returns a score for how well the plant will survive in given temperature conditions over the whole year.
    '''
    std = diff / 3.0
    total = 0.0
    for temp in temps:
        total += tempScore(avg, std, temp)
    return total/len(temps)

def csvParser(fileName: str) -> list[float]:
    '''
    Parses the temperature data from ilmatieteenlaitos temperature data. The header line has to be removed manually.
    '''
    with open(fileName) as data:
        temps: list[float] = []
        for line in data:
            try:
                temps.append(float(line.split(",")[-1].strip("\n").strip("'").strip('"'))) # this looks bad, but please for the love of god don't touch
            except:
                pass
            try:
                temps.append(float(line.split(",")[-2].strip('"')))
            except:
                pass
    return temps

def scoreFromCsv(plantName: str, tempLocation: str):
    '''
    Returns the temperature compatibility of the plant given the location of temperature data.
    '''
    temps = csvParser(tempLocation)
    with open("plants.json", "r") as file:
        data = json.load(file)
    avg = data['Plants'][plantName]['tempAvg']
    diff = data['Plants'][plantName]['tempDiff']
    score = tempScoreAvg(avg, diff, temps)
    return score

if __name__ == "__main__":
    import random
    from datetime import datetime

    print(scoreFromCsv("Horse chestnut", "Temp Data\Turku lentoasema_ 1.1.2020 - 31.12.2023_bb93018f-170c-4c7a-983b-911db9ccce39.csv"))


    # tempData = csvParser(fileName)

    # tempData = []
    # for i in range(730):
    #     tempData.append(random.randint(290, 310) + 0.1)
    # startTime = datetime.now()
    # score = tempScoreAvg(283, 10, tempData)
    # print(score)
    # dt = datetime.now() - startTime
    # print(dt.seconds)