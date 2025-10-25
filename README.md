# 💉 Vaccine Hesitancy Research Project

## Socio-Demographic Determinants and Digital Sentiments Behind Vaccine Hesitancy in India (2015–2025)

**Author:** Dr. Siddalingaiah H S, MD, MPH
**Affiliation:** Professor and Head, Department of Community Medicine, Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH), Tumkur, Karnataka, India
**Email:** hssling@yahoo.com
**Phone:** +91-8941087719

**Repository:** [GitHub Repository](https://github.com/hssling/Socio-Demographic-Determinants-and-Digital-Sentiments-Behind-Vaccine-Hesitancy-in-India-2015-2025-)

---

## 🚀 Quick Start

### Option 1: Automated Pipeline (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/hssling/Socio-Demographic-Determinants-and-Digital-Sentiments-Behind-Vaccine-Hesitancy-in-India-2015-2025-.git
cd Socio-Demographic-Determinants-and-Digital-Sentiments-Behind-Vaccine-Hesitancy-in-India-2015-2025-

# 2. Set up environment
python -m venv .venv
.\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run complete analysis
python projects/vaccine_hesitancy/run_all.py

# 5. Launch interactive dashboard
streamlit run projects/vaccine_hesitancy/dashboards/app.py
```

### Option 2: Drag & Drop Data Upload
1. **📁 Add your data files** to the appropriate directories:
   - `projects/vaccine_hesitancy/data/nfhs/` - NFHS-5 survey data (CSV format)
   - `projects/vaccine_hesitancy/data/twitter/` - Twitter/X data (CSV format)
   - `projects/vaccine_hesitancy/data/trends/` - Google Trends data (CSV format)

2. **🔄 Run analysis** with your data:
   ```bash
   python projects/vaccine_hesitancy/run_all.py
   ```

3. **📊 View results** in the interactive dashboard

---

## 📋 Project Overview

This comprehensive research project analyzes vaccine hesitancy patterns in India using multiple data sources and advanced analytics. The system provides:

### 🎯 Key Features
- **🔄 Automated Data Pipeline** - Multi-source data collection and processing
- **📊 Advanced Statistical Analysis** - Logistic regression and predictive modeling
- **🧠 AI-Powered Sentiment Analysis** - TextBlob-based social media analysis
- **📈 Interactive Visualizations** - Plotly charts and comprehensive dashboards
- **📝 Publication-Ready Manuscripts** - Automated research paper generation
- **🚀 CI/CD Integration** - Automated testing and deployment

### 📊 Analysis Components
1. **Data Extraction** - Automated collection from multiple sources
2. **Data Cleaning** - Standardization and quality validation
3. **Sentiment Analysis** - Twitter/X social media sentiment analysis
4. **Statistical Modeling** - Logistic regression and factor analysis
5. **Visualization Generation** - Interactive charts and plots
6. **Manuscript Generation** - Complete research paper creation

---

## 📁 Project Structure

```
projects/vaccine_hesitancy/
 ┣ 📂 data/                          # Data directories
 ┃ ┣ 📂 nfhs/                        # NFHS-5 survey data
 ┃ ┃ ┗ 📄 nfhs5_vaccine_sample.csv   # Sample dataset
 ┃ ┣ 📂 twitter/                     # Twitter/X data
 ┃ ┃ ┗ 📄 vaccine_tweets_india.csv   # Sample social media data
 ┃ ┗ 📂 trends/                      # Google Trends data
 ┃   ┗ 📄 vaccine_trends_india.csv   # Sample trends data
 ┣ 📂 scripts/                       # Analysis scripts
 ┃ ┣ 📄 data_extraction.py           # Multi-source data collection
 ┃ ┣ 📄 clean_data.py                # Data cleaning & preprocessing
 ┃ ┣ 📄 twitter_sentiment.py         # Sentiment analysis
 ┃ ┣ 📄 analyze_factors.py           # Statistical modeling
 ┃ ┣ 📄 generate_visualizations.py   # Chart generation
 ┃ ┗ 📄 generate_manuscript.py       # Research paper creation
 ┣ 📂 outputs/                       # Generated results
 ┃ ┣ 📂 tables/                      # Cleaned datasets
 ┃ ┣ 📂 plots/                       # Visualizations
 ┃ ┗ 📂 reports/                     # Manuscripts & statistics
 ┣ 📂 dashboards/                    # Interactive interfaces
 ┃ ┗ 📄 app.py                       # Streamlit dashboard
 ┣ 📂 .github/                       # CI/CD configuration
 ┃ ┗ 📂 workflows/                   # GitHub Actions
 ┣ 📄 run_all.py                     # Main execution script
 ┣ 📄 README.md                      # This file
 ┗ 📄 requirements.txt               # Python dependencies
```

---

## 🔧 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **Git** (for version control)
- **Internet connection** (for data download)

### Environment Setup
```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate environment
.\.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt
```

### Required Packages
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly, streamlit
- **Machine Learning:** scikit-learn, statsmodels
- **Natural Language Processing:** textblob
- **Web Framework:** streamlit
- **Document Processing:** pypandoc (optional, for DOCX export)

---

## 📊 Data Sources & Formats

### NFHS-5 Survey Data
**Location:** `data/nfhs/`
**Format:** CSV files
**Required Columns:**
```csv
state,gender,education,income,religion,vaccine_hesitant,age,rural_urban,wealth_index
```

**Example:**
```csv
state,gender,education,income,religion,vaccine_hesitant,age,rural_urban,wealth_index
Maharashtra,Male,Secondary,High,Hindu,0,35,Urban,Rich
Karnataka,Female,Higher,Medium,Muslim,1,28,Rural,Poor
```

### Twitter/X Data
**Location:** `data/twitter/`
**Format:** CSV files
**Required Columns:**
```csv
text,date,user_location,retweets,likes
```

### Google Trends Data
**Location:** `data/trends/`
**Format:** CSV files
**Required Columns:**
```csv
date,search_term,trend_value,region
```

---

## 🚀 Usage Guide

### Basic Usage
```bash
# 1. Activate environment
.\.venv\Scripts\activate

# 2. Run complete analysis
python projects/vaccine_hesitancy/run_all.py

# 3. Launch dashboard
streamlit run projects/vaccine_hesitancy/dashboards/app.py
```

### Individual Components
```bash
# Data extraction only
python projects/vaccine_hesitancy/scripts/data_extraction.py

# Data cleaning only
python projects/vaccine_hesitancy/scripts/clean_data.py

# Sentiment analysis only
python projects/vaccine_hesitancy/scripts/twitter_sentiment.py

# Statistical analysis only
python projects/vaccine_hesitancy/scripts/analyze_factors.py

# Generate visualizations only
python projects/vaccine_hesitancy/scripts/generate_visualizations.py

# Generate manuscript only
python projects/vaccine_hesitancy/scripts/generate_manuscript.py
```

---

## 📈 Output Files

### Generated Datasets
- **`outputs/tables/nfhs_clean.csv`** - Cleaned survey data
- **`outputs/tables/twitter_sentiment_timeseries.csv`** - Sentiment analysis results
- **`outputs/tables/twitter_sentiment_detailed.csv`** - Detailed sentiment data

### Statistical Reports
- **`outputs/reports/summary_statistics.txt`** - Key metrics and statistics
- **`outputs/reports/logit_summary.txt`** - Regression model results
- **`outputs/reports/logit_odds_ratios.csv`** - Odds ratios and confidence intervals

### Visualizations
- **`outputs/plots/*.html`** - Interactive Plotly charts
- **`outputs/plots/*.png`** - Static images for publications
- **`outputs/plots/vaccine_hesitancy_dashboard.png`** - Summary dashboard

### Manuscripts
- **`outputs/reports/vaccine_hesitancy_manuscript.md`** - Complete research paper (Markdown)
- **`outputs/reports/vaccine_hesitancy_manuscript.docx`** - Microsoft Word format

---

## 🔄 Drag & Drop Data Upload

### Step 1: Prepare Your Data
1. **Format your data** according to the specifications above
2. **Save as CSV files** with proper encoding (UTF-8)
3. **Validate data quality** (check for missing values, correct column names)

### Step 2: Upload Data Files
**📁 Method 1: Direct File Placement**
```bash
# Copy your files to the appropriate directories
copy your_nfhs_data.csv projects/vaccine_hesitancy/data/nfhs/
copy your_twitter_data.csv projects/vaccine_hesitancy/data/twitter/
copy your_trends_data.csv projects/vaccine_hesitancy/data/trends/
```

**🌐 Method 2: GitHub Web Interface**
1. Go to the [GitHub Repository](https://github.com/hssling/Socio-Demographic-Determinants-and-Digital-Sentiments-Behind-Vaccine-Hesitancy-in-India-2015-2025-)
2. Click **"Add file"** → **"Upload files"**
3. Drag and drop your CSV files to the appropriate folders
4. Click **"Commit changes"**

**💻 Method 3: Git Command Line**
```bash
# Add your data files
git add projects/vaccine_hesitancy/data/nfhs/your_file.csv
git commit -m "Add NFHS data file"
git push
```

### Step 3: Run Analysis
```bash
# After uploading data files
python projects/vaccine_hesitancy/run_all.py
```

### Step 4: View Results
- **📊 Dashboard:** `streamlit run projects/vaccine_hesitancy/dashboards/app.py`
- **📄 Manuscript:** View `outputs/reports/vaccine_hesitancy_manuscript.md`
- **📈 Visualizations:** Check `outputs/plots/` directory

---

## 🔧 CI/CD Pipeline

### Automated Workflows
The project includes GitHub Actions for automated:
- **✅ Code validation** and testing
- **🔄 Dependency installation** and environment setup
- **📊 Automated analysis** execution
- **🚀 Result generation** and artifact creation

### Triggering Workflows
**Automatic Triggers:**
- Push to `main` or `master` branch
- Pull requests to main branches
- Manual trigger via GitHub Actions tab

**Manual Trigger:**
1. Go to **Actions** tab in GitHub repository
2. Select **"Vaccine Hesitancy Research Pipeline"**
3. Click **"Run workflow"**

### Workflow Steps
1. **Environment Setup** - Python 3.9, dependencies
2. **Project Validation** - Structure and file checks
3. **Data Validation** - CSV format and content validation
4. **Analysis Execution** - Complete pipeline run
5. **Artifact Generation** - Results packaging
6. **Deployment Ready** - Output preparation

---

## 📊 Dashboard Features

### Interactive Sections
1. **📈 Overview** - Project status and key metrics
2. **📋 NFHS Survey Data** - Socio-demographic analysis
3. **🐦 Twitter Sentiment** - Social media analysis
4. **📊 Regression Analysis** - Statistical model results
5. **📁 Data Sources** - Methodology and documentation

### Navigation
- **Sidebar navigation** for easy section switching
- **Real-time updates** when new data is processed
- **Interactive charts** with zoom and filter options
- **Export functionality** for charts and data

---

## 🔬 Analysis Pipeline Details

### 1. Data Extraction
- **Multi-source collection** from NFHS-5, Twitter/X, Google Trends
- **Format standardization** and validation
- **Sample data generation** for testing

### 2. Data Cleaning
- **Column standardization** and renaming
- **Missing value handling** and imputation
- **Data type validation** and conversion
- **Quality assessment** and reporting

### 3. Sentiment Analysis
- **Text preprocessing** (cleaning, tokenization)
- **TextBlob sentiment scoring** (-1 to +1 scale)
- **Temporal aggregation** and trend analysis
- **State-wise sentiment mapping**

### 4. Statistical Modeling
- **Logistic regression** for hesitancy prediction
- **Odds ratio calculation** with confidence intervals
- **Model diagnostics** and validation
- **Feature importance analysis**

### 5. Visualization Generation
- **Interactive Plotly charts** for web viewing
- **Static PNG images** for publications
- **Comprehensive dashboard** with all results
- **Export functionality** for further use

### 6. Manuscript Generation
- **Complete research paper** with all sections
- **Statistical tables** and formatted references
- **Professional formatting** for journal submission
- **Multiple formats** (Markdown, DOCX)

---

## 📝 Data Format Specifications

### NFHS-5 Data Format
```csv
state,gender,education,income,religion,vaccine_hesitant,age,rural_urban,wealth_index
Maharashtra,Male,Secondary,High,Hindu,0,35,Urban,Rich
Karnataka,Female,Higher,Medium,Muslim,1,28,Rural,Poor
Tamil Nadu,Male,Primary,Low,Christian,0,42,Urban,Middle
```

**Column Specifications:**
- **state:** Indian state name (string)
- **gender:** Male/Female (string)
- **education:** No Education/Primary/Secondary/Higher (string)
- **income:** Low/Middle/High (string)
- **religion:** Hindu/Muslim/Christian/Sikh/Other (string)
- **vaccine_hesitant:** 0 (not hesitant) or 1 (hesitant) (integer)
- **age:** Age in years (integer)
- **rural_urban:** Rural/Urban (string)
- **wealth_index:** Poorest/Poorer/Middle/Richer/Richest (string)

### Twitter Data Format
```csv
text,date,user_location,retweets,likes
"Vaccines are important for public health #VaccineForAll",2023-01-15,Mumbai,25,45
"Not sure about COVID vaccine safety 😟 #VaccineHesitancy",2023-02-20,Delhi,12,18
```

**Column Specifications:**
- **text:** Tweet content (string)
- **date:** Tweet date in YYYY-MM-DD format (string)
- **user_location:** User location (string)
- **retweets:** Number of retweets (integer)
- **likes:** Number of likes (integer)

### Google Trends Data Format
```csv
date,search_term,trend_value,region
2023-01-01,COVID vaccine,45,India
2023-01-02,vaccine registration,67,India
```

**Column Specifications:**
- **date:** Date in YYYY-MM-DD format (string)
- **search_term:** Search term (string)
- **trend_value:** Google Trends value 0-100 (integer)
- **region:** Geographic region (string)

---

## 🛠️ Troubleshooting

### Common Issues

**❌ "No module named 'textblob'"**
```bash
pip install textblob
python -m textblob.download_corpora
```

**❌ "No data files found"**
- Check that your CSV files are in the correct directories
- Verify column names match the specifications
- Ensure proper file encoding (UTF-8)

**❌ "Memory error with large datasets"**
```bash
# Process data in chunks
python scripts/clean_data.py --chunk_size 1000
```

**❌ "GitHub push blocked by secrets"**
- Remove sensitive files from git history
- Use `.gitignore` to prevent future commits of secrets
- Consider using GitHub's secret unblocking feature

### Performance Optimization
- **Large datasets:** Process in batches using chunk processing
- **Memory usage:** Monitor with `python -m memory_profiler`
- **Execution time:** Use parallel processing for independent tasks

---

## 🤝 Contributing

### Development Setup
```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/your-username/repository-name.git

# 3. Create feature branch
git checkout -b feature/new-analysis

# 4. Make changes and test
python projects/vaccine_hesitancy/run_all.py

# 5. Commit and push
git add .
git commit -m "Add new feature"
git push origin feature/new-analysis

# 6. Create Pull Request
```

### Code Standards
- **Documentation:** All functions must have docstrings
- **Error Handling:** Include try-catch blocks for file operations
- **Code Style:** Follow PEP 8 guidelines
- **Testing:** Add unit tests for new functions

---

## 📄 License & Citation

### Citation
When using this research project or methodology, please cite:

> Siddalingaiah H S. (2025). Socio-Demographic Determinants and Digital Sentiments Behind Vaccine Hesitancy in India (2015–2025): An Automated Research Pipeline. Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH), Tumkur, Karnataka, India.

### License
This project is made available for research and educational purposes. Please respect the intellectual property and cite appropriately when using the code or methodology.

---

## 📞 Contact & Support

**Principal Investigator:**
Dr. Siddalingaiah H S, MD, MPH
Professor and Head, Department of Community Medicine
Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH)
Tumkur, Karnataka, India
📧 hssling@yahoo.com
📱 +91-8941087719

**Technical Support:**
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review the CI/CD pipeline logs

---

## 🎯 Project Status

- **✅ Complete Analysis Pipeline** - All components functional
- **✅ Interactive Dashboard** - Multi-section interface ready
- **✅ Publication-Ready Manuscript** - Automated generation working
- **✅ Comprehensive Visualizations** - Charts and plots created
- **✅ CI/CD Integration** - GitHub Actions configured
- **✅ Documentation** - Complete usage guide provided

**🚀 Ready for research, collaboration, and publication!**

---

*Built with ❤️ for Public Health Research | Automated Vaccine Hesitancy Analysis Pipeline*
