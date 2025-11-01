# Practice Exercises

These exercises will help you understand and practice ELT data modeling concepts. Start with the beginner exercises and progress to more advanced ones.

## 📚 Before You Start

1. Make sure you've completed the setup in [GETTING_STARTED.md](GETTING_STARTED.md)
2. Read [ELT_CONCEPTS.md](ELT_CONCEPTS.md) to understand the theory
3. Run the existing pipeline to see how it works

## 🟢 Beginner Exercises

### Exercise 1: Explore the Raw Data

**Goal**: Understand the source data files.

**Tasks**:
1. Load each raw data file using pandas
2. Check the shape (rows, columns) of each dataset
3. Look at the first 5 rows of each file
4. Identify columns with missing values

**Code Template**:
```python
import pandas as pd

# Load sales data
sales = pd.read_csv('data/raw_data/sales_data.csv')

# Check shape
print(f"Sales data shape: {sales.shape}")

# View first 5 rows
print(sales.head())

# Check for missing values
print(sales.isnull().sum())
```

**Questions to Answer**:
- How many sales transactions are there?
- Which columns have missing values?
- What are the unique payment methods?

---

### Exercise 2: Understand Bronze Layer

**Goal**: See how raw data is preserved in Bronze layer.

**Tasks**:
1. Run the Bronze layer script
2. Compare bronze_sales.csv with sales_data.csv
3. Identify what metadata columns were added
4. Count the records in both files

**Code Template**:
```python
import pandas as pd

# Load raw and bronze data
raw_sales = pd.read_csv('data/raw_data/sales_data.csv')
bronze_sales = pd.read_csv('data/bronze/bronze_sales.csv')

# Compare columns
print("Raw columns:", raw_sales.columns.tolist())
print("Bronze columns:", bronze_sales.columns.tolist())

# Compare record counts
print(f"Raw records: {len(raw_sales)}")
print(f"Bronze records: {len(bronze_sales)}")
```

**Questions to Answer**:
- What new columns were added in Bronze?
- Is any data modified or removed in Bronze?
- Why is it important to preserve raw data?

---

### Exercise 3: Analyze Data Quality Issues

**Goal**: Identify data quality problems in raw data.

**Tasks**:
1. Load the bronze_sales.csv file
2. Find records with missing customer_id
3. Find records with missing store_id
4. Check if there are any duplicate transaction_ids

**Code Template**:
```python
import pandas as pd

bronze_sales = pd.read_csv('data/bronze/bronze_sales.csv')

# Find missing customer_id
missing_customer = bronze_sales[bronze_sales['customer_id'].isnull()]
print(f"Records with missing customer_id: {len(missing_customer)}")

# TODO: Add code to find missing store_id
# TODO: Check for duplicates
```

**Questions to Answer**:
- How many records have missing customer_id?
- How many records have missing store_id?
- Are there any duplicate transaction IDs?

---

## 🟡 Intermediate Exercises

### Exercise 4: Add a New Transformation to Silver Layer

**Goal**: Modify the Silver layer to add new data cleaning rules.

**Tasks**:
1. Add a validation rule to ensure price > 0 for all sales
2. Add a new column `payment_method_category` that groups payment methods:
   - "Card" for Credit Card and Debit Card
   - "Cash" for Cash
3. Calculate and add `revenue_per_unit` (price per single item)

**Hint**: Modify `scripts/silver_layer.py` in the `clean_sales_data()` function.

**Validation**:
```python
import pandas as pd

silver_sales = pd.read_csv('data/silver/silver_sales.csv')
print(silver_sales['payment_method_category'].value_counts())
print(silver_sales['revenue_per_unit'].describe())
```

---

### Exercise 5: Create a New Gold Layer Report

**Goal**: Add a new business metric to the Gold layer.

**Tasks**:
Create a new function in `gold_layer.py` that generates a "Store Performance Report" with:
- Total revenue by store
- Number of transactions by store
- Average transaction value by store
- Most popular product category by store

**Code Template**:
```python
def create_store_performance(sales_df, products_df):
    """
    Create store performance metrics.
    """
    # Join sales with products
    sales_with_products = sales_df.merge(
        products_df[['product_id', 'category']], 
        on='product_id', 
        how='left'
    )
    
    # TODO: Aggregate by store_id
    # TODO: Calculate metrics
    # TODO: Find most popular category per store
    
    return store_performance
```

---

### Exercise 6: Handle Missing Values Strategically

**Goal**: Implement different strategies for handling missing data.

**Tasks**:
1. For missing customer_id in sales: Create a placeholder "GUEST_CUSTOMER"
2. For missing store_id: Use "ONLINE_STORE" as the value
3. For missing phone in customers: Keep as "Not Provided"
4. Track how many values were imputed

