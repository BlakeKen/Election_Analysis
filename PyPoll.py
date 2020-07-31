# Dependencies 
import os 
import csv

# assign variable to load from
file_to_load = os.path.join("Resources" , "election_results.csv")

# assign variable for path to save to
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter 
total_votes = 0 

#declare variable for canidate options
canidate_options = [] 

#create empty dictionary
canidate_votes = {}


# use open statement to open file
with open(file_to_load) as election_data:
 #read the file using reading function
    file_reader = csv.reader(election_data)

    #Read the header row 
    headers= next(file_reader)
   
    #Print each row in the csv file
    for row in file_reader:
      #add to the total votes
      total_votes += 1 # same as number= number + 

      #print the canidate name for each row 
      canidate_name= row[2]


      #If the canidate does not matching a canidate already added
      if canidate_name not in canidate_options:
        #add it to the list of canidates
        canidate_options.append(canidate_name)

        #track current canidates votes 
        canidate_votes[canidate_name] = 0 

       #print total votes
       # print(total_votes)
 
      #add a vote to the canidates count
      canidate_votes[canidate_name] += 1


#print the canidate vote dictionary
print(canidate_votes)

#Complete list of canidates with votes

#the percentage of votes each canidate won

#the total number of votes for each canidate 

#the winner based on the most votes