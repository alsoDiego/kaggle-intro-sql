from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#q1
# Count tables in the dataset
tables = list(client.list_tables(dataset))
cont_tables = 0
for table in tables:
    cont_tables = cont_tables + 1
print(cont_tables)

#q2
# How many columns in the crime table have TIMESTAMP data?
table_ref = dataset_ref.table("crime") # reference to the crime table
table = client.get_table(table_ref)
table.schema

