# ELT Data Modeling: Bronze, Silver, Gold Architecture

A comprehensive teaching repository for learning ELT (Extract, Load, Transform) data pipelines using the Medallion Architecture (Bronze/Silver/Gold layers).

## 🎯 Learning Objectives

This repository teaches you to:

1. **Understand ELT Concepts**: Learn the difference between ETL and ELT approaches
2. **Implement Bronze Layer**: Ingest raw data without modifications
3. **Implement Silver Layer**: Clean, validate, and standardize data
4. **Implement Gold Layer**: Create business-ready aggregated metrics
5. **Apply Best Practices**: Follow industry standards for data engineering

## 📚 What's Included

### 1. Data Design and Modeling (20%)
- **Layered Data Modeling**: Complete implementation of Bronze, Silver, and Gold layers
- **Business Requirements Analysis**: Sample business metrics and KPIs
- **Pipeline Specification**: Documented transformations and data flows

### 2. Raw Data Engineering
- Sample datasets (sales, customers, products)
- Data quality issues for hands-on learning
- Realistic business scenarios

### 3. Documentation
- Comprehensive guides and tutorials
- Conceptual explanations
- Hands-on exercises

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Basic understanding of data manipulation
- Familiarity with CSV files

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/anaslahr/01-elt-data-modeling.git
cd 01-elt-data-modeling
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the pipeline**
```bash
python scripts/run_elt_pipeline.py
```

## 📁 Project Structure

```
01-elt-data-modeling/
│
├── data/                          # Data layers
│   ├── raw_data/                 # Source data (READ ONLY)
│   │   ├── sales_data.csv        # Transaction records
│   │   ├── customer_data.csv     # Customer information
│   │   └── product_data.csv      # Product catalog
│   │
│   ├── bronze/                   # 🥉 Raw data ingestion layer
│   ├── silver/                   # 🥈 Cleaned & validated layer
│   └── gold/                     # 🥇 Business-ready metrics layer
│
├── scripts/                       # Pipeline scripts
│   ├── bronze_layer.py           # Raw data ingestion
│   ├── silver_layer.py           # Data cleaning & validation
│   ├── gold_layer.py             # Business aggregations
│   └── run_elt_pipeline.py       # Execute complete pipeline
│
├── docs/                          # Documentation
│   ├── GETTING_STARTED.md        # Setup and installation guide
│   ├── ELT_CONCEPTS.md           # Theory and concepts
│   └── EXERCISES.md              # Hands-on practice exercises
│
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## 🎓 Learning Path

### Step 1: Understand the Concepts
Read [docs/ELT_CONCEPTS.md](docs/ELT_CONCEPTS.md) to learn about:
- ELT vs ETL
- The Medallion Architecture
- Bronze, Silver, Gold layers
- Best practices

### Step 2: Set Up Your Environment
Follow [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) to:
- Install dependencies
- Understand the project structure
- Run your first pipeline

### Step 3: Practice with Exercises
Work through [docs/EXERCISES.md](docs/EXERCISES.md) to:
- Explore the data
- Modify transformations
- Create new metrics
- Build your own pipeline

## 🥉 Bronze Layer (Raw Data)

**Purpose**: Store data exactly as received from source systems.

**Key Features**:
- No transformations applied
- Preserves all records (including bad data)
- Adds ingestion metadata
- Immutable data storage

**Example Output**:
```
bronze_sales.csv
bronze_customers.csv
bronze_products.csv
```

## 🥈 Silver Layer (Cleaned Data)

**Purpose**: Clean and validate data for analysis.

**Key Features**:
- Remove duplicates
- Handle missing values
- Standardize formats
- Apply data type conversions
- Filter invalid records

**Example Output**:
```
silver_sales.csv         (cleaned transactions)
silver_customers.csv     (validated customers)
silver_products.csv      (normalized products)
```

## 🥇 Gold Layer (Business Metrics)

**Purpose**: Create business-ready aggregated metrics.

**Key Features**:
- Pre-aggregated KPIs
- Joined datasets
- Business logic applied
- Optimized for reporting

**Example Output**:
```
gold_sales_summary.csv           (revenue by category)
gold_customer_metrics.csv        (customer lifetime value)
gold_product_performance.csv     (product rankings)
gold_daily_sales_trend.csv       (time-series metrics)
```

## 🔧 Running the Pipeline

### Run Complete Pipeline
```bash
python scripts/run_elt_pipeline.py
```

### Run Individual Layers
```bash
# Bronze: Ingest raw data
python scripts/bronze_layer.py

# Silver: Clean and validate
python scripts/silver_layer.py

# Gold: Create business metrics
python scripts/gold_layer.py
```

## 📊 Sample Business Metrics

The pipeline generates these business insights:

- **Sales Summary**: Revenue and units sold by product category
- **Customer Segmentation**: High/Medium/Low value customers
- **Product Performance**: Revenue rankings and profit margins
- **Daily Trends**: Time-series analysis of sales patterns

## 🎯 Use Cases

This repository demonstrates:

1. **E-commerce Analytics**: Track sales, customers, and products
2. **Data Quality**: Handle missing values and duplicates
3. **Business Intelligence**: Create KPIs and dashboards
4. **Data Warehouse Design**: Implement dimensional modeling

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **CSV**: Data storage format

## 📖 Additional Resources

- [Databricks Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)
- [Data Engineering Best Practices](https://www.getdbt.com/analytics-engineering/transformation/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🤝 Contributing

This is a teaching repository. Students are encouraged to:
- Complete the exercises
- Suggest improvements
- Share their solutions
- Ask questions

## 📝 License

This project is created for educational purposes.

## 👨‍🏫 For Instructors

This repository provides:
- Complete ELT pipeline implementation
- Progressive difficulty exercises
- Real-world data scenarios
- Comprehensive documentation
- Hands-on learning approach

Students will gain practical experience in:
- Data pipeline design
- ETL/ELT patterns
- Data quality management
- Business metrics creation
- Python data engineering

## 🆘 Getting Help

- Check [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) for setup issues
- Review [docs/ELT_CONCEPTS.md](docs/ELT_CONCEPTS.md) for concept questions
- Try [docs/EXERCISES.md](docs/EXERCISES.md) for hands-on practice

---

**Happy Learning! 🚀**

Start your data engineering journey by understanding how raw data transforms into valuable business insights through the Bronze, Silver, and Gold layers!