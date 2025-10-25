import subprocess, sys
def run(c): print("==>",c); r=subprocess.run(c,shell=True);
run(sys.executable + " projects/vaccine_hesitancy/scripts/data_extraction.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/clean_data.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/twitter_sentiment.py")
run(sys.executable + " projects/vaccine_hesitancy/scripts/analyze_factors.py")
print("🎯 Done. Launch dashboard with:\nstreamlit run projects/vaccine_hesitancy/dashboards/app.py")
