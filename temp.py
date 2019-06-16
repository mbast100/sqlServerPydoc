import pandas as pd
from SQLconnection import df, tables_Id, table_attributes, table_constraint_keys,db
import re
import numpy as np

"""

1- retrive table name, strip it 
2- append its attributes
3- retrive next table name, strip it check if table already in df.columns
4- if not repeat steps 2


Note: probably gonna need to use concat for different lengths of arrays formed by the different 
attributes of the tables



print("table name and DB: ", "\n",df.head(5))
print("tables ID: ","\n", tables_Id.head(5))
print("tables attributes: ","\n", table_attributes.head(5))
"""

def get_tables_data(objective):
    
    """
    returns all different tables in a databse with their attributes
    
    """
    if objective is None:
        raise Exception("search parameter needed")
        
    new_df = pd.DataFrame()
    
    if objective == "dbInfo":
        
        print(table_attributes.head(5))
        for i in range(len(table_attributes)):
            variable = table_attributes.iloc[i,2]
            modified_var = re.split("(\d+)",variable)
            modified_var = modified_var[0]
            
            if modified_var not in new_df.columns:
                a = []
                b = []
                c = []
                d = []
                temp_df = pd.DataFrame()
                temp = i
                while(table_attributes.iloc[temp,2]==variable):
                    a.append(table_attributes.iloc[temp,3])
                    b.append(table_attributes.iloc[temp,5])
                    c.append(table_attributes.iloc[temp,4])
                    d.append(" ")
                    temp = temp+1
                temp_df[modified_var] = a
                temp_df[modified_var+"_Data_Type"] = b
                temp_df[modified_var+"_Nullable"] = c
                temp_df[modified_var+"_Description"] = d
                new_df = pd.concat([new_df,temp_df], axis =1)
                    
            else:
                
                continue
    
    elif objective == "dbConstraints":
        
        if table_constraint_keys.empty:
            
            raise Exception("Illegal argument exception: no constraints in database")
        else:
            for i in range(len(table_constraint_keys)):
    
                variable = table_constraint_keys.iloc[i,1]
                modified_var = re.split("(\d+)",variable)
                modified_var = modified_var[0]
                
                if modified_var not in new_df.columns:
                    a = []
                    b = []
                    temp_df = pd.DataFrame()
                    temp = i
                    while(table_constraint_keys.iloc[temp,1]==variable):
                        a.append(table_constraint_keys.iloc[temp,2])
                        b.append(table_constraint_keys.iloc[temp,0])
                        temp = temp+1
                    temp_df[modified_var] = a
                    temp_df[modified_var+"_constraints"] = b
                    new_df = pd.concat([new_df,temp_df], axis =1)
                        
                else:
                    
                    continue

    return new_df.T.rename_axis("Table_Name", axis = 0)

def getKeys(*args,**kwargs):
    
    search = "PK"
    columnName = "Primary Keys"
    
    if table_constraint_keys.empty:
        return "no constraints in database"
    
    if "FK" in args:
        search = "FK"
        columnName = "Foreign Keys"
        
    elif "PK" in args:
        search = "PK"
        columnName = "Primary Keys"
    
    a = []
    b = []
    for i in range(len(table_constraint_keys)):
        
        key = table_constraint_keys.iloc[i,0]
        if key.startswith(search):
            
            a.append(table_constraint_keys.iloc[i,2])
            b.append(table_constraint_keys.iloc[i,1])
    
    return pd.DataFrame({"Parent Table":b,columnName:a})


def unifyData(dataFrame,**kwargs):
    
    if dataFrame.empty:
        raise Exception("DataFrame cannot be empty")
    else:
        new_df = pd.DataFrame()
        a = []
        b = [[]]
        for k,v in kwargs.items():
            if k != "axis":
                unifyOn = 0
        else:
            for k,v in kwargs.items():
                if k =="axis":
                    unifyOn = v
                else:
                    continue
        for i in range(len(dataFrame)):
            variable = dataFrame.iloc[i,unifyOn]
            modified_var = re.split("(\d+)",variable)
            modified_var = modified_var[0]
            if modified_var not in a:
                a.append(modified_var)
                b.append(dataFrame.iloc[i,:])
            else:
                continue
        new_df["unique_"+dataFrame.columns[unifyOn]] = a
        for j in range(len(b[0])):
            
            new_df[j] = b[:,j]
    
    return new_df

print(table_attributes.head(5))
test = unifyData(table_attributes, axis =2)
print(test.head(10))
            
            

    
    
#test = getKeys()
#print(test.head(5))
#test.to_csv(db+"_PrimaryKeys.csv")
#                
#                
#    
#
#tablesTest_dbConstraints = get_tables_data("dbConstraints")
#tablesTest_dbInfo = get_tables_data("dbInfo")
#print(tablesTest_dbConstraints.head(5))
#
## uncomment this to get output
#tablesTest_dbInfo.to_csv(db+"_Tables_attributes.csv") 
#tablesTest_dbConstraints.to_csv(db+"_variables_constraints.csv")

def getDictData():
    
    data = get_tables_data()
    dataMod = data.transpose()
    return dataMod.to_dict()





print("constraints table : ","\n",table_constraint_keys.head(5))


        



        





