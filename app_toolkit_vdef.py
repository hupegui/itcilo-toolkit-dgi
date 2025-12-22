import streamlit as st
import logging

# ==============================================================================
# 1. CONFIGURACIÓN E IMPORTACIONES SEGURAS
# ==============================================================================
logging.basicConfig(level=logging.INFO)

def safe_import(module_path: str):
    try:
        mod = __import__(module_path, fromlist=['run'])
        return mod, True
    except Exception as e:
        logging.error(f"Error importando {module_path}: {e}")
        return None, False

# Intentar importar los módulos de la carpeta /apps
MADUREZ_MOD, MADUREZ_AVAILABLE = safe_import("apps.madurez_digital")
HERRAMIENTAS_MOD, HERRAMIENTAS_AVAILABLE = safe_import("apps.herramientas")
BIBLIOTECA_MOD, BIBLIOTECA_AVAILABLE = safe_import("apps.biblioteca")

# ==============================================================================
# 2. DICCIONARIO DE TEXTOS
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
# 3. CSS (Corregido para Móvil)
# ==============================================================================
def inject_custom_css():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { background-color: #f0f2f6; }
        .stApp { background-color: #ffffff; }
        /* Ajuste de botones para que no se corten en móvil */
        div.stButton > button {
            width: 100% !important;
            display: flex !important;
            justify-content: flex-start !important;
            align-items: center !important;
            padding: 10px !important;
            border-radius: 10px !important;
        }
        @media (max-width: 600px) {
            .module-card { margin-bottom: 10px; }
            h1 { font-size: 1.8rem !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. APLICACIÓN PRINCIPAL
# ==============================================================================
def main():
    st.set_page_config(page_title="Toolkit DGI", layout="wide", page_icon="🛠️", initial_sidebar_state="auto")
    inject_custom_css()

    if 'active_app' not in st.session_state: st.session_state.active_app = "mod_home"
    if 'user_lang' not in st.session_state: st.session_state.user_lang = "Español"
    if 'user_name' not in st.session_state: st.session_state.user_name = ""
    if 'user_location' not in st.session_state: st.session_state.user_location = ""
    
    lang = st.session_state.user_lang

    with st.sidebar:
        st.title(TEXTS["title"][lang])
        st.session_state.user_lang = st.selectbox("🌐 Idioma", ["Español", "English", "Français"], 
                                                 index=["Español", "English", "Français"].index(lang))
        st.session_state.user_name = st.text_input(TEXTS["input_name"][lang], value=st.session_state.user_name)
        st.session_state.user_location = st.text_input(TEXTS["input_location"][lang], value=st.session_state.user_location)
        if st.button(TEXTS["btn_confirm"][lang], use_container_width=True):
            st.toast("✅ Datos guardados")
        
        st.markdown("---")
        # AGREGAMOS UN MENÚ DE RESPALDO EN LA SIDEBAR PARA MÓVILES
        st.subheader(TEXTS["header_modules"][lang])
        for k in ["mod_home", "app_madurez", "app_herramientas", "mod_bib"]:
            if st.button(f"{TEXTS[k]['icon']} {TEXTS[k]['name'][lang]}", key=f"side_{k}"):
                st.session_state.active_app = k
                st.rerun()

    app_config = {
        "mod_home": {"name": TEXTS["mod_home"]["name"][lang], "icon": TEXTS["mod_home"]["icon"], "func": None, "desc": TEXTS["mod_home"]["desc"][lang]},
        "app_madurez": {"name": TEXTS["app_madurez"]["name"][lang], "icon": TEXTS["app_madurez"]["icon"], "func": MADUREZ_MOD.run if MADUREZ_AVAILABLE else None, "desc": TEXTS["app_madurez"]["desc"][lang]},
        "app_herramientas": {"name": TEXTS["app_herramientas"]["name"][lang], "icon": TEXTS["app_herramientas"]["icon"], "func": HERRAMIENTAS_MOD.run if HERRAMIENTAS_AVAILABLE else None, "desc": TEXTS["app_herramientas"]["desc"][lang]},
        "mod_bib": {"name": TEXTS["mod_bib"]["name"][lang], "icon": TEXTS["mod_bib"]["icon"], "func": BIBLIOTECA_MOD.run if BIBLIOTECA_AVAILABLE else None, "desc": TEXTS["mod_bib"]["desc"][lang]}
    }

    # CUERPO PRINCIPAL
    active_key = st.session_state.active_app
    selected_app = app_config[active_key]

    if active_key == "mod_home":
        st.header(TEXTS["header_modules"][lang])
        # En móvil, las columnas se ven mal, así que usamos un layout más simple
        cols = st.columns(2)
        keys = ["app_madurez", "app_herramientas", "mod_bib"]
        for i, k in enumerate(keys):
            with cols[i % 2]:
                if st.button(f"{app_config[k]['icon']} {app_config[k]['name']}", key=f"main_{k}"):
                    st.session_state.active_app = k
                    st.rerun()
        
        st.markdown("---")
        st.subheader(f"{selected_app['icon']} {selected_app['name']}")
        st.write(selected_app['desc'])
    else:
        # BOTÓN PARA VOLVER AL INICIO (Vital en móviles)
        if st.button("⬅️ Volver al Menú Principal"):
            st.session_state.active_app = "mod_home"
            st.rerun()
            
        if selected_app["func"]:
            selected_app["func"](
                st, 
                name=st.session_state.user_name,
                lang=st.session_state.user_lang,
                location=st.session_state.user_location,
                superapp_name="Toolkit DGI"
            )
        else:
            st.error("Módulo no disponible")

if __name__ == "__main__":
    main()
