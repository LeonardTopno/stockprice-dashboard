from google.cloud import bigquery
from google.oauth2 import service_account # pip3 install google-auth
import json

#credentials = service_account.Credentials.from_service_account_file('assets/leo-project-name-198aed8804a0.json')

credentials = service_account.Credentials.from_service_account_file('assets/atd-inc-bigquery-coeuser.json')
#project_id = 'leo-project-name'
project_id = 'atd-dlk-prd'

client = bigquery.Client(credentials=credentials, project=project_id) # initiating an instance

#QUERY = """ SELECT * FROM leo_dataset_id.leo_table LIMIT 4 """
#QUERY = """ SELECT * FROM atd_dlk_planninganalytics_data.SO99_Snapshot_Lag3_1 LIMIT 4 """

QUERY = """ SELECT * FROM analytics_261099212.events_20221124 LIMIT 4 """

# atd-dlk-prd.atd_dlk_planninganalytics_data.SO99_Snapshot_Lag3_1
# atd-dlk-prd.analytics_261099212.events_20221124

query_job = client.query(QUERY)  # API request

result = query_job.result()  # Waits for query to finish
# results = query_job.result()


#print(list(rows))
print(type(result)) # RowIterator
print("Total rows available: ", result.total_rows) # RowIterator has an attribute called total_rows
print("Total rows available: ", result.num_results)
for row in result:
    print("Total rows avaialabel", row.items)

jsonrecord = [dict(row) for row in query_job]
json_obj = json.dumps(str(jsonrecord))

print("\n\n", json_obj)
"""
for row in rows:
    #print(row.items)
    #print("------")
    print(row.items)
"""