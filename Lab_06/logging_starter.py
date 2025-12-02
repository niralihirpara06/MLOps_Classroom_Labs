"""
Data Processing Pipeline - Logging Implementation with Real Data
Author: Nirali Hirpara
Date: December 1, 2025
Description: A practical logging system for an e-commerce data analytics pipeline
"""

import logging
import pandas as pd
import os
from datetime import datetime

# ============================================================================
# Section 1: Pipeline Configuration Setup
# ============================================================================
print("\n=== Section 1: Initializing Data Pipeline Logger ===")
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# ============================================================================
# Section 2: Data Pipeline Stages Logging
# ============================================================================
print("\n=== Section 2: Tracking Data Pipeline Stages ===")
logging.debug("Pipeline initialized - checking system resources")
logging.info("Starting data extraction from source database")

# Check if file exists
if os.path.exists('sales_data.csv'):
    file_size = os.path.getsize('sales_data.csv')
    if file_size > 1000:
        logging.warning(f"Dataset size is {file_size} bytes - processing may take longer")
    else:
        logging.info(f"Dataset size is {file_size} bytes - optimal for processing")
else:
    logging.critical("sales_data.csv not found - pipeline cannot proceed")
    exit(1)


# ============================================================================
# Section 3: Module-Specific Loggers for Data Loading
# ============================================================================
print("\n=== Section 3: Loading Data with Component-Specific Loggers ===")
data_loader = logging.getLogger("DataLoader")
data_cleaner = logging.getLogger("DataCleaner")
analytics_engine = logging.getLogger("AnalyticsEngine")

# Actually load the data
try:
    data_loader.debug("Connecting to sales data file...")
    df = pd.read_csv('sales_data.csv')
    data_loader.info(f"Successfully loaded {len(df)} sales records from CSV")
    data_loader.info(f"Dataset contains columns: {list(df.columns)}")
except Exception as e:
    data_loader.error(f"Failed to load data file: {str(e)}")
    exit(1)


# ============================================================================
# Section 4: Data Quality Checks and Error Handling
# ============================================================================
print("\n=== Section 4: Performing Data Quality Checks ===")

# Check for missing values
missing_data = df.isnull().sum()
for column, count in missing_data.items():
    if count > 0:
        data_cleaner.warning(f"Found {count} missing values in column '{column}'")
    else:
        data_cleaner.debug(f"Column '{column}' has no missing values")

# Check for duplicate customers
try:
    duplicate_customers = df[df['customer_name'].notna()]['customer_name'].duplicated().sum()
    if duplicate_customers > 0:
        data_cleaner.info(f"Identified {duplicate_customers} repeat customers in dataset")
except Exception as e:
    data_cleaner.exception("Error while checking for duplicate customers")


# ============================================================================
# Section 5: Pipeline Activity Log File
# ============================================================================
print("\n=== Section 5: Creating Detailed Pipeline Activity Log ===")
pipeline_logger = logging.getLogger("PipelineMonitor")
pipeline_logger.setLevel(logging.DEBUG)

# Create handler for pipeline log file
pipeline_handler = logging.FileHandler('pipeline_activity.log')
pipeline_handler.setLevel(logging.DEBUG)

# Custom format for pipeline logs
pipeline_format = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
pipeline_handler.setFormatter(pipeline_format)
pipeline_logger.addHandler(pipeline_handler)

# Log data cleaning activities
pipeline_logger.debug("Starting data validation checks")
pipeline_logger.info(f"Original dataset shape: {df.shape}")

# Clean the data and log the process
original_rows = len(df)
df_clean = df.dropna(subset=['customer_name', 'product', 'price']).copy()
cleaned_rows = len(df_clean)
rows_removed = original_rows - cleaned_rows

if rows_removed > 0:
    pipeline_logger.warning(f"Removed {rows_removed} rows with missing critical data")
else:
    pipeline_logger.info("No rows removed - dataset is complete")

pipeline_logger.info(f"Cleaned dataset shape: {df_clean.shape}")
print("Check 'pipeline_activity.log' for detailed cleaning steps")


# ============================================================================
# Section 6: Environment-Based Analytics Logging
# ============================================================================
print("\n=== Section 6: Running Analytics with Environment-Specific Logging ===")
production_logger = logging.getLogger("ProductionAnalytics")
production_logger.setLevel(logging.WARNING)

