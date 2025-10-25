"""
Visualization Generator for Vaccine Hesitancy Research
Creates comprehensive plots and charts for the analysis results
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np

BASE = Path("projects/vaccine_hesitancy")
OUTPUTS = BASE/"outputs"
TABLES = OUTPUTS/"tables"
REPORTS = OUTPUTS/"reports"
PLOTS = OUTPUTS/"plots"

def setup_plotting():
    """Set up plotting parameters"""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    PLOTS.mkdir(parents=True, exist_ok=True)

def load_data():
    """Load all analysis data for visualization"""
    data = {}

    try:
        # Load NFHS data
        if (TABLES/"nfhs_clean.csv").exists():
            data['nfhs'] = pd.read_csv(TABLES/"nfhs_clean.csv")

        # Load Twitter sentiment
        if (TABLES/"twitter_sentiment_timeseries.csv").exists():
            data['twitter_sentiment'] = pd.read_csv(TABLES/"twitter_sentiment_timeseries.csv")

        if (TABLES/"twitter_sentiment_detailed.csv").exists():
            data['twitter_detailed'] = pd.read_csv(TABLES/"twitter_sentiment_detailed.csv")

        # Load odds ratios
        if (REPORTS/"logit_odds_ratios.csv").exists():
            data['odds_ratios'] = pd.read_csv(REPORTS/"logit_odds_ratios.csv")

        # Load summary statistics
        if (REPORTS/"hesitancy_by_state.csv").exists():
            data['state_stats'] = pd.read_csv(REPORTS/"hesitancy_by_state.csv")

        if (REPORTS/"hesitancy_by_education.csv").exists():
            data['education_stats'] = pd.read_csv(REPORTS/"hesitancy_by_education.csv")

        if (REPORTS/"hesitancy_by_gender.csv").exists():
            data['gender_stats'] = pd.read_csv(REPORTS/"hesitancy_by_gender.csv")

    except Exception as e:
        print(f"Warning: Could not load some data: {e}")

    return data

def create_nfhs_visualizations(data):
    """Create visualizations for NFHS survey data"""
    print("📊 Creating NFHS survey visualizations...")

    if 'nfhs' not in data:
        print("⚠ NFHS data not available")
        return

    df = data['nfhs']

    # 1. Vaccine hesitancy by state
    if 'state' in df.columns:
        state_hesitancy = df.groupby('state')['vaccine_hesitant'].mean().reset_index()
        state_hesitancy = state_hesitancy.sort_values('vaccine_hesitant', ascending=False)

        fig = px.bar(state_hesitancy, x='state', y='vaccine_hesitant',
                    title='Vaccine Hesitancy Rate by State',
                    labels={'vaccine_hesitant': 'Hesitancy Rate', 'state': 'State'})
        fig.update_layout(xaxis_tickangle=-45)
        fig.write_html(PLOTS/"hesitancy_by_state.html")
        fig.write_image(PLOTS/"hesitancy_by_state.png")
        print("✅ State hesitancy chart created")

    # 2. Hesitancy by education level
    if 'education' in df.columns:
        edu_hesitancy = df.groupby('education')['vaccine_hesitant'].agg(['count', 'mean']).reset_index()

        fig = px.bar(edu_hesitancy, x='education', y='mean',
                    title='Vaccine Hesitancy by Education Level',
                    labels={'mean': 'Hesitancy Rate', 'education': 'Education Level'})
        fig.write_html(PLOTS/"hesitancy_by_education.html")
        fig.write_image(PLOTS/"hesitancy_by_education.png")
        print("✅ Education hesitancy chart created")

    # 3. Rural vs Urban hesitancy
    if 'rural' in df.columns:
        rural_urban = df.groupby('rural')['vaccine_hesitant'].mean().reset_index()
        rural_urban['location'] = rural_urban['rural'].map({0: 'Urban', 1: 'Rural'})

        fig = px.pie(rural_urban, values='vaccine_hesitant', names='location',
                    title='Vaccine Hesitancy: Rural vs Urban')
        fig.write_html(PLOTS/"hesitancy_rural_urban.html")
        fig.write_image(PLOTS/"hesitancy_rural_urban.png")
        print("✅ Rural-urban hesitancy chart created")

    # 4. Correlation heatmap
    numeric_cols = ['age', 'education_level', 'rural', 'vaccine_hesitant']
    available_cols = [col for col in numeric_cols if col in df.columns]

    if len(available_cols) > 1:
        corr_df = df[available_cols].corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0, square=True)
        plt.title('Correlation Matrix: Vaccine Hesitancy Factors')
        plt.tight_layout()
        plt.savefig(PLOTS/"correlation_heatmap.png", dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Correlation heatmap created")

def create_twitter_visualizations(data):
    """Create visualizations for Twitter sentiment analysis"""
    print("🐦 Creating Twitter sentiment visualizations...")

    if 'twitter_sentiment' not in data:
        print("⚠ Twitter sentiment data not available")
        return

    sentiment_df = data['twitter_sentiment']

    # 1. Sentiment trend over time
    if 'month' in sentiment_df.columns and 'sentiment_mean' in sentiment_df.columns:
        fig = px.line(sentiment_df, x='month', y='sentiment_mean',
                     title='Twitter Sentiment Trend on Vaccines',
                     labels={'sentiment_mean': 'Average Sentiment', 'month': 'Month'})
        fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Neutral")
        fig.write_html(PLOTS/"twitter_sentiment_trend.html")
        fig.write_image(PLOTS/"twitter_sentiment_trend.png")
        print("✅ Twitter sentiment trend created")

    # 2. Sentiment distribution
    if 'twitter_detailed' in data:
        detailed_df = data['twitter_detailed']
        if 'label' in detailed_df.columns:
            sentiment_counts = detailed_df['label'].value_counts()

            fig = px.pie(sentiment_counts, values=sentiment_counts.values,
                        names=sentiment_counts.index, title='Twitter Sentiment Distribution')
            fig.write_html(PLOTS/"twitter_sentiment_distribution.html")
            fig.write_image(PLOTS/"twitter_sentiment_distribution.png")
            print("✅ Twitter sentiment distribution created")

def create_regression_visualizations(data):
    """Create visualizations for regression analysis"""
    print("📈 Creating regression analysis visualizations...")

    if 'odds_ratios' not in data:
        print("⚠ Odds ratios data not available")
        return

    odds_df = data['odds_ratios']

    # 1. Odds ratios bar chart
    odds_df_sorted = odds_df.sort_values('odds_ratio', ascending=False)

    fig = px.bar(odds_df_sorted, x='odds_ratio', y=odds_df_sorted.index,
                orientation='h', title='Odds Ratios for Vaccine Hesitancy Factors',
                labels={'odds_ratio': 'Odds Ratio', 'index': 'Factor'})
    fig.add_vline(x=1, line_dash="dash", line_color="red", annotation_text="No Effect")
    fig.write_html(PLOTS/"odds_ratios.html")
    fig.write_image(PLOTS/"odds_ratios.png")
    print("✅ Odds ratios visualization created")

    # 2. Feature importance (absolute coefficient values)
    if 'coefficient' in odds_df.columns:
        importance_df = odds_df.copy()
        importance_df['abs_coefficient'] = abs(importance_df['coefficient'])
        importance_df = importance_df.sort_values('abs_coefficient', ascending=True)

        fig = px.bar(importance_df, x='abs_coefficient', y=importance_df.index,
                    orientation='h', title='Feature Importance in Vaccine Hesitancy Model',
                    labels={'abs_coefficient': 'Absolute Coefficient', 'index': 'Factor'})
        fig.write_html(PLOTS/"feature_importance.html")
        fig.write_image(PLOTS/"feature_importance.png")
        print("✅ Feature importance visualization created")

def create_summary_dashboard(data):
    """Create a comprehensive summary dashboard"""
    print("📋 Creating summary dashboard...")

    # Create a comprehensive summary figure
    fig = plt.figure(figsize=(20, 12))

    # Subplot 1: Key metrics
    plt.subplot(2, 3, 1)
    if 'nfhs' in data:
        df = data['nfhs']
        hesitancy_rate = df['vaccine_hesitant'].mean()
        plt.pie([hesitancy_rate, 1-hesitancy_rate],
               labels=['Hesitant', 'Not Hesitant'],
               autopct='%1.1f%%', colors=['#ff6b6b', '#4ecdc4'])
        plt.title('Overall Vaccine Hesitancy Rate')

    # Subplot 2: Education breakdown
    plt.subplot(2, 3, 2)
    if 'education_stats' in data:
        edu_stats = data['education_stats']
        plt.bar(range(len(edu_stats)), edu_stats['mean'])
        plt.xticks(range(len(edu_stats)), edu_stats['education'], rotation=45)
        plt.title('Hesitancy by Education')
        plt.ylabel('Hesitancy Rate')

    # Subplot 3: State variation
    plt.subplot(2, 3, 3)
    if 'state_stats' in data:
        state_stats = data['state_stats'].head(10)  # Top 10 states
        plt.barh(range(len(state_stats)), state_stats['mean'])
        plt.yticks(range(len(state_stats)), state_stats['state'])
        plt.title('Top 10 States by Hesitancy')
        plt.xlabel('Hesitancy Rate')

    # Subplot 4: Twitter sentiment
    plt.subplot(2, 3, 4)
    if 'twitter_sentiment' in data:
        sentiment_df = data['twitter_sentiment']
        if 'sentiment_mean' in sentiment_df.columns:
            plt.plot(range(len(sentiment_df)), sentiment_df['sentiment_mean'])
            plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
            plt.title('Twitter Sentiment Trend')
            plt.ylabel('Sentiment Score')

    # Subplot 5: Gender comparison
    plt.subplot(2, 3, 5)
    if 'gender_stats' in data:
        gender_stats = data['gender_stats']
        plt.bar(range(len(gender_stats)), gender_stats['mean'])
        plt.xticks(range(len(gender_stats)), gender_stats['gender'])
        plt.title('Hesitancy by Gender')
        plt.ylabel('Hesitancy Rate')

    # Subplot 6: Odds ratios
    plt.subplot(2, 3, 6)
    if 'odds_ratios' in data:
        odds_df = data['odds_ratios'].head(8)  # Top 8 factors
        colors = ['red' if x > 1 else 'green' for x in odds_df['odds_ratio']]
        plt.barh(range(len(odds_df)), odds_df['odds_ratio'], color=colors)
        plt.axvline(x=1, color='black', linestyle='--', alpha=0.5)
        plt.yticks(range(len(odds_df)), odds_df.index)
        plt.title('Key Odds Ratios')
        plt.xlabel('Odds Ratio')

    plt.tight_layout()
    plt.savefig(PLOTS/"vaccine_hesitancy_dashboard.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Summary dashboard created")

def generate_all_visualizations():
    """Generate all visualizations"""
    print("🎨 Starting visualization generation...")

    setup_plotting()
    data = load_data()

    if not data:
        print("⚠ No data available for visualization. Run analysis first:")
        print("  python projects/vaccine_hesitancy/run_all.py")
        return

    # Create different types of visualizations
    create_nfhs_visualizations(data)
    create_twitter_visualizations(data)
    create_regression_visualizations(data)
    create_summary_dashboard(data)

    print("\n✅ All visualizations created!")
    print("📊 Charts saved in: projects/vaccine_hesitancy/outputs/plots/")
    print("🌐 Interactive HTML charts available for web viewing")

def main():
    """Main function to generate all visualizations"""
    generate_all_visualizations()

if __name__ == "__main__":
    main()
