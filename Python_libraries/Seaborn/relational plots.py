import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from itertools import combinations

numbers = [1, 2, 3, 4]

result = list(combinations(numbers, 2))

# print(result)

# car_crashes

# print("Shape of dataset : ",df.shape) # (51[rows], 8[columns])
print()
# print(df.head())
# total  speeding  alcohol  not_distracted  no_previous  ins_premium  ins_losses abbrev

# sns.lineplot(
#     data=df,
#     x=df["total"],
#     y=df["speeding"],
#     hue=df["total"],
#     palette="bright"
# )

# plt.show()
#* ================================ car crashes dataframe =================================
def car_crashes():
    columns = list(df.columns)

    df = sns.load_dataset("car_crashes")
    comb = list(combinations(columns,2))
    print(f"Total Number of combinations : {len(comb)}\n")
    print("++++++*******&&&&^^^%%%%%%%%%%%%%%%")
    print(comb)

    for i in comb:

        if(i[0].startswith("total") or i[0]=="speeding"):

            plt.figure(figsize=(10,7))
            plt.title(f"{i[0]} vs {i[1]}")
            sns.lineplot(
                data = df,
                x = i[0],
                y = i[1],
                palette="bright",
                linestyle ="--",
                markers="s"
            )

            plt.show()

# total = columns[0]

# for i in range(1,len(columns)):
#     # print(columns[i])
#     sns.lineplot(
#         data=df,
#         x = total ,
#         y = columns[i],
#         palette="bright",
#     )
#     plt.show()

# print(columns)
# sns.lineplot(
#     data=df,
#     x="total",
#     y="alcohol",
#     palette="bright",
# )
# plt.show()

# sns.lineplot(
#     data=df,
#     x="total",
#     y="not_distracted",
#     palette="bright",
# )
# plt.show()


# sns.lineplot(
#     data=df,
#     x="total",
#     y="no_previous",
#     palette="bright",
# )
# plt.show()

# sns.lineplot(
#     data=df,
#     x="total",
#     y="ins_premium",
#     palette="bright",
# )
# plt.xlabel()
# plt.ylabel()
# plt.title()


"""
String columns in tips :  ['sex', 'smoker', 'day', 'time']
Numeric columns in tips :  ['total_bill', 'tip', 'size']

"""

def tips_linePlots():
    df = sns.load_dataset("tips")
    print(df.head())
    num_columns = ['total_bill', 'tip', 'size']

    num_columns_combinations = list(combinations(num_columns,2))
    # print(num_columns_combinations)
    for column in num_columns_combinations:
        plt.figure(figsize=(10,9))
        plt.title(f"{column[0]} vs {column[1]}")
        sns.lineplot(
            data = df,
            x = column[0],
            y = column[1],
            palette="dark",
            linestyle="-"
        )
        plt.show()

# tips_linePlots()
"""
* ******* Common line styles *******
-------------------------------------
Style	    Code	    Appearance
Solid	    "-"	        ─────────
Dashed	    "--"	    - - - - - -
Dotted	    ":"	        ·········
Dash-dot	"-."	    ─ · ─ · ─
"""

total_bill = [300,500,100,600,200]
customers_size = [2,3,1,2,6]

df = pd.DataFrame({"total":total_bill,"size":customers_size})
print(df)
sns.scatterplot(
    data=df,
    x = "size",
    y = "total",
    hue="total",
    palette="dark",
    s=200

)
plt.grid()
plt.show()