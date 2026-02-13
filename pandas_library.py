import pandas as pd

df = pd.read_csv("movies.csv")

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 5 rows ---")
print(df.tail())

print("\n--- Shape of DataFrame ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Data Info ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe(include='all'))

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

print("\n--- Drop rows with missing values ---")
df_dropped = df.dropna()
print(df_dropped.shape)

print("\n--- Fill missing values with 'Unknown' ---")
df_filled = df.fillna("Unknown")

print("\n--- Select Single Column ---")
print(df[df.columns[0]].head())

print("\n--- Select Multiple Columns ---")
print(df[df.columns[:3]].head())

print("\n--- Rename Columns ---")
df_renamed = df.rename(columns={df.columns[0]: "First_Column"})
print(df_renamed.columns)

print("\n--- Filter rows using condition (example) ---")
numeric_cols = df.select_dtypes(include='number').columns

if len(numeric_cols) > 0:
    print(df[df[numeric_cols[0]] > df[numeric_cols[0]].mean()].head())

if len(numeric_cols) > 0:
    print("\n--- Sort values ---")
    print(df.sort_values(by=numeric_cols[0], ascending=False).head())

if len(numeric_cols) > 0:
    print("\n--- GroupBy example ---")
    print(df.groupby(df.columns[0])[numeric_cols[0]].mean().head())

if len(numeric_cols) > 0:
    print("\n--- Apply function ---")
    df["Squared_Value"] = df[numeric_cols[0]].apply(lambda x: x*x if pd.notnull(x) else x)
    print(df[["Squared_Value"]].head())

print("\n--- Value Counts ---")
print(df[df.columns[0]].value_counts().head())

df_dropped_col = df.drop(columns=[df.columns[0]])
print("\n--- After Dropping Column ---")
print(df_dropped_col.head())

