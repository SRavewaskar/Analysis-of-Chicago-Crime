"""
@author : Saurabh Rewaskar (ssr1137)
Description : This program creates a new csv file which has equal number of
arrests and release records in order to get a frequent data with equal records
of both target classes to find patterns and trends in the data.
"""

import csv # to read from and write into a csv file


def main():
    '''
    Creating a new dataset with equal number of Arrests and
    Releases onto a new file.
    :return: None
    '''
    flag = False
    false_count = 1
    true_count = 1
    writer = csv.writer(open("Binary_Arrests.csv", 'w', newline='')) # writes to a new file
    with open("Every_Month_Data.csv") as file:
        for line in csv.reader(file): # this loop creates a new file with equal arrests and releases
            if flag is True:
                if line[6] == "FALSE": # checks if arrests were made or not
                    if false_count <= 2500:
                        writer.writerow(line)
                        false_count += 1
                else:
                    if true_count <= 2500:
                        writer.writerow(line)
                        true_count += 1
            else:
                flag = True
                writer.writerow(line)
    file.close()


if __name__ == '__main__':
    main()