"""
@author : Saurabh Rewaskar (ssr1137)
Description : This program creates a new csv file which has the time of the crime split
up into 3 new attributes
"""
with open('Crime_Data.csv') as file: #master data set
    dateLst=[]
    fLine=file.readline().strip().split(",")
    frstLine=fLine[0:2]
    frstLine.extend(("Month","Day","Hour"))#add header name for new attrbutes
    frstLine=frstLine+fLine[3:]
    fle=open("Process_Date.csv","w+")#file to write processed data
    fle.write(",".join(frstLine)+"\n")
    for line in file:
        date=line.split(",")[2].split(" ")
        date[1]=str(int(date[1][0:2])+12)+date[1][2:]#converting to 24 hour format
        if date[1][0:2]=="24":#if exact 24 then make it 00 AM.
            date[1]="00"+date[1][2:]
        date=date[0:2]
        temp=line.split(",")[0:2]
        temp.append(date[0][0:2])
        temp.append(date[0][3:5])
        temp.append(date[1][0:2])
        temp+=(line.split(",")[3:])
        fle.write(",".join(temp))
        dateLst.append(temp)
    fle.close()