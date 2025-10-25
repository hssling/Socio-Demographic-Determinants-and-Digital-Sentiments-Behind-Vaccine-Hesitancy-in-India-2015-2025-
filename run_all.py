import subprocess, sys
def run(c): print("==>",c); r=subprocess.run(c,shell=True);
run(sys.executable + " projects/vaccine_hesitancy/scripts/data_extraction.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/clean_data.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/twitter_sentiment.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/analyze_factors.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/generate_visualizations.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/generate_manuscript.py")
print("🎯 Complete analysis pipeline finished!")
print("📊 Results available in: projects/vaccine_hesitancy/outputs/")
print("📈 Visualizations: projects/vaccine_hesitancy/outputs/plots/")
print("📄 Manuscript: projects/vaccine_hesitancy/outputs/reports/vaccine_hesitancy_manuscript.md")
print("🚀 Launch dashboard with:\nstreamlit run projects/vaccine_hesitancy/dashboards/app.py")
