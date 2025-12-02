# Lab 06: Python Logging Implementation

## 📋 Overview
This lab demonstrates a comprehensive implementation of Python's logging library in the context of a real-world e-commerce data analytics pipeline. The project showcases various logging techniques including basic configuration, custom loggers, file handlers, exception tracking, and multi-destination logging.

## 📁 Project Structure
```
Lab_06/
│
├── logging_starter.py          # Main Python script with logging implementation
├── sales_data.csv              # Sample e-commerce dataset (15 records)
├── pipeline_activity.log       # Auto-generated log file (audit trail)
└── README.md                   # Project documentation
```

## 🎯 Learning Objectives
This lab covers the following Python logging concepts:

1. **Basic Logging Configuration** - Setting up logging levels and formats
2. **Log Levels** - DEBUG, INFO, WARNING, ERROR, CRITICAL
3. **Custom Loggers** - Module-specific logger instances
4. **File Logging** - Writing logs to external files
5. **Log Handlers** - Multiple output destinations (console + file)
6. **Exception Logging** - Capturing and logging errors with tracebacks
7. **Log Level Control** - Environment-specific logging configurations
8. **Real-world Application** - Data pipeline monitoring and debugging


## 📊 Dataset Description
The `sales_data.csv` file contains e-commerce transaction data with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| order_id | Integer | Unique order identifier |
| customer_name | String | Customer name |
| product | String | Product name |
| quantity | Integer | Number of units ordered |
| price | Float | Unit price in USD |
| order_date | Date | Order placement date |
| region | String | Geographic region (North/South/East/West) |

**Data Quality Issues (Intentional):**
- Missing customer names (1 record)
- Missing product names (1 record)
- Missing prices (1 record)

These data quality issues are intentionally included to demonstrate error handling and logging capabilities.

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas
```

### Execution
```bash
python logging_starter.py
```

### Expected Output
The script will:
1. Display progress messages in the console
2. Generate a `pipeline_activity.log` file
3. Show a summary report with analytics results

## 📈 Features Implemented

### Section 1: Pipeline Configuration
- Initializes logging with custom format
- Sets logging level to DEBUG for comprehensive tracking

### Section 2: Data Pipeline Stages
- Logs system resource checks
- Validates file existence and size
- Tracks data extraction process

### Section 3: Component-Specific Loggers
- **DataLoader**: Handles CSV file loading
- **DataCleaner**: Manages data quality checks
- **AnalyticsEngine**: Performs business analytics

### Section 4: Data Quality Checks
- Identifies missing values across all columns
- Detects duplicate customer records
- Logs warnings for data quality issues

### Section 5: Pipeline Activity Log
- Creates dedicated log file for audit trail
- Tracks data cleaning operations
- Records before/after dataset shapes

### Section 6: Environment-Based Logging
- Simulates production environment settings
- Filters logs by severity (WARNING and above)
- Monitors performance thresholds

### Section 7: ETL Process with Dual Logging
- Logs to both console and file simultaneously
- Creates calculated columns (total_amount)
- Performs regional sales aggregation
- Identifies best-selling products

### Section 8: Advanced Error Handling
- **ValueError**: Handles invalid price data
- **FileNotFoundError**: Manages missing backup files
- Logs full exception tracebacks for debugging

### Section 9: Summary Report
- Total records processed: 12/15
- Revenue calculations
- Average order value
- Top-selling product identification
- Regional analysis summary

## 📊 Sample Output

### Console Output
```
=== Section 9: Pipeline Summary ===
============================================================
DATA PIPELINE EXECUTION SUMMARY
============================================================
Records Processed: 12/15
Total Revenue: $3399.83
Average Order Value: $283.32
Top Product: Mouse
Regions Analyzed: 4
============================================================
```

### Log File Sample
```
2025-12-01 20:35:49 | DataLoader | INFO | Successfully loaded 15 sales records from CSV
2025-12-01 20:35:49 | DataCleaner | WARNING | Found 1 missing values in column 'price'
2025-12-01 20:35:49 | PipelineMonitor | WARNING | Removed 3 rows with missing critical data
2025-12-01 20:35:49 | ETL_Process | INFO | Best-selling product: Mouse with 10 units sold
```

## 🔍 Key Logging Features

### Log Format
```
%(asctime)s | %(name)s | %(levelname)s | %(message)s
```

### Log Levels Used
- **DEBUG**: Detailed diagnostic information
- **INFO**: General informational messages
- **WARNING**: Potential issues or anomalies
- **ERROR**: Errors that don't stop execution
- **CRITICAL**: Severe errors (would halt pipeline)

### Handlers Implemented
1. **Console Handler** (StreamHandler): Real-time feedback
2. **File Handler** (FileHandler): Persistent audit trail

## 📝 Business Insights Generated

### Analytics Results
- **Total Revenue**: $3,399.83
- **Average Order Value**: $283.32
- **Best-Selling Product**: Mouse (10 units)
- **Regional Performance**:
  - North: $1,403.98
  - West: $1,319.98
  - South: $600.87
  - East: $75.00

### Data Quality Findings
- **15 total records** in source data
- **3 records removed** due to missing critical fields
- **12 clean records** used for analysis
- **4 repeat customers** identified

## 🛠️ Error Handling Scenarios

1. **Missing Price Data**
   - Error Type: `ValueError`
   - Impact: 1 order cannot be processed
   - Action: Logged with full traceback

2. **Backup File Not Found**
   - Error Type: `FileNotFoundError`
   - Impact: Cannot load backup data
   - Action: Logged and proceeded with primary dataset

## 📚 Lessons Learned

1. **Structured Logging**: Using different log levels helps filter information based on importance
2. **Module-Specific Loggers**: Creates clear separation of concerns in complex applications
3. **Exception Tracking**: Comprehensive error logging aids in debugging and maintenance
4. **Audit Trails**: File logging provides permanent records for compliance and troubleshooting
5. **Production Readiness**: Environment-based log levels ensure optimal performance