# 🚢 Titanic Exploratory Data Analysis (EDA)

An interactive data analysis dashboard built using Python and Streamlit to explore the Titanic passenger dataset, understand survival patterns, perform data cleaning, and generate statistical insights.

## 🌐 Live Demo

[Open Titanic EDA Dashboard](https://titanic-edas.streamlit.app/)

## 📌 About the Project

This project explores the Titanic passenger dataset through an interactive dashboard. It demonstrates data analysis, data cleaning, statistical calculations, and data visualization using Python libraries.

The main objective is to understand passenger survival patterns and explore how factors such as gender and passenger class are associated with survival rates.

## ✨ Features

- **Dataset Overview:** View passenger records, dataset dimensions, duplicate rows, and summary statistics.
- **Missing Value Analysis:** Identify missing values and their percentages.
- **Data Cleaning:** Handle missing Age values using median imputation, missing Embarked values using mode imputation, and remove the Cabin column due to excessive missing data.
- **Statistical Analysis:** Calculate passenger survival counts and survival percentages.
- **Gender Analysis:** Compare survival rates between male and female passengers.
- **Passenger Class Analysis:** Explore survival rates across first, second, and third class.
- **Interactive Visualizations:** Display statistical charts using Plotly.
- **Correlation vs Causation:** Understand the difference between statistical relationships and direct causes.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

## 📊 Dataset

The project uses the Titanic passenger dataset from:

[ Titanic Dataset – DataScienceDojo ](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)

The dataset includes information such as passenger age, gender, passenger class, ticket details, embarkation port, and survival status.

## 📂 Project Structure

```text
titanic-EDA-/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Anmolpatel0/titanic-EDA-.git
```

### 2. Open the project folder

```bash
cd titanic-EDA-
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📈 Key Learning Outcomes

- Working with real-world datasets using Pandas.
- Identifying and handling missing data.
- Performing grouping and aggregation operations.
- Calculating survival rates and percentages.
- Creating interactive visualizations using Plotly.
- Building and deploying a Python data analysis dashboard.

## 👨‍💻 Author

**Anmol Patel**

GitHub: [Anmolpatel0](https://github.com/Anmolpatel0)

LinkedIn: [Anmol Patel](https://www.linkedin.com/in/anmol-patel-7a5b78378/)

---

⭐ If you find this project useful, consider giving the repository a star!
