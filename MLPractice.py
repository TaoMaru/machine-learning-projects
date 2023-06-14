# MLPractic.py - This program is intended to facilitate practice with
## Machine Learning concepts. Using numpy and scipy, this program is
## built with a modular approach to manipulating small data sets.
## Dev: Maria J. - June 13, 2023.

import numpy as np
from scipy import stats as st
import math as mt

#calc the mean speed from an array of speeds
def calcMeanSpeed( speeds ):
    mean = np.mean(speeds)
    return mean

#calc the median speed from an array of speeds
def calcMedianSpeed( speeds ):
    median = np.median(speeds)
    return median

#calc the mode from an array of speeds
def calcModeOfSpeed( speeds ):
    mode = st.mode(speeds)
    return mode

#calc the standard deviation from an array of speeds
def calcStdDev( speeds ):
    stdD = np.std(speeds)
    return stdD

#calc the variance from an array of speeds
def calcVar( speeds ):
    var = np.var(speeds)
    return var

#append an item to a cumulative list of data
def addToSpeedData( dataList, dataItem ):
    dataList.append(dataItem)
    
#calc the percentile from a data set given as a list
def calcPercentile( dataSet, targetPercentile ):
    perc = np.percentile( dataSet, targetPercentile )
    return perc
    
#stdDevAsSqRt = mt.sqrt(speedVar) # calc std dev. as sqrt variance

#print("Std deviation as sqrt of variance:", stdDevAsSqRt) #print it



def main():

    ## Basic Stats
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] # list of speeds
    speedSummaryData = []
    
    meanSpeed = calcMeanSpeed(speed) # calc the mean from speed
    addToSpeedData( speedSummaryData, meanSpeed )
    
    print("Mean speed:", speedSummaryData[0]) # print the mean

    medSpeed = calcMedianSpeed(speed) # calc the median from speed
    addToSpeedData( speedSummaryData, medSpeed )
    
    print("Median speed:", speedSummaryData[1]) # print the median

    #modeSpeed = calcMode(speed) # calc the mode from speed

    #print("Mode speed:", modeSpeed) # print mode result

    stdDev = calcStdDev(speed) # calc std deviation from speed
    addToSpeedData( speedSummaryData, stdDev )

    print("Std deviation:", speedSummaryData[2]) # print std dev.

    speedVar = calcVar(speed) # calc variance
    addToSpeedData( speedSummaryData, speedVar )

    print("Variance:", speedSummaryData[3]) #print variance

    ## Percentiles
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    #list of random ages

    perc75 = calcPercentile( ages, 75 ) # calc 75th percentile from ages
    print("75th percentile:", perc75)

    perc90 = calcPercentile( ages, 90 ) # calc 90th percentile from ages
    print("90th percdntile:", perc90)

#run main()
main()
