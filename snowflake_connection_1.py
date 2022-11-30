# Python to Snowflake DB connection using Snowflake Connector with external browser authentication

import snowflake.connector
import pandas as pd 
import numpy as numpy
ctx = snowflake.connector.connect(
    account = '<account name>', #vc21971.us-central1.gcp
    user = '<username>',
    warehouse = '<warehouse name>',
    role = '<As specified by Snowflake Admin>',
    authentication='externalbrowser',
)
cur = ctx.cursor
