# 🚗 Uber Ride Analytics Dashboard (2024)

An interactive **Streamlit dashboard** for analyzing Uber ride data — providing insights into **bookings, cancellations, revenue trends, customer behavior, and ride patterns**.  

This dashboard helps analysts, managers, and business users understand **performance metrics, demand fluctuations, cancellations, and satisfaction trends** with **appealing visualizations** powered by Plotly, Seaborn, and Matplotlib.  

---

## ✨ Features

- **Filters** for Vehicle Type and Payment Method  
- **Key Performance Indicators (KPIs)**: Total Bookings, Completed Rides, Total Revenue  
- **Visualizations**:
  - Booking Status Distribution (Pie Chart)  
  - Revenue Contribution by Vehicle Type (Bar Chart)  
  - Correlation Heatmap of numeric variables  
  - Analytics Overview Section:  
    - Rides by Hour (Line Chart)  
    - Cancellations by Vehicle Type (Bar Chart)  
    - Ratings Comparison (Driver vs Customer)  
    - Revenue Trends Over Time (Area Chart)  

---

## 🛠️ Tech Stack

- [Python 3.8+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Plotly Express](https://plotly.com/python/plotly-express/)  
- [Seaborn](https://seaborn.pydata.org/)  
- [Matplotlib](https://matplotlib.org/)  

---

## 📂 Project Structure

uber-analytics-dashboard/<br>
│── app.py # Main Streamlit app <br>
│── ncr_ride_bookings.csv # Dataset (sample) <br>
│── README.md # Project documentation <br>
│── requirements.txt # Dependencies <br>


---

## 🚀 Installation & Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/uber-analytics-dashboard.git
cd uber-analytics-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

---
### 5. Open in browser

Go to 👉 ([dashbaord](https://uber-anlytics-dashboard-itv3kjahgtjdnghgc8bnf5.streamlit.app/))

---

## 📊 Sample Dashboard Preview

Interactive charts and filters let you explore ride demand, cancellations, and revenue over time.

<img width="3048" height="957" alt="image" src="https://github.com/user-attachments/assets/699815e9-a4c1-4498-af18-bc697a99b28d" />


---

## 📌 Future Enhancements

- Add Geo-visualization (maps) of pickup/drop locations  
- Implement Predictive Analytics for demand forecasting  
- Export reports in PDF/Excel format  

---

## 👨‍💻 Author

**Aymen Baig**  
Built with ❤️ using Streamlit & Python
