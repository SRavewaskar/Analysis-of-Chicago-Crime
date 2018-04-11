@author:Saurabh Rewaskar

Data was obtained from:
https://data.cityofchicago.org/Public-Safety/Crimes-2017/d62x-nvdr

Processing was done using Python, R and Weka
Subsets of data formed were;
Crime_Data : original data
Every_Month_Data : equal instances for every month
Process_data : Data selected from master dataset Crime_Data only considering relevant attributes
Binary_Arrests : equal arrests and non-arrests

/Code folder contains python files to generate these datasets.

Run:
1] ProcessedData.py to generate Process_Data.csv using Crime_Data.csv
2] EveryMonth.py to generate Every_Month_Data.csv
3] Equal_Arrests.py to generate Binary_Arrests.csv

Feed this files into Weka and come up with different hypotheses.
I've shared my findings in the report.