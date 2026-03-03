import pandas as pd

def convert_csv_to_batch_request(file_path: str):
    df = pd.read_csv(file_path)

    # Just ensure price isn't there accidentally
    if "price" in df.columns:
        df = df.drop("price", axis=1)

    return {
        "houses": df.to_dict(orient="records")
    }