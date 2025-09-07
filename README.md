# Tiko Analytics

## **A simple open-source Python tool to check your social media performance.**

## Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Support](#support)
- [License](#license)

---

## About

Tiko Analytics is a Python program that helps you understand your social media account. It shows simple statistics and business insights. The tool makes it easier to find what works and what needs improvement.

---

## Features

Tiko Analytics works in three main steps:

1. **Data Loading & Cleaning**

   - Make column names uppercase.
   - Remove duplicate rows and useless columns.
   - Fill or handle missing values (NaN).
   - Detect and remove outliers if needed.

2. **Descriptive Analytics**

   - Summarize monthly metrics (Views, Likes, Comments, Shares).
   - Calculate mean, median, and mode.
   - Calculate variance, standard deviation, and IQR.

3. **Business Insights**

   - Check account health (engagement, conversion, etc.).
   - Give clear suggestions to improve performance.

---

## Requirements

- **Python** 3.11 or newer.
- **Editor**: VS Code or any modern code editor.
- **Libraries**: pandas, numpy, openpyxl.
- **Data file**: `Overview.xlsx` from your social media analytics.

**How to get `Overview.xlsx` from TikTok (example):**

1. Log in to TikTok on the web.
2. Open Creator Center or Business Suite.
3. Go to Analytics and click Export.
4. Choose a date range and download the file.
5. Put the file in `data/raw/Overview.xlsx`.

---

## Installation

Follow these steps to run the project locally:

```bash
# Clone the repo
git clone https://github.com/PandhuPrayogo/Tiko-Analytics.git
cd tiko-analytics

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Or Windows (CMD)
.\venv\Scripts\activate

# Install packages
pip install pandas numpy openpyxl
```

---

## Project Structure

```
tiko-analytics/
├── data/
│   └── raw/
│       └── Overview.xlsx
├── src/
│   ├── business.py
│   ├── data_clean.py
│   └── desc_analyst.py
├── main.py
└── README.md
```

- `main.py` runs the analysis.
- `src/` has the core code.
- `data/raw/` holds the raw data file.

---

## Examples

Run the program with:

```bash
python main.py
```

You will see a short report with:

- A preview of the loaded data (first rows).
- Descriptive statistics by month.
- A simple account health summary and suggestions.

Sample output lines:

```
==== Welcome to Tiko Analytics ====
File: 'data/raw/Overview.xlsx' loaded successfully.
==== Descriptive Statistics ====
...monthly summaries...
==== Business Insights ====
Engagement Rate (%): 1.23
Engagement Status: Needs Improvement
Conversion Rate (%): 2.45
==== Data Analysis Completed ====
```

---

## Support

If you like this project, you can support me:

Buy me a coffee: [https://saweria.co/Yewonnie](https://saweria.co/Yewonnie)

---
