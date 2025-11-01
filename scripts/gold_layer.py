"""
Gold Layer - Business-Ready Aggregated Data
============================================
The Gold layer creates business-ready datasets optimized for analytics and reporting.

Purpose:
- Aggregate data for business metrics
- Join data from multiple sources
- Create dimension and fact tables
- Optimize for query performance
- Implement business logic

Best Practices:
- Design for specific business use cases
- Create pre-aggregated metrics
- Implement star/snowflake schemas
- Document business logic clearly
- Optimize for reporting tools
"""

import pandas as pd
import os
from datetime import datetime


def create_sales_summary(sales_df, products_df):
    """
    Create aggregated sales summary by product category.
    
    Business metrics:
    - Total revenue by category
    - Total units sold by category
    - Average transaction value
    - Number of transactions
    """
    print("[Gold Layer] Creating sales summary...")
    
    # Join sales with products to get category
    sales_with_products = sales_df.merge(
        products_df[['product_id', 'category', 'product_name']], 
        on='product_id', 
        how='left'
    )
    
    # Aggregate by category
    summary = sales_with_products.groupby('category').agg({
        'total_amount': 'sum',
        'quantity': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    
    summary.columns = ['category', 'total_revenue', 'total_units_sold', 'number_of_transactions']
    summary['avg_transaction_value'] = (summary['total_revenue'] / summary['number_of_transactions']).round(2)
    
    # Sort by revenue
    summary = summary.sort_values('total_revenue', ascending=False)
    
    print(f"[Gold Layer] Created sales summary with {len(summary)} categories")
    return summary


def create_customer_metrics(sales_df, customers_df):
    """
    Create customer-level metrics and segmentation.
    
    Business metrics:
    - Customer lifetime value
    - Number of purchases
    - Average order value
    - Total amount spent
    """
    print("[Gold Layer] Creating customer metrics...")
    
    # Aggregate sales by customer
    customer_sales = sales_df.groupby('customer_id').agg({
        'total_amount': ['sum', 'mean'],
        'transaction_id': 'count'
    }).reset_index()
    
    customer_sales.columns = ['customer_id', 'total_spent', 'avg_order_value', 'number_of_purchases']
    customer_sales['avg_order_value'] = customer_sales['avg_order_value'].round(2)
    customer_sales['total_spent'] = customer_sales['total_spent'].round(2)
    
    # Join with customer data
    customer_metrics = customers_df.merge(customer_sales, on='customer_id', how='left')
    
    # Fill NaN values for customers with no purchases
    customer_metrics['total_spent'] = customer_metrics['total_spent'].fillna(0)
    customer_metrics['avg_order_value'] = customer_metrics['avg_order_value'].fillna(0)
    customer_metrics['number_of_purchases'] = customer_metrics['number_of_purchases'].fillna(0).astype(int)
    
    # Create customer segment based on spending
    def categorize_customer(total_spent):
        if total_spent >= 1000:
            return 'High Value'
        elif total_spent >= 500:
            return 'Medium Value'
        elif total_spent > 0:
            return 'Low Value'
        else:
            return 'No Purchases'
    
    customer_metrics['customer_segment'] = customer_metrics['total_spent'].apply(categorize_customer)
    
    print(f"[Gold Layer] Created metrics for {len(customer_metrics)} customers")
    return customer_metrics


def create_product_performance(sales_df, products_df):
    """
    Create product performance metrics.
    
    Business metrics:
    - Revenue by product
    - Units sold by product
    - Profit margins
    - Product rankings
    """
    print("[Gold Layer] Creating product performance metrics...")
    
    # Aggregate sales by product
    product_sales = sales_df.groupby('product_id').agg({
        'total_amount': 'sum',
        'quantity': 'sum',
        'transaction_id': 'count'
    }).reset_index()
    
    product_sales.columns = ['product_id', 'total_revenue', 'units_sold', 'number_of_transactions']
    
    # Join with product data
    product_performance = products_df.merge(product_sales, on='product_id', how='left')
    
    # Fill NaN values for products with no sales
    product_performance['total_revenue'] = product_performance['total_revenue'].fillna(0)
    product_performance['units_sold'] = product_performance['units_sold'].fillna(0).astype(int)
    product_performance['number_of_transactions'] = product_performance['number_of_transactions'].fillna(0).astype(int)
    
    # Calculate total profit
    product_performance['total_profit'] = (
        (product_performance['list_price'] - product_performance['cost_price']) * 
        product_performance['units_sold']
    ).round(2)
    
    # Add performance rank
    product_performance['revenue_rank'] = product_performance['total_revenue'].rank(ascending=False, method='dense').astype(int)
    
    # Sort by revenue
    product_performance = product_performance.sort_values('total_revenue', ascending=False)
    
    print(f"[Gold Layer] Created performance metrics for {len(product_performance)} products")
    return product_performance


def create_daily_sales_trend(sales_df):
    """
    Create daily sales trend for time-series analysis.
    
    Business metrics:
    - Daily revenue
    - Daily transaction count
    - Daily average order value
    """
    print("[Gold Layer] Creating daily sales trend...")
    
    # Extract date from transaction_date
    sales_df['date'] = pd.to_datetime(sales_df['transaction_date']).dt.date
    
    # Aggregate by date
    daily_sales = sales_df.groupby('date').agg({
        'total_amount': 'sum',
        'transaction_id': 'count',
        'quantity': 'sum'
    }).reset_index()
    
    daily_sales.columns = ['date', 'daily_revenue', 'daily_transactions', 'daily_units_sold']
    daily_sales['avg_order_value'] = (daily_sales['daily_revenue'] / daily_sales['daily_transactions']).round(2)
    
    print(f"[Gold Layer] Created daily trend for {len(daily_sales)} days")
    return daily_sales


def process_to_gold(silver_path, gold_path):
    """
    Process Silver layer data to Gold layer.
    
    Args:
        silver_path: Path to Silver layer directory
        gold_path: Path to Gold layer directory
    """
    # Ensure Gold directory exists
    os.makedirs(gold_path, exist_ok=True)
    
    # Load Silver layer data
    print("[Gold Layer] Loading Silver layer data...")
    sales_df = pd.read_csv(os.path.join(silver_path, "silver_sales.csv"))
    customers_df = pd.read_csv(os.path.join(silver_path, "silver_customers.csv"))
    products_df = pd.read_csv(os.path.join(silver_path, "silver_products.csv"))
    
    # Create Gold layer tables
    sales_summary = create_sales_summary(sales_df, products_df)
    sales_summary.to_csv(os.path.join(gold_path, "gold_sales_summary.csv"), index=False)
    
    customer_metrics = create_customer_metrics(sales_df, customers_df)
    customer_metrics.to_csv(os.path.join(gold_path, "gold_customer_metrics.csv"), index=False)
    
    product_performance = create_product_performance(sales_df, products_df)
    product_performance.to_csv(os.path.join(gold_path, "gold_product_performance.csv"), index=False)
    
    daily_sales = create_daily_sales_trend(sales_df)
    daily_sales.to_csv(os.path.join(gold_path, "gold_daily_sales_trend.csv"), index=False)


def main():
    """Main function to process Silver to Gold layer."""
    
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    silver_path = os.path.join(base_path, "data", "silver")
    gold_path = os.path.join(base_path, "data", "gold")
    
    print("=" * 60)
    print("GOLD LAYER: BUSINESS-READY AGGREGATIONS")
    print("=" * 60)
    
    process_to_gold(silver_path, gold_path)
    
    print("\n[Gold Layer] Processing complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
