# Recreated Phishing Research Website

This is a recreation based on the website description and screenshots in the uploaded dissertation. It is not the author's original source repository.

## Included
- Flask site with 12 research sections and responsive navigation.
- Overview with cross-dataset experiment matrix.
- URL input form and `POST /api/predict` endpoint.
- URL validation without fetching or opening the submitted website.

## Model integration limitation
The uploaded DOCX describes eight trained model instances, a 34-feature URL pipeline, SHAP explanations and a stored results bundle. It does not include the original source repository, trained model files, complete feature extraction code or results bundle. Therefore, the prediction endpoint intentionally returns HTTP 503 rather than inventing a prediction. Add the matching, verified feature extractor and model artefacts to enable real predictions.

## Run on Windows
1. Extract this ZIP.
2. Open the extracted folder in VS Code or PyCharm.
3. Open a terminal in that folder.
4. Run `python -m venv .venv`
5. Activate it: PowerShell `.\.venv\Scripts\Activate.ps1` or CMD `.venv\Scripts\activate`
6. Run `python -m pip install -r requirements.txt`
7. Run `python run.py`
8. Open http://127.0.0.1:5000/

This is a local educational prototype, not a production security service. Do not enter passwords or sensitive information.
