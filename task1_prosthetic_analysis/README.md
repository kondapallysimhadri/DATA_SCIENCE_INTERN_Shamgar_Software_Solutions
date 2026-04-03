# Prosthetic EMG Signal Analysis Dashboard

## Project Overview

This project presents an interactive **Streamlit dashboard** for analyzing **Electromyography (EMG) signals** used in prosthetic systems.
The goal is to understand muscle activation patterns and improve prosthetic control using data-driven insights.

---

## Objectives

* Analyze multi-channel EMG signals
* Visualize signal patterns over time
* Identify muscle activation peaks
* Understand relationships between channels
* Provide meaningful insights for prosthetic performance

---

## Features

***Time-Series Visualization** (Signal vs Time)
***Signal Distribution Analysis**
***Multi-Channel Comparison**
***Correlation Heatmap**
***Peak Detection (Muscle Activation)**
***RMS Calculation (Signal Strength)**
***Interactive Filters (Channel & Label)**
**Download Dataset Option**

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## Project Structure

```
task1_prosthetic_analysis/
│
├── data/
│   └── EMG_data.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶ How to Run the Project

### 1️ Clone the Repository

```
git clone https://github.com/your-username/emg-analysis-dashboard.git
cd emg-analysis-dashboard
```

### 2️ Create Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
```

### 3️ Install Dependencies

```
pip install -r requirements.txt
```

### 4️ Run the App

```
streamlit run app.py
```

---

## Key Insights

* EMG signals vary across time and channels
* High peaks indicate strong muscle contractions
* RMS value represents overall muscle effort
* Channel correlation shows coordinated muscle activity
* Different labels represent distinct movement patterns

---

## Future Improvements

* Add machine learning model for movement prediction
* Real-time EMG signal integration
* Advanced signal processing (FFT, filtering)
* Enhanced UI with Plotly

---

## Author

**Simhadri Kondapally**
Aspiring Data Scientist | AI & ML Enthusiast

---

## Acknowledgment

This project was developed as part of a **Data Science Internship Task** to demonstrate practical EMG signal analysis and visualization skills.
