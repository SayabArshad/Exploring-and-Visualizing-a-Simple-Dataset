# Exploring and Visualizing a Simple Dataset

## 🎯 Objective

This task involves exploring and visualizing a simple dataset using Python. We use the **Iris dataset**, a classic dataset in machine learning, to understand feature relationships and distributions through basic data visualizations.

---

## 📊 Dataset Description

- **Dataset Name:** Iris
- **Source:** Seaborn built-in dataset (`sns.load_dataset('iris')`)
- **Rows:** 150
- **Columns:** 5
- **Features:**
  - `sepal_length`
  - `sepal_width`
  - `petal_length`
  - `petal_width`
  - `species` (target class: setosa, versicolor, virginica)

---

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook (run using VS Code)

---

## 🧪 Approach

1. **Data Loading & Inspection**
   - Loaded the dataset using Seaborn’s `load_dataset()` function.
   - Inspected shape, column names, and previewed first few rows using:
     - `.shape`
     - `.columns`
     - `.head()`

2. **Visualizations**
   - **Scatter Plot** – Examined the relationship between `sepal_length` and `sepal_width`, colored by species.
   - **Histogram** – Viewed distributions of all numeric features.
   - **Box Plot** – Analyzed feature spread and detected outliers.

---

## 📈 Results & Insights

- The dataset contains no missing values and is well-structured.
- The **Setosa** species is distinctly clustered based on sepal features.
- **Histograms** revealed different distribution patterns across features.
- **Box plots** highlighted variability and potential outliers, especially in petal dimensions.

---

## 📂 Project Files

- `Task-01.ipynb` – Jupyter Notebook containing code and visualizations.
- `README.md` – Documentation of the task, approach, and findings.

---

## ✅ Internship Submission Checklist

- [x] Jupyter Notebook with code and markdown descriptions
- [x] Introduction, dataset overview, and inspection
- [x] Scatter plot, histogram, and box plot
- [x] Well-commented, clean code
- [x] README.md summarizing the task
- [x] Pushed to GitHub repository
- [x] Link submitted via Google Classroom

---

## 🚀 How to Run This Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SayabArshad/Task-1-Exploring-and-Visualizing-a-Simple-Dataset.git
