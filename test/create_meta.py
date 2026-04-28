import pandas as pd

def get_csv_metadata(file_path):
    df = pd.read_csv(file_path)
    schema = []
    
    for col in df.columns:
        schema.append({
            "name": col,
            "type": str(df[col].dtype),
            "not_null": not df[col].isnull().any(),
            "unique_values": df[col].nunique(),
            "examples": df[col].dropna().unique()[:3].tolist()
        })
    
    return {
        "filename": file_path,
        "rows": len(df),
        "schema": schema
    }
