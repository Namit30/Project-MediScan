import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie


# loading the saved models

diabetes_model = pickle.load(open('C:\\Users\\nishi\\Desktop\\project\\trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:\\Users\\nishi\\Desktop\\project\\heart_disease\\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:\\Users\\nishi\\Desktop\\project\\parkinsoz\\parkinsons_model.sav', 'rb'))





# Sidebar menu as a panel on the left side
with st.sidebar:
    selected = option_menu(
        'MediScan',
        ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'About Us'],
        icons=['house', 'activity', 'heart', 'person', 'people-fill'],
        default_index=0
    )

# Custom CSS to enhance your website
st.markdown(
    """
    <style>
    .background {
        background: url('https://i.postimg.cc/8CD7pVXp/240-F-822344329-1c-ABb-Vqe5m-RI7293hp5ltuip-MRLx-KKjt.jpg') no-repeat center center fixed;
        background-size: cover;
        height: 100vh;
        color: #fff; /* Text color to ensure readability on background image */
    }
    .font {
        font-size: 60px; 
        text-align: center; 
        font-weight: bold; 
        font-family: 'Courier New'; 
        background: linear-gradient(45deg, #00FF00, #008000); /* Gradient green */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
        animation: glow 1.5s ease-in-out infinite;
        margin-bottom: 20px;
    }
    @keyframes glow {
        0% {
            text-shadow: 0 0 5px #00FF00, 0 0 10px #00FF00, 0 0 15px #00FF00, 0 0 20px #008000, 0 0 25px #008000, 0 0 30px #008000, 0 0 35px #008000;
        }
        50% {
            text-shadow: 0 0 10px #00FF00, 0 0 20px #00FF00, 0 0 30px #00FF00, 0 0 40px #008000, 0 0 50px #008000, 0 0 60px #008000, 0 0 70px #008000;
        }
        100% {
            text-shadow: 0 0 5px #00FF00, 0 0 10px #00FF00, 0 0 15px #00FF00, 0 0 20px #008000, 0 0 25px #008000, 0 0 30px #008000, 0 0 35px #008000;
        }
    }
    .content {
        color: grey; 
        font-size: 18px; 
        font-family: 'Georgia'; 
        font-weight: bold; 
        margin-bottom: 20px;
        background: rgba(0, 0, 0, 0.5); /* Semi-transparent background for better readability */
        padding: 20px;
        border-radius: 10px;
    }
    .image-container {
        text-align: center; /* Center-align images within the container */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home
if selected == 'Home':
    st.markdown('<p class="font">MediScan ⚕️</p>', unsafe_allow_html=True)

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(
        "https://cdn0.iconfinder.com/data/icons/medical-services-2-1/256/Doctor_on_Duty-512.png",
        width=500
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write(
        "<p class='content'>Our web application stands at the intersection of healthcare⚕️ and technology, "
        "empowered by cutting-edge Python models that predict a spectrum of health conditions. The realm of modern healthcare "
        "confronts numerous complex challenges, such as limited accessibility to comprehensive health data, potential inaccuracies "
        "in diagnostics, and the need for personalized treatment plans.</p>",
        unsafe_allow_html=True
    )
    st.write(
        "<p class='content'>At the core of our mission is the goal to democratize healthcare. We aspire to mitigate disparities in "
        "healthcare access and empower individuals by leveraging technology. Our app embodies this vision, emphasizing the transformative "
        "role of technology in the medical landscape. Through our initiative, we envision a future where informed and proactive healthcare "
        "decisions are within reach of all.</p>",
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.write('</div>', unsafe_allow_html=True)







# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Diabetes Prediction</p>",unsafe_allow_html=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        missing_fields = []

# Check each field and add to the list if empty
        if not Pregnancies:
            missing_fields.append('Number of Pregnancies')
        if not Glucose:
            missing_fields.append('Glucose Level')
        if not BloodPressure:
            missing_fields.append('Blood Pressure value')
        if not SkinThickness:
            missing_fields.append('Skin Thickness value')
        if not Insulin:
            missing_fields.append('Insulin Level')
        if not BMI:
            missing_fields.append('BMI value')
        if not DiabetesPedigreeFunction:
            missing_fields.append('Diabetes Pedigree Function value')
        if not Age:
            missing_fields.append('Age of the Person')

        if missing_fields:
            st.error(f"Please fill in the following fields: {', '.join(missing_fields)}")
        if not (Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age):
            st.error("\nAll fields are required!")
        else:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        
            st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Heart Disease Prediction</p>",unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction

        
    if st.button('Heart Disease Test Result'):
       missing_fields = []
       
       if not age:
           missing_fields.append('Age')
       if not sex:
           missing_fields.append('Sex')
       if not cp:
           missing_fields.append('Chest Pain types')
       if not trestbps:
           missing_fields.append('Resting Blood Pressure')
       if not chol:
           missing_fields.append('Serum Cholestoral in mg/dl')
       if not fbs:
           missing_fields.append('Fasting Blood Sugar > 120 mg/dl')
       if not restecg:
           missing_fields.append('Resting Electrocardiographic results')
       if not thalach:
           missing_fields.append('Maximum Heart Rate achieved')
       if not exang:
           missing_fields.append('Exercise Induced Angina')
       if not oldpeak:
           missing_fields.append('ST depression induced by exercise')
       if not slope:
           missing_fields.append('Slope of the peak exercise ST segment')
       if not ca:
           missing_fields.append('Major vessels colored by flourosopy')
       if not thal:
           missing_fields.append('thal')
       
       if missing_fields:
           st.error(f"Please fill in the following fields: {', '.join(missing_fields)}")
       if not (age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal):
            st.error("All fields are required!")
            
       else:
        
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])                       
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
  
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Parkinson's Disease Prediction</p>",unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    
    if st.button("Parkinson's Test Result"):
        missing_fields = []
        
        if not fo:
            missing_fields.append('MDVP:Fo(Hz)')
        if not fhi:
            missing_fields.append('MDVP:Fhi(Hz)')
        if not flo:
            missing_fields.append('MDVP:Flo(Hz)')
        if not Jitter_percent:
            missing_fields.append('MDVP:Jitter(%)')
        if not Jitter_Abs:
            missing_fields.append('MDVP:Jitter(Abs)')
        if not RAP:
            missing_fields.append('MDVP:RAP')
        if not PPQ:
            missing_fields.append('MDVP:PPQ')
        if not DDP:
            missing_fields.append('Jitter:DDP')
        if not Shimmer:
            missing_fields.append('MDVP:Shimmer')
        if not Shimmer_dB:
            missing_fields.append('MDVP:Shimmer(dB)')
        if not APQ3:
            missing_fields.append('Shimmer:APQ3')
        if not APQ5:
            missing_fields.append('Shimmer:APQ5')
        if not APQ:
            missing_fields.append('MDVP:APQ')
        if not DDA:
            missing_fields.append('Shimmer:DDA')
        if not NHR:
            missing_fields.append('NHR')
        if not HNR:
            missing_fields.append('HNR')
        if not RPDE:
            missing_fields.append('RPDE')
        if not DFA:
            missing_fields.append('DFA')
        if not spread1:
            missing_fields.append('spread1')
        if not spread2:
            missing_fields.append('spread2')
        if not D2:
            missing_fields.append('D2')
        if not PPE:
            missing_fields.append('PPE')
        
        if missing_fields:
            st.error(f"Please fill in the following fields: {', '.join(missing_fields)}")
        if not (fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and RPDE and DFA and spread1 and spread2 and D2 and PPE):
            st.error("All fields are required!")
        else:  
             parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
             if (parkinsons_prediction[0] == 1):
                 parkinsons_diagnosis = "The person has Parkinson's disease"
             else:
                 parkinsons_diagnosis = "The person does not have Parkinson's disease"
      
             st.success(parkinsons_diagnosis)


if (selected == 'About Us'):
    
    # page title
    st.markdown(""" <style> .font {
font-size:50px ; text-align:center; font-weight: bold; font-family: 'Courier New'; color:#98FF98;} 
</style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About Us</p>', unsafe_allow_html=True)

    #desc
    st.write("<p style='color:green ;text-align:center; font-size: 20px;font-family:'Courier New'; font-weight: bold;'>We are a committed team of developers who have crafted a web application employing Python models to predict various health conditions. Our objective is to offer precise forecasts, enabling individuals to take proactive measures in managing their well-being effectively.</p>",unsafe_allow_html=True)
    st.write("---")
    st.write("<p style='color:lightGreen; font-size:40px; font-family:'Courier New';font-weight: bold;'>Our team</p>",unsafe_allow_html=True)
    
    coli3,coli1,coli2=st.columns([1,2,2])

    #Namit-----------------------------------------
    #coli1.image("pp4.jpg",width=120)
    coli1.write("<p style='color:lightgreen; font-size: 25px; font-family: 'Georgia';font-weight: bold;'>Namit Mehrotra</p>",unsafe_allow_html=True)
    
    linkedin_url="https://www.linkedin.com/in/namit0730"
    github_url="https://github.com/namit30"

    
    linkedin_icon="https://static.vecteezy.com/system/resources/previews/017/339/624/original/linkedin-icon-free-png.png"
    github_icon="https://cdn0.iconfinder.com/data/icons/shift-logotypes/32/Github-512.png"
   
    coli1.write("<p style='color:green; font-size:20px; font-family: 'Georgia';font-weight: bold;'>Connect with me</p>",unsafe_allow_html=True)
    coli1.markdown(f'<a href="{github_url}"><img src="{github_icon}" width="40" height="35"></a>'
            f'<a href="{linkedin_url}"><img src="{linkedin_icon}" width="60" height="60"></a>'
            ,unsafe_allow_html=True)
    
    
    


def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by Namit Mehrotra
                &nbsp;
                <a href="https://www.linkedin.com/in/namit0730">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/namit30">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://i.postimg.cc/K8NNNhz1/Screenshot-2024-08-17-112535.jpg", opacity=0.8)
