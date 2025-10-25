# 💉 Vaccine Hesitancy in India – Research Project

## Socio-Demographic Determinants and Digital Sentiments Behind Vaccine Hesitancy in India (2015–2025)

This project analyzes vaccine hesitancy patterns in India using both survey data (NFHS-5) and digital sentiment analysis (Twitter/X posts). The system includes automated data extraction, cleaning, statistical analysis, and interactive visualization.

### Project Structure

```
projects/vaccine_hesitancy/
 ┣ data/
 ┃ ┣ nfhs/          # NFHS-5 survey data (CSV files)
 ┃ ┣ twitter/       # Twitter/X data (CSV files)
 ┃ ┗ trends/        # Google Trends data
 ┣ scripts/
 ┃ ┣ data_extraction.py     # Automated data extraction from multiple sources
 ┃ ┣ clean_data.py          # Data cleaning and preprocessing
 ┃ ┣ twitter_sentiment.py   # Twitter sentiment analysis with TextBlob
 ┃ ┗ analyze_factors.py     # Statistical analysis & regression modeling
 ┣ outputs/
 ┃ ┣ tables/        # Cleaned data and results
 ┃ ┣ plots/         # Visualizations
 ┃ ┗ reports/       # Analysis reports and statistics
 ┣ dashboards/
 ┃ ┗ app.py         # Interactive Streamlit dashboard
 ┗ run_all.py       # Main execution script
```

### Setup

1. **Install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install pandas numpy matplotlib seaborn plotly geopandas folium tweepy textblob langchain transformers huggingface_hub vaderSentiment scikit-learn pypandoc statsmodels rich tqdm streamlit
   ```

2. **Run the complete analysis:**
   ```bash
   .\.venv\Scripts\activate
   python projects/vaccine_hesitancy/run_all.py
   ```

3. **Launch dashboard:**
   ```bash
   streamlit run projects/vaccine_hesitancy/dashboards/app.py
   ```

### Data Sources

#### NFHS-5 Survey Data
- **Source**: National Family Health Survey 2021 (India)
- **Variables**: Socio-demographic factors, vaccination status, health indicators
- **Access**: Download from [DHS Program](https://dhsprogram.com/data/dataset/India_Standard-DHS_2021.cfm)
- **Expected columns**: state, gender, education, income, religion, vaccine_hesitant, vaccination_status

#### Twitter/X Sentiment Data
- **Source**: Social media posts about vaccines in India
- **Analysis**: TextBlob sentiment analysis
- **Expected columns**: text, date, user_location, retweets, likes

#### Google Trends Data
- **Source**: Vaccine-related search trends
- **Analysis**: Temporal patterns in search behavior

### Key Features

- **🔄 Automated Data Extraction**: Multi-source data collection
- **🧹 Data Cleaning**: Standardization and missing value handling
- **📊 Statistical Analysis**: Logistic regression for hesitancy prediction
- **🧠 Sentiment Analysis**: TextBlob-based social media analysis
- **📈 Interactive Dashboard**: Real-time visualization with Plotly
- **🔗 End-to-End Pipeline**: Automated workflow from data to insights

### Analysis Pipeline

1. **Data Extraction** (`data_extraction.py`)
   - Fetches data from multiple sources
   - Creates sample datasets for testing
   - Handles API connections (when available)

2. **Data Cleaning** (`clean_data.py`)
   - Standardizes column names
   - Handles missing values
   - Creates derived variables
   - Generates summary statistics

3. **Sentiment Analysis** (`twitter_sentiment.py`)
   - Text preprocessing and cleaning
   - TextBlob sentiment scoring
   - Time-series aggregation
   - State-wise analysis

4. **Statistical Modeling** (`analyze_factors.py`)
   - Logistic regression analysis
   - Odds ratio calculation
   - Feature importance analysis
   - Model diagnostics

5. **Visualization** (`dashboards/app.py`)
   - Interactive dashboard with multiple sections
   - Real-time data visualization
   - Statistical results display

### Outputs

- **Cleaned Data**: `outputs/tables/nfhs_clean.csv`
- **Sentiment Analysis**: `outputs/tables/twitter_sentiment_timeseries.csv`
- **Regression Results**: `outputs/reports/logit_summary.txt`
- **Odds Ratios**: `outputs/reports/logit_odds_ratios.csv`
- **Summary Statistics**: `outputs/reports/summary_statistics.txt`
- **Interactive Dashboard**: Web interface with visualizations

### Using Real Data

#### Option 1: Add Your Own Data
1. Place NFHS-5 CSV files in `data/nfhs/`
2. Place Twitter data in `data/twitter/`
3. Run the pipeline: `python projects/vaccine_hesitancy/run_all.py`

#### Option 2: API Integration
1. Set up API keys in `.env` file:
   ```
   TWITTER_BEARER_TOKEN=your_token_here
   NEWS_API_KEY=your_key_here
   ```
2. Update scripts to use live API data

#### Option 3: Download from Official Sources
- **NFHS-5**: [DHS Program Website](https://dhsprogram.com/data/available-datasets.cfm)
- **Twitter Data**: Academic API or existing datasets
- **Google Trends**: Official Google Trends API

### Sample Data

The project includes sample datasets for testing:
- Sample NFHS-5 data with 1,000 respondents
- Sample Twitter data with 500 vaccine-related tweets
- Sample Google Trends data with 2 years of daily trends

### Dashboard Sections

1. **Overview**: Project status and key metrics
2. **NFHS Survey Data**: Socio-demographic analysis
3. **Twitter Sentiment**: Social media sentiment trends
4. **Regression Analysis**: Statistical model results
5. **Data Sources**: Methodology and data information

### Technical Details

- **Python Version**: 3.8+
- **Key Libraries**: pandas, numpy, statsmodels, textblob, streamlit, plotly
- **Statistical Methods**: Logistic regression, sentiment analysis
- **Data Formats**: CSV, JSON, text files
- **Visualization**: Interactive Plotly charts

### Troubleshooting

**Common Issues:**
- **Missing data**: Run data extraction first
- **API errors**: Check API keys and rate limits
- **Memory issues**: Process data in batches for large datasets
- **Encoding errors**: Ensure UTF-8 encoding for text data

**Performance Tips:**
- Use sample data for initial testing
- Process large datasets in chunks
- Monitor memory usage for big data

### Next Steps

1. **Add Real Data**: Replace sample data with actual datasets
2. **API Integration**: Set up live data collection
3. **Advanced Analysis**: Add machine learning models
4. **Publication Ready**: Generate manuscript-ready outputs
5. **Deployment**: Deploy dashboard to cloud platform

### Contributing

1. Fork the repository
2. Create feature branch
3. Add tests and documentation
4. Submit pull request

### License

This project is for research purposes. Please cite appropriately when using the code or methodology.

### Contact

For questions or collaboration opportunities, please refer to the project documentation or create an issue in the repository.

---

**Built with ❤️ for Public Health Research**
*Automated Vaccine Hesitancy Analysis Pipeline*
