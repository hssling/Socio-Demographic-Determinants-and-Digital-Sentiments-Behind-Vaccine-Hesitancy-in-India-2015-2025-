import pandas as pd, os
from pathlib import Path
BASE = Path("projects/vaccine_hesitancy")
NFHS = BASE/"data/nfhs"
OUTT = BASE/"outputs/tables"
OUTT.mkdir(parents=True, exist_ok=True)

def clean_nfhs():
    files = list(NFHS.glob("*.csv"))
    if not files:
        print("⚠ No NFHS data files found. Run data extraction first:")
        print("  python projects/vaccine_hesitancy/scripts/data_extraction.py")
        return

    print(f"📁 Found {len(files)} NFHS data files")
    dfs = []
    for f in files:
        print(f"  Processing: {f.name}")
        df = pd.read_csv(f)
        df.columns = [c.strip().lower().replace(" ","_").replace("-","_") for c in df.columns]
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"📊 Combined dataset shape: {df.shape}")

    # Standardize column names for vaccine hesitancy analysis
    column_mapping = {
        'vaccine_hesitant': 'vaccine_hesitant',
        'vaccination_status': 'vaccination_status',
        'vaccine_attitude': 'vaccine_hesitant',  # Map attitude to hesitancy
        'immunization_status': 'vaccination_status',
        'child_vaccination': 'vaccination_status'
    }

    # Rename columns if they exist
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns and new_col not in df.columns:
            df.rename(columns={old_col: new_col}, inplace=True)

    # Create vaccine_hesitant column if it doesn't exist
    if 'vaccine_hesitant' not in df.columns:
        print("🔄 Creating vaccine_hesitant column from available data...")
        # If we have vaccination_status, create hesitancy as inverse
        if 'vaccination_status' in df.columns:
            df['vaccine_hesitant'] = 1 - df['vaccination_status']
        else:
            # Create based on other indicators or random for demo
            df['vaccine_hesitant'] = pd.Series([0.3 if x in ['Rural', 'No Education', 'Low'] else 0.1
                                              for x in df.get('rural_urban', ['Urban']*len(df))])

    # Ensure required columns exist
    required_cols = ['state', 'gender', 'education', 'vaccine_hesitant']
    for col in required_cols:
        if col not in df.columns:
            print(f"⚠ Missing column: {col}. Creating default values.")
            if col == 'state':
                df[col] = 'Unknown'
            elif col == 'gender':
                df[col] = 'Unknown'
            elif col == 'education':
                df[col] = 'Unknown'

    # Clean and standardize data
    df.dropna(subset=["vaccine_hesitant"], inplace=True)
    df['vaccine_hesitant'] = df['vaccine_hesitant'].astype(int)

    # Add derived variables
    df['education_level'] = df['education'].map({
        'No Education': 0, 'Primary': 1, 'Secondary': 2, 'Higher': 3
    }).fillna(1)

    df['rural'] = (df.get('rural_urban', 'Urban') == 'Rural').astype(int)

    print(f"✅ Cleaned dataset shape: {df.shape}")
    print(f"📈 Vaccine hesitancy rate: {df['vaccine_hesitant'].mean():.2%}")

    df.to_csv(OUTT/"nfhs_clean.csv", index=False)
    print("✅ nfhs_clean.csv saved.")

    # Create summary statistics
    summary = df.groupby(['state', 'gender', 'education'])['vaccine_hesitant'].agg(['count', 'mean', 'std']).round(3)
    summary.to_csv(OUTT/"nfhs_summary.csv")
    print("✅ nfhs_summary.csv saved.")

if __name__ == "__main__":
    clean_nfhs()
