"""
@author: Mohammad Kazemi Beydokhti
"""

import pandas as pd

EquivalentTools = pd.read_csv('Equivalent Tools.csv').values.tolist()
APEGeneratedSolutions = pd.read_csv('GeneratedSolutions.csv').values.tolist()

# EquivalentTools = []
# for i in EquivalentToolscsv:
#     EquivalentTools.append([x for x in i if x])
    
#EquivalentTools.remove(EquivalentTools[0])

def equivalentTools (tool):
    result = [x for x in EquivalentTools if tool in x]
    result2 = [item for sublist in result for item in sublist]
    
    return list(dict.fromkeys(result2))


def GroupTool(GeneratedSolutions):

    FinalGrouping = []
    for i in GeneratedSolutions:
        groupsIndex = []
        for j in GeneratedSolutions:
            
            if ( (i != j ) & ( [item for item in FinalGrouping if tuple(j) in item]== [] ) & (equivalentTools(i[0]) == equivalentTools(j[0])) & (equivalentTools(i[1]) == equivalentTools(j[1])) & (equivalentTools(i[2]) == equivalentTools(j[2]))) :
                groupsIndex.append(tuple(j))
            
        if (groupsIndex != []):        
            FinalGrouping.append([tuple(i)]+groupsIndex)
                    
        if ( [item for item in FinalGrouping if tuple(i) in item]== [] ):
            FinalGrouping.append(tuple(i))
        
    
    return FinalGrouping
        
        
        
GroupedSolutions = GroupTool(APEGeneratedSolutions)

 
