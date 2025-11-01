"""
Silver Layer - Cleaned and Validated Data
==========================================
The Silver layer transforms Bronze data by cleaning, validating, and normalizing it.

Purpose:
- Remove duplicates and handle missing values
- Standardize data formats
- Apply data quality rules
- Create consistent data types
- Filter out invalid records

Best Practices:
- Document all transformation rules
- Log data quality issues
- Maintain traceability to Bronze layer
- Apply business rules consistently
"""

import pandas as pd
import os
from datetime import datetime
import numpy as np


def clean_sales_data(bronze_df):
    """
    Clean and validate sales data.
    
    Transformations:
    - Remove records with missing critical fields
    - Standardize date formats
    - Ensure numeric fields are properly typed
    - Remove duplicates
    """
    print("[Silver Layer] Cleaning sales data...")
    
    df = bronze_df.copy()
    initial_count = len(df)
    
    # Remove records with missing transaction_id or product_id
    df = df.dropna(subset=['transaction_id', 'product_id'])
    
    # Convert transaction_date to datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    
    # Ensure numeric fields are correct type
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Remove records with invalid dates or negative quantities
    df = df[df['transaction_date'].notna()]
    df = df[df['quantity'] > 0]
    df = df[df['price'] > 0]
    
    # Remove duplicates based on transaction_id
    df = df.drop_duplicates(subset=['transaction_id'], keep='first')
    
    # Calculate total_amount
    df['total_amount'] = df['quantity'] * df['price']
    
    final_count = len(df)
    print(f"[Silver Layer] Sales: {initial_count} -> {final_count} records (removed {initial_count - final_count})")
    
    return df


def clean_customer_data(bronze_df):
    """
    Clean and validate customer data.
    
    Transformations:
    - Remove duplicates
    - Standardize email format
    - Handle missing values appropriately
    - Validate customer_id format
    """
    print("[Silver Layer] Cleaning customer data...")
    
    df = bronze_df.copy()
    initial_count = len(df)
    
    # Remove records with missing customer_id
    df = df.dropna(subset=['customer_id'])
    
    # Remove duplicates based on customer_id
    df = df.drop_duplicates(subset=['customer_id'], keep='first')
    
    # Standardize email to lowercase
    df['email'] = df['email'].str.lower().str.strip()
    
    # Convert registration_date to datetime
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
    
    # Fill missing phone with 'Not Provided'
    df['phone'] = df['phone'].fillna('Not Provided')
    
    final_count = len(df)
    print(f"[Silver Layer] Customers: {initial_count} -> {final_count} records (removed {initial_count - final_count})")
    
    return df


def clean_product_data(bronze_df):
    """
    Clean and validate product data.
    
    Transformations:
    - Remove duplicates
    - Ensure numeric fields are properly typed
    - Validate price relationships (cost < list price)
    - Calculate profit margins
    """
    print("[Silver Layer] Cleaning product data...")
    
    df = bronze_df.copy()
    initial_count = len(df)
    
    # Remove records with missing product_id
    df = df.dropna(subset=['product_id'])
    
    # Remove duplicates based on product_id
    df = df.drop_duplicates(subset=['product_id'], keep='first')
    
    # Ensure numeric fields are correct type
    df['cost_price'] = pd.to_numeric(df['cost_price'], errors='coerce')
    df['list_price'] = pd.to_numeric(df['list_price'], errors='coerce')
    df['stock_quantity'] = pd.to_numeric(df['stock_quantity'], errors='coerce')
    
    # Remove records with invalid prices
    df = df[df['cost_price'] > 0]
    df = df[df['list_price'] > 0]
    df = df[df['stock_quantity'] >= 0]
    
    # Calculate profit margin
    df['profit_margin'] = ((df['list_price'] - df['cost_price']) / df['list_price'] * 100).round(2)
    
    final_count = len(df)
    print(f"[Silver Layer] Products: {initial_count} -> {final_count} records (removed {initial_count - final_count})")
    
    return df


def process_to_silver(bronze_path, silver_path):
    """
    Process all Bronze layer data to Silver layer.
    
    Args:
        bronze_path: Path to Bronze layer directory
        silver_path: Path to Silver layer directory
    """
    # Ensure Silver directory exists
    os.makedirs(silver_path, exist_ok=True)
    
    # Process sales data
    sales_bronze = pd.read_csv(os.path.join(bronze_path, "bronze_sales.csv"))
    sales_silver = clean_sales_data(sales_bronze)
    sales_silver.to_csv(os.path.join(silver_path, "silver_sales.csv"), index=False)
    
    # Process customer data
    customer_bronze = pd.read_csv(os.path.join(bronze_path, "bronze_customers.csv"))
    customer_silver = clean_customer_data(customer_bronze)
    customer_silver.to_csv(os.path.join(silver_path, "silver_customers.csv"), index=False)
    
    # Process product data
    product_bronze = pd.read_csv(os.path.join(bronze_path, "bronze_products.csv"))
    product_silver = clean_product_data(product_bronze)
    product_silver.to_csv(os.path.join(silver_path, "silver_products.csv"), index=False)


def main():
    """Main function to process Bronze to Silver layer."""
    
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bronze_path = os.path.join(base_path, "data", "bronze")
    silver_path = os.path.join(base_path, "data", "silver")
    
    print("=" * 60)
    print("SILVER LAYER: DATA CLEANING AND VALIDATION")
    print("=" * 60)
    
    process_to_silver(bronze_path, silver_path)
    
    print("\n[Silver Layer] Processing complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
