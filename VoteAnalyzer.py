import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# ElectionUSA2012.csv
def readCSV(fileName):    #This function provides the given file to be read.
    rows = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader:
            rows.append(i)
        return rows

def writeFile(fileName, data):  #This function provides the given file to be write.
    with open(fileName, 'w') as f:
        f.write(data)

rows = readCSV(sys.argv[1])
def retrieveData(fileName, nominees):   #This function assigns the particular values on the given rows to a particular list.
    rows = readCSV(fileName)
    columns = rows[0]
    res = []
    for n in nominees:
        for r in rows[1:]:
            res.append(r[columns.index(n)])
    writeFile("retrieveData.txt", ",".join(res))
    return rows
retrieveData(sys.argv[1],sys.argv[2].split(','))
rows_S = []
data_R = []
data_O =[]
data_J = []
data_ST = []
def rowAssigner():   # This function adds the particular values on the rows to the given lists.
    rows = readCSV(sys.argv[1])
    for y in rows[1:]:
        rows_S.append(y[0])
        data_O.append(int(y[3]))
        data_R.append(int(y[4]))
        data_J.append(int(y[5]))
        data_ST.append(int(y[6]))
    
rowAssigner()




def DispBarPlot():  #This function creates a chart to show that the most voted nominees.
    x_axis =np.arange(len(rows_S))
    plt.xticks(x_axis, rows_S, rotation=90)
    plt.bar(x_axis-0.15,data_R,label="Romney",width=0.3,color=['red'], edgecolor= ['black'])
    plt.bar(x_axis+0.15,data_O,label="Obama",width=0.3,color=['blue'], edgecolor= ['black'])
    plt.xlabel('States')
    plt.ylabel('Vote Count')
    plt.title("Comparative Demonstration with Bar Plot")
    plt.gca().yaxis.set_major_formatter("{x}")
    plt.legend()
    plt.gcf().set_size_inches(20, 8)
    plt.savefig("ComparativeVotes.pdf", format="pdf", bbox_inches="tight",dpi=100)
    plt.cla()
    plt.rcParams.update(plt.rcParamsDefault)
    
DispBarPlot()


# Convert data to integer for each value in the data and calculates vote percentages and creates a graph from this data.
def compareVoteonBar():
    o_int = [int(i) for i in data_O]
    r_int = [int(i) for i in data_R]
    j_int = [int(i) for i in data_J]
    st_int = [int(i) for i in data_ST]
    total_O = 0
    total_R = 0
    total_J = 0
    total_ST = 0
    for ele in range(0, len(o_int)):
        total_O = total_O + o_int[ele]

    for ele in range(0, len(r_int)):
        total_R = total_R + r_int[ele]

    for ele in range(0, len(data_J)):
        total_J = total_J + j_int[ele]

    for ele in range(0, len(data_ST)):
        total_ST = total_ST + st_int[ele]
    total_vote = total_O + total_J + total_R + total_ST
    avg_o = ((total_O)/(total_vote) * 100)
    avg_r = ((total_R)/(total_vote) * 100)
    avg_j = ((total_J)/(total_vote) * 100)
    avg_st = ((total_ST)/(total_vote) * 100)
    
    x_axis = [avg_o, avg_r, avg_j,avg_st]
    

    plt.bar([format(x,'.3f') + " %" for x in x_axis],x_axis,label=rows[0][3:7],width=0.3, color=['red','blue', 'yellow', 'cyan'], edgecolor= ['black'])
    plt.xlabel('Nominees')
    plt.ylabel('Vote percentages')
    plt.gca().yaxis.set_major_formatter("{x}")
    plt.ylim(0,60)
    plt.legend()
    plt.savefig("CompVotePercs.pdf", format="pdf", bbox_inches="tight")
    plt.cla()
    plt.rcParams.update(plt.rcParamsDefault)
    

compareVoteonBar()


def obtainHistogram(numbers: list):   # Takes ones and tens of each value from the list that is given in the parameter and calculates the frequency.
    p = [0] *10
    for x in numbers:
        x = str(float(x)).split('.')[0]
        ones = x[-1]
        if len(x) >1:
            tens = x[-2]
        else:
            tens = 0
        p[int(tens)]+=1
        p[int(ones)]+=1
    s = sum(p)
    
    return [x/s for x in p]


def plotHistogram(numbers: list):    # Plots the frequency of digits.
    plt.axhline(0.10, color='g', linestyle='dashed')
    plt.plot(numbers, color='r')
    plt.xticks([x for x in range(10)])
    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.title('Histogram of least sign. digits')
    plt.legend(['Mean', 'Digit Dist.'])
    plt.savefig("Histogram.pdf", format="pdf", bbox_inches="tight")
    plt.cla()
    plt.rcParams.update(plt.rcParamsDefault)

all_data = data_ST + data_J + data_O + data_R
plotHistogram(obtainHistogram(all_data))

def plotHistogramWithSample():    # Creats random samples from list of size of the list sizes and plots these random samples.
    prot = [10, 50, 100,1000,10000]
    colrs = ['r','b','y','c','purple']
    l = []
    for w in prot:
        inter_l = []
        for i in range(0,w):
            inter_l.append(random.randint(0, 100))
        
        index = prot.index(w)
        l.append(inter_l)
        plt.plot(obtainHistogram(inter_l), color=colrs[index])
        plt.axhline(0.10, color='g', linestyle='dashed')
        plt.xticks([x for x in range(10)])
        plt.xlabel('Digits')
        plt.ylabel('Distribution')
        plt.title(f'Histogram of least sign. digits - Sample:{index+1}')
        plt.legend(['Mean', 'Digit Dist.'])
        plt.autoscale(tight=True)
        plt.savefig(f"HistogramSample{index+1}.pdf", format="pdf", bbox_inches="tight")
        plt.cla()
        plt.rcParams.update(plt.rcParamsDefault)

    return l
        
listOfSamples = plotHistogramWithSample()

def calculateMSE(l1:list, l2:list):    # Calculates the Mean Squared Error.
    err = 0
    for i in range(len(l1)):
        err+= ((l1[i] - l2[i])**2)
    return err/len(l1)

usaMSE = calculateMSE(obtainHistogram(all_data), [0.1]*len(all_data))

print(f"MSE value of 2012 USA election is {usaMSE}")


