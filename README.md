# Retail Data Quality Pipeline (Azure ADF + FastAPI + Power BI)

This repository contains an Azure Data Factory–centric data quality pipeline
for the **Retail Store Sales: Dirty for Data Cleaning** dataset.

High-level stages:

- Ingest raw retail sales CSV into Azure Data Lake (raw zone)
- Cleanse & validate via ADF Mapping Data Flows + FastAPI
- Quarantine invalid rows with error codes
- Load curated data into Azure SQL
- Visualise data quality in Power BI
