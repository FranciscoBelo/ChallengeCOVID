# Data Pipeline Architecture

## GitHub View (Mermaid Diagram)
```mermaid
flowchart LR
    A[Synapse Pipeline] --> B[Databricks Job]
    B --> C[Reconciliation Notebook]
    C --> D[(dv_reconciliation_log)]
    C --> E[(dv_reconciliation_log_keys)]
    C --> F[(dv_reconciliation_log_attributes)]
    C --> G[(dv_reconciliation_log_attributes_summary)]
    D & E & F & G --> H[Power BI Dashboard]
```

## Databricks View (Image)
For Databricks notebooks, use the following image:

![Pipeline Diagram](pipeline_diagram.png)

### Using in Databricks Notebooks
To use this diagram in Databricks markdown cells, you have two options:

**Option 1: Upload to DBFS**
1. Upload `pipeline_diagram.png` to DBFS (e.g., `/FileStore/images/pipeline_diagram.png`)
2. Reference it in your markdown cell:
   ```
   ![Pipeline Diagram](/files/images/pipeline_diagram.png)
   ```

**Option 2: Use from Repository**
1. If your notebook is synced with this GitHub repository
2. Reference the image directly:
   ```
   ![Pipeline Diagram](pipeline_diagram.png)
   ```
