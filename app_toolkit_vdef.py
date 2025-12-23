import streamlit as st
import logging

# ==============================================================================
# 1. CONFIGURACIÓN E IMPORTACIONES SEGURAS (INTACTO)
# ==============================================================================
logging.basicConfig(level=logging.INFO)

def safe_import(module_path: str):
    try:
        mod = __import__(module_path, fromlist=['run'])
        return mod, True
    except ImportError:
        return None, False

MADUREZ_MOD, MADUREZ_AVAILABLE = safe_import("apps.madurez_digital")
HERRAMIENTAS_MOD, HERRAMIENTAS_AVAILABLE = safe_import("apps.herramientas")
BIBLIOTECA_MOD, BIBLIOTECA_AVAILABLE = safe_import("apps.biblioteca")

# ==============================================================================
# 2. DICCIONARIO DE TEXTOS (INTACTO)
# ==============================================================================
TEXTS = {
    "title": {"Español": "🛠️ Toolkit DGI", "English": "🛠️ DGI Toolkit", "Français": "🛠️ Boîte à outils DGI"},
    "input_name": {"Español": "👤 Nombre:", "English": "👤 Name:", "Français": "👤 Nom:"},
    "input_location": {"Español": "📍 Lugar:", "English": "📍 Location:", "Français": "📍 Lieu:"},
    "header_modules": {"Español": "🚀 Módulos", "English": "🚀 Modules", "Français": "🚀 Modules"},
    "info_panel": {"Español": "ℹ️ Info", "English": "ℹ️ Info", "Français": "ℹ️ Info"},
    "btn_confirm": {"Español": "✅ Confirmar", "English": "✅ Confirm", "Français": "✅ Confirmer"},
    "mod_home": {
        "icon": "🏠", 
        "name": {"Español": "Inicio", "English": "Home", "Français": "Accueil"}, 
        "desc": {"Español": "Bienvenido al Toolkit. Seleccione una herramienta para comenzar.", "English": "Welcome to the Toolkit. Select a tool to start.", "Français": "Bienvenue. Sélectionnez un outil."}
    },
    "app_madurez": {
        "icon": "🧠", 
        "name": {"Español": "Madurez", "English": "Maturity", "Français": "Maturité"}, 
        "desc": {"Español": "Evaluación de madurez digital individual y organizacional.", "English": "Individual and organizational digital maturity assessment.", "Français": "Évaluation de la maturité numérique."}
    },
    "app_herramientas": {
        "icon": "🛠️", 
        "name": {"Español": "Herramientas", "English": "Tools", "Français": "Outils"}, 
        "desc": {
            "Español": "Centro de utilidades digitales: herramientas de soporte para el mundo digital.", 
            "English": "Digital utility center: support tools for the digital world.", 
            "Français": "Centre d'utilitaires numériques : outils de support pour le monde numérique."
        }
    },
    "mod_bib": {
        "icon": "📚", 
        "name": {"Español": "Biblioteca", "English": "Library", "Français": "Bibliothèque"}, 
        "desc": {"Español": "Acceso a documentación y recursos DGI.", "English": "Access to DGI docs and resources.", "Français": "Accès aux documents DGI."}
    }
}

