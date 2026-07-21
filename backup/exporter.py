import os
import pandas as pd

os.makedirs("reports", exist_ok=True)


def export_csv(data, filename):

    df = pd.DataFrame(data)

    output = f"reports/{filename}"

    df.to_csv(output, index=False)

    print(f"✓ Created {output}")

    return df

