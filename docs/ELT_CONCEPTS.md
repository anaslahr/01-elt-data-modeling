# ELT Data Modeling Concepts

## What is ELT?

**ELT** stands for **Extract, Load, Transform**. It's a modern data integration pattern where:

1. **Extract**: Data is extracted from source systems
2. **Load**: Raw data is loaded directly into the data warehouse/lake
3. **Transform**: Data is transformed within the warehouse using SQL/Python

### ELT vs ETL

| Aspect | ETL (Traditional) | ELT (Modern) |
|--------|-------------------|--------------|
| Transform Location | Before loading (staging area) | After loading (in warehouse) |
| Best For | Structured data, limited storage | Big data, cloud warehouses |
| Flexibility | Less flexible | Highly flexible |
| Speed | Slower initial load | Faster initial load |
| Cost | Higher processing costs | Lower with cloud computing |

## The Medallion Architecture: Bronze, Silver, Gold

The **Medallion Architecture** (also called Multi-Hop Architecture) organizes data into three layers of increasing quality and refinement.

### 🥉 Bronze Layer (Raw Data)

**Purpose**: Store raw data exactly as received from source systems.

**Characteristics**:
- Data "as-is" from source
- No transformations applied
- Includes all records (good and bad)
- Append-only (immutable)
- Includes ingestion metadata

**Use Cases**:
- Data audit trail
- Reprocessing if needed
- Historical data preservation
- Compliance and governance

**Example**:
```python
# Raw sales data
transaction_id,customer_id,price,date
TXN001,CUST123,1200.00,2024-01-15
TXN002,,25.50,2024-01-15  # Missing customer_id
```

### 🥈 Silver Layer (Cleaned Data)

**Purpose**: Cleaned, validated, and deduplicated data ready for analysis.

**Characteristics**:
- Data quality rules applied
- Duplicates removed
- Missing values handled
- Standardized formats
- Type conversions
- Basic business rules

**Transformations**:
- Remove invalid records
- Standardize date/time formats
- Normalize text (lowercase, trim)
- Handle NULL values
- Convert data types
- Remove duplicates

**Use Cases**:
- Data science and ML
- Exploratory analysis
- Joining multiple sources
- Enterprise-wide datasets

**Example**:
```python
# Cleaned sales data
transaction_id,customer_id,price,date,total_amount
TXN001,CUST123,1200.00,2024-01-15,1200.00
# Invalid record removed
```

### 🥇 Gold Layer (Business-Ready Data)

**Purpose**: Highly refined, aggregated data optimized for specific business use cases.

**Characteristics**:
- Business logic applied
- Pre-aggregated metrics
- Dimension and fact tables
- Optimized for queries
- Use-case specific

**Transformations**:
- Join multiple sources
- Calculate KPIs
- Create aggregations
- Implement business rules
- Build star/snowflake schemas

**Use Cases**:
- BI dashboards
- Executive reports
- Customer-facing analytics
- Operational reports

**Example**:
```python
# Sales summary by category
category,total_revenue,total_units_sold,avg_transaction_value
Electronics,3900.00,4,975.00
Accessories,232.50,9,25.83
```

## Data Flow Diagram

```
Source Systems
    │
    ├─> [EXTRACT] ─> Raw Files
    │                    │
    │                    ├─> [LOAD: Bronze Layer]
    │                    │    • Raw data ingestion
    │                    │    • No transformations
    │                    │    • Add metadata
    │                    │
    │                    ├─> [TRANSFORM: Silver Layer]
    │                    │    • Data cleaning
    │                    │    • Validation
    │                    │    • Deduplication
    │                    │
    │                    └─> [TRANSFORM: Gold Layer]
    │                         • Aggregations
    │                         • Business logic
    │                         • KPIs
    │
    └─> BI Tools / Reports / ML Models
```

## Best Practices

### Bronze Layer
1. ✅ Keep data in its original format
2. ✅ Add ingestion timestamp and source identifier
3. ✅ Never modify or delete Bronze data
4. ✅ Make it append-only for audit trail
5. ❌ Don't apply transformations or filters

### Silver Layer
1. ✅ Document all cleaning rules
2. ✅ Log rejected records for investigation
3. ✅ Standardize naming conventions
4. ✅ Apply consistent data types
5. ❌ Don't delete Bronze data after processing

### Gold Layer
1. ✅ Design for specific business questions
2. ✅ Pre-aggregate for performance
3. ✅ Document business logic clearly
4. ✅ Create separate tables for different use cases
5. ❌ Don't over-aggregate; maintain flexibility

## When to Use Each Layer

### Use Bronze When:
- You need the original raw data
- Auditing or compliance requirements
- Need to reprocess data
- Want to preserve data lineage

### Use Silver When:
- Doing data science or ML
- Need clean, consistent data
- Joining multiple data sources
- Exploratory data analysis

### Use Gold When:
- Creating BI dashboards
- Generating reports
- Need specific business metrics
- Optimizing query performance

## Common Patterns

### Incremental Loading
```python
# Load only new data since last run
last_run = get_last_run_timestamp()
new_data = load_data_since(last_run)
```

### Change Data Capture (CDC)
```python
# Track changes (inserts, updates, deletes)
track_changes(operation='INSERT', timestamp=now())
```

### Slowly Changing Dimensions (SCD)
```python
# Track historical changes in dimension tables
# Type 2: Keep full history with effective dates
```

## References and Further Reading

- [Databricks Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)
- [Data Lake vs Data Warehouse](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/)
- [Modern Data Stack](https://www.getdbt.com/modern-data-stack/)