**Questions to Consider**:
- When should you remove records vs. impute values?
- What business impact does each strategy have?

---

## 🔴 Advanced Exercises

### Exercise 7: Implement Customer Segmentation

**Goal**: Create a sophisticated customer segmentation model in Gold layer.

**Tasks**:
Create a new Gold table with customer segments based on:
- RFM Analysis (Recency, Frequency, Monetary)
- Recency: Days since last purchase
- Frequency: Number of purchases
- Monetary: Total amount spent

Assign each customer to a segment:
- "Champions": High frequency, high monetary, recent
- "At Risk": High monetary, but not recent
- "Potential Loyalists": Recent, good frequency
- "New Customers": Recent, low frequency

**Hint**: Use quantiles to create segments.

---

### Exercise 8: Add Time-Based Analysis

**Goal**: Implement temporal analysis in the Gold layer.

**Tasks**:
Create a new report that shows:
1. Week-over-week revenue growth
2. Month-to-date vs. previous month comparison
3. Best performing day of the week
4. Peak sales hours (if timestamp is available)

**Code Template**:
```python
import pandas as pd

def create_temporal_analysis(sales_df):
    sales_df['transaction_date'] = pd.to_datetime(sales_df['transaction_date'])
    sales_df['week'] = sales_df['transaction_date'].dt.isocalendar().week
    sales_df['day_of_week'] = sales_df['transaction_date'].dt.day_name()
    
    # TODO: Calculate week-over-week growth
    # TODO: Aggregate by day of week
    
    return temporal_analysis
```

---

### Exercise 9: Build a Data Quality Dashboard

**Goal**: Create comprehensive data quality metrics.

**Tasks**:
Create a script that generates a data quality report with:
1. Completeness: Percentage of non-null values per column
2. Uniqueness: Percentage of unique values
3. Validity: Percentage passing business rules
4. Consistency: Checks across related columns

Save the report as `gold_data_quality_report.csv`.

---

### Exercise 10: Implement Slowly Changing Dimensions (SCD Type 2)

**Goal**: Track historical changes in customer data.

**Tasks**:
1. Modify customer data to track changes over time
2. Add columns: `effective_start_date`, `effective_end_date`, `is_current`
3. When a customer's city changes, keep both records
4. Implement logic to insert new record and close old record

**This simulates**:
- How to maintain historical data
- How to query "as of" a specific date
- How to track changes over time

---

## 🎯 Challenge Projects

### Challenge 1: Add Data Validation Framework

Create a reusable data validation framework with:
- Schema validation (column names, data types)
- Business rule validation (ranges, formats)
- Referential integrity checks (foreign keys)
- Automated test cases

### Challenge 2: Implement Incremental Loading

Modify the pipeline to support:
- Only load new/changed data (not full refresh)
- Track watermarks (last processed timestamp)
- Merge updates into existing data
- Handle deletions

### Challenge 3: Create a Data Lineage Tracker

Build a system that tracks:
- Source of each record (which raw file)
- Transformations applied to each record
- When each record was processed
- Version history of transformations

---

## 📊 Self-Assessment Checklist

After completing the exercises, you should be able to:

**Bronze Layer**:
- [ ] Explain why we preserve raw data
- [ ] Add ingestion metadata to source files
- [ ] Understand immutable data storage

**Silver Layer**:
- [ ] Identify data quality issues
- [ ] Apply cleaning transformations
- [ ] Handle missing values appropriately
- [ ] Remove duplicates correctly
- [ ] Standardize data formats

**Gold Layer**:
- [ ] Create business metrics from clean data
- [ ] Join multiple data sources
- [ ] Build aggregations for reporting
- [ ] Implement business logic
- [ ] Optimize for specific use cases

**General ELT Concepts**:
- [ ] Explain ELT vs ETL differences
- [ ] Understand when to use each layer
- [ ] Apply the Medallion Architecture
- [ ] Design data pipelines
- [ ] Document transformations

---

## 💡 Tips for Success

1. **Start Simple**: Begin with the beginner exercises and build up
2. **Test Frequently**: Run your code after each change
3. **Compare Results**: Check if your output makes business sense
4. **Document Everything**: Add comments explaining your logic
5. **Ask "Why"**: Understand the business reason for each transformation
6. **Review Examples**: Look at existing code for patterns

## 🆘 Need Help?

If you're stuck:
1. Re-read the relevant section in [ELT_CONCEPTS.md](ELT_CONCEPTS.md)
2. Look at similar code in the existing scripts
3. Print intermediate results to debug
4. Start with a smaller subset of data
5. Draw out the data flow on paper

Good luck with your learning journey! 🚀
