from flask import Flask, render_template, request, jsonify
from urllib.parse import urlsplit
import re

app = Flask(__name__)
PAGES = [
("overview","Overview"),("about","About the research"),("methodology","Methodology"),
("dataset-analysis","Dataset analysis"),("data-preprocessing","Data preprocessing"),
("models","Machine-learning models"),("performance","Performance and evaluation metrics"),
("cross-dataset","Cross-dataset evaluation"),("explainability","Explainability"),
("findings","Research findings"),("limitations","Limitations and responsible use"),
("project-info","Project information")]
CONTENT = {
"overview":[("Research question","When feature extraction is held constant, how well do URL-based classifiers trained on one phishing dataset perform on an independently collected dataset?"),("Research design","Two datasets, one shared URL-feature pipeline and four classifiers evaluated within and across datasets."),("Detection tool","The intended tool analyses URLs as text. It must not visit submitted websites or store submitted URLs.")],
"about":[("Background","Phishing websites imitate trusted services to obtain passwords, payment details or other sensitive information."),("Aim","Evaluate cross-dataset generalisation of URL-based classifiers and identify URL features that remain informative."),("Objectives","Build a reproducible pipeline; compare classifiers; measure transfer; examine feature importance; present the evidence.")],
"methodology":[("Research design","Quantitative controlled experiment using secondary data."),("Controlled variables","Normalisation, cleaning, feature extraction, split policy, tuning budget and threshold rule are held constant."),("Experiments","Bias audit; within-dataset evaluation; random versus grouped split; cross-dataset evaluation; host-only analysis; ablation; explainability.")],
"dataset-analysis":[("Dataset A","PhiUSIIL Phishing URL Dataset. The dissertation uses raw URL strings and labels, not supplied precomputed features."),("Dataset B","A collection described using PhishTank and OpenPhish phishing URLs and real inner-page URLs from popular domains."),("Important","The original dataset files are not included in this recreated website package.")],
"data-preprocessing":[("Normalisation","Remove scheme, leading www, fragment and default port; lower-case host while retaining path and query."),("Cleaning","Remove exact and normalised duplicates, contradictory labels, cap URLs per registered domain and remove shared domains."),("Splitting","The dissertation describes an 80/20 split grouped by registered domain and grouped five-fold cross-validation.")],
"models":[("Logistic Regression","A linear baseline that estimates a phishing probability."),("Linear Support Vector Machine","A linear margin-based classifier."),("Random Forest","An ensemble of decision trees."),("XGBoost","A gradient-boosted tree model.")],
"performance":[("Primary metric","PR-AUC (average precision), selected because class balance affects interpretation."),("Additional metrics","ROC-AUC, precision, recall, F1, false-positive rate, false-negative rate, confusion matrix and Matthews correlation coefficient."),("Uncertainty","Domain-level bootstrap confidence intervals and paired McNemar tests are described in the dissertation.")],
"cross-dataset":[("A to B","Train using Dataset A and evaluate using Dataset B."),("B to A","Train using Dataset B and evaluate using Dataset A."),("Interpretation","Compare transfer performance with within-dataset performance.")],
"explainability":[("SHAP","Explain how features contribute to a model prediction."),("Permutation importance","Estimate performance change when a feature is permuted."),("Caution","Correlated features can distort individual feature-importance rankings.")],
"findings":[("Add your results","This package does not include the original experiment result files. Populate this page from your own verified results."),("Recommended evidence","Include result tables, precision-recall curves, confusion matrices, cross-dataset comparisons and feature-importance plots.")],
"limitations":[("Not a safety guarantee","A model prediction is not proof that a website is safe or malicious."),("URL-only scope","URL features cannot detect every compromised legitimate domain or inspect page content."),("Responsible use","Treat submitted URLs as text. Do not open suspected phishing URLs or store user input.")],
"project-info":[("Technology","Python, Flask, Jinja2, HTML, CSS and JavaScript. The dissertation also describes scikit-learn, XGBoost and SHAP."),("Run locally","Create a virtual environment, install requirements and run python run.py."),("Reproducibility","Record dataset provenance, package versions, random seeds, model artefacts and code for every reported result.")]
}
@app.route("/")
def home():
    return render_template("page.html", pages=PAGES, active="overview", title="Overview", sections=CONTENT["overview"], is_home=True)
@app.route("/page/<slug>")
def page(slug):
    item=next((p for p in PAGES if p[0]==slug),None)
    if not item: return "Page not found",404
    return render_template("page.html", pages=PAGES, active=slug, title=item[1], sections=CONTENT[slug], is_home=False)
@app.route("/api/predict",methods=["POST"])
def predict():
    data=request.get_json(silent=True) or {}
    url=data.get("url","")
    if not isinstance(url,str) or not url.strip(): return jsonify(error="Please enter a URL."),400
    url=url.strip()
    if len(url)>2048: return jsonify(error="The URL is too long."),413
    candidate=url if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://",url) else "https://"+url
    try:
        parsed=urlsplit(candidate)
        if parsed.scheme not in ("http","https") or not parsed.hostname: raise ValueError()
        _=parsed.port
    except Exception: return jsonify(error="Enter a valid HTTP or HTTPS URL."),400
    return jsonify(error="The interface is ready, but the original trained models and matching 34-feature extraction pipeline were not included in the uploaded DOCX. Add verified model artefacts and feature code before enabling predictions."),503
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=False)
