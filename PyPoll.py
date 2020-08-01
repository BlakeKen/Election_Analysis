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
candidate_options = [] 

#create empty dictionary
candidate_votes = {}

# Winning Candidate and Count Tracker
#declare variable that holds empty string for the winning canidate 
winning_candidate = ""
#declare winning count variable equal to zero
winning_count = 0
#declare winning percentage variable equal to zero
winning_percentage = 0

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
      candidate_name= row[2]


      #If the canidate does not matching a canidate already added
      if candidate_name not in candidate_options:
        #add it to the list of canidates
        candidate_options.append(candidate_name)

        #track current canidates votes for dictionary
        candidate_votes[candidate_name] = 0 

        #print total votes
        #print(total_votes)
 
      #add a vote to the canidates count
      candidate_votes[candidate_name] += 1
      #save the results to the text file
with open(file_to_save, "w") as txt_file:

  #Print final count to the terminal
  election_results= (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes {total_votes:,}\n"
    f"-------------------------\n")
  print(election_results, end="")
  #Save the final count to text file
  txt_file.write(election_results)

  # Determine the percentage of votes for each candidate by looping through counts.
  # Iterate through the candidate list
  for candidate_name in candidate_votes:
      #Retrieve vote count of a candidate.
      votes = candidate_votes[candidate_name]
      #Calculate the percentage of votes.
      vote_percentage = float(votes) / float(total_votes) * 100
      #Print out the  candidate, vote count and percentage
      candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      #print candidate results
      print(candidate_results)
      # Write candidate results to text file
      txt_file.write(candidate_results)

      # Determine winning vote count and candidate
      #If the votes and vote percentage are greater than the winning count.
      if (votes > winning_count) and (vote_percentage > winning_percentage):
          # If true then set winning_count = votes and winning_percent =
          # vote_percentage.
          winning_count = votes
          winning_percentage = vote_percentage
          # Set the winning_candidate equal to the candidate's name.
          winning_candidate = candidate_name
  winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count :{winning_count:,}\n"
        f"Wiining Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
  print(winning_candidate_summary)
  #write the winning candidate's name to the text file
  txt_file.write(winning_candidate_summary)