# ==============================================================================
# 3. CSS (OPTIMIZADO PARA GUI MÓVIL/DESKTOP) - SOLO CAMBIOS AQUÍ
# ==============================================================================
def inject_custom_css():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { background-color: #f0f2f6; }
        .stApp { background-color: #ffffff; }
        
        /* Contenedor del Botón como Card */
        div.stButton > button {
            background-color: #ffffff !important;
            border: 1px solid #e1e4e8 !important;
            border-radius: 16px !important;
            padding: 25px 10px !important;
            height: 140px !important; /* Altura fija para consistencia */
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important;
            align-items: center !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04) !important;
        }
        
        /* Efectos Hover y Click (Reactividad Táctil) */
        div.stButton > button:hover {
            border-color: #ff4b4b !important;
            box-shadow: 0 10px 15px rgba(0,0,0,0.08) !important;
            transform: translateY(-4px) !important;
        }
        div.stButton > button:active {
            transform: scale(0.95) !important;
            background-color: #fefefe !important;
        }
        
        /* Estilo del texto dentro de la Card */
        div.stButton > button p {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            margin-top: 10px !important;
            color: #31333F !important;
        }

        /* Ajuste de iconos grandes */
        .card-icon {
            font-size: 45px !important;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. APLICACIÓN PRINCIPAL (REFACTORIZADO SOLO GUI DE MÓDULOS)
# ==============================================================================
def main():
    st.set_page_config(page_title="Toolkit DGI", layout="wide", page_icon="🛠️")
    inject_custom_css()

    if 'active_app' not in st.session_state: st.session_state.active_app = "mod_home"
    if 'user_lang' not in st.session_state: st.session_state.user_lang = "Español"
    if 'user_name' not in st.session_state: st.session_state.user_name = ""
    if 'user_location' not in st.session_state: st.session_state.user_location = ""
    
    lang = st.session_state.user_lang

    with st.sidebar:
        st.title(TEXTS["title"][lang])
        st.markdown("---")
        st.session_state.user_lang = st.selectbox("🌐 Idioma", ["Español", "English", "Français"], 
                                                 index=["Español", "English", "Français"].index(lang))
        st.session_state.user_name = st.text_input(TEXTS["input_name"][lang], value=st.session_state.user_name)
        st.session_state.user_location = st.text_input(TEXTS["input_location"][lang], value=st.session_state.user_location)
        if st.button(TEXTS["btn_confirm"][lang], use_container_width=True):
            st.toast("✅ Datos guardados")

    app_config = {
        "mod_home": {
            "name": TEXTS["mod_home"]["name"][lang], "icon": TEXTS["mod_home"]["icon"],
            "func": None, "desc": TEXTS["mod_home"]["desc"][lang]
        },
        "app_madurez": {
            "name": TEXTS["app_madurez"]["name"][lang], "icon": TEXTS["app_madurez"]["icon"],
            "func": MADUREZ_MOD.run if MADUREZ_AVAILABLE else None, "desc": TEXTS["app_madurez"]["desc"][lang]
        },
        "app_herramientas": {
            "name": TEXTS["app_herramientas"]["name"][lang], "icon": TEXTS["app_herramientas"]["icon"],
            "func": HERRAMIENTAS_MOD.run if HERRAMIENTAS_AVAILABLE else None, "desc": TEXTS["app_herramientas"]["desc"][lang]
        },
        "mod_bib": {
            "name": TEXTS["mod_bib"]["name"][lang], "icon": TEXTS["mod_bib"]["icon"],
            "func": BIBLIOTECA_MOD.run if BIBLIOTECA_AVAILABLE else None, "desc": TEXTS["mod_bib"]["desc"][lang]
        }
    }

    col_izq, col_der = st.columns([7, 3])

    with col_izq:
        st.header(TEXTS["header_modules"][lang])
        keys = list(app_config.keys())
        
        # Grid adaptativo: 2 columnas que se ven bien en móvil y escritorio
        m_cols = st.columns(2)
        for i, k in enumerate(keys):
            with m_cols[i % 2]:
                # Inyectamos el icono con una clase para controlarlo por CSS
                # El texto se maneja directamente en el label del botón
                label = f"{app_config[k]['icon']}\n\n{app_config[k]['name']}"
                if st.button(label, key=f"btn_{k}", use_container_width=True):
                    st.session_state.active_app = k
                    st.rerun()

        st.markdown("---")
        active_key = st.session_state.active_app
        selected_app = app_config[active_key]

        if selected_app["func"]:
            selected_app["func"](
                st, 
                name=st.session_state.user_name,
                lang=st.session_state.user_lang,
                location=st.session_state.user_location,
                superapp_name="Toolkit DGI"
            )
        else:
            st.subheader(f"{selected_app['icon']} {selected_app['name']}")
            st.info(selected_app['desc'])

    with col_der:
        st.subheader(TEXTS["info_panel"][lang])
        with st.container(border=True):
            st.markdown(f"### {app_config[active_key]['icon']} {app_config[active_key]['name']}")
            st.write(app_config[active_key]["desc"])
            st.markdown("---")
            st.caption(f"👤 {st.session_state.user_name or '---'}")
            st.caption(f"📍 {st.session_state.user_location or '---'}")

if __name__ == "__main__":
    main()
