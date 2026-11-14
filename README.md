# ⚡ Smart Electricity Consumption Analyzer

A Python-based electricity consumption analysis system that helps households monitor electricity usage, calculate estimated electricity bills, detect unusual consumption, forecast future usage, and receive energy-saving recommendations.

This project is developed using **Pure Python** and Python's built-in modules, without any external libraries.

## 📌 Project Overview

Managing electricity consumption is important for reducing electricity costs and avoiding unnecessary energy waste.

The Smart Electricity Consumption Analyzer processes household electricity readings and provides useful insights through automated calculations, consumption analysis, forecasting, and report generation.

## ✨ Features

### 1. Electricity Data Management
- Load electricity records from CSV files.
- View existing household electricity readings.
- Add new electricity readings.
- Validate meter readings and prevent duplicate entries.

### 2. Electricity Consumption Analysis
- Calculate total electricity consumption.
- Calculate average consumption.
- Identify highest and lowest consumption.
- Analyze household-wise consumption.
- Compare monthly electricity usage.

### 3. Electricity Bill Calculator
- Calculate electricity charges using progressive tariff slabs.
- Include fixed charges.
- Calculate additional charges.
- Display estimated electricity bills.

### 4. Anomaly Detection
- Identify unusual electricity consumption.
- Compare current usage with historical averages.
- Classify unusual readings as WARNING or CRITICAL.

### 5. Electricity Bill Forecasting
- Predict next month's electricity consumption.
- Use a three-month moving average.
- Estimate future electricity bills.

### 6. Energy-Saving Recommendations
- Analyze household electricity usage.
- Identify increased consumption.
- Generate rule-based energy-saving suggestions.

### 7. Electricity Report Generation
- Generate household electricity summaries.
- Calculate consumption statistics.
- Export reports into CSV format.
- Save generated reports automatically.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Storage:** CSV and JSON
- **Python Modules:** csv, json, os, datetime
- **Concepts:** Functions, Lists, Dictionaries, File Handling, Exception Handling, Data Validation, Modular Programming

**External Libraries:** None

## 📂 Project Structure

```text
Smart-Electricity-Analyzer/
│
├── data/
│   ├── electricity_readings.csv
│   └── tariff_settings.json
│
├── reports/
│   └── electricity_summary_report.csv
│
├── code/
│   ├── main.py
│   ├── data_manager.py
│   ├── consumption_analyzer.py
│   ├── bill_calculator.py
│   ├── anomaly_detector.py
│   ├── bill_forecaster.py
│   ├── energy_recommender.py
│   └── report_generator.py
│
├── README.md
│
└── tests/
```

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 3: Open the Project Folder

```bash
cd Smart-Electricity-Analyzer
```

### Step 4: Run the Application

```bash
python code/main.py
```

No external package installation is required.

## 🖥️ Application Menu

The application provides the following menu options:

```text
==================================================
       SMART ELECTRICITY CONSUMPTION ANALYZER
==================================================
1. View Electricity Records
2. Add New Electricity Reading
3. Analyze Electricity Consumption
4. Calculate Electricity Bill
5. View All Household Bills
6. Detect Unusual Consumption
7. Forecast Next Month's Electricity Bill
8. Energy-Saving Recommendations
9. View Electricity Summary Report
10. Export Report to CSV
11. Exit
==================================================
```

## 📊 Sample Data

The project uses sample household electricity readings stored in a CSV file.

Example:

| House ID | Month | Units Consumed |
|---|---|---:|
| H001 | 2026-01 | 150 |
| H001 | 2026-02 | 180 |
| H001 | 2026-03 | 220 |
| H002 | 2026-01 | 120 |
| H002 | 2026-02 | 130 |

The application also uses a JSON configuration file to store electricity tariff settings.

**Note:** The sample readings and tariff rates are illustrative and are not official electricity billing data.

## 📈 Forecasting Method

The project uses a simple three-month moving average to estimate future electricity consumption.

The predicted consumption is calculated using the average of the latest three available monthly readings.

This is a basic forecasting approach and does not use machine learning.

## 🎯 Project Objectives

- Apply Core Python concepts to a real-world problem.
- Understand file handling using CSV and JSON.
- Develop modular and reusable Python programs.
- Analyze household electricity consumption.
- Automate electricity bill calculations.
- Generate useful consumption insights and reports.

## 🚀 Future Improvements

- Add user authentication and login functionality.
- Add automated unit testing.
- Improve data validation and error handling.
- Add graphical electricity consumption visualizations.
- Support multiple electricity tariff configurations.
- Improve forecasting using more historical data.

## 👨‍💻 Author

**Aakash Muthal**

Aspiring Python Developer | Data Science Enthusiast

GitHub: https://github.com/AakashMuthal

---

⭐ If you find this project useful, consider giving the repository a star!