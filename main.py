import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Auto Generated Dashboard",
    page_icon="📊",
    layout="wide"
)

# ================== TITLE ==================
st.title("📊 Auto Generated Dashboard")
st.caption("Upload any CSV file and get instant insights")

# ================== FILE UPLOAD ==================
file = st.file_uploader("📂 Upload your CSV file", type=["csv","xlsx"])

if file is not None:
    # ================== READ DATA ==================
    if file is not None:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
    # ================== DATA PREVIEW ==================
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    # ================== BASIC INFO ==================
    st.subheader("📌 Dataset Info")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # ================== COLUMN TYPES ==================
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    # ================== FILTERS ==================
    st.sidebar.header("🎛️ Filters")
    filtered_df = df.copy()

    for col in categorical_cols:
        selected = st.sidebar.multiselect(f"Filter {col}", df[col].unique())
        if selected:
            filtered_df = filtered_df[filtered_df[col].isin(selected)]

    # ================== KPI SECTION ==================
    st.subheader("📈 Key Metrics")
    if len(numeric_cols) > 0:
        kpi_col = st.selectbox("Select numeric column for KPI", numeric_cols)
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Mean", round(filtered_df[kpi_col].mean(), 2))
        k2.metric("Max", filtered_df[kpi_col].max())
        k3.metric("Min", filtered_df[kpi_col].min())
        k4.metric("Sum", round(filtered_df[kpi_col].sum(), 2))

    # ================== MULTIPLE VISUALIZATIONS ==================
    st.subheader("📊 Multiple Visualizations (6+ Charts)")
    selected_col = st.selectbox("Select column to visualize", df.columns)

    # ---------- NUMERIC VISUALS ----------
    if selected_col in numeric_cols:
        c1, c2 = st.columns(2)

        # 1️⃣ Histogram
        with c1:
            fig1 = px.histogram(filtered_df, x=selected_col, title="Histogram")
            st.plotly_chart(fig1, use_container_width=True)

        # 2️⃣ Box Plot
        with c2:
            fig2 = px.box(filtered_df, y=selected_col, title="Box Plot")
            st.plotly_chart(fig2, use_container_width=True)

        c3, c4 = st.columns(2)

        # 3️⃣ Line Chart
        with c3:
            fig3 = px.line(filtered_df, y=selected_col, title="Line Chart")
            st.plotly_chart(fig3, use_container_width=True)

        # 4️⃣ Scatter Plot
        with c4:
            fig4 = px.scatter(filtered_df, y=selected_col, title="Scatter Plot")
            st.plotly_chart(fig4, use_container_width=True)

        # 5️⃣ Violin Plot (Graph Objects)
        fig5 = go.Figure()
        fig5.add_trace(go.Violin(
            y=filtered_df[selected_col],
            box_visible=True,
            meanline_visible=True
        ))
        fig5.update_layout(title="Violin Plot")
        st.plotly_chart(fig5, use_container_width=True)

    # ---------- CATEGORICAL VISUALS ----------
    elif selected_col in categorical_cols:
        value_counts = filtered_df[selected_col].value_counts().reset_index()
        value_counts.columns = [selected_col, "Count"]

        c1, c2 = st.columns(2)

        # 6️⃣ Bar Chart
        with c1:
            fig6 = px.bar(
                value_counts,
                x=selected_col,
                y="Count",
                text="Count",
                title="Bar Chart"
            )
            st.plotly_chart(fig6, use_container_width=True)

        # 7️⃣ Donut Chart
        with c2:
            fig7 = go.Figure(
                data=[go.Pie(
                    labels=value_counts[selected_col],
                    values=value_counts["Count"],
                    hole=0.4
                )]
            )
            fig7.update_layout(title="Donut Chart")
            st.plotly_chart(fig7, use_container_width=True)

    else:
        st.info("⚠️ Selected column type not supported.")

    # ================== CORRELATION HEATMAP ==================
    if len(numeric_cols) > 1:
        st.subheader("🔗 Correlation Heatmap")
        corr = filtered_df[numeric_cols].corr()
        fig8 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
        st.plotly_chart(fig8, use_container_width=True)

else:
    st.info("👆 Upload a CSV file to generate the dashboard")
