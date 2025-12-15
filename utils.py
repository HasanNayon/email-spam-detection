import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def transform_text(text):
    """Transform input text using NLP preprocessing techniques"""
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

def get_custom_css():
    """Return custom CSS for cybersecurity theme"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
        color: #00ff41;
    }
    .main {
        background: transparent;
        padding: 1rem;
    }
    .header-container {
        background: linear-gradient(135deg, rgba(0,255,65,0.1) 0%, rgba(0,230,118,0.05) 100%);
        border: 2px solid #00ff41;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 30px rgba(0,255,65,0.3);
        position: relative;
        overflow: hidden;
    }
    .header-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,255,65,0.2), transparent);
        animation: scan 3s infinite;
    }
    @keyframes scan {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    .title-text {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 900;
        color: #00ff41;
        font-family: 'Orbitron', sans-serif;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px rgba(0,255,65,0.8), 0 0 40px rgba(0,255,65,0.5);
        letter-spacing: 3px;
    }
    .subtitle-text {
        text-align: center;
        font-size: 1.1rem;
        color: #00e676;
        font-family: 'Share Tech Mono', monospace;
        margin-bottom: 1rem;
        text-shadow: 0 0 10px rgba(0,230,118,0.5);
    }
    .security-badge {
        text-align: center;
        font-size: 0.9rem;
        color: #64ffda;
        font-family: 'Share Tech Mono', monospace;
        padding: 0.5rem;
        border: 1px solid #00e676;
        border-radius: 5px;
        display: inline-block;
        margin: 0 auto;
        background: rgba(0,230,118,0.1);
    }
    .result-box {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 0 40px rgba(0,0,0,0.8);
        animation: fadeIn 0.5s;
        border: 3px solid;
        position: relative;
    }
    .spam-box {
        background: linear-gradient(135deg, rgba(255,23,68,0.2) 0%, rgba(139,0,0,0.3) 100%);
        border-color: #ff1744;
        box-shadow: 0 0 50px rgba(255,23,68,0.6);
    }
    .not-spam-box {
        background: linear-gradient(135deg, rgba(0,230,118,0.2) 0%, rgba(0,200,83,0.3) 100%);
        border-color: #00e676;
        box-shadow: 0 0 50px rgba(0,230,118,0.6);
    }
    .result-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 10px currentColor);
    }
    .result-text {
        font-size: 2.2rem;
        font-weight: 900;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 20px currentColor;
        letter-spacing: 2px;
    }
    .spam-text {
        color: #ff1744;
    }
    .safe-text {
        color: #00e676;
    }
    .confidence-text {
        font-size: 1.1rem;
        margin-top: 1rem;
        opacity: 0.9;
        font-family: 'Share Tech Mono', monospace;
    }
    .threat-level {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: 700;
        margin-top: 1rem;
        font-family: 'Orbitron', sans-serif;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00e676 0%, #00c853 100%);
        color: #0a0e27;
        font-size: 1.2rem;
        font-weight: 700;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: 2px solid #00ff41;
        box-shadow: 0 0 30px rgba(0,230,118,0.5);
        transition: all 0.3s ease;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 50px rgba(0,230,118,0.8);
        background: linear-gradient(135deg, #00ff41 0%, #00e676 100%);
    }
    .info-box {
        background: linear-gradient(135deg, rgba(100,255,218,0.1) 0%, rgba(0,230,118,0.1) 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #00e676;
        margin-bottom: 2rem;
        color: #64ffda;
        border: 1px solid rgba(0,230,118,0.3);
        font-family: 'Share Tech Mono', monospace;
    }
    .info-box h4 {
        color: #00ff41;
        font-family: 'Orbitron', sans-serif;
    }
    .stTextArea textarea {
        background-color: rgba(10,14,39,0.8) !important;
        color: #00ff41 !important;
        border: 2px solid #00e676 !important;
        border-radius: 10px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 1rem !important;
    }
    .stTextArea label {
        color: #00ff41 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1a2e 100%);
        border-right: 2px solid #00e676;
    }
    section[data-testid="stSidebar"] .block-container {
        color: #00ff41;
    }
    section[data-testid="stSidebar"] h3 {
        color: #00ff41 !important;
        font-family: 'Orbitron', sans-serif !important;
        text-shadow: 0 0 10px rgba(0,255,65,0.5);
    }
    .sidebar-box {
        background: rgba(0,230,118,0.1);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid rgba(0,230,118,0.3);
        margin-bottom: 1rem;
        color: #64ffda;
        font-family: 'Share Tech Mono', monospace;
    }
    </style>
    """
