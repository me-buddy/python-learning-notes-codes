"""
======================================= seaborn =====================================

=> line plot
=> bar plot
=> scatter plot
=> histogram
=> pie chart
=> box chart
=> violin plot
=> area plot
...

NOTE :- It Provides built-in Datasets for analysis and visualization.

sns.get_dataset_name() => return the list of all available datasets.
sns.load_dataset(datasetName) => return the given dataset


DataSet => name
shape => shape
columns => name1 , name2 , name3 ...
-------------------------------------
DataSet => name
shape => shape
columns => name1 , name2 , name3 ...
"""

import seaborn as sns
import pandas 
import numpy
datasets = sns.get_dataset_names()
# print(datasets)
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 
# 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 
# 'taxis', 'tips', 'titanic']



#* to get some information on each dataFrames :-
# ------------------------------------------------
def description():
    for i in datasets:
    
        dfs=sns.load_dataset(i)

        print(f"""
        dataset name : {i}
        Shape: {dfs.shape}
        Total number of rows:{dfs.shape[0]}
        Total number of columns:{dfs.shape[1]}
        COLUMNS NAMES :- """)
        # columns name :{dfs.columns}
        
        for columns in dfs.columns:
            print("\t",columns,end="\t")
        print()

        print(f"""\t{dfs.isnull().sum()}""")
        print("\n\n============================================\n\n")

# description()
#* to extract numeric and string columns from dataframes :-
def numeric_or_string():
    for data in sns.get_dataset_names():
        st = []
        num = []

        df = sns.load_dataset(data)

        for i in df:
            if isinstance(df[i].dtype, pandas.CategoricalDtype):
                st.append(i)

            if isinstance(df[i].dtype, numpy.dtypes.Float64DType) or isinstance(df[i].dtype, numpy.dtypes.Int64DType):
                num.append(i)

        print(f"String columns in {data} : ", st)
        print(f"Numeric columns in {data} : ", num)
        print("\n=====================================================================================================\n")
# numeric_or_string()



# print(df.shape)
# print("Total number of rows:",df.shape[0])
# print("Total number of columns:",df.shape[1])
# print(" Total numbers of datasets available:")
# print(len(datasets))

# ===================================================================================
# import seaborn as sns
# import pandas
# import numpy

# df = sns.load_dataset("tips")
# st=[]
# for i in df:
#     print(i, type(df[i].dtype))
    
#     if isinstance(df[i].dtype, pandas.CategoricalDtype):
#         st.append(i)
# print(st)

# isinstance(df[i],numpy.dtypes.Float64DType) # floating columns
# isinstance(df[i],numpy.dtypes.Int64DType) # integer columns

# ===================================================================================
"""
&Seaborn Chart Categories
Seaborn is a Python data-visualization library built on top of Matplotlib. Its charts can be grouped into the following categories:

*1. Relational Plots
Used to show relationships between variables.
.................................................
^Scatter Plot — sns.scatterplot() ==> To show relation between two numerical columns.
.................................................
^Line Plot — sns.lineplot()  ====> Used to represent time-series analysis

*2. Distribution Plots
Used to understand the distribution and spread of data.
.................................................
^Histogram — sns.histplot()
.................................................
^KDE Plot — sns.kdeplot()
.................................................
^ECDF Plot — sns.ecdfplot()
.................................................
^Rug Plot — sns.rugplot()
.................................................
^Box Plot — sns.boxplot()
.................................................
^Violin Plot — sns.violinplot()

*3. Categorical Plots
Used to compare values across categories.
.................................................
^Bar Plot — sns.barplot()
.................................................
^Count Plot — sns.countplot()
.................................................
^Box Plot — sns.boxplot()
.................................................
^Violin Plot — sns.violinplot()
.................................................
^Strip Plot — sns.stripplot()
.................................................
^Swarm Plot — sns.swarmplot()
.................................................
^Point Plot — sns.pointplot()

*4. Matrix Plots
Used to represent data in a matrix or grid format.
.................................................
^Heatmap — sns.heatmap()
.................................................
^Cluster Map — sns.clustermap()

*5. Regression Plots
Used to show relationships and regression trends.
.................................................
^Regression Plot — sns.regplot()
.................................................
^Linear Model Plot — sns.lmplot()
.................................................
^Residual Plot — sns.residplot()

*6. Multi-Plot / Figure-Level Plots
Used to create multiple plots or complex visualizations.
.................................................
^Pair Plot — sns.pairplot()
.................................................
^Joint Plot — sns.jointplot()
.................................................
^Facet Grid — sns.FacetGrid()
.................................................
^Pair Grid — sns.PairGrid()
.................................................
^Joint Grid — sns.JointGrid()

"""

"""
* ================================= All built-in Datasets in seaborn =====================================

String columns in anagrams :  []
Numeric columns in anagrams :  ['subidr', 'num1', 'num2', 'num3']

=====================================================================================================

String columns in anscombe :  []
Numeric columns in anscombe :  ['x', 'y']

=====================================================================================================

String columns in attention :  []
Numeric columns in attention :  ['Unnamed: 0', 'subject', 'solutions', 'score']

=====================================================================================================

String columns in brain_networks :  []
Numeric columns in brain_networks :  []

=====================================================================================================

String columns in car_crashes :  []
Numeric columns in car_crashes :  ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses']

=====================================================================================================

String columns in diamonds :  ['cut', 'color', 'clarity']
Numeric columns in diamonds :  ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']

=====================================================================================================

String columns in dots :  []
Numeric columns in dots :  ['time', 'coherence', 'firing_rate']

=====================================================================================================

String columns in dowjones :  []
Numeric columns in dowjones :  ['Price']

=====================================================================================================

String columns in exercise :  ['diet', 'time', 'kind']
Numeric columns in exercise :  ['Unnamed: 0', 'id', 'pulse']

=====================================================================================================

String columns in flights :  ['month']
Numeric columns in flights :  ['year', 'passengers']

=====================================================================================================

String columns in fmri :  []
Numeric columns in fmri :  ['timepoint', 'signal']

=====================================================================================================

String columns in geyser :  []
Numeric columns in geyser :  ['duration', 'waiting']

=====================================================================================================

String columns in glue :  []
Numeric columns in glue :  ['Year', 'Score']

=====================================================================================================

String columns in healthexp :  []
Numeric columns in healthexp :  ['Year', 'Spending_USD', 'Life_Expectancy']

=====================================================================================================

String columns in iris :  []
Numeric columns in iris :  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

=====================================================================================================

String columns in mpg :  []
Numeric columns in mpg :  ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']

=====================================================================================================

String columns in penguins :  []
Numeric columns in penguins :  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

=====================================================================================================

String columns in planets :  []
Numeric columns in planets :  ['number', 'orbital_period', 'mass', 'distance', 'year']

=====================================================================================================

String columns in seaice :  []
Numeric columns in seaice :  ['Extent']

=====================================================================================================

String columns in taxis :  []
Numeric columns in taxis :  ['passengers', 'distance', 'fare', 'tip', 'tolls', 'total']

=====================================================================================================

String columns in tips :  ['sex', 'smoker', 'day', 'time']
Numeric columns in tips :  ['total_bill', 'tip', 'size']

=====================================================================================================

String columns in titanic :  ['class', 'deck']
Numeric columns in titanic :  ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']

=====================================================================================================
"""