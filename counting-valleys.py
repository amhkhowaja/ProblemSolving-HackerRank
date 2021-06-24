def countingValleys(steps, path):
    summ=0
    count_valley=0
    for s in path:
        if s=='U':
            summ+=1
        elif s=='D':
            summ-=1
        if s=='U' and summ==0:
            count_valley+=1  
    return count_valley  
