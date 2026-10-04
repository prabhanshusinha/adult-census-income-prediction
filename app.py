import streamlit as st
import pandas as pd
import joblib


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(
    "adult_census_income_prediction.joblib"
)

le = joblib.load(
    "label_encoder.joblib"
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Adult Census Income Prediction",
    page_icon="💰",
    layout="wide"
)


# ============================================================
# HEADER IMAGE
# ============================================================

st.image(
    "D:\streamlit\ADULT_CENSUS_INCOME\Adult Census Income Prediction Dashboard.png",
    use_container_width=True
)


# ============================================================
# TITLE
# ============================================================

st.title("💰 Adult Census Income Prediction")

st.write(
    "Use the sidebar to enter the person's details and predict "
    "whether their annual income is **<=50K** or **>50K**."
)

st.divider()


# ============================================================
# EDUCATION MAPPING
# ============================================================

education_mapping = {

    "Preschool": 1,
    "1st-4th": 2,
    "5th-6th": 3,
    "7th-8th": 4,
    "9th": 5,
    "10th": 6,
    "11th": 7,
    "12th": 8,
    "HS-grad": 9,
    "Some-college": 10,
    "Assoc-voc": 11,
    "Assoc-acdm": 12,
    "Bachelors": 13,
    "Masters": 14,
    "Prof-school": 15,
    "Doctorate": 16

}


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("👤 Person Details")

st.sidebar.write(
    "Enter the information below."
)

st.sidebar.divider()


# ============================================================
# AGE
# ============================================================

age = st.sidebar.slider(
    "Age",
    min_value=17,
    max_value=100,
    value=30
)


# ============================================================
# WORKCLASS
# ============================================================

workclass = st.sidebar.selectbox(
    "Workclass",
    [
        "Private",
        "Self-emp-not-inc",
        "Self-emp-inc",
        "Federal-gov",
        "Local-gov",
        "State-gov",
        "Without-pay",
        "Never-worked"
    ]
)


# ============================================================
# EDUCATION
# ============================================================

education = st.sidebar.selectbox(
    "Education",
    [
        "Bachelors",
        "Some-college",
        "11th",
        "HS-grad",
        "Masters",
        "9th",
        "Doctorate",
        "Assoc-acdm",
        "Assoc-voc",
        "7th-8th",
        "12th",
        "10th",
        "1st-4th",
        "5th-6th",
        "Preschool"
    ]
)


# Automatically calculate education.num
education_num = education_mapping[education]


# ============================================================
# MARITAL STATUS
# ============================================================

marital_status = st.sidebar.selectbox(
    "Marital Status",
    [
        "Married-civ-spouse",
        "Divorced",
        "Never-married",
        "Separated",
        "Widowed",
        "Married-spouse-absent",
        "Married-AF-spouse"
    ]
)


# ============================================================
# OCCUPATION
# ============================================================

occupation = st.sidebar.selectbox(
    "Occupation",
    [
        "Tech-support",
        "Craft-repair",
        "Other-service",
        "Sales",
        "Exec-managerial",
        "Prof-specialty",
        "Handlers-cleaners",
        "Machine-op-inspct",
        "Adm-clerical",
        "Farming-fishing",
        "Transport-moving",
        "Priv-house-serv",
        "Protective-serv",
        "Armed-Forces"
    ]
)


# ============================================================
# RELATIONSHIP
# ============================================================

relationship = st.sidebar.selectbox(
    "Relationship",
    [
        "Wife",
        "Own-child",
        "Husband",
        "Not-in-family",
        "Other-relative",
        "Unmarried"
    ]
)


# ============================================================
# RACE
# ============================================================

race = st.sidebar.selectbox(
    "Race",
    [
        "White",
        "Asian-Pac-Islander",
        "Amer-Indian-Eskimo",
        "Other",
        "Black"
    ]
)


# ============================================================
# SEX
# ============================================================

sex = st.sidebar.selectbox(
    "Sex",
    [
        "Male",
        "Female"
    ]
)


# ============================================================
# CAPITAL GAIN
# ============================================================

capital_gain = st.sidebar.slider(
    "Capital Gain",
    min_value=0,
    max_value=100000,
    value=0,
    step=100
)


# ============================================================
# CAPITAL LOSS
# ============================================================

capital_loss = st.sidebar.slider(
    "Capital Loss",
    min_value=0,
    max_value=5000,
    value=0,
    step=100
)


# ============================================================
# HOURS PER WEEK
# ============================================================

hours_per_week = st.sidebar.slider(
    "Hours per Week",
    min_value=1,
    max_value=100,
    value=40
)


# ============================================================
# NATIVE COUNTRY
# ============================================================

