import streamlit as st
from save_data import load_user_data

# ==========================================
# 1. إعدادات الصفحة (Page Configuration)
# ==========================================
st.set_page_config(
    page_title="Smart Home Expert System",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# 2. التصميم الاحترافي (Dark & Metallic Gold Theme)
# ==========================================
st.markdown("""
    <style>
    /* خلفية سودة فخمة بتدرج لوني */
    .stApp {
        background: radial-gradient(circle at top right, #1A1A24, #0B0C10) !important;
        color: #E2E8F0 !important;
    }
    
    /* العناوين تبقى ذهبي معدني */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        font-weight: bold !important;
    }
    
    /* ألوان الأزرار (ذهبي معدني متوهج) */
    .stButton > button {
        background: linear-gradient(135deg, #D4AF37, #AA7700) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important;
    }
    
    /* كروت الأرقام في الرئيسية (زجاجية وحدودها ذهبية) */
    div[data-testid="stMetric"] {
        background: rgba(26, 26, 36, 0.8) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5) !important;
    }
    
    div[data-testid="stMetric"] label {
        color: #A1A1AA !important;
        font-size: 14px !important;
    }
    
    /* الأرقام نفسها ذهبية وكبيرة */
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #D4AF37 !important;
        font-weight: 900 !important;
        font-size: 32px !important;
    }
    
    /* القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #12141D !important;
        border-right: 1px solid rgba(212, 175, 55, 0.2) !important;
    }
    
    /* مربعات الإدخال */
    div[data-baseweb="select"] > div, .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background-color: #1A1A24 !important;
        border: 1px solid #333340 !important;
        color: white !important;
        border-radius: 10px !important;
    }
    
    /* الكروت (زي صفحة الأجهزة) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(26, 26, 36, 0.6) !important;
        border: 1px solid #333340 !important;
        border-radius: 15px !important;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. تهيئة المتغيرات (Session State Defaults)
# ==========================================
defaults = {
    "logged_in": False,
    "profile_completed": False,
    "user_name": "",
    "user_email": "",
    "user_phone": "",
    "home_name": "",
    "home_address": "",
    "rooms": 3,
    "security_log": [],
    "temperature": 24,
    "light_setting": "Auto",
    "ac_enabled": True,
    "heater_enabled": True,
    "ac_status": "OFF",
    "heater_status": "OFF",
    "tv_status": "OFF",
    "smart_light_status": "OFF",
    "garage_door_status": "Closed",
    "camera_status": "ON",
    "vacuum_status": "Charging",
    "smart_lock_status": "Locked",
    "curtain_status": "Closed",
    "speaker_status": "OFF",
    "washer_status": "OFF",
    "dishwasher_status": "OFF",
    "energy_rates": {
        "AC": {"power": 1.5, "water": 0},
        "Heater": {"power": 2.0, "water": 0},
        "TV": {"power": 0.1, "water": 0},
        "Lights": {"power": 0.05, "water": 0},
        "Camera": {"power": 0.01, "water": 0},
        "Vacuum": {"power": 0.8, "water": 0},
        "Lock": {"power": 0.01, "water": 0},
        "Curtains": {"power": 0.02, "water": 0},
        "Speaker": {"power": 0.05, "water": 0},
        "Washer": {"power": 1.0, "water": 50},
        "Dishwasher": {"power": 1.2, "water": 15}
    },
    "home_lat": 30.0444,
    "home_lon": 31.2357,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================
# 4. تحميل البيانات المحفوظة (Load Data)
# ==========================================
saved_data = load_user_data()
if saved_data:
    st.session_state.user_name = saved_data.get("user_name", "")
    st.session_state.user_email = saved_data.get("user_email", "")
    st.session_state.user_phone = saved_data.get("user_phone", "")
    st.session_state.home_name = saved_data.get("home_name", "")
    st.session_state.home_address = saved_data.get("home_address", "")
    st.session_state.rooms = saved_data.get("rooms", 3)
    st.session_state.home_lat = saved_data.get("home_lat", 30.0444)
    st.session_state.home_lon = saved_data.get("home_lon", 31.2357)
    st.session_state.profile_completed = True

# ==========================================
# 5. تعريف الصفحات (Define Pages)
# ==========================================
page_login = st.Page("views/login.py", title="Login", icon="🔐")
page_profile = st.Page("views/profile.py", title="Profile", icon="👤")
page_edit_profile = st.Page("views/edit_profile.py", title="Edit Profile", icon="✏️")
page_settings = st.Page("views/settings.py", title="Settings", icon="⚙️")

page_home = st.Page("views/home.py", title="Home", icon="🏠")
page_light_temp = st.Page("views/lighting_temp.py", title="Lighting & Temp", icon="💡")
page_devices = st.Page("views/devices.py", title="Devices", icon="📺")
page_security = st.Page("views/security.py", title="Security", icon="🛡️")
page_rooms = st.Page("views/rooms.py", title="Smart Rooms", icon="🚪")
page_voice = st.Page("views/voice_assistant.py", title="Voice Assistant", icon="🎙️")
page_emergency = st.Page("views/emergency_map.py", title="Emergency Map", icon="🚨")

page_expert = st.Page("views/expert_decisions.py", title="Expert Decisions", icon="🤖")
page_logs = st.Page("views/logs.py", title="Logs", icon="📝")
page_reports = st.Page("views/reports.py", title="Reports & Analytics", icon="📊")

# ==========================================
# 6. التنقل بين الصفحات (Navigation Logic)
# ==========================================
if not st.session_state.logged_in:
    pg = st.navigation([page_login], position="sidebar")
elif not st.session_state.profile_completed:
    pg = st.navigation([page_profile], position="sidebar")
else:
    pg = st.navigation(
        {
            "Main": [page_home, page_light_temp, page_devices, page_security, page_rooms, page_voice, page_emergency],
            "System": [page_expert, page_logs, page_reports],
            "Account": [page_profile, page_edit_profile, page_settings],
        },
        position="sidebar",
    )

# ==========================================
# 7. زرار تسجيل الخروج (Logout Button)
# ==========================================
if st.session_state.logged_in:
    with st.sidebar:
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

# ==========================================
# 8. تشغيل الصفحة (Run Page)
# ==========================================
pg.run()