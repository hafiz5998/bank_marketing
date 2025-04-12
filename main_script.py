import duckdb
import pandas as pd

# Load CSV into a DuckDB 
con = duckdb.connect()
con.execute("CREATE TABLE bank_raw AS SELECT * FROM read_csv_auto('bank.csv');")
# Execute the normalization SQL
con.execute("""
CREATE TABLE dim_job AS 
SELECT DISTINCT row_number() OVER () AS job_id, job FROM bank_raw;

CREATE TABLE dim_marital AS 
SELECT DISTINCT row_number() OVER () AS marital_id, marital FROM bank_raw;

CREATE TABLE dim_education AS 
SELECT DISTINCT row_number() OVER () AS education_id, education FROM bank_raw;

CREATE TABLE dim_finance AS 
SELECT DISTINCT row_number() OVER () AS finance_id, "default", housing, loan FROM bank_raw;

CREATE TABLE bank_customer_interactions AS 
SELECT DISTINCT row_number() OVER () AS customer_id,
    b.customer_id,
    b.contact,
    b.age,
    b.balance,
    b.day,
    b.month,
    b.duration,
    b.campaign,
    b.pdays,
    b.previous,
    b.poutcome,
    b.deposit FROM bank_raw b;

CREATE OR REPLACE TABLE bank_customer_interactions AS
SELECT
    b.customer_id,
    b.contact,
    b.age,
    b.balance,
    b.day,
    b.month,
    b.duration,
    b.campaign,
    b.pdays,
    b.previous,
    b.poutcome,
    b.deposit,
    j.job_id,
    m.marital_id,
    e.education_id,
    f.finance_id
FROM bank_customer_interactions b
JOIN dim_job j ON b.customer_id = j.job_id
JOIN dim_marital m ON b.customer_id = m.marital_id
JOIN dim_education e ON b.customer_id = e.education_id
JOIN dim_finance f ON b.customer_id = f.finance_id ;

""")

df = con.execute("SELECT * FROM bank_customer_interactions LIMIT 100").fetchdf()
print(df)

#export to Parquet
con.execute("COPY bank_raw TO 'bank_raw.parquet' (FORMAT PARQUET);")
con.execute("COPY bank_customer_interactions TO 'bank_customer_interactions.parquet' (FORMAT PARQUET);")