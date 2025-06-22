CSV to Parquet Conversion using PySpark

This small project shows how I used Pyspark to conver a CSV file into Parquet format. It's a basic example but a good starting point if you're learning how to work with data using Spark and Python.

What is in the Repo
convert_to_parquet.py  -  A python script that reads a CSV file using PySpark and writes it out as a Parquet file.

Tools Used
- Python 3.10  
- PySpark  
- Java JDK 17  
- (On Windows) `winutils.exe` is needed to avoid permission errors with Hadoop
- 
How to Run the script
1. Make sure you have Java and PySpark installed.
2. Save a CSV file (like `people.csv`) in the same folder as the script.
3. Run the script with:
bash
python convert_to_parquet.py

