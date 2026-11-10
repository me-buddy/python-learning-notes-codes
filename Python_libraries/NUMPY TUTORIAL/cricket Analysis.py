"""
numpy.genfromtxt is a powerful NumPy function used to load tabular data from text files (like .txt or .csv) into a NumPy array.
Unlike the faster numpy.loadtxt, genfromtxt is specifically designed to handle missing data, mixed data types, 
and custom text formatting
"""

import numpy as np
"""
arr = np.array([
    [1,2,3,4,5],
    [10,22,32,4,54]
    ])

# print(arr[row,col])
# print(arr[0,0]) # 1
# print(arr[:,0]) # 1,10 => return all records from 1 column in all rows.
"""

data = np.genfromtxt(r"C:\Users\sagar\Desktop\shreyas AIML\NUMPY TUTORIAL\cricket_stats.csv",
                     delimiter=",",
                     dtype=str,
                     skip_header=1
)
player_names  = data[:,0]
teams = data[:,1]
numeric_records = data[:,2:].astype(float) #^ generate an array of all numeric records from the data array.
# for name in numeric_records:
#     print(name)

# * Batting Analysis
print(numeric_records)
#^ extract columns from numeric_records nested list
matches = numeric_records[:,0]
runs = numeric_records[:,1]
balls = numeric_records[:,2]
fours = numeric_records[:,3]
sixes = numeric_records[:,4]

print("match\truns\tballs\tfour\tsix")
for m , r , b , f , s in zip(matches,runs,balls,fours,sixes):
    print(f"{m}\t{r}\t{b}\t{f}\t{s}")

#print()
#print('StrikeRate = ( Runs/balls )×100 \n')

#&1. CALCULATING STRIKE RATE 
strike_rate = np.array(np.divide(runs,balls)*100)

# print(strike_rate)
# print("\n",(650/560)*100)

mx = np.max(strike_rate)
mn = np.min(strike_rate)

#
# for player,strike_rate in zip(player_names,strike_rate):
#     print(f"{player}\t = {strike_rate}")
#     print("-------------------------------------------")

strike_records = np.array(list(zip(player_names,strike_rate)))

max_index = np.argmax(strike_records[:, 1].astype("float64"))                           

#^ 2. Extract the name (column 0) and strike rate (column 1)
best_player = strike_records[max_index, 0]
max_sr = strike_records[max_index, 1]

print(f"Highest Strike Rate: {best_player} => ({max_sr})")


#&2. Boundary Runs

boundry_runs = (fours*4) + (sixes*6)                                                               
# print("\nBoundry Runs : \n",boundry_runs.astype("int"))

players_run_boundry = np.array(list(zip(player_names , boundry_runs)))
# print(players_run_boundry)

max_boundry_index = np.argmax(players_run_boundry[:,1].astype("float64"))
# print(max_boundry_index)

best_player = players_run_boundry[max_boundry_index, 0]
max_rn = players_run_boundry[max_boundry_index, 1]

print(f"\nHighest Boundry Runs: {best_player} => ({max_rn})")


#&3. Boundary Percentage

Boundary_percentage = (boundry_runs/runs)*100
# print(Boundary_percentage)

players_boundry_percentage_array = np.array(list(zip(player_names,Boundary_percentage)))
# print(players_boundry_percentage_array)

max_boundry_index = np.argmax(players_boundry_percentage_array[:,1].astype("float64"))

best_player = players_boundry_percentage_array[max_boundry_index,0]
max_boundry_percentage = players_boundry_percentage_array[max_boundry_index,1]
#print(f"Player : {best_player}\nBoundry-Percentage : {max_boundry_percentage}")


#================== practice============================

#* ====== calculating strike rate================

strike_rate=np.array(np.divide(runs,balls)*100)
#print(strike_rate)
print("\n",(650/560)*100)

mx=np.max(strike_rate)
mn=np.min(strike_rate)
#print("maximum strike rate :",mx)
#print("minimum strike rate:",mn)


strike_records= np.array(list(zip(player_names,strike_rate)))
max_index=np.argmax(strike_records[:,1].astype("float64"))
best_player=strike_records[max_index,1]

#print(f"highest strike rate :{best_player}=>({max_sr})")



# ======================================================== economy per player:=========================================================================
# economy=runsgiven/over

print("------------------------------------------------------------------")
runs_given=numeric_records[:,7]
overs=numeric_records[:,6]
# economy=runs_given/overs
economy=np.divide(runs_given,overs)

#* np.nanargmax(array) :- return the index of  maximum value which is not a nan
#! NOTE :- Bydefault argmax() return nan value has highest index.

records = np.array(list(zip(player_names,economy)))
print(records)
min_economy_index = np.nanargmin(records[:,1].astype("float64")) # 40
# print(player_names[min_economy_index])

print(records[min_economy_index][0]," => Economy => ",records[min_economy_index][1])

