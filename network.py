# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:05:33 2019

@author: bastama
"""

import networkx as nx
from dataCleaning import related_tables
import pandas as pd 

print(related_tables.head(5))

def interaction_db():
    
    if related_tables.empty:
        raise Exception("No related tables in this database")
    else:
        v1 = []
        interaction = [[]]
        y = 0
        for i in range(len(related_tables)):
            
            variable = related_tables.iloc[i,6]
            if variable not in v1:
                v1.append(variable)
                temp = i
                while(variable == related_tables.iloc[temp,6]):
                    print("interactions:", "\n", interaction[y])
                    print(temp)
                    interaction[y].append(related_tables.iloc[temp,4])
                    temp = temp+1
                y= y+1
            else:
                continue
    return pd.DataFrame({"user":v1, "interactions":interaction})

test = interaction_db()
print(test.head(5))
            
my_graph = nx.Graph()

my_graph.add_edges_from([(1,2),(1,3),(3,4),(1,5),(3,5),(4,2),(2,3),(3,0)])

nx.draw(my_graph, with_labels= True, front_weight = "bold")
