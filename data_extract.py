import json
from pprint import pprint 
with open('data/lag6_10.json') as lg1:
    jdata = json.load(lg1)
print("Type of json data after load", type(jdata))    
print("Type of elem in json data after load", type(jdata[0])) 
pprint(jdata[0])



# Getting the list of distinct items
items = [elem['Item'] for elem in jdata]
items_ = sorted(list(set(items)))
#print("Items: ",items_)
print("No. of items:", len(items_))

# Getting the list of distinct DCs
dc = [d['DC'] for d in jdata]
dc_ = sorted(list(set(dc)))
#print("Items: ", dc_)
#print("No. of items:", len(dc_))


period = {
    "SEP-21": "9-2021",
    "OCT-21": "10-2021",
    "NOV-21": "11-2021",
    "DEC-21": "12-2021",
    "JAN-22": "1-2022",
    "FEB-22": "2-2022",
    "MAR-22": "3-2022",
    "APR-22": "4-2022",
    "MAY-22": "5-2022",
    "JUN-22": "6-2022",
    "JUL-22": "7-2022",
    "AUG-22": "8-2022",
    "SEP-22": "9-2022",
    "OCT-22": "10-2022",
    "NOV-22": "11-2022",
    "DEC-22": "12-2022",
}

tb_headers = ["Period", "Actuals", "Lag1", "Lag3", "Lag6"]

print("Values of Period", period.values())
#print(period.keys())

#data_for_2022_11 = [elem for elem in jdata if elem["Fiscal_year"]=="2022" and elem["Fiscal_month"]=='11']
# Lag1
data_all_item_2021_9 = [elem for elem in jdata if (elem['Fiscal_month']=='9' and elem['Fiscal_year']=='2021')]
data_all_item_2021_10 = [elem for elem in jdata if (elem['Fiscal_month']=='10' and elem['Fiscal_year']=='2021')]
data_all_item_2021_11 = [elem for elem in jdata if (elem['Fiscal_month']=='11' and elem['Fiscal_year']=='2021')]
data_all_item_2021_12 = [elem for elem in jdata if (elem['Fiscal_month']=='12' and elem['Fiscal_year']=='2021')]

data_all_item_2022_1 = [elem for elem in jdata if (elem['Fiscal_month']=='1' and elem['Fiscal_year']=='2022')]
data_all_item_2022_2 = [elem for elem in jdata if (elem['Fiscal_month']=='2' and elem['Fiscal_year']=='2022')]
data_all_item_2022_3 = [elem for elem in jdata if (elem['Fiscal_month']=='3' and elem['Fiscal_year']=='2022')]
data_all_item_2022_4 = [elem for elem in jdata if (elem['Fiscal_month']=='4' and elem['Fiscal_year']=='2022')]
data_all_item_2022_5 = [elem for elem in jdata if (elem['Fiscal_month']=='5' and elem['Fiscal_year']=='2022')]
data_all_item_2022_6 = [elem for elem in jdata if (elem['Fiscal_month']=='6' and elem['Fiscal_year']=='2022')]
data_all_item_2022_7 = [elem for elem in jdata if (elem['Fiscal_month']=='7' and elem['Fiscal_year']=='2022')]
data_all_item_2022_8 = [elem for elem in jdata if (elem['Fiscal_month']=='8' and elem['Fiscal_year']=='2022')]
data_all_item_2022_9 = [elem for elem in jdata if (elem['Fiscal_month']=='9' and elem['Fiscal_year']=='2022')]
data_all_item_2022_10 = [elem for elem in jdata if (elem['Fiscal_month']=='10' and elem['Fiscal_year']=='2022')]
data_all_item_2022_11 = [elem for elem in jdata if (elem['Fiscal_month']=='11' and elem['Fiscal_year']=='2022')]
data_all_item_2022_12 = [elem for elem in jdata if (elem['Fiscal_month']=='12' and elem['Fiscal_year']=='2022')]


print(len(data_all_item_2021_9))
print(len(data_all_item_2021_10))
print(len(data_all_item_2021_11))
print(len(data_all_item_2021_12))

print(len(data_all_item_2022_1))
print(len(data_all_item_2022_2))
print(len(data_all_item_2022_3))
print(len(data_all_item_2022_4))
print(len(data_all_item_2022_5))
print(len(data_all_item_2022_6))
print(len(data_all_item_2022_7))
print(len(data_all_item_2022_8))
print(len(data_all_item_2022_9))
print(len(data_all_item_2022_10))
print(len(data_all_item_2022_11))
print(len(data_all_item_2022_12))

for elem in list(period.values()):
    print(elem[-4:])