import streamlit as st
import logging
from streamlit_searchbox import st_searchbox # Opcional, pero mantenemos tus imports

# ==============================================================================
# 1. CONFIGURACIÓN E IMPORTACIONES SEGURAS (SIN CAMBIOS)
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
# 2. DICCIONARIO DE TEXTOS (INTEGRO, SIN CAMBIOS)
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
            "Français": "Centre d'utilitaires numériques : outils de support para el mundo digital."
        }
    },
    "mod_bib": {
        "icon": "📚", 
        "name": {"Español": "Biblioteca", "English": "Library", "Français": "Bibliothèque"}, 
        "desc": {"Español": "Acceso a documentación y recursos DGI.", "English": "Access to DGI docs and resources.", "Français": "Accès aux documents DGI."}
    }
}

# ==============================================================================
# 3. CSS RESPONSIVO (CORRECCIÓN DE DISPLAY PARA MÓVIL)
# ==============================================================================
def inject_custom_css():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { background-color: #f0f2f6; }
        .stApp { background-color: #ffffff; }
        
        /* BOTÓN RESPONSIVO: Asegura que el icono y el texto se vean siempre */
        [data-testid="stMain"] div.stButton > button {
            height: auto !important;
            min-height: 60px !important;
            background-color: #ffffff !important;
            border: 1px solid #e0e0e0 !important;
            border-radius: 10px !important;
            display: flex !important;
            flex-direction: row !important; /* Icono al lado del texto */
            justify-content: flex-start !important;
            align-items: center !important;
            width: 100% !important;
            padding: 10px 15px !important;
            margin-bottom: 10px !important;
        }
        
        /* Estilo del texto dentro del botón */
        [data-testid="stMain"] div.stButton > button p { 
            font-size: 18px !important; 
            margin: 0 !important;
            padding-left: 10px !important;
            text-align: left !important;
            white-space: normal !important;
        }

        /* Estilo del icono */
        .module-icon-container {
            font-size: 25px !important;
            margin-right: 10px !important;
        }

        /* Forzar que las columnas no se achiquen a cero en móvil */
        @media (max-width: 768px) {
            [data-testid="column"] {
                min-width: 100% !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. APLICACIÓN PRINCIPAL
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

    # Diseño principal: 2 columnas en Web, se apilan en Móvil
    col_izq, col_der = st.columns([7, 3])

    with col_izq:
        st.header(TEXTS["header_modules"][lang])
        keys = list(app_config.keys())
        
        # SOLUCIÓN DE DISPLAY: Eliminamos sub-columnas complejas. 
        # Ponemos el icono DENTRO del botón (o justo al lado) de forma simple.
        for k in keys:
            # Creamos una fila por módulo para máxima compatibilidad móvil
            col_m1, col_m2 = st.columns([1, 10]) # Espacio mínimo para icono, máximo para botón
            with col_m1:
                st.markdown(f"<div class='module-icon-container'>{app_config[k]['icon']}</div>", unsafe_allow_html=True)
            with col_m2:
                if st.button(f"{app_config[k]['name']}", key=f"btn_{k}"):
                    st.session_state.active_app = k
                    st.rerun()

        st.markdown("---")
        active_key = st.session_state.active_app
        selected_app = app_config[active_key]

        # SECCIÓN DE CONTENIDO (MANTENIDA ÍNTEGRA)
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