prod_handler = logging.StreamHandler()
prod_handler.setFormatter(pipeline_format)
production_logger.addHandler(prod_handler)

# Perform actual analytics
try:
    total_revenue = (df_clean['quantity'] * df_clean['price']).sum()
    avg_order_value = total_revenue / len(df_clean)
    
    production_logger.debug(f"Revenue calculation details - won't show")
    production_logger.info(f"Total Revenue: ${total_revenue:.2f} - won't show")
    
    # Check for anomalies
    if avg_order_value < 100:
        production_logger.warning(f"Average order value ${avg_order_value:.2f} is below target")
    
    if total_revenue < 5000:
        production_logger.error(f"Total revenue ${total_revenue:.2f} below monthly threshold")
        
except Exception as e:
    production_logger.error(f"Analytics calculation failed: {str(e)}")


# ============================================================================
# Section 7: Multi-Destination Logging for ETL Process
# ============================================================================
print("\n=== Section 7: ETL Process with Dual Logging ===")
etl_logger = logging.getLogger("ETL_Process")
etl_logger.setLevel(logging.DEBUG)

# Console handler
console_output = logging.StreamHandler()
console_output.setLevel(logging.INFO)
console_output.setFormatter(pipeline_format)

# File handler
audit_file = logging.FileHandler('pipeline_activity.log')
audit_file.setLevel(logging.DEBUG)
audit_file.setFormatter(pipeline_format)

# Attach both handlers
etl_logger.addHandler(console_output)
etl_logger.addHandler(audit_file)

# Perform transformations
etl_logger.debug("Starting data transformation phase")

# Add calculated column
df_clean['total_amount'] = df_clean['quantity'] * df_clean['price']
etl_logger.info("Created 'total_amount' calculated column")

# Group by region
region_sales = df_clean.groupby('region')['total_amount'].sum()
etl_logger.info(f"Aggregated sales by region: {len(region_sales)} regions analyzed")

for region, sales in region_sales.items():
    etl_logger.debug(f"{region} region total sales: ${sales:.2f}")

# Find best-selling product
product_sales = df_clean.groupby('product')['quantity'].sum().sort_values(ascending=False)
top_product = product_sales.index[0]
top_quantity = product_sales.iloc[0]
etl_logger.info(f"Best-selling product: {top_product} with {top_quantity} units sold")


# ============================================================================
# Section 8: Advanced Error Tracking with Real Scenarios
# ============================================================================
print("\n=== Section 8: Handling Real Data Processing Errors ===")

# Scenario 1: Try to process invalid numeric data
try:
    # Attempt to calculate statistics on potentially corrupted data
    invalid_prices = df[df['price'].isna()]
    if len(invalid_prices) > 0:
        etl_logger.error(f"Cannot process {len(invalid_prices)} orders with missing prices")
        raise ValueError(f"Found {len(invalid_prices)} records with invalid price data")
except ValueError:
    etl_logger.exception("Price validation failed during revenue calculation")

# Scenario 2: Try to access non-existent backup file
try:
    backup_df = pd.read_csv("backup_sales_data.csv")
    etl_logger.info("Successfully loaded backup data")
except FileNotFoundError:
    etl_logger.exception("Backup data file not found - proceeding with primary dataset only")


# ============================================================================
# Section 9: Generate Summary Report
# ============================================================================
print("\n=== Section 9: Pipeline Summary ===")
analytics_engine.info("="*60)
analytics_engine.info("DATA PIPELINE EXECUTION SUMMARY")
analytics_engine.info("="*60)
analytics_engine.info(f"Records Processed: {len(df_clean)}/{len(df)}")
analytics_engine.info(f"Total Revenue: ${total_revenue:.2f}")
analytics_engine.info(f"Average Order Value: ${avg_order_value:.2f}")
analytics_engine.info(f"Top Product: {top_product}")
analytics_engine.info(f"Regions Analyzed: {len(region_sales)}")
analytics_engine.info("="*60)

print("\n✅ Data Pipeline Logging Demonstration Complete")
print("📊 Check 'pipeline_activity.log' for complete audit trail")