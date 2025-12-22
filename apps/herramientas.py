# apps/app_herramientas.py
import streamlit as st
from typing import Dict, List, Any

# ====================================================================
# --- 1. BASE DE DATOS DE HERRAMIENTAS (MULTILINGÜE) ---
# ====================================================================

DATA_HERRAMIENTAS = [
    {
        "elemento": {"es": "Datos y Encuestas", "en": "Data & Surveys", "fr": "Données et Enquêtes"},
        "nombre": "KoboToolbox",
        "tipo": "Survey & Feedback (ODK Standard)",
        "play": "https://www.kobotoolbox.org/",
        "tutorial": "https://www.youtube.com/watch?v=h6S_S_v96YI"
    },
    {
        "elemento": {"es": "Datos y Encuestas", "en": "Data & Surveys", "fr": "Données et Enquêtes"},
        "nombre": "LimeSurvey",
        "tipo": "Open Source Research Surveys",
        "play": "https://community.limesurvey.org/",
        "tutorial": "https://www.youtube.com/watch?v=0hX0K6n8f6U"
    },
    {
        "elemento": {"es": "Herramientas (Open Source)", "en": "Tools (Open Source)", "fr": "Outils (Open Source)"},
        "nombre": "OpenIMIS",
        "tipo": "Social Insurance Management",
        "play": "https://wiki.openimis.org/",
        "tutorial": "https://www.youtube.com/watch?v=7uV8-17_I4U"
    },
    {
        "elemento": {"es": "Herramientas (Reportes)", "en": "Tools (Reporting)", "fr": "Outils (Rapports)"},
        "nombre": "Grafana Play",
        "tipo": "Dashboard & BI Real-time",
        "play": "https://play.grafana.org/",
        "tutorial": "https://www.youtube.com/watch?v=N6a3Z9-mGCo"
    },
    {
        "elemento": {"es": "Herramientas (Reportes)", "en": "Tools (Reporting)", "fr": "Outils (Rapports)"},
        "nombre": "Metabase OSS",
        "tipo": "Easy Data Visualization",
        "play": "https://www.metabase.com/start/oss/",
        "tutorial": "https://www.youtube.com/watch?v=fXfS_Tz9Dbc"
    },
    {
        "elemento": {"es": "Procesos", "en": "Process", "fr": "Processus"},
        "nombre": "n8n.io",
        "tipo": "Workflow Automation",
        "play": "https://n8n.io/",
        "tutorial": "https://www.youtube.com/watch?v=0-9M_mN0Q0A"
    },
    {
        "elemento": {"es": "Metodología", "en": "Methodology", "fr": "Méthodologie"},
        "nombre": "Keycloak Guide",
        "tipo": "Digital Identity & IAM",
        "play": "https://www.keycloak.org/guides",
        "tutorial": "https://www.youtube.com/watch?v=VlS9_p6pXRE"
    },
    {
        "elemento": {"es": "Personas", "en": "People", "fr": "Personnes"},
        "nombre": "Decidim Demo",
        "tipo": "Citizen Engagement Platform",
        "play": "https://demo.decidim.org/",
        "tutorial": "https://www.youtube.com/watch?v=N_o_Sly9964"
    }
]

L10N_HERRAMIENTAS = {
    'es': {
        'TITULO': "🛠️ Centro de Herramientas Digitales",
        'DISCLOSURE': "⚠️ **Aviso:** Esta lista tiene fines exclusivamente académicos y no constituye una publicidad, promoción o recomendación de estas herramientas sobre otras existentes. Su uso es responsabilidad exclusiva del usuario.",
        'INFO': "Bienvenido {user_name}. Explore estos entornos para probar soluciones de gobernanza digital.",
        'BTN_PLAY': "Probar Online",
        'BTN_TUTO': "Ver Guía"
    },
    'en': {
        'TITULO': "🛠️ Digital Tools Center",
        'DISCLOSURE': "⚠️ **Disclosure:** This list is for academic purposes only and does not constitute publicity, promotion, or recommendation of these tools over existing ones. Use is solely the responsibility of the user.",
        'INFO': "Welcome {user_name}. Explore these environments to test digital governance solutions.",
        'BTN_PLAY': "Test Online",
        'BTN_TUTO': "Watch Guide"
    },
    'fr': {
        'TITULO': "🛠️ Centre d'Outils Numériques",
        'DISCLOSURE': "⚠️ **Avis :** Cette liste est fournie à des fins académiques uniquement et ne constituye pas une publicité, une promotion ou une recommandation de ces outils par rapport à d'autres existants. L'utilisation relève de la seule responsabilité de l'utilisateur.",
        'INFO': "Bienvenue {user_name}. Explorez ces environnements pour tester des solutions de gouvernance numérique.",
        'BTN_PLAY': "Tester Online",
        'BTN_TUTO': "Voir Guide"
    }
}

# ====================================================================
# --- 2. LOGIC HELPERS ---
# ====================================================================

def get_lang_code(lang_full: str) -> str:
    mapping = {'español': 'es', 'english': 'en', 'français': 'fr'}
    return mapping.get(str(lang_full).lower(), 'es')

# ====================================================================
# --- 3. RUN MODULE ---
# ====================================================================

def run(st_context=None, **kwargs: Any):
    user_name = kwargs.get('name', 'User')
    lang_full = kwargs.get('lang', 'Español')
    
    lang_code = get_lang_code(lang_full)
    strings = L10N_HERRAMIENTAS.get(lang_code, L10N_HERRAMIENTAS['es'])

    # Title and Disclosure
    st.title(strings['TITULO'])
    st.warning(strings['DISCLOSURE']) # Disclosure highlight
    
    st.info(strings['INFO'].format(user_name=user_name))
    st.markdown("---")

    for item in DATA_HERRAMIENTAS:
        with st.container():
            col1, col2, col3, col4 = st.columns([1.5, 2, 1, 1])
            
            with col1:
                st.markdown(f"**{item['elemento'][lang_code]}**")
                st.caption(f"{item['tipo']}")
            
            with col2:
                st.markdown(f"### {item['nombre']}")
            
            with col3:
                st.link_button(strings['BTN_PLAY'], item['play'], use_container_width=True)
            
            with col4:
                st.link_button(strings['BTN_TUTO'], item['tutorial'], use_container_width=True, type="secondary")
            
            st.markdown("---")