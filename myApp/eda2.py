import streamlit as st
import pandas as pd
import altair as alt


def eda_dashboard():

    #st.set_page_config(page_title="Bank Customer EDA", layout="wide")
    st.title("📊 Exploratory Data Analysis")

    # Load Parquet data
    df = pd.read_parquet("data/bank_raw.parquet")

    # Sidebar filters
    st.sidebar.header("Filter Options")

    # Job filter
    job_filter = st.sidebar.multiselect("Select Job", df['job'].unique(), default=df['job'].unique())

    # Housing loan filter
    housing_filter = st.sidebar.selectbox("Select Housing Loan Status", options=["All", "Yes", "No"])

    # Apply filters
    df_filtered = df[df['job'].isin(job_filter)]
    if housing_filter == "Yes":
        df_filtered = df_filtered[df_filtered['housing'] == True]
    elif housing_filter == "No":
        df_filtered = df_filtered[df_filtered['housing'] == False]

    # Age Distribution
    st.subheader("Age Distribution")
    age_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('age', bin=True),
        y='count()'
    )
    st.altair_chart(age_chart, use_container_width=True)
    st.markdown("**Insights:** Analysis start with range of age that have actives connection with Bank. Go for older but not too old!")


    # Balance by Job
    st.subheader("Average Balance by Job")
    balance_chart = alt.Chart(df_filtered).mark_bar().encode(
        x='job',
        y='average(balance)',
        tooltip=['job', 'average(balance)']
    ).interactive()
    st.altair_chart(balance_chart, use_container_width=True)
    st.markdown("**Insights:** [Career] Type of Job vs Average of balance. Jobs contribute and affect value differently")

    # Balance by Marital Status
    st.subheader("Average Balance by Marital Status")
    marital_chart = alt.Chart(df_filtered).mark_bar().encode(
        x='marital',
        y='average(balance)',
        color='marital',
        tooltip=['marital', 'average(balance)']
    ).interactive()
    st.altair_chart(marital_chart, use_container_width=True)
    st.markdown("**Insights:** Marital status do affect average of balance. Approach them!")


    # Balance by Education
    st.subheader("Average Balance by Education Level")
    education_chart = alt.Chart(df_filtered).mark_bar().encode(
        x='education',
        y='average(balance)',
        color='education',
        tooltip=['education', 'average(balance)']
    ).interactive()
    st.altair_chart(education_chart, use_container_width=True)
    st.markdown("**Insights:** Higher level of education will contributes more to Banks!")


    # Balance by Housing Loan Status
    # st.subheader("Average Balance by Housing Loan Status")
    # housing_chart = alt.Chart(df_filtered).mark_bar().encode(
    #     x='housing',
    #     y='average(balance)',
    #     color='housing',
    #     tooltip=['housing', 'average(balance)']
    # ).interactive()
    # st.altair_chart(housing_chart, use_container_width=True)

    # Count of Customers with/without Housing Loans
    st.subheader("Count of Customers with/without Housing Loans")
    housing_count_chart = alt.Chart(df_filtered).mark_bar().encode(
        x='housing',
        y='count()',
        color='housing',
        tooltip=['housing', 'count()']
    )
    st.altair_chart(housing_count_chart, use_container_width=True)
    st.markdown("**Insights:** No significant different between numbers of client with housing loan and without loan")


    # Age Distribution of Customers with Housing Loans
    st.subheader("Age Distribution of Customers with Housing Loans")
    # housing_yes_df = df_filtered[df_filtered['housing'] == True]
    housing_age_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('age', bin=True),
        y='count()',
        tooltip=['age']
    )
    st.altair_chart(housing_age_chart, use_container_width=True)

    # Insights and Assumptions
    st.markdown("**Assumption:** Customers with more stable jobs, education, marital status show higher balances on average.")
    #st.markdown("**Insight:** This helps determine if customers with housing loans tend to maintain higher or lower balances.")
