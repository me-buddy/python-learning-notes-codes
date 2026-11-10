import pandas as pd

df = pd.read_csv(r"C:\Users\sagar\Desktop\shreyas AIML\NUMPY TUTORIAL\cricket_stats.csv")
"""
1 => df[condition]

"""
# print(df.head())
print("====================================================================================\n\n")
# print(df.tail())

players_above_600 = df[df["Runs"]>=600]

#* .loc[]
# players_above_600 = df.loc[df["Runs"]>600,["Player","Team","Runs"]] # single condition

players_above_600 = df.loc[(df["Runs"]>=650) & (df["Runs"]<=800),["Player","Team","Runs"]] # multiple conditions (logical and(&))

# players_above_600 = df.loc[(df["Runs"]>=650) | (df["Runs"]<=800),["Player","Team","Runs"]] # multiple conditions (logical or(|))

# players_above_600 = df.loc[~(df["Runs"]>=650),["Player","Team","Runs"]] # multiple conditions (logical or(|))
print(players_above_600)

# players_above_600=df.loc[df["Runs"]>600,["player","team","runs"]]
players_above=df.loc[(df["Runs"]>=500) & (df["Runs"]<=800), ["Player","Runs","Team"]]
print(players_above)
print("======================================")

#* .between(start,end)

sixes_df = df[df["Sixes"].between(24,26)]

# print(sixes_df)  


# .isin([value,value])

result = df[df["Player"].isin(["Fakhar Zaman","Travis Head"])]
# print(result)

#* .query("condition")

# df2 = df[(df["Runs"]>=650) & (df["Runs"]<=800)]
# OR
df2 = df.query("Runs >= 500 and Runs<=600")
# print(df2)


# print(df.columns)

#* Adding New column in DataFrame 
"""
df["ColumnName"] = condition
"""
import numpy as np

# print(np.array(df["Runs"]))
runs = np.array(df["Runs"]) # <class 'numpy.ndarray'>
balls = np.array(df["Balls"]) # <class 'numpy.ndarray'>

df["Strike_Rate"] =  np.divide(runs,balls)*100


mx = df["Strike_Rate"].max()

# print(df.loc[df["Strike_Rate"]==mx , ["Player","Team","Matches",  "Runs" , "Balls","Strike_Rate"]])
print(df.head())

#* get unique team names from df ===> np.unique(df["columnName"]) ===> list of all teams
# print(np.unique(df["Team"]))
# print(df[df["Team"] =="India"])


sm = df.groupby("Team")["Runs"].sum()
# print(sm.head)


# df.iloc[rowNow,columnNumber] => indexed based
# df.loc[rowNow,[columnName]] => label based