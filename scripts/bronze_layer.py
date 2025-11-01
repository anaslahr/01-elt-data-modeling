"""
Bronze Layer - Raw Data Ingestion
==================================
The Bronze layer is the first layer in the ELT pipeline.
It loads raw data as-is from source systems without any transformations.

Purpose:
- Preserve raw data exactly as received from source
- Maintain data lineage and audit trail
- Allow for reprocessing if needed
- No data quality checks or transformations

Best Practices:
- Add ingestion timestamp
- Preserve original data types where possible
- Store data in its original format
- Maintain source system identifiers
"""

import pandas as pd
import os
from datetime import datetime


def ingest_to_bronze(source_path, destination_path, dataset_name):
    """
    Ingest raw data into Bronze layer.
    
    Args:
        source_path: Path to raw data file
        destination_path: Path to Bronze layer directory
        dataset_name: Name of the dataset
    """
    print(f"[Bronze Layer] Ingesting {dataset_name}...")
    
    # Read raw data
    df = pd.read_csv(source_path)
    
    # Add metadata columns
    df['_ingestion_timestamp'] = datetime.now()
    df['_source_file'] = os.path.basename(source_path)
    
    # Save to Bronze layer
    output_file = os.path.join(destination_path, f"bronze_{dataset_name}.csv")
    df.to_csv(output_file, index=False)
    
    print(f"[Bronze Layer] Successfully ingested {len(df)} records to {output_file}")
    return output_file


def main():
    """Main function to ingest all raw data files to Bronze layer."""
    
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data_path = os.path.join(base_path, "data", "raw_data")
    bronze_path = os.path.join(base_path, "data", "bronze")
    
    # Ensure Bronze directory exists
    os.makedirs(bronze_path, exist_ok=True)
    
    # List of datasets to ingest
    datasets = [
        ("sales_data.csv", "sales"),
        ("customer_data.csv", "customers"),
        ("product_data.csv", "products")
    ]
    
    print("=" * 60)
    print("BRONZE LAYER: RAW DATA INGESTION")
    print("=" * 60)
    
    # Ingest each dataset
    for filename, dataset_name in datasets:
        source_file = os.path.join(raw_data_path, filename)
        if os.path.exists(source_file):
            ingest_to_bronze(source_file, bronze_path, dataset_name)
        else:
            print(f"[Warning] File not found: {source_file}")
    
    print("\n[Bronze Layer] Ingestion complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
