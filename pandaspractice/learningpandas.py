import pandas as pd

data = {
    "Name" : ["Andy", "John", "Jane"],
    "Age" : [30, 35, 50],
}

df = pd.DataFrame(data, index=["E1", "E2", "E3"])

# Adding a new column
df["Job"] = ["Manager", "Clerk", "Cook"]

# Adding a new row: Needs a dictionary for each
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Tester"}], index=["E4"])
df = pd.concat([df, new_row])

###########################

df = pd.read_csv("tcg1.csv", index_col="Name")

# Selecting all between charizard and blastoise, height and weight
print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

tall_pokemon = df[df["Height"] >= 2]

heavy_pokemon = df[df["Weight"] > 100]