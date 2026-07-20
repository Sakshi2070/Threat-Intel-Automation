import os
import pandas as pd

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

def export_csv(data, filename):
    """
    Export a list of dictionaries to a CSV file.
    """
    df = pd.DataFrame(data)

    output_path = f"reports/{filename}"

    df.to_csv(output_path, index=False)

    print(f"✓ Created {output_path}")

    return df

