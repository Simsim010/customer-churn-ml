import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# MODEL
# =========================================================

MODEL_PATH = "models/churn_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 25px;
}

.risk-high {
    padding: 25px;
    border-radius: 15px;
    background-color: #ffe5e5;
    text-align: center;
    margin-top: 20px;
}

.risk-medium {
    padding: 25px;
    border-radius: 15px;
    background-color: #fff4cc;
    text-align: center;
    margin-top: 20px;
}

.risk-low {
    padding: 25px;
    border-radius: 15px;
    background-color: #e5f7e5;
    text-align: center;
    margin-top: 20px;
}

.factor {
    padding: 10px;
    margin: 5px 0;
    border-radius: 8px;
    background-color: #f5f5f5;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning tabanlı müşteri kaybı (churn) risk tahmin sistemi'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.header("👤 Customer Information")

col1, col2 = st.columns(2)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )


with col2:

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )


# =========================================================
# FINANCIAL INFORMATION
# =========================================================

st.header("💳 Financial Information")

col3, col4, col5 = st.columns(3)


with col3:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Credit card (automatic)",
            "Bank transfer (automatic)"
        ]
    )


with col4:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )


with col5:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )


estimated_lifetime_value = st.number_input(
    "Estimated Lifetime Value",
    min_value=0.0,
    value=1000.0
)


is_new_customer = st.selectbox(
    "New Customer",
    [0, 1]
)