native_country = st.sidebar.selectbox(
    "Native Country",
    [
        "United-States",
        "Cambodia",
        "Canada",
        "China",
        "Columbia",
        "Cuba",
        "Dominican-Republic",
        "Ecuador",
        "El-Salvador",
        "England",
        "France",
        "Germany",
        "Greece",
        "Guatemala",
        "Haiti",
        "Holand-Netherlands",
        "Honduras",
        "Hong",
        "Hungary",
        "India",
        "Iran",
        "Ireland",
        "Italy",
        "Jamaica",
        "Japan",
        "Laos",
        "Mexico",
        "Nicaragua",
        "Outlying-US(Guam-USVI-etc)",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Puerto-Rico",
        "Scotland",
        "South",
        "Taiwan",
        "Thailand",
        "Trinadad&Tobago",
        "Vietnam",
        "Yugoslavia"
    ]
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.sidebar.divider()

predict_button = st.sidebar.button(
    "🔮 Predict Income",
    use_container_width=True
)


# ============================================================
# MAIN AREA
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame({

        "age": [age],

        "workclass": [workclass],

        "education": [education],

        "education.num": [education_num],

        "marital.status": [marital_status],

        "occupation": [occupation],

        "relationship": [relationship],

        "race": [race],

        "sex": [sex],

        "capital.gain": [capital_gain],

        "capital.loss": [capital_loss],

        "hours.per.week": [hours_per_week],

        "native.country": [native_country]

    })


    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(
        input_data
    )

    prediction_label = le.inverse_transform(
        prediction
    )[0]


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.subheader("📊 Prediction Result")


    if prediction_label == ">50K":

        st.success(
            f"## 💰 Predicted Income: {prediction_label}"
        )

    else:

        st.info(
            f"## 💼 Predicted Income: {prediction_label}"
        )


    # ========================================================
    # PREDICTION PROBABILITY
    # ========================================================

    st.divider()

    st.subheader("📈 Prediction Probability")

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_data
        )[0]

        probability_data = pd.DataFrame({

            "Income Class": le.classes_,

            "Probability": probabilities

        })

        probability_data = probability_data.set_index(
            "Income Class"
        )

        st.bar_chart(
            probability_data,
            y="Probability",
            use_container_width=True
        )

        st.caption(
            "Probability estimated by the Random Forest classifier."
        )


    # ========================================================
    # FINANCIAL PROFILE
    # ========================================================

    st.divider()

    st.subheader("💰 Financial Profile")

    financial_data = pd.DataFrame(

        {
            "Amount": [
                capital_gain,
                capital_loss
            ]
        },

        index=[
            "Capital Gain",
            "Capital Loss"
        ]

    )

    st.bar_chart(
        financial_data,
        y="Amount",
        use_container_width=True
    )


    # ========================================================
    # PERSONAL PROFILE
    # ========================================================

    st.divider()

    st.subheader("👤 Personal Profile")

    profile_data = pd.DataFrame(

        {
            "Value": [
                age,
                education_num,
                hours_per_week
            ]
        },

        index=[
            "Age",
            "Education Number",
            "Hours per Week"
        ]

    )

    st.bar_chart(
        profile_data,
        y="Value",
        use_container_width=True
    )


    # ========================================================
    # INPUT SUMMARY
    # ========================================================

    st.divider()

    st.subheader("📋 Input Summary")

    display_data = pd.DataFrame({

        "Feature": [

            "Age",
            "Workclass",
            "Education",
            "Education Number",
            "Marital Status",
            "Occupation",
            "Relationship",
            "Race",
            "Sex",
            "Capital Gain",
            "Capital Loss",
            "Hours per Week",
            "Native Country"

        ],

        "Value": [

            age,
            workclass,
            education,
            education_num,
            marital_status,
            occupation,
            relationship,
            race,
            sex,
            capital_gain,
            capital_loss,
            hours_per_week,
            native_country

        ]

    })


    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# INITIAL SCREEN
# ============================================================

else:

    st.info(
        "👈 Enter the person's details in the sidebar "
        "and click **Predict Income**."
    )


# ============================================================
# ABOUT THE MODEL
# ============================================================

st.divider()

st.subheader("🧠 About the Model")


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        """
        ### 📊 Dataset

        **Adult Census Income**

        Used to predict annual income
        based on demographic and
        employment information.
        """
    )


with col2:

    st.info(
        """
        ### 🌲 Model

        **Random Forest Classifier**

        The trained preprocessing
        pipeline is stored with the
        model in the `.joblib` file.
        """
    )


with col3:

    st.info(
        """
        ### 🎯 Prediction

        The model predicts one of:

        **<=50K**

        **>50K**
        """
    )


# ============================================================
# DASHBOARD IMAGE
# ============================================================

st.divider()

st.subheader("📈 Machine Learning Dashboard")

st.image(
    "D:\streamlit\ADULT_CENSUS_INCOME\Dark Adult Census Income Dashboard.png",
    caption="Adult Census Income Prediction — Data Analytics Dashboard",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Built with Python • Pandas • Scikit-learn • Random Forest • Streamlit"
)