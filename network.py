# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:05:33 2019

@author: bastama
"""

import networkx as nx
from dataCleaning import related_tables
import pandas as pd 
import matplotlib.pyplot as plt
from SQLconnection import db

print(related_tables.head(5))

def get_dependencies(**kwargs):

    
    if related_tables.empty:
        raise Exception("No related tables in this database")
    

    else:
        v1 = []
        interaction = []
        for i in range(len(related_tables)):
            
            variable = related_tables.iloc[i,6]
            if variable not in v1:
                v1.append(variable)
                temp = i
                temp_array = []
                while(related_tables.iloc[temp,6] == variable ):
                    temp_array.append(related_tables.iloc[temp,4])
                    temp = temp+1
                    if temp >= len(related_tables):
                        break
                    print(related_tables.iloc[temp,6])

                interaction.append(temp_array)
            else:
                continue
    
    return pd.DataFrame({"parent":v1, "dependencies":interaction})

test = get_dependencies()
print("test : ","\n",test.head(5))





#print([g.degree(name) for name in parents])


def map_database():
    
    parents = list(related_tables.name.unique())
    interaction = list(related_tables.name_y.unique())
    
    plt.figure(figsize=(11,11))
    g = nx.from_pandas_edgelist(related_tables,source = "name", target = "name_y")
    
    layout = nx.spring_layout(g,k = 1,iterations=100)
    parent_size = [g.degree(parent)*100 for parent in parents]
    nx.draw_networkx_nodes(g, layout, nodelist = parents, node_size=parent_size, node_color ="lightblue")
    
    nx.draw_networkx_nodes(g,layout,nodelist=interaction, node_color = "#cccccc", node_size=150)
    
    nx.draw_networkx_edges(g,layout,width=1,edge_color="#cccccc")
    
    node_labels = dict(zip(parents,parents))
    more_labels = dict(zip(interaction,interaction))
    nx.draw_networkx_labels(g,layout, labels=node_labels)
    nx.draw_networkx_labels(g,layout, labels=more_labels)
    
    plt.axis("off")
    plt.title(db+" database mapping")
    plt.legend(scatterpoints = 1)
    plt.show()

                       
                                              
                       
if __name__ =="__main__":
    
    map_database()
                       
                       
                       
                       
                       
                       
                       





