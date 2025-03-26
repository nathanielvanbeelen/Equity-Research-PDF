import pandas as pd

def read_excel_file(file_path="test_module3.xlsx", sheet_name="Sheet1"):
    """Read Excel file into DataFrame and return it."""
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    df = read_excel_file()
    
    if df is not None:
        print("\nDataFrame Contents:")
        print(df)