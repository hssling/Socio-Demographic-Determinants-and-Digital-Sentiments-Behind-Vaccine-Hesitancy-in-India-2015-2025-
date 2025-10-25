import pandas as pd, statsmodels.api as sm
from pathlib import Path
import numpy as np

BASE = Path("projects/vaccine_hesitancy")
TABS = BASE/"outputs/tables"
OUTR = BASE/"outputs/reports"
OUTR.mkdir(parents=True, exist_ok=True)

def analyze_vaccine_hesitancy():
    """Analyze factors associated with vaccine hesitancy"""
    try:
        df = pd.read_csv(TABS/"nfhs_clean.csv")
        print(f"📊 Analyzing {len(df)} records for vaccine hesitancy factors")
    except FileNotFoundError:
        print("⚠ NFHS clean data not found. Run data cleaning first:")
        print("  python projects/vaccine_hesitancy/scripts/clean_data.py")
        return

    # Prepare features for analysis
    features = []

    # Demographic factors
    if "gender" in df.columns:
        features.append("gender")
    if "education_level" in df.columns:
        features.append("education_level")
    elif "education" in df.columns:
        features.append("education")
    if "rural" in df.columns:
        features.append("rural")
    if "age" in df.columns:
        features.append("age")
    if "religion" in df.columns:
        features.append("religion")
    if "wealth_index" in df.columns:
        features.append("wealth_index")

    if not features:
        print("⚠ No suitable features found for analysis")
        return

    print(f"🔍 Analyzing factors: {features}")

    # Create feature matrix
    X = df[features].copy()

    # Handle categorical variables
    categorical_cols = []
    for col in features:
        if df[col].dtype == 'object' or len(df[col].unique()) < 20:
            categorical_cols.append(col)

    # One-hot encode categorical variables
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    # Ensure all columns are numeric
    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = pd.to_numeric(X[col], errors='coerce')

    # Drop columns with all NaN
    X = X.dropna(axis=1, how='all')

    # Add constant for intercept
    X = sm.add_constant(X)

    # Target variable
    y = df["vaccine_hesitant"]

    # Remove any rows with missing values
    valid_idx = X.dropna().index
    X = X.loc[valid_idx]
    y = y.loc[valid_idx]

    if len(X) < 50:
        print("⚠ Insufficient data for regression analysis")
        return

    print(f"📈 Running logistic regression with {len(X)} observations and {len(X.columns)} features")

    # Fit logistic regression
    try:
        model = sm.Logit(y, X).fit(disp=False)

        # Save detailed results
        with open(OUTR/"logit_summary.txt", "w") as f:
            f.write("VACCINE HESITANCY LOGISTIC REGRESSION ANALYSIS\n")
            f.write("="*50 + "\n\n")
            f.write(f"Sample size: {len(X)}\n")
            f.write(f"Features: {list(X.columns)}\n")
            f.write(f"Hesitancy rate: {y.mean():.3f}\n\n")
            f.write(model.summary().as_text())

        # Save odds ratios
        odds_ratios = np.exp(model.params)
        conf_int = np.exp(model.conf_int())

        results_df = pd.DataFrame({
            'coefficient': model.params,
            'odds_ratio': odds_ratios,
            'conf_int_lower': conf_int[0],
            'conf_int_upper': conf_int[1],
            'p_value': model.pvalues
        })

        results_df.to_csv(OUTR/"logit_odds_ratios.csv")
        print("✅ Odds ratios saved to reports/logit_odds_ratios.csv")

        # Create feature importance plot data
        feature_importance = results_df.abs().sort_values('coefficient', ascending=False)
        feature_importance.to_csv(OUTR/"feature_importance.csv")
        print("✅ Feature importance saved to reports/feature_importance.csv")

        print(f"🎯 Model AIC: {model.aic:.2f}")
        print(f"📊 Pseudo R-squared: {model.prsquared:.3f}")

        # Interpret key findings
        significant_features = results_df[results_df['p_value'] < 0.05]
        if len(significant_features) > 0:
            print("\n📋 Significant factors (p < 0.05):")
            for idx, row in significant_features.iterrows():
                coef = row['coefficient']
                or_val = row['odds_ratio']
                print(f"  {idx}: OR={or_val:.3f} ({'increases' if coef > 0 else 'decreases'} hesitancy)")

    except Exception as e:
        print(f"⚠ Regression analysis failed: {str(e)}")
        print("💡 This might be due to:")
        print("  - Perfect separation in the data")
        print("  - Insufficient variation in predictors")
        print("  - Multicollinearity issues")

def create_summary_statistics():
    """Create comprehensive summary statistics"""
    try:
        df = pd.read_csv(TABS/"nfhs_clean.csv")

        # Overall statistics
        stats = {
            'total_respondents': len(df),
            'hesitancy_rate': df['vaccine_hesitant'].mean(),
            'vaccination_rate': 1 - df['vaccine_hesitant'].mean()
        }

        # Group-wise statistics
        if 'state' in df.columns:
            state_stats = df.groupby('state')['vaccine_hesitant'].agg(['count', 'mean', 'std']).round(3)
            state_stats.to_csv(OUTR/"hesitancy_by_state.csv")
            print("✅ State-wise hesitancy statistics saved")

        if 'education' in df.columns:
            edu_stats = df.groupby('education')['vaccine_hesitant'].agg(['count', 'mean', 'std']).round(3)
            edu_stats.to_csv(OUTR/"hesitancy_by_education.csv")
            print("✅ Education-wise hesitancy statistics saved")

        if 'gender' in df.columns:
            gender_stats = df.groupby('gender')['vaccine_hesitant'].agg(['count', 'mean', 'std']).round(3)
            gender_stats.to_csv(OUTR/"hesitancy_by_gender.csv")
            print("✅ Gender-wise hesitancy statistics saved")

        # Save overall statistics
        with open(OUTR/"summary_statistics.txt", "w") as f:
            f.write("VACCINE HESITANCY SUMMARY STATISTICS\n")
            f.write("="*40 + "\n\n")
            for key, value in stats.items():
                f.write(f"{key}: {value}\n")

        print("✅ Summary statistics saved")

    except FileNotFoundError:
        print("⚠ Clean data not found for summary statistics")

if __name__ == "__main__":
    analyze_vaccine_hesitancy()
    create_summary_statistics()
