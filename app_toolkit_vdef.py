import streamlit as st
import logging

# ==============================================================================
# 1. CONFIGURACIÓN E IMPORTACIONES SEGURAS
# ==============================================================================
logging.basicConfig(level=logging.INFO)

def safe_import(module_path: str):
    try:
        # En Linux (Streamlit Cloud) las rutas deben usar puntos o barras normales
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
# 2. DICCIONARIO DE TEXTOS (Multilenguaje)
# ==============================================================================
TEXTS = {
    "title": {"Español": "🛠️ Toolkit DGI", "English": "🛠️ DGI Toolkit", "Français": "🛠️ Boîte à outils DGI"},
    "input_name": {"Español": "👤 Nombre:", "English": "👤 Name:", "Français": "👤 Nom:"},
    "input_location": {"Español": "📍 Lugar:", "English": "📍 Location:", "Français": "📍 Lieu:"},
    "header_modules": {"Español": "🚀 Módulos de Innovación", "English": "🚀 Innovation Modules", "Français": "🚀 Modules d'Innovation"},
    "btn_confirm": {"Español": "✅ Guardar Perfil", "English": "✅ Save Profile", "Français": "✅ Enregistrer le profil"},
    "mod_home": {
        "icon": "🏠", 
        "name": {"Español": "Inicio", "English": "Home", "Français": "Accueil"}, 
        "desc": {"Español": "Plataforma central de herramientas digitales.", "English": "Central platform for digital tools.", "Français": "Plateforme centrale d'outils numériques."}
    },
    "app_madurez": {
        "icon": "🧠", 
        "name": {"Español": "Madurez Digital", "English": "Digital Maturity", "Français": "Maturité Numérique"}, 
        "desc": {"Español": "Evaluación de capacidades digitales.", "English": "Digital capability assessment.", "Français": "Évaluation des capacités numériques."}
    },
    "app_herramientas": {
        "icon": "🛠️", 
        "name": {"Español": "Herramientas", "English": "Tools", "Français": "Outils"}, 
        "desc": {"Español": "Centro de utilidades y soporte.", "English": "Utility and support center.", "Français": "Centre d'utilitaires y support."}
    },
    "mod_bib": {
        "icon": "📚", 
        "name": {"Español": "Biblioteca", "English": "Library", "Français": "Bibliothèque"}, 
        "desc": {"Español": "Recursos y documentación DGI.", "English": "DGI resources and documentation.", "Français": "Ressources et documentation DGI."}
    }
}

