# VOTE ANALYZER

In a society where freedom and democracy reign, people have a right to return to their ruling
class. Election is a formal way of accepting or rejecting a political proposition by voting.
People, particularly those living in poor countries, worry about their votes and question
whether the election is trustworthy. However, thanks to the statistical tools, we can easily
find out if any fraud attempts were made.

In this project, I implemented a Python program that analyzes the results of the
2012 presidential election in the United States of America (USA) and interprets whether it
is fraudulent or not. It was an election with four major parties (Democratic, Republican,
Libertarian, and Green) and 30 nominees, most of whom were write-in candidates. Democrat
nominee Obama B., republican nominee Romney M., libertarian nominee Jonhson G., and
the green nominee Stein J. participated in the election that resulted in the victory of the
Democrats. You are given the election results in a file named ElectionUSA2012.csv2.
This file records the number of votes separately for each state. Each row represents a state in
the USA, and there are eight different information in a single row: State name, total votes,
electoral votes, total vote, # of votes for Obama, Romney, Johnson, Stein, and others. To sum
up, there are 204 election results (you can exclude the votes for ‘others’ in this assignment)
you care about to reveal fraudulence, if any.

Instructions: To run this program, you should write the command provided below

python voteanalyzer.py ElectionUSA2012.csv candidate_separated_by_comma

