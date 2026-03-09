# Auto-Generator-Visualization
An automated data visualization dashboard built with Streamlit, Pandas, and Plotly. Users can upload CSV or Excel files to instantly generate dataset previews, key metrics, interactive filters, multiple charts (histogram, box, scatter, bar, donut), and a correlation heatmap for quick exploratory data analysis.
📊 Auto Generated Dashboard (Streamlit)

This project is a dynamic data visualization dashboard built using Streamlit, Pandas, and Plotly. The application allows users to upload any CSV or Excel dataset and automatically generate insights, key metrics, and multiple visualizations without writing any code.

🚀 Features
- Upload CSV or Excel datasets
- Automatic dataset preview and summary
- Key metrics (Mean, Max, Min, Sum)
- Interactive sidebar filters
- Multiple visualizations:
  - Histogram
  - Box Plot
  - Line Chart
  - Scatter Plot
  - Violin Plot
  - Bar Chart
  - Donut Chart
- Correlation Heatmap for numeric data
- Dynamic charts based on column type

🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly

📂 How It Works
1. Upload a dataset (CSV or Excel).
2. The app automatically detects numeric and categorical columns.
3. Interactive filters allow users to slice the data.
4. The dashboard generates KPIs and multiple visualizations instantly.

🎯 Use Cases
- Quick data exploration
- Business analytics dashboards
- Data science projects
- Automated EDA (Exploratory Data Analysis)

▶️ Run the App
```bash
streamlit run auto_dashboard.py
