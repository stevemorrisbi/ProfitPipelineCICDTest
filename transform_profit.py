import pandas as pd
import argparse
from pathlib import Path

def add_profit_column(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path)
    df["profit"] = df["sale_price"] - df["purchase_price"]

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)
    print(f"Saved file with profit column to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    add_profit_column(args.input, args.output)
