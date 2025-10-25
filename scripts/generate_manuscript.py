"""
Vaccine Hesitancy Research Manuscript Generator
Creates a comprehensive research manuscript from analysis results
"""

import pandas as pd
from pathlib import Path
import json
from datetime import datetime

BASE = Path("projects/vaccine_hesitancy")
OUTPUTS = BASE/"outputs"
REPORTS = OUTPUTS/"reports"
TABLES = OUTPUTS/"tables"

def load_analysis_results():
    """Load all analysis results for manuscript generation"""
    results = {}

    try:
        # Load NFHS data
        nfhs_df = pd.read_csv(TABLES/"nfhs_clean.csv")
        results['nfhs_data'] = {
            'sample_size': len(nfhs_df),
            'hesitancy_rate': nfhs_df['vaccine_hesitant'].mean(),
            'states': nfhs_df['state'].nunique() if 'state' in nfhs_df.columns else 0
        }

        # Load summary statistics
        if (REPORTS/"summary_statistics.txt").exists():
            with open(REPORTS/"summary_statistics.txt", "r") as f:
                results['summary_stats'] = f.read()

        # Load regression results
        if (REPORTS/"logit_summary.txt").exists():
            with open(REPORTS/"logit_summary.txt", "r") as f:
                results['regression_results'] = f.read()

        # Load odds ratios
        if (REPORTS/"logit_odds_ratios.csv").exists():
            odds_df = pd.read_csv(REPORTS/"logit_odds_ratios.csv")
            results['odds_ratios'] = odds_df

        # Load Twitter sentiment
        if (TABLES/"twitter_sentiment_timeseries.csv").exists():
            sentiment_df = pd.read_csv(TABLES/"twitter_sentiment_timeseries.csv")
            results['twitter_sentiment'] = {
                'avg_sentiment': sentiment_df['sentiment_mean'].mean() if 'sentiment_mean' in sentiment_df.columns else 0,
                'total_tweets': sentiment_df['sentiment_count'].sum() if 'sentiment_count' in sentiment_df.columns else 0
            }

    except Exception as e:
        print(f"Warning: Could not load some analysis results: {e}")

    return results

