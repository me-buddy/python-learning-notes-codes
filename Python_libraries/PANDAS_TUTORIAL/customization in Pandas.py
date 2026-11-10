"""
PANDAS_TUTORIAL/customization in Pandas.py

* .apply(functionCall)
"""
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\NUMPY TUTORIAL\cricket_stats.csv")
balls = df["Balls"]
runs = df["Runs"]
# print(balls)
# print("------------")
# print(runs)

# print(df.head())

"""
Performance Categories
-----------------------
*Classify batsmen.
--------------------------------
Strike Rate         Category
--------------------------------
    >140            Explosive
    120–140         Aggressive
    90–120          Balanced
    <90             Defensive
--------------------------------

"""
df["Strike_rate"] = np.divide(runs,balls)*100
print(df.head())

def player_category(Strike_rate):
    if(Strike_rate>140):
        return "Explosive"
    elif(Strike_rate>=120 and Strike_rate<=140):
        return "Aggresive"
    elif(Strike_rate>=90 and Strike_rate<120):
        return "Balanced"
    else:
        return "Defensive"

#* create a players_category column
df["players_category"] = df["Strike_rate"].apply(player_category)

print("\n=======================================================================================\n")

# print(df.head())
Explosive_players = df.loc[df["players_category"]=="Explosive",["Player","Strike_rate"]]
aggresive_players = df.loc[df["players_category"]=="Aggresive",["Player","Strike_rate"]]

print("Explosive Players : \n",Explosive_players)
print("Aggresive Players : \n",aggresive_players)

print("\n=============================================\n")

# print("Explosive Players : \n",Explosive_players.max())
# print("\nAggresive Players : \n",aggresive_players.max())

# print("Total Explosive Players",Explosive_players.count() )
# print("Total Aggresive Players",aggresive_players.count() )


# ================= rename a column ======================
# df.rename(columns={"RunsGiven":"Total_Run_Given"},inplace=True)
# # df["Total_Run_Given"] = df["RunsGiven"]
# print("\n\n",df.head())
df.rename(columns={"Player":"players"},inplace=True)
print("\n\n",df.head())