# ==============================================================================
# 3. CSS PROFESIONAL (Responsivo)
# ==============================================================================
def inject_custom_css():
    st.markdown("""
        <style>
        /* Fondo y Sidebar */
        [data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #e0e0e0; }
        
        /* Botones estilo tarjeta */
        div.stButton > button {
            width: 100% !important;
            height: auto !important;
            padding: 20px !important;
            border-radius: 15px !important;
            border: 1px solid #dce1e6 !important;
            background-color: #ffffff !important;
            transition: all 0.3s ease;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
        }
        div.stButton > button:hover {
            border-color: #007bff !important;
            background-color: #f0f7ff !important;
            transform: translateY(-2px);
        }
        
        /* Ajustes para móviles */
        @media (max-width: 640px) {
            .stHeader { font-size: 1.5rem !important; }
            [data-testid="stSidebar"] { width: 80% !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. LÓGICA DE NAVEGACIÓN
# ==============================================================================
def main():
    st.set_page_config(page_title="Toolkit DGI", layout="wide", page_icon="🛠️")
    inject_custom_css()

    # Inicializar Session State
    if 'active_app' not in st.session_state: st.session_state.active_app = "mod_home"
    if 'user_lang' not in st.session_state: st.session_state.user_lang = "Español"
    if 'user_name' not in st.session_state: st.session_state.user_name = ""
    if 'user_location' not in st.session_state: st.session_state.user_location = ""
    
    lang = st.session_state.user_lang

    # --- SIDEBAR ---
    with st.sidebar:
        st.title(TEXTS["title"][lang])
        st.session_state.user_lang = st.selectbox("🌐 Idioma / Language", ["Español", "English", "Français"], 
                                                 index=["Español", "English", "Français"].index(lang))
        
        with st.expander("👤 Perfil de Usuario", expanded=True):
            st.session_state.user_name = st.text_input(TEXTS["input_name"][lang], value=st.session_state.user_name)
            st.session_state.user_location = st.text_input(TEXTS["input_location"][lang], value=st.session_state.user_location)
            if st.button(TEXTS["btn_confirm"][lang]):
                st.toast("💾 Datos actualizados")

        st.divider()
        if st.button("🏠 " + TEXTS["mod_home"]["name"][lang], use_container_width=True):
            st.session_state.active_app = "mod_home"
            st.rerun()

    # --- CONTENIDO PRINCIPAL ---
    app_config = {
        "mod_home": {"name": TEXTS["mod_home"]["name"][lang], "icon": TEXTS["mod_home"]["icon"], "func": None, "desc": TEXTS["mod_home"]["desc"][lang]},
        "app_madurez": {"name": TEXTS["app_madurez"]["name"][lang], "icon": TEXTS["app_madurez"]["icon"], "func": MADUREZ_MOD.run if MADUREZ_AVAILABLE else None, "desc": TEXTS["app_madurez"]["desc"][lang]},
        "app_herramientas": {"name": TEXTS["app_herramientas"]["name"][lang], "icon": TEXTS["app_herramientas"]["icon"], "func": HERRAMIENTAS_MOD.run if HERRAMIENTAS_AVAILABLE else None, "desc": TEXTS["app_herramientas"]["desc"][lang]},
        "mod_bib": {"name": TEXTS["mod_bib"]["name"][lang], "icon": TEXTS["mod_bib"]["icon"], "func": BIBLIOTECA_MOD.run if BIBLIOTECA_AVAILABLE else None, "desc": TEXTS["mod_bib"]["desc"][lang]}
    }

    active_key = st.session_state.active_app
    selected_app = app_config[active_key]

    if active_key == "mod_home":
        st.header(TEXTS["header_modules"][lang])
        st.write(selected_app['desc'])
        
        # DISEÑO RESPONSIVO: Columnas en Web, Lista en Móvil
        # En Web (pantalla ancha) se verán 3 columnas. En móvil se apilarán solas.
        m1, m2, m3 = st.columns(3)
        
        with m1:
            if st.button(f"{app_config['app_madurez']['icon']}\n\n{app_config['app_madurez']['name']}", key="btn_mad"):
                st.session_state.active_app = "app_madurez"
                st.rerun()
        with m2:
            if st.button(f"{app_config['app_herramientas']['icon']}\n\n{app_config['app_herramientas']['name']}", key="btn_her"):
                st.session_state.active_app = "app_herramientas"
                st.rerun()
        with m3:
            if st.button(f"{app_config['mod_bib']['icon']}\n\n{app_config['mod_bib']['name']}", key="btn_bib"):
                st.session_state.active_app = "mod_bib"
                st.rerun()

    else:
        # PANTALLA DE MÓDULO ACTIVO (Preguntas del Test)
        # Usamos márgenes laterales solo en Web para que no se estire el texto
        col_main_izq, col_main_centro, col_main_der = st.columns([1, 10, 1])
        
        with col_main_centro:
            if st.button("⬅️ " + TEXTS["mod_home"]["name"][lang]):
                st.session_state.active_app = "mod_home"
                st.rerun()
            
            st.title(f"{selected_app['icon']} {selected_app['name']}")
            st.caption(selected_app['desc'])
            st.divider()

            if selected_app["func"]:
                try:
                    selected_app["func"](
                        st, 
                        name=st.session_state.user_name,
                        lang=st.session_state.user_lang,
                        location=st.session_state.user_location,
                        superapp_name="Toolkit DGI"
                    )
                except Exception as e:
                    st.error(f"❌ Error al cargar contenido: {e}")
            else:
                st.warning("Próximamente disponible.")

if __name__ == "__main__":
    main()