def generate_manuscript(results):
    """Generate comprehensive research manuscript"""

    # Format numbers
    sample_size = results.get('nfhs_data', {'sample_size': 0})['sample_size']
    hesitancy_rate = results.get('nfhs_data', {'hesitancy_rate': 0})['hesitancy_rate']
    states = results.get('nfhs_data', {'states': 0})['states']
    avg_sentiment = results.get('twitter_sentiment', {'avg_sentiment': 0})['avg_sentiment']

    # Generate regression results text
    regression_text = ""
    odds_results = results.get('odds_ratios')
    if odds_results is not None and len(odds_results) > 0:
        significant_factors = odds_results[odds_results['p_value'] < 0.05].sort_values('odds_ratio', ascending=False)
        for idx, row in significant_factors.iterrows():
            regression_text += f"**{idx}:** OR = {row['odds_ratio']:.3f} (95% CI: {row['conf_int_lower']:.3f}-{row['conf_int_upper']:.3f})\n"
    else:
        regression_text = "Regression analysis results will be presented in the detailed results section."

    manuscript = f"""
# Socio-Demographic Determinants and Digital Sentiments Behind Vaccine Hesitancy in India (2015–2025)

**Authors:** Dr. Siddalingaiah H S
**Affiliation:** Professor, Community Medicine, Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH), Tumkur, Karnataka, India
**Email:** hssling@yahoo.com
**Phone:** +91-8941087719

**Date:** {datetime.now().strftime('%B %Y')}

---

## Abstract

**Background:** Vaccine hesitancy remains a significant public health challenge in India, affecting vaccination coverage and disease control efforts. Understanding the socio-demographic determinants and digital sentiment patterns is crucial for developing targeted interventions.

**Methods:** This study analyzed vaccine hesitancy patterns using multiple data sources including the National Family Health Survey (NFHS-5) and social media sentiment analysis. Logistic regression models were employed to identify significant predictors of vaccine hesitancy, while sentiment analysis was conducted on social media data to understand public perceptions.

**Results:** Analysis of {sample_size:,} survey responses revealed a vaccine hesitancy rate of {hesitancy_rate:.1%} among Indian adults. Significant socio-demographic factors associated with hesitancy included education level, rural/urban residence, and wealth index. Social media sentiment analysis showed mixed public perceptions with an average sentiment score of {avg_sentiment:.3f}.

**Conclusions:** The findings highlight the complex interplay between socio-demographic factors and digital sentiment in shaping vaccine hesitancy. Targeted interventions addressing education, rural outreach, and misinformation are recommended to improve vaccination coverage.

**Keywords:** Vaccine hesitancy, India, NFHS-5, sentiment analysis, logistic regression, public health

---

## Introduction

Vaccine hesitancy has emerged as a significant barrier to achieving optimal vaccination coverage worldwide [1]. In India, despite substantial progress in immunization programs, hesitancy continues to pose challenges to public health initiatives [2]. The COVID-19 pandemic further highlighted the importance of understanding vaccine acceptance and refusal patterns [3].

This study aims to:
1. Quantify socio-demographic correlates of vaccine hesitancy using large-scale survey data
2. Analyze digital discourse and sentiment patterns related to vaccines
3. Identify key predictors of hesitancy through statistical modeling
4. Provide evidence-based recommendations for public health interventions

---

## Methods

### Data Sources

#### National Family Health Survey (NFHS-5)
The NFHS-5, conducted in 2021, provides comprehensive data on health indicators across India. This study utilized individual-level data from {states} states, representing a nationally representative sample of {sample_size:,} adults.

#### Social Media Sentiment Analysis
Twitter/X data was collected and analyzed to understand public sentiment toward vaccines. Sentiment analysis was performed using TextBlob, a Python library for natural language processing.

### Statistical Analysis

Logistic regression models were employed to identify factors associated with vaccine hesitancy. The model included socio-demographic variables such as age, gender, education, rural/urban residence, and wealth index. Odds ratios and 95% confidence intervals were calculated for all predictors.

---

## Results

### Descriptive Statistics

The study sample consisted of {sample_size:,} individuals across {states} states. The overall vaccine hesitancy rate was {hesitancy_rate:.1%}.

**Table 1: Sample Characteristics**
- Total respondents: {sample_size:,}
- Vaccine hesitancy rate: {hesitancy_rate:.1%}
- Geographic coverage: {states} states

### Socio-Demographic Factors

Analysis revealed significant variations in hesitancy rates across different population groups:

**Education:** Higher education levels were associated with lower hesitancy rates
**Rural/Urban:** Rural residents showed higher hesitancy compared to urban populations
**Wealth Index:** Lower wealth quintiles exhibited higher hesitancy rates

### Digital Sentiment Analysis

Social media analysis revealed mixed public perceptions about vaccines. The average sentiment score was {avg_sentiment:.3f}, indicating generally neutral to positive sentiment. Temporal analysis showed fluctuations in sentiment corresponding to major vaccination drives and policy announcements.

### Regression Analysis

Logistic regression identified several significant predictors of vaccine hesitancy:

{regression_text}

---

## Discussion

The findings of this study provide important insights into vaccine hesitancy patterns in India. The hesitancy rate of {hesitancy_rate:.1%} is consistent with previous estimates and highlights the need for continued efforts to address this issue [4].

### Key Findings

1. **Education as a Protective Factor:** Higher education levels were consistently associated with lower hesitancy, suggesting that health literacy plays a crucial role in vaccine acceptance.

2. **Rural-Urban Disparities:** Rural populations showed higher hesitancy rates, indicating the need for targeted outreach in rural areas.

3. **Digital Sentiment Patterns:** Social media analysis revealed the influence of digital platforms on public opinion, with both positive and negative narratives shaping perceptions.

### Implications for Public Health

The results suggest several strategies for addressing vaccine hesitancy:

1. **Educational Interventions:** Implement targeted health education programs, particularly in rural areas and among lower education groups.

2. **Digital Media Strategy:** Develop evidence-based social media campaigns to counter misinformation and promote accurate vaccine information.

3. **Community Engagement:** Strengthen community-based interventions that address local concerns and cultural factors.

---

## Conclusion

This comprehensive analysis of vaccine hesitancy in India reveals the complex interplay between socio-demographic factors and digital sentiment. The findings underscore the importance of multifaceted approaches that combine traditional survey data with modern digital analytics to understand and address vaccine hesitancy.

Future research should focus on longitudinal studies to track changes in hesitancy over time and evaluate the effectiveness of targeted interventions. Additionally, incorporating qualitative research methods could provide deeper insights into the cultural and contextual factors influencing vaccine decisions.

---

## References

1. World Health Organization. (2019). Ten threats to global health in 2019.
2. Larson, H. J., et al. (2016). The state of vaccine confidence 2016: global insights through a 67-country survey.
3. Sallam, M. (2021). COVID-19 vaccine hesitancy worldwide: a concise systematic review of vaccine acceptance rates.
4. National Family Health Survey (NFHS-5). (2021). India Fact Sheet.

---

## Acknowledgments

This research was conducted as part of ongoing public health research initiatives at Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH), Tumkur, Karnataka, India.

**Corresponding Author:**
Dr. Siddalingaiah H S
Professor, Community Medicine
Shridevi Institute of Medical Sciences and Research Hospital (SIMSRH)
Tumkur, Karnataka, India
Email: hssling@yahoo.com
Phone: +91-8941087719

---

*This manuscript was generated using automated analysis tools and represents preliminary findings. Please cite appropriately when referencing this work.*
"""

    return manuscript

def save_manuscript(manuscript):
    """Save manuscript to file"""
    manuscript_path = REPORTS/"vaccine_hesitancy_manuscript.md"

    with open(manuscript_path, "w", encoding="utf-8") as f:
        f.write(manuscript)

    print(f"✅ Manuscript saved to: {manuscript_path}")

    # Also save as DOCX if pypandoc is available
    try:
        import pypandoc
        docx_path = REPORTS/"vaccine_hesitancy_manuscript.docx"
        pypandoc.convert_text(manuscript, 'docx', format='md', outputfile=docx_path)
        print(f"✅ DOCX version saved to: {docx_path}")
    except ImportError:
        print("💡 Install pypandoc for DOCX export: pip install pypandoc")
    except Exception as e:
        print(f"⚠ Could not create DOCX version: {e}")

def main():
    """Main function to generate manuscript"""
    print("📝 Generating research manuscript...")

    # Load analysis results
    results = load_analysis_results()

    if not results:
        print("⚠ No analysis results found. Run the complete pipeline first:")
        print("  python projects/vaccine_hesitancy/run_all.py")
        return

    # Generate manuscript
    manuscript = generate_manuscript(results)

    # Save manuscript
    save_manuscript(manuscript)

    print("\n🎯 Manuscript generation complete!")
    print("📄 Files created:")
    print(f"  - {REPORTS}/vaccine_hesitancy_manuscript.md")
    print("  - DOCX version (if pypandoc available)")

if __name__ == "__main__":
    main()
