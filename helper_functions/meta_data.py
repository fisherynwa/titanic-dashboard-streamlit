import pandas as pd
import seaborn as sns


def load_data():
    return sns.load_dataset("titanic")

def meta_data():
    data = {
        "Variable": [
            "survived", 
            "pclass",
            "sibsp",
            "parch",
            "fare",
            "embarked"
        ],
        "Definition": [
            "Survival", 
            "Ticket class", 
            "# of siblings / spouses aboard", 
            "# of parents / children aboard",
            "Passenger fare", 
            "Port of Embarkation"
        ],
        "Key": [
            "0 = No, 1 = Yes", 
            "1 = 1st, 2 = 2nd, 3 = 3rd",
            "", 
            "", 
            "", 
            "C = Cherbourg, Q = Queenstown, S = Southampton"
        ]
    }
    return pd.DataFrame(data)