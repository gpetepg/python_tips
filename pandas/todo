"""
df = pd.read_csv("grades.csv")

aggregation = {
    "grades" : {. # Which column to work on
        "highest grade" : "max" # We give a name to the aggregate column and what function we want applied there
    }
}

# Add our where, groupby and aggregation
newdf = df[df["last_name"] == "Guo"].groupby("month").agg(aggregation)

# We ravel() to join the newly named column with the aggregation function for readability
newdf.columns = ["_".join(col) for col in newdf.columns.ravel()]

# We reset it to make it look pretty like Manda
newdf.reset_index()


Find column and row and assign it
t.loc[(t["ID"] == 1938), "BATCHID"] = [1,2,3,4]


# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
"""
