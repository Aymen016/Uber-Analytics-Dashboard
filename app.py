import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------- LOAD DATA -----------------
@st.cache_data
def load_data():
    df = pd.read_csv("ncr_ride_bookings.csv", parse_dates=["Date"])
    df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
    return df

df = load_data()

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Uber Ride Analytics 2024",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- TITLE -----------------
st.title("🚗 Uber Ride Analytics Dashboard (2024)")
st.markdown("Gain insights into **rides, cancellations, revenue, and customer behavior** with interactive filters below.")

# ----------------- SIDEBAR FILTERS -----------------
st.sidebar.header("🔎 Filters")
vehicle = st.sidebar.multiselect(
    "Select Vehicle Type", 
    df['Vehicle Type'].unique(), 
    default=df['Vehicle Type'].unique()
)
payment = st.sidebar.multiselect(
    "Select Payment Method", 
    df['Payment Method'].unique(), 
    default=df['Payment Method'].unique()
)

filtered_df = df[(df['Vehicle Type'].isin(vehicle)) & (df['Payment Method'].isin(payment))]

# ----------------- KPIs -----------------
st.markdown("### 📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Bookings", f"{len(filtered_df):,}")
with col2:
    st.metric("Completed Rides", f"{(filtered_df['Booking Status']=='Completed').sum():,}")
with col3:
    st.metric("Total Revenue", f"${filtered_df.loc[filtered_df['Booking Status']=='Completed','Booking Value'].sum():,.2f}")

# ----------------- BOOKING STATUS DISTRIBUTION -----------------
st.markdown("---")
st.markdown("### 📊 Booking Status Distribution")
status_fig = px.pie(
    filtered_df, 
    names="Booking Status", 
    title="Booking Status Share", 
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(status_fig, use_container_width=True)

# ----------------- REVENUE BY VEHICLE -----------------
st.markdown("### 💰 Revenue by Vehicle Type")
rev_by_veh = filtered_df[filtered_df['Booking Status']=="Completed"].groupby("Vehicle Type")["Booking Value"].sum().reset_index()
rev_fig = px.bar(
    rev_by_veh, 
    x="Vehicle Type", 
    y="Booking Value", 
    color="Vehicle Type", 
    text_auto=True,
    title="Revenue Contribution by Vehicle Type"
)
st.plotly_chart(rev_fig, use_container_width=True)


# ----------------- CORRELATION HEATMAP -----------------
st.markdown("### 🔥 Correlation Heatmap (Numeric Variables)")
num_cols = ['Booking Value','Ride Distance','Driver Ratings','Customer Rating','Avg VTAT','Avg CTAT']
num_cols = [c for c in num_cols if c in filtered_df.columns]
corr = filtered_df[num_cols].corr()

fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax, linewidths=0.5)
st.pyplot(fig)

# ----------------- ANALYTICS OVERVIEW -----------------
st.markdown("---")
st.markdown("## 📈 Analytics Overview")
st.markdown("Explore deeper insights into ride patterns, cancellations, demand by time, and customer satisfaction.")

# 1️⃣ Rides by Hour (Demand Trend)
st.markdown("### ⏰ Rides by Hour of Day")
rides_by_hour = filtered_df.groupby("Hour").size().reset_index(name="Rides")
hour_fig = px.line(
    rides_by_hour, 
    x="Hour", y="Rides", 
    markers=True, 
    title="Hourly Ride Demand",
    color_discrete_sequence=["#636EFA"]
)
st.plotly_chart(hour_fig, use_container_width=True)

# 2️⃣ Cancellations by Vehicle Type
st.markdown("### ❌ Cancellations by Vehicle Type")
cancel_by_veh = filtered_df[filtered_df['Booking Status'].str.contains("Cancelled", na=False)].groupby("Vehicle Type").size().reset_index(name="Cancellations")
cancel_fig = px.bar(
    cancel_by_veh, 
    x="Vehicle Type", y="Cancellations", 
    color="Vehicle Type", 
    text_auto=True,
    title="Cancellations Breakdown"
)
st.plotly_chart(cancel_fig, use_container_width=True)

# 3️⃣ Average Ratings (Driver vs Customer)
st.markdown("### ⭐ Ratings Comparison")
if "Driver Ratings" in filtered_df.columns and "Customer Rating" in filtered_df.columns:
    ratings_df = pd.DataFrame({
        "Metric": ["Driver Ratings", "Customer Rating"],
        "Average": [filtered_df["Driver Ratings"].mean(), filtered_df["Customer Rating"].mean()]
    })
    ratings_fig = px.bar(
        ratings_df, 
        x="Metric", y="Average", 
        color="Metric", 
        text_auto=True,
        title="Average Ratings Overview",
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    st.plotly_chart(ratings_fig, use_container_width=True)

# 4️⃣ Revenue Trends Over Time
st.markdown("### 📅 Revenue Trends Over Time")
if "Date" in filtered_df.columns:
    revenue_trend = filtered_df[filtered_df['Booking Status']=="Completed"].groupby("Date")["Booking Value"].sum().reset_index()
    rev_trend_fig = px.area(
        revenue_trend, 
        x="Date", y="Booking Value", 
        title="Daily Revenue Trend",
        color_discrete_sequence=["#2CA02C"]
    )
    st.plotly_chart(rev_trend_fig, use_container_width=True)
