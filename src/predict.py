import joblib
import pandas as pd


MODEL_PATH = "models/churn_model.pkl"


def load_model():
    """Kaydedilmiş churn modelini yükler."""
    return joblib.load(MODEL_PATH)


def predict_churn(customer_data):
    """
    Bir müşterinin churn olasılığını tahmin eder.
    """

    model = load_model()

    # Dictionary -> DataFrame
    df = pd.DataFrame([customer_data])

    # Churn olasılığı
    probability = model.predict_proba(df)[0][1]

    # %50 eşik
    prediction = int(probability >= 0.50)

    # Risk seviyesi
    if probability >= 0.70:
        risk_level = "High"
    elif probability >= 0.40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "Churn_Probability": round(float(probability), 4),
        "Risk_Level": risk_level,
        "Predicted_Churn": prediction
    }


if __name__ == "__main__":

    # Örnek müşteri
    example_customer = {
        "gender": "Female",
        "SeniorCitizen": 1,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 8,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 100.15,
        "TotalCharges": 908.55,
        "EstimatedLifetimeValue": 801.20,
        "IsNewCustomer": 0
    }

    result = predict_churn(example_customer)

    print("Churn Tahmin Sonucu")
    print("-------------------")
    print(f"Churn Probability: {result['Churn_Probability']}")
    print(f"Risk Level: {result['Risk_Level']}")
    print(f"Predicted Churn: {result['Predicted_Churn']}")