st.divider()


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button(
    "🔮 Analyze Churn Risk",
    use_container_width=True
):

    # -----------------------------------------------------
    # CREATE CUSTOMER DATA
    # -----------------------------------------------------

    customer_data = pd.DataFrame([{

        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "EstimatedLifetimeValue": estimated_lifetime_value,
        "IsNewCustomer": is_new_customer

    }])


    # -----------------------------------------------------
    # MODEL PREDICTION
    # -----------------------------------------------------

    probability = model.predict_proba(
        customer_data
    )[0][1]


    prediction = int(
        probability >= 0.50
    )


    # -----------------------------------------------------
    # RISK LEVEL
    # -----------------------------------------------------

    if probability >= 0.70:

        risk_level = "High"

    elif probability >= 0.40:

        risk_level = "Medium"

    else:

        risk_level = "Low"


    # =====================================================
    # RESULTS
    # =====================================================

    st.divider()

    st.header("📊 Churn Risk Analysis")


    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )


    with result_col2:

        st.metric(
            "Risk Level",
            risk_level
        )


    with result_col3:

        st.metric(
            "Predicted Churn",
            "Yes" if prediction == 1 else "No"
        )


    # -----------------------------------------------------
    # PROBABILITY BAR
    # -----------------------------------------------------

    st.subheader("Churn Probability")

    st.progress(
        probability
    )


    # =====================================================
    # RISK MESSAGE
    # =====================================================

    if risk_level == "High":

        st.markdown(
            f"""
            <div class="risk-high">

            <h2>🔴 High Risk Customer</h2>

            <p>
            Bu müşterinin churn olasılığı
            <strong>{probability:.2%}</strong>.
            </p>

            <p>
            Müşteriyi elde tutmaya yönelik aksiyonların
            değerlendirilmesi önerilir.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    elif risk_level == "Medium":

        st.markdown(
            f"""
            <div class="risk-medium">

            <h2>🟡 Medium Risk Customer</h2>

            <p>
            Bu müşterinin churn olasılığı
            <strong>{probability:.2%}</strong>.
            </p>

            <p>
            Müşteri davranışlarının yakından takip edilmesi
            önerilir.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    else:

        st.markdown(
            f"""
            <div class="risk-low">

            <h2>🟢 Low Risk Customer</h2>

            <p>
            Bu müşterinin churn olasılığı
            <strong>{probability:.2%}</strong>.
            </p>

            <p>
            Mevcut müşteri ilişkisinin korunması önerilir.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # RISK FACTOR ANALYSIS
    # =====================================================

    st.divider()

    st.header("🧠 Risk Factor Analysis")

    st.write(
        "Girilen müşteri profiline göre churn riskini "
        "artırabilecek temel faktörler:"
    )


    risk_factors = []


    if contract == "Month-to-month":

        risk_factors.append(
            "🔴 Month-to-month contract"
        )


    if internet_service == "Fiber optic":

        risk_factors.append(
            "🔴 Fiber optic internet service"
        )


    if tenure < 12:

        risk_factors.append(
            "🔴 Low customer tenure"
        )


    if online_security == "No":

        risk_factors.append(
            "🔴 No online security"
        )


    if tech_support == "No":

        risk_factors.append(
            "🔴 No technical support"
        )


    if payment_method == "Electronic check":

        risk_factors.append(
            "🔴 Electronic check payment method"
        )


    if monthly_charges >= 80:

        risk_factors.append(
            "🔴 High monthly charges"
        )


    if is_new_customer == 1:

        risk_factors.append(
            "🔴 New customer"
        )


    if risk_factors:

        for factor in risk_factors:

            st.markdown(
                f'<div class="factor">{factor}</div>',
                unsafe_allow_html=True
            )

    else:

        st.success(
            "Bu müşteri profili için belirgin bir yüksek-risk "
            "faktörü tespit edilmedi."
        )


    # =====================================================
    # RECOMMENDED ACTION
    # =====================================================

    st.divider()

    st.header("💡 Recommended Action")


    if risk_level == "High":

        st.warning(
            "Bu müşteri yüksek churn riski taşıyor. "
            "Kişiselleştirilmiş retention kampanyası, "
            "indirim veya sözleşme yükseltme teklifleri "
            "değerlendirilebilir."
        )


    elif risk_level == "Medium":

        st.info(
            "Bu müşteri orta seviyede churn riski taşıyor. "
            "Müşteri davranışlarının izlenmesi ve "
            "erken müdahale stratejileri uygulanması önerilir."
        )


    else:

        st.success(
            "Bu müşterinin churn riski düşük. "
            "Mevcut müşteri memnuniyetinin korunmasına "
            "odaklanılması önerilir."
        )


    # =====================================================
    # CUSTOMER DATA
    # =====================================================

    with st.expander("🔎 View Customer Data"):

        st.dataframe(
            customer_data,
            use_container_width=True
        )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📌 About the Model")

    st.write(
        "Bu uygulama, müşterilerin churn etme "
        "olasılığını tahmin etmek için Machine Learning "
        "tabanlı bir Logistic Regression modeli kullanır."
    )

    st.divider()

    st.write("**Model:** Logistic Regression")

    st.write("**ROC-AUC:** 0.847")

    st.write("**Recall:** 0.800")

    st.write("**F1 Score:** 0.630")

    st.divider()

    st.caption(
        "Customer Churn Prediction Project"
    )


    # =========================================================
# MODEL PERFORMANCE
# =========================================================

st.divider()

st.header("📈 Model Performance")

st.write(
    "Model, müşteri churn tahmini için test veri seti üzerinde "
    "değerlendirilmiştir."
)


# ---------------------------------------------------------
# PERFORMANCE METRICS
# ---------------------------------------------------------

metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:

    st.metric(
        "Accuracy",
        "75.1%"
    )


with metric2:

    st.metric(
        "Precision",
        "52.0%"
    )


with metric3:

    st.metric(
        "Recall",
        "80.0%"
    )


with metric4:

    st.metric(
        "ROC-AUC",
        "84.7%"
    )


st.divider()


# ---------------------------------------------------------
# MODEL COMPARISON
# ---------------------------------------------------------

st.subheader("🤖 Model Comparison")


model_comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "Gradient Boosting"
    ],

    "Accuracy": [
        0.751,
        0.762,
        0.797
    ],

    "Precision": [
        0.520,
        0.536,
        0.643
    ],

    "Recall": [
        0.800,
        0.772,
        0.528
    ],

    "F1 Score": [
        0.630,
        0.633,
        0.579
    ],

    "ROC-AUC": [
        0.847,
        0.846,
        0.840
    ]
})


st.dataframe(
    model_comparison.style.format({
        "Accuracy": "{:.1%}",
        "Precision": "{:.1%}",
        "Recall": "{:.1%}",
        "F1 Score": "{:.1%}",
        "ROC-AUC": "{:.1%}"
    }),
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# MODEL INTERPRETATION
# ---------------------------------------------------------

st.subheader("🎯 Model Interpretation")

st.info(
    """
    **Logistic Regression** modeli tercih edilmiştir çünkü churn 
    problemlerinde yalnızca tahmin yapmak değil, model sonuçlarını 
    yorumlayabilmek de önemlidir.

    Modelin ROC-AUC skoru **0.847** olup müşterileri churn 
    eğilimine göre ayırt etme konusunda güçlü bir performans 
    göstermektedir.

    Recall değerinin **%80** olması, gerçek churn edecek 
    müşterilerin önemli bir bölümünün yakalanabildiğini 
    göstermektedir.
    """
)


# ---------------------------------------------------------
# CONFUSION MATRIX VALUES
# ---------------------------------------------------------

st.subheader("🔍 Confusion Matrix")

cm_col1, cm_col2, cm_col3, cm_col4 = st.columns(4)


with cm_col1:

    st.metric(
        "True Negative",
        "744"
    )


with cm_col2:

    st.metric(
        "False Positive",
        "291"
    )


with cm_col3:

    st.metric(
        "False Negative",
        "77"
    )


with cm_col4:

    st.metric(
        "True Positive",
        "297"
    )