# Dependencies 
import os 
import csv

# assign variable to load fro
file_to_load = os.path.join("Resources" , "election_results.csv")

# assign variable for path to save to

file_to_save = os.path.join("analysis", "election_analysis.txt")

# use open statement to open file
with open(file_to_load) as election_data:
 #read the file using reading function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers= next(file_reader)
    print (headers)

    #Print each row in the csv file
  #  for row in file_reader:
  #      print(row)




#total numer of votes 

#Complete list of canidates with votes

#the percentage of votes each canidate won

#the total number of votes for each canidate 

#the winner based on the most votes