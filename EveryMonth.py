"""
@author : Saurabh Rewaskar (ssr1137)
Description : This program creates a new csv file which has equal number of
records from each month.
"""

with open('Process_Date.csv') as file: #master data set
    firstLine=file.readline()
    data=[]
    #new file with processed data set
    fle=open('Every_Month_Data.csv','w+')
    fle.write(firstLine)
    for line in file:
        line=line.split(",")
        data.append(line)
    actualData=[]
    for ind in range(1,10):
        #list comprehension to select frist 1500 records for every month index from 1 to 9.
        tmp=[x for x in data if x[2]=="0"+str(ind)][0:1500]
        for record in tmp:
            #convert list to comma separated string.
            fle.write(",".join(record))
    fle.close()
