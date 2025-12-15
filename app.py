import streamlit as st
import pickle
from utils import transform_text, get_custom_css

# Page configuration
st.set_page_config(
    page_title="Network Security - Spam Threat Detection",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Load models
tfidf = pickle.load(open('model/vectorizer.pkl','rb'))
model = pickle.load(open('model/model.pkl','rb'))

# Header with cybersecurity theme
st.markdown("""
    <div class="header-container">
        <p class="title-text">🔒 NETWORK SECURITY</p>
        <p class="subtitle-text">[ SPAM THREAT DETECTION SYSTEM ]</p>
        <center><span class="security-badge">⚡ AI-POWERED THREAT ANALYSIS ⚡</span></center>
    </div>
""", unsafe_allow_html=True)

# Information box
st.markdown("""
    <div class="info-box">
        <h4>🛡️ SYSTEM INFORMATION:</h4>
        <p><b>Purpose:</b> Real-time detection and classification of malicious spam messages using Natural Language Processing and Machine Learning algorithms.</p>
        <p><b>Method:</b> Advanced text vectorization with TF-IDF and trained classification model.</p>
        <p><b>Status:</b> <span style="color: #00ff41;">● SYSTEM ONLINE</span></p>
    </div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Text input area
    input_sms = st.text_area(
        "📨 INPUT MESSAGE FOR THREAT ANALYSIS:",
        height=150,
        placeholder="[Enter suspicious message content here for security analysis...]",
        help="Paste the complete message text for threat assessment"
    )
    
    # Predict button
    predict_button = st.button('⚡ INITIATE THREAT SCAN', use_container_width=True)
    
    if predict_button:
        if input_sms.strip() == "":
            st.warning("⚠️ ERROR: No input detected. Please enter message content for analysis.")
        else:
            with st.spinner('🔄 SCANNING... Analyzing threat patterns...'):
                # 1. preprocess
                transformed_sms = transform_text(input_sms)
                # 2. vectorize
                vector_input = tfidf.transform([transformed_sms])
                # 3. predict
                result = model.predict(vector_input)[0]
                # 4. Get prediction probability
                try:
                    proba = model.predict_proba(vector_input)[0]
                    confidence = max(proba) * 100
                except:
                    confidence = None
                
                # 5. Display result with cybersecurity theme
                if result == 1:
                    threat_level = "CRITICAL" if confidence and confidence > 90 else "HIGH" if confidence and confidence > 75 else "MEDIUM"
                    st.markdown(f"""
                        <div class="result-box spam-box">
                            <div class="result-icon">🚨</div>
                            <div class="result-text spam-text">⚠ THREAT DETECTED ⚠</div>
                            <div class="threat-level" style="background: rgba(255,23,68,0.3); color: #ff1744; border: 2px solid #ff1744;">
                                THREAT LEVEL: {threat_level}
                            </div>
                            {f'<div class="confidence-text" style="color: #ff6b6b;">Detection Confidence: {confidence:.2f}%</div>' if confidence else ''}
                            <p style="color: #ffcccb; margin-top: 1.5rem; font-size: 1rem; font-family: Share Tech Mono, monospace;">
                                <b>⚠️ SECURITY ALERT:</b> This message has been classified as SPAM/MALICIOUS content.<br/>
                                <b>Recommended Action:</b> Delete immediately. Do not click links or respond.<br/>
                                <b>Risk:</b> Potential phishing attempt or malware distribution.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="result-box not-spam-box">
                            <div class="result-icon">✅</div>
                            <div class="result-text safe-text">✓ SECURE MESSAGE ✓</div>
                            <div class="threat-level" style="background: rgba(0,230,118,0.3); color: #00e676; border: 2px solid #00e676;">
                                THREAT LEVEL: NONE
                            </div>
                            {f'<div class="confidence-text" style="color: #69f0ae;">Detection Confidence: {confidence:.2f}%</div>' if confidence else ''}
                            <p style="color: #b9f6ca; margin-top: 1.5rem; font-size: 1rem; font-family: Share Tech Mono, monospace;">
                                <b>✓ SECURITY STATUS:</b> Message classified as LEGITIMATE communication.<br/>
                                <b>Assessment:</b> No malicious patterns detected.<br/>
                                <b>Status:</b> Safe to proceed with normal caution.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

# Sidebar with network security information
with st.sidebar:
    st.markdown("### 🎓 PROJECT DETAILS")
    st.markdown("""
    <div class="sidebar-box">
    <b>Subject:</b> Network Security<br/>
    <b>Project:</b> Email/SMS Spam Detection<br/>
    <b>Technology:</b> Machine Learning & NLP<br/>
    <b>Algorithm:</b> Supervised Classification
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔐 SECURITY FEATURES")
    st.markdown("""
    <div class="sidebar-box">
    ✔ Real-time Threat Detection<br/>
    ✔ NLP-based Text Analysis<br/>
    ✔ TF-IDF Vectorization<br/>
    ✔ High-Accuracy ML Model<br/>
    ✔ Instant Classification<br/>
    ✔ Zero Data Storage
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🛡️ THREAT TYPES")
    st.markdown("""
    <div class="sidebar-box" style="border-color: rgba(255,23,68,0.5);">
    <b style="color: #ff6b6b;">Common Spam Threats:</b><br/>
    ▪ Phishing Attempts<br/>
    ▪ Fraudulent Offers<br/>
    ▪ Malware Distribution<br/>
    ▪ Social Engineering<br/>
    ▪ Lottery/Prize Scams<br/>
    ▪ Financial Fraud
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚡ BEST PRACTICES")
    st.markdown("""
    <div class="sidebar-box" style="border-color: rgba(0,230,118,0.5);">
    ▪ Verify sender identity<br/>
    ▪ Never click suspicious links<br/>
    ▪ Do not share personal data<br/>
    ▪ Report spam messages<br/>
    ▪ Use strong authentication<br/>
    ▪ Keep systems updated
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <center style="color: #00e676; font-family: 'Share Tech Mono', monospace; font-size: 0.8rem;">
    🔒 Secure System<br/>
    Network Security Project<br/>
    &copy; 2025
    </center>
    """, unsafe_allow_html=True)
