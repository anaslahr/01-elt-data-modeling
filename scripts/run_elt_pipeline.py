"""
ELT Pipeline Runner
===================
This script runs the complete ELT pipeline: Bronze -> Silver -> Gold

Usage:
    python run_elt_pipeline.py
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bronze_layer import main as run_bronze
from silver_layer import main as run_silver
from gold_layer import main as run_gold


def main():
    """Run the complete ELT pipeline."""
    
    print("\n" + "=" * 60)
    print("STARTING ELT PIPELINE")
    print("=" * 60 + "\n")
    
    try:
        # Step 1: Bronze Layer (Raw Data Ingestion)
        print("\nSTEP 1: BRONZE LAYER")
        print("-" * 60)
        run_bronze()
        
        # Step 2: Silver Layer (Data Cleaning and Validation)
        print("\nSTEP 2: SILVER LAYER")
        print("-" * 60)
        run_silver()
        
        # Step 3: Gold Layer (Business Aggregations)
        print("\nSTEP 3: GOLD LAYER")
        print("-" * 60)
        run_gold()
        
        print("\n" + "=" * 60)
        print("ELT PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 60 + "\n")
        
        print("Output files created:")
        print("  Bronze Layer: data/bronze/")
        print("  Silver Layer: data/silver/")
        print("  Gold Layer:   data/gold/")
        print()
        
    except Exception as e:
        print(f"\n[ERROR] Pipeline failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
