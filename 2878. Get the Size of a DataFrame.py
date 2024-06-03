import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = len(players.axes[0])
    cols = len(players.axes[1])
    return [rows,cols]

#Importing libraries
# defining function name getDataFrames
# players takes the argument of dataframe
# List[int]: - return type
# axes[0],axes[1] - acessing 1st row and 2nd axis ie. columns
#len(players.axes[0]),cols = len(players.axes[1]) - calculating no of rows and columns
# return total number of rows and columns
