{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python394jvsc74a57bd0c06ecb8de50cb2414ac45cc017d01f8fa8736973dfcdddd26f318d0e2b6c565d",
   "display_name": "Python 3.9.4 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "c06ecb8de50cb2414ac45cc017d01f8fa8736973dfcdddd26f318d0e2b6c565d"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [],
   "source": [
    "## import modules\n",
    "import os\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [],
   "source": [
    "## set/ define file path\n",
    "pyPoll_path = os.path.join(os.getcwd(), 'Resources', 'election_data.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'c:\\\\Users\\\\vaab2\\\\Desktop\\\\My_Python_Script\\\\Resources\\\\election_data.csv'"
      ]
     },
     "metadata": {},
     "execution_count": 205
    }
   ],
   "source": [
    "pyPoll_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "votes = 0\n",
    "vote_count = []\n",
    "candidates = []\n",
    "csvreader = ['1','2']\n",
    "#open csv file as a reader and determine the total number of votes cast\n",
    "with open (pyPoll_path,'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter =',')\n",
    "    # from statistics import mean\n",
    "    #skip header\n",
    "    header = next(csvreader)           \n",
    "    for row in csvreader:\n",
    "        #Finding Total votes\n",
    "        votes = votes + 1\n",
    "        #finding votes per candidateCandidates\n",
    "        candidate = row[2]\n",
    "        #Votes per candidate\n",
    "        if candidate in candidates:\n",
    "           candidate_count = candidates.index(candidate)\n",
    "           vote_count[candidate_count] = vote_count[candidate_count] + 1\n",
    "        else:\n",
    "           candidates.append(candidate)\n",
    "           vote_count.append(1)  \n",
    "           \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "['Voter ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "print(header)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "#finding the Percentages per vote per candidate\n",
    "percentages = []\n",
    "max_votes = vote_count[0]\n",
    "max_votes_index = 0\n",
    "for count in range(len(candidates)):\n",
    "    vote_percentage = vote_count[count]/votes*100\n",
    "    percentages.append(vote_percentage)\n",
    "    if vote_count[count] > max_votes:\n",
    "        print(max_votes)\n",
    "        max_votes_index = count\n",
    "    winner = candidates[max_votes_index]\n",
    "    percentages = [round (i,2) for i in percentages]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "\nElection Results\n--------------------------------\nTotal Votes: 3521001\n--------------------------------\nKhan: 63.0% (2218231)\nCorrey: 20.0% (704200)\nLi: 14.0% (492940)\nO'Tooley: 3.0% (105630)\n--------------------------------\nWinner:  Khan\n--------------------------------\n"
     ]
    }
   ],
   "source": [
    "#Print results           \n",
    "print()\n",
    "print(\"Election Results\")\n",
    "print(\"--------------------------------\")\n",
    "print(f\"Total Votes: {votes}\")\n",
    "print(\"--------------------------------\")\n",
    "for count in range(len(candidates)):\n",
    "    print(f\"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\")\n",
    "print(\"--------------------------------\")\n",
    "print(f\"Winner:  {winner}\")\n",
    "print(\"--------------------------------\")\n",
    "f.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Specify file path to write file to\n",
    "election_output_path = os.path.join(os.getcwd(), 'Resources', 'new_election_file.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "c:\\Users\\vaab2\\Desktop\\My_Python_Script\\Resources\\new_election_file.csv\n"
     ]
    }
   ],
   "source": [
    "print(election_output_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open the file in write mode\n",
    "with open(election_output_path, 'w') as csvfile:\n",
    "    csvwriter= csv.writer(csvfile, delimiter =\",\")\n",
    "    # write in the lines\n",
    "    csvwriter.writerow(\"Election Results\")\n",
    "    csvwriter.writerow(f\"Total Votes: {votes}\")\n",
    "    csvwriter.writerow(f\"{candidates[count]}: {percentages[count]}% ({vote_count[count]})\")\n",
    "    csvwriter.writerow(f\"Winner:  {winner}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}