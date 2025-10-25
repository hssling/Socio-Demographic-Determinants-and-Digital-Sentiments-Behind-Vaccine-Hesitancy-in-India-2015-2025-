import streamlit as st, pandas as pd, plotly.express as px, plotly.graph_objects as go
from pathlib import Path
import os

st.set_page_config(page_title="Vaccine Hesitancy Dashboard", layout="wide", page_icon="💉")
BASE = Path("projects/vaccine_hesitancy")
TABS = BASE/"outputs/tables"
REPORTS = BASE/"outputs/reports"

st.title("💉 Vaccine Hesitancy in India")
st.markdown("### Socio-Demographic Determinants and Digital Sentiments (2015–2025)")

# Sidebar for navigation
st.sidebar.title("📊 Analysis Sections")
section = st.sidebar.radio(
    "Navigate to:",
    ["Overview", "NFHS Survey Data", "Twitter Sentiment", "Regression Analysis", "Data Sources"]
)

if section == "Overview":
    st.header("📈 Project Overview")

    col1, col2, col3 = st.columns(3)

    # Check if data files exist
    nfhs_exists = os.path.exists(TABS/"nfhs_clean.csv")
    twitter_exists = os.path.exists(TABS/"twitter_sentiment_timeseries.csv")
    regression_exists = os.path.exists(REPORTS/"logit_summary.txt")

    with col1:
        st.metric("NFHS Data", "✅ Ready" if nfhs_exists else "⏳ Pending")
    with col2:
        st.metric("Twitter Analysis", "✅ Ready" if twitter_exists else "⏳ Pending")
    with col3:
        st.metric("Regression Model", "✅ Ready" if regression_exists else "⏳ Pending")

    st.info("""
    This dashboard analyzes vaccine hesitancy patterns in India using:
    - **NFHS-5 Survey Data**: Socio-demographic factors
    - **Twitter/X Sentiment**: Public opinion trends
    - **Statistical Models**: Predictors of hesitancy
    """)

    # Quick data summary
    if nfhs_exists:
        try:
            df = pd.read_csv(TABS/"nfhs_clean.csv")
            st.success(f"📊 Dataset loaded: {len(df):,} respondents")

            if 'vaccine_hesitant' in df.columns:
                hesitancy_rate = df['vaccine_hesitant'].mean()
                st.metric("Vaccine Hesitancy Rate", f"{hesitancy_rate:.1%}")
        except Exception as e:
            st.error(f"Error loading data: {e}")

elif section == "NFHS Survey Data":
    st.header("📋 NFHS-5 Survey Analysis")

    try:
        df = pd.read_csv(TABS/"nfhs_clean.csv")
        st.success(f"✅ Loaded {len(df):,} survey responses")

        col1, col2 = st.columns(2)

        # Hesitancy by education
        if "education" in df.columns:
            fig1 = px.histogram(df, x="education", color="vaccine_hesitant",
                              barmode="group", title="Vaccine Hesitancy by Education Level")
            col1.plotly_chart(fig1, use_container_width=True)

        # Hesitancy by state
        if "state" in df.columns:
            state_hesitancy = df.groupby("state")["vaccine_hesitant"].mean().reset_index()
            fig2 = px.bar(state_hesitancy.sort_values("vaccine_hesitant", ascending=False),
                         x="state", y="vaccine_hesitant", title="Vaccine Hesitancy by State")
            col2.plotly_chart(fig2, use_container_width=True)

        # Gender analysis
        if "gender" in df.columns:
            gender_stats = df.groupby("gender")["vaccine_hesitant"].agg(["count", "mean"]).round(3)
            st.dataframe(gender_stats)

    except FileNotFoundError:
        st.warning("NFHS data not found. Run the analysis pipeline first.")
        st.info("Execute: python projects/vaccine_hesitancy/run_all.py")

elif section == "Twitter Sentiment":
    st.header("🐦 Twitter/X Sentiment Analysis")

    col1, col2 = st.columns(2)

    try:
        sentiment_df = pd.read_csv(TABS/"twitter_sentiment_timeseries.csv")

        # Sentiment trend over time
        if "month" in sentiment_df.columns and "sentiment_mean" in sentiment_df.columns:
            fig1 = px.line(sentiment_df, x="month", y="sentiment_mean",
                          title="Twitter Sentiment Trend on Vaccines")
            col1.plotly_chart(fig1, use_container_width=True)

        # Sentiment distribution
        try:
            detailed_df = pd.read_csv(TABS/"twitter_sentiment_detailed.csv")
            sentiment_counts = detailed_df["label"].value_counts()
            fig2 = px.pie(sentiment_counts, values=sentiment_counts.values,
                         names=sentiment_counts.index, title="Sentiment Distribution")
            col2.plotly_chart(fig2, use_container_width=True)
        except:
            col2.info("Detailed sentiment data not available")

    except FileNotFoundError:
        st.warning("Twitter sentiment data not found.")
        st.info("Run the analysis pipeline to generate sentiment data.")

elif section == "Regression Analysis":
    st.header("📊 Statistical Analysis")

    try:
        with open(REPORTS/"logit_summary.txt", "r") as f:
            summary_text = f.read()

        st.text_area("Regression Results", summary_text, height=400)

        # Odds ratios
        try:
            odds_df = pd.read_csv(REPORTS/"logit_odds_ratios.csv")
            st.dataframe(odds_df.round(3))

            # Feature importance
            fig = px.bar(odds_df.sort_values("odds_ratio", ascending=False),
                        x="odds_ratio", y=odds_df.index, orientation="h",
                        title="Odds Ratios by Factor")
            st.plotly_chart(fig, use_container_width=True)

        except FileNotFoundError:
            st.info("Odds ratios data not available")

    except FileNotFoundError:
        st.warning("Regression analysis not found.")
        st.info("Run the analysis pipeline to generate regression results.")

elif section == "Data Sources":
    st.header("📁 Data Sources & Methodology")

    st.subheader("Data Sources")
    st.markdown("""
    - **NFHS-5 (2021)**: National Family Health Survey data for socio-demographic analysis
    - **Twitter/X API**: Social media sentiment analysis (sample data provided)
    - **Google Trends**: Vaccine-related search trends (sample data provided)
    """)

    st.subheader("Methodology")
    st.markdown("""
    1. **Data Extraction**: Automated collection from multiple sources
    2. **Data Cleaning**: Standardization and missing value handling
    3. **Sentiment Analysis**: TextBlob-based sentiment scoring
    4. **Statistical Modeling**: Logistic regression for hesitancy prediction
    5. **Visualization**: Interactive dashboard with Plotly
    """)

    st.subheader("Next Steps")
    st.info("""
    To use with real data:
    1. Replace sample data in `data/` directories with actual datasets
    2. Update API keys in `.env` file for live data collection
    3. Run: `python projects/vaccine_hesitancy/run_all.py`
    """)

# Footer
st.markdown("---")
st.markdown("*Vaccine Hesitancy Research Project | Built with Streamlit & Python*")
