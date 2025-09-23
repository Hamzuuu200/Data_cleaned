import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🧹 Universal Data Cleaning App")

# Step 1: Upload file
file = st.file_uploader("Upload any CSV file", type="csv")

if file:
    df = pd.read_csv(file)
    st.write("📌 Original Data (first 10 rows)", df.head(10))

    # Step 2: Handle numeric columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Step 3: Handle categorical columns
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
    for col in categorical_cols:
        df[col] = df[col].replace(["UNKNOWN", "ERROR", ""], pd.NA)
        df[col] = df[col].fillna("Missing")

    # Step 4: Handle dates
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Step 5: Drop rows with all NaN values
    df = df.dropna(how="all")

    # Step 6: Remove duplicates
    df = df.drop_duplicates()

    # Step 7: Show cleaned data with slider
    rows = st.slider("Select number of rows to display:", 5, len(df), 10)
    st.write("✅ Cleaned Data", df.head(rows))

    # Step 8: Scatter Plot
    st.subheader("📊 Scatter Plot")
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("Select X-axis", numeric_cols)
        y_col = st.selectbox("Select Y-axis", numeric_cols)
        
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col], alpha=0.7)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} vs {x_col}")
        st.pyplot(fig)
    else:
        st.info("Not enough numeric columns for scatter plot.")

    # Step 9: Download button
    st.download_button("⬇️ Download Cleaned CSV", df.to_csv(index=False), "cleaned.csv")
