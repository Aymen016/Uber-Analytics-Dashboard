import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("ncr_ride_bookings.csv", parse_dates=["Date"])
    df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
    return df

df = load_data()

# Title
st.title("🚗 Uber Ride Analytics 2024")

# Sidebar Filters
vehicle = st.sidebar.multiselect("Select Vehicle Type", df['Vehicle Type'].unique(), default=df['Vehicle Type'].unique())
payment = st.sidebar.multiselect("Select Payment Method", df['Payment Method'].unique(), default=df['Payment Method'].unique())

filtered_df = df[(df['Vehicle Type'].isin(vehicle)) & (df['Payment Method'].isin(payment))]

# KPIs
st.metric("Total Bookings", len(filtered_df))
st.metric("Completed Rides", (filtered_df['Booking Status']=="Completed").sum())
st.metric("Total Revenue", filtered_df.loc[filtered_df['Booking Status']=="Completed","Booking Value"].sum())

# Charts
st.subheader("Booking Status Distribution")
st.bar_chart(filtered_df['Booking Status'].value_counts())

st.subheader("Revenue by Vehicle Type")
rev_by_veh = filtered_df[filtered_df['Booking Status']=="Completed"].groupby("Vehicle Type")["Booking Value"].sum()
st.bar_chart(rev_by_veh)


# Correlation Heatmap
st.subheader("Correlation Heatmap")
num_cols = ['Booking Value','Ride Distance','Driver Ratings','Customer Rating','Avg VTAT','Avg CTAT']
num_cols = [c for c in num_cols if c in filtered_df.columns]
corr = filtered_df[num_cols].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
