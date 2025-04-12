import streamlit as st
import duckdb
import pandas as pd


def show_query():

    st.title("🧮 SQL Query Interface")

    # Load DuckDB with Parquet
    con = duckdb.connect()

    # Use SQL Editor
    query = st.text_area("Write your SQL Query", 
                        value="SELECT * FROM read_parquet('data/bank_raw.parquet') LIMIT 10")

    if st.button("Run Query"):
        try:
            result_df = con.execute(query).fetchdf()
            st.success("Query executed successfully!")
            st.dataframe(result_df)

            # Export button
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download as CSV", data=csv, file_name="query_result.csv", mime="text/csv")

        except Exception as e:
            st.error(f"Error: {e}")
