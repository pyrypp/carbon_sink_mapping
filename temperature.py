from math import exp

def tempScore(avg: float, std: float, temp: float) -> float:
    '''
    Returs a score for a single datapoint of surface temperature corresponding how well the plant likes the temperature.
    '''
    value = exp(-((temp-avg) ** 2)/(2 * std ** 2))
    return value

def tempScoreAvg(avg: float, std: float, temps: list[float]) -> float:
    '''
    Returns a score for how well the plant will survive in given temperature conditions over the whole year.
    '''
    total = 0.0
    for temp in temps:
        total += tempScore(avg, std, temp)
    return total/len(temps)

if __name__ == "__main__":
    import random
    from datetime import datetime
    
    tempData = []
    for i in range(730):
        tempData.append(random.randint(290, 310))
    startTime = datetime.now()
    score = tempScoreAvg(296.5, 5.4, tempData)
    print(score)
    dt = datetime.now() - startTime
    print(dt.microseconds)