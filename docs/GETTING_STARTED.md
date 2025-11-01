# Getting Started with ELT Data Modeling

Welcome to the ELT Data Modeling course! This repository will teach you how to build a robust data pipeline using the Bronze, Silver, Gold (Medallion) architecture.

## Prerequisites

- Basic Python knowledge
- Understanding of CSV files and data formats
- Familiarity with command line/terminal

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anaslahr/01-elt-data-modeling.git
cd 01-elt-data-modeling
```

### 2. Create a Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python --version  # Should be Python 3.8+
pip list          # Should show pandas, numpy installed
```

## Project Structure

```
01-elt-data-modeling/
│
├── data/                      # Data storage
│   ├── raw_data/             # Source data files (READ ONLY)
│   │   ├── sales_data.csv
│   │   ├── customer_data.csv
│   │   └── product_data.csv
│   │
│   ├── bronze/               # Bronze layer (raw ingestion)
│   ├── silver/               # Silver layer (cleaned data)
│   └── gold/                 # Gold layer (business metrics)
│
├── scripts/                   # Python scripts
│   ├── bronze_layer.py       # Bronze layer ingestion
│   ├── silver_layer.py       # Silver layer transformations
│   ├── gold_layer.py         # Gold layer aggregations
│   └── run_elt_pipeline.py   # Run complete pipeline
│
├── docs/                      # Documentation
│   ├── GETTING_STARTED.md    # This file
│   ├── ELT_CONCEPTS.md       # Theory and concepts
│   └── EXERCISES.md          # Practice exercises
│
├── requirements.txt           # Python dependencies
└── README.md                 # Project overview
```

## Running the Pipeline

### Option 1: Run Complete Pipeline

Run all three layers in sequence:

```bash
python scripts/run_elt_pipeline.py
```

### Option 2: Run Individual Layers

Run each layer separately:

```bash
# Step 1: Bronze Layer
python scripts/bronze_layer.py

# Step 2: Silver Layer
python scripts/silver_layer.py

# Step 3: Gold Layer
python scripts/gold_layer.py
```

## Understanding the Output

After running the pipeline, check the generated files:

### Bronze Layer Output
```bash
ls -lh data/bronze/
# bronze_sales.csv
# bronze_customers.csv
# bronze_products.csv
```

These files contain the raw data with added metadata columns:
- `_ingestion_timestamp`: When the data was ingested
- `_source_file`: Original source file name

### Silver Layer Output
```bash
ls -lh data/silver/
# silver_sales.csv
# silver_customers.csv
# silver_products.csv
```

These files contain cleaned and validated data:
- Duplicates removed
- Missing values handled
- Data types standardized
- Invalid records filtered out

### Gold Layer Output
```bash
ls -lh data/gold/
# gold_sales_summary.csv
# gold_customer_metrics.csv
# gold_product_performance.csv
# gold_daily_sales_trend.csv
```

These files contain business-ready metrics:
- Aggregated sales by category
- Customer lifetime value
- Product performance rankings
- Daily sales trends

## Exploring the Data

### Using Python

```python
import pandas as pd

# Load Bronze data
bronze_sales = pd.read_csv('data/bronze/bronze_sales.csv')
print(bronze_sales.head())

# Load Silver data
silver_sales = pd.read_csv('data/silver/silver_sales.csv')
print(silver_sales.head())

# Load Gold data
gold_summary = pd.read_csv('data/gold/gold_sales_summary.csv')
print(gold_summary)
```

### Using Command Line

```bash
# View first few rows
head data/bronze/bronze_sales.csv

# Count records
wc -l data/bronze/bronze_sales.csv

# View specific columns
cut -d',' -f1,2,3 data/silver/silver_sales.csv | head
```

## Next Steps

1. **Read the Concepts**: Check out [ELT_CONCEPTS.md](ELT_CONCEPTS.md) to understand the theory
2. **Examine the Code**: Look at each script to understand the transformations
3. **Try the Exercises**: Work through [EXERCISES.md](EXERCISES.md) to practice
4. **Modify the Pipeline**: Try adding your own transformations

## Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution**: Make sure you've activated the virtual environment and installed requirements:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: [Errno 2] No such file or directory"
**Solution**: Make sure you're running scripts from the project root:
```bash
cd /path/to/01-elt-data-modeling
python scripts/run_elt_pipeline.py
```

### Issue: Silver or Gold layer fails
**Solution**: Make sure you've run the Bronze layer first. The layers are sequential:
```bash
python scripts/bronze_layer.py  # Run this first
python scripts/silver_layer.py  # Then this
python scripts/gold_layer.py    # Finally this
```

## Learning Resources

- [ELT Concepts Documentation](ELT_CONCEPTS.md) - Theory and best practices
- [Practice Exercises](EXERCISES.md) - Hands-on exercises
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Data manipulation library
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Getting Help

If you're stuck:
1. Read the error message carefully
2. Check the [ELT_CONCEPTS.md](ELT_CONCEPTS.md) documentation
3. Look at the example code in the scripts
4. Try the simpler exercises first in [EXERCISES.md](EXERCISES.md)

## Tips for Success

1. 🔍 **Explore the data**: Use `head()`, `info()`, `describe()` to understand the data
2. 📝 **Document your changes**: Add comments to explain your transformations
3. 🧪 **Test incrementally**: Run each layer and verify output before moving on
4. 🤔 **Ask questions**: Why are we doing each transformation? What business value does it provide?
5. 🎯 **Focus on concepts**: Understanding WHY is more important than memorizing HOW

Happy learning! 🚀
