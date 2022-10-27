import _csv
import os
# Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# declaring our variables 

total_votes = 0
candidate_options = []
#empty dictonary : canidate name, number of votes
candidate_votes = {}
# winning candidate and winning vote count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = _csv.reader(election_data)
    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #pull canidate name from row of data 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
           #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            #add a vote to that candidates count        
        candidate_votes[candidate_name] += 1
            #For loop through dictionary to find percentage of voters
for candidate_name in candidate_votes:
    # get number of votes per canidate 
    votes = candidate_votes[candidate_name]
    # math to make percent 
    vote_percentage = float(votes) / float(total_votes) * 100
    #display canidate name and number of votes
# Code for winning vote count and candidate 
# Determine if the votes are greater than the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage): 
    #2 if above is true then set winning_count = votes and winning_percent =
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name  
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = ( 
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
print(winning_candidate_summary)
