import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit Page Config
st.set_page_config(
    page_title="Titanic EDA & Insights", page_icon="🚢", layout="wide"
)

st.title("🚢 Titanic Exploratory Data Analysis (EDA)")
st.write(
    "Interactive dashboard for data cleaning, statistical insights, and hypothesis verification."
)


# 1. Load Data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = pd.read_csv(url)
    return data


raw_df = load_data()
df = raw_df.copy()

# Sidebar Setup
st.sidebar.title("📌 Navigation")
options = st.sidebar.radio(
    "Select Section:",
    [
        "1. Dataset Overview",
        "2. Data Cleaning & Rationale",
        "3. Statistical Insights (Real Numbers)",
        "4. Correlation vs Causation Analysis",
    ],
)

# ----------------------------------------------------
# Section 1: Overview
# ----------------------------------------------------
if options == "1. Dataset Overview":
    st.header("1. DataFrame Operations & Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Passengers", len(df))
    col2.metric("Total Columns", len(df.columns))
    col3.metric("Duplicate Rows", df.duplicated().sum())

    st.subheader("Preview: First 5 Rows (`df.head()`)")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("Summary Statistics (`df.describe()`)")
    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("Dataset Info & Missing Values")
    missing_data = pd.DataFrame(
        {
            "Data Type": df.dtypes,
            "Missing Values": df.isnull().sum(),
            "Missing (%)": (df.isnull().sum() / len(df) * 100).round(2),
        }
    )
    st.dataframe(missing_data, use_container_width=True)

# ----------------------------------------------------
# Section 2: Data Cleaning
# ----------------------------------------------------
elif options == "2. Data Cleaning & Rationale":
    st.header("2. Transparent Data Cleaning Decisions")
    st.info(
        "**Rule:** Do not drop rows blindly. Every missing value strategy is explicitly justified below."
    )

    # Perform Cleaning
    age_median = df["Age"].median()
    df["Age"] = df["Age"].fillna(age_median)

    embarked_mode = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(embarked_mode)

    df_cleaned = df.drop(columns=["Cabin"])

    # Rationale Display
    with st.expander("📝 1. Handling Missing `Age` (177 missing / 19.87%)", expanded=True):
        st.write(
            f"- **Action:** Imputed with median age (**{age_median} years**)."
        )
        st.write(
            "- **Rationale:** Dropping 177 rows would lose ~20% of the dataset. Median was selected over mean to avoid skewing from age outliers."
        )

    with st.expander("📝 2. Handling Missing `Embarked` (2 missing / 0.22%)", expanded=True):
        st.write(
            f"- **Action:** Imputed with most frequent port (**'{embarked_mode}' - Southampton**)."
        )
        st.write(
            "- **Rationale:** Only 2 records were missing. Mode imputation preserves sample size with minimal distortion."
        )

    with st.expander("📝 3. Handling Missing `Cabin` (687 missing / 77.10%)", expanded=True):
        st.write("- **Action:** Dropped the `Cabin` column entirely.")
        st.write(
            "- **Rationale:** Over 77% missing data. Imputation would add artificial noise/guesswork."
        )

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(df_cleaned.head(), use_container_width=True)

# ----------------------------------------------------
# Section 3: Statistical Insights
# ----------------------------------------------------
elif options == "3. Statistical Insights (Real Numbers)":
    st.header("3. Grouping & Aggregation Analysis")

    # Clean data for stats
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    total = len(df)
    survived = df["Survived"].sum()
    perished = total - survived

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Passengers", f"{total}")
    col2.metric("Survivors", f"{survived} ({survived/total*100:.2f}%)")
    col3.metric("Perished", f"{perished} ({perished/total*100:.2f}%)")

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Survival by Gender")
        gender_df = (
            df.groupby("Sex")
            .agg(
                Total=("Survived", "count"),
                Survivors=("Survived", "sum"),
                Rate=("Survived", lambda x: (x.sum() / x.count()) * 100),
            )
            .reset_index()
        )
        st.dataframe(gender_df.round(2), use_container_width=True)

        fig_sex = px.bar(
            gender_df,
            x="Sex",
            y="Rate",
            color="Sex",
            title="Survival Rate by Gender (%)",
            text_auto=".2f",
        )
        st.plotly_chart(fig_sex, use_container_width=True)

    with col_right:
        st.subheader("Survival by Passenger Class (`Pclass`)")
        class_df = (
            df.groupby("Pclass")
            .agg(
                Total=("Survived", "count"),
                Survivors=("Survived", "sum"),
                Rate=("Survived", lambda x: (x.sum() / x.count()) * 100),
            )
            .reset_index()
        )
        st.dataframe(class_df.round(2), use_container_width=True)

        fig_class = px.bar(
            class_df,
            x="Pclass",
            y="Rate",
            color="Pclass",
            title="Survival Rate by Class (%)",
            text_auto=".2f",
        )
        st.plotly_chart(fig_class, use_container_width=True)

    st.subheader("Combined Analysis: Class & Gender")
    multi_df = (
        df.groupby(["Pclass", "Sex"])
        .agg(
            Total=("Survived", "count"),
            Survivors=("Survived", "sum"),
            Survival_Rate_Pct=("Survived", lambda x: (x.sum() / x.count()) * 100),
        )
        .reset_index()
    )
    st.dataframe(multi_df.round(2), use_container_width=True)

# ----------------------------------------------------
# Section 4: Correlation vs Causation
# ----------------------------------------------------
elif options == "4. Correlation vs Causation Analysis":
    st.header("4. Key Takeaways & Statistical Warnings")

    st.warning(
        "⚠️ **Correlation is NOT Causation:** High correlation indicates statistical association, not a direct mechanical cause."
    )

    st.markdown(
        """
    ### Exact Findings Summary:
    * **Gender Disparity:** 
      * **233 out of 314 females** survived (**74.20%**).
      * **109 out of 577 males** survived (**18.89%**).
      * *Context:* This reflects evacuation protocols (*"Women and children first"*), not biological differences.
      
    * **Socioeconomic Status (Class):**
      * **1st Class:** 136 / 216 survived (**62.96%**).
      * **2nd Class:** 87 / 184 survived (**47.28%**).
      * **3rd Class:** 119 / 491 survived (**24.24%**).
      * *Context:* Ticket class correlates with deck location and lifeboat access proximity, which directly impacted survival odds.
    """
    )
