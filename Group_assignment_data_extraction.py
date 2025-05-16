
# Reading lines from the file              #Lines - Refers back to the .txt file(score.txt)
def read_file():
    with open("scores.csv", "r") as file:  #Opens the .txt file
        lines = file.readlines()           #reads all the lines
    return lines                           #Returns to the lines in the .txt file

# Dictionary
def score(lines):
    scores = {}                            #Empty dictionary
    # for loop to go through each line
    for line in lines:                     #Key value pairs, dictionaries cannot have duplicate keys.
        name, score = line.strip().split(":")
        scores[name] = int(score)          #to store the score as an integer
    return scores                          #returns to the dictionary (scores)containing the data in the .txt file

# Sorting
def show_top_3(scores):
     #sorts the dictionary by the score in descending order
     #x - gives the name
     #x[1] - Gives the score
     #key=lambda x: x[1] - Sorts based on score
     #reverse=True - Sorts from highest to lowest
    print("Scores Dictionary:", scores)     #Checks the dictionary if it has data
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_scores[:3]               #Shows the first 3 items in the list
    print("Top 3 Scorers:")
    #For loop to print the names and scores
    for name, score in top_3:
        print(name, "-", score)

# Main program
lines = read_file()             #Reads the lines in the file
scores = score(lines)           #Creates a dictionary for the lines in score.txt
show_top_3(scores)