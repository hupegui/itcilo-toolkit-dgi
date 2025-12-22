# apps/biblioteca.py - CÓDIGO FINAL CORREGIDO PARA INTEGRACIÓN CON SUPERAPP
import streamlit as st
from typing import Dict, List, Any

# ====================================================================
# --- 1. DEFINICIÓN DE CONSTANTES (FUENTES Y ENLACES) ---
# ====================================================================

FUENTES_BIBLIOTECA: Dict[str, List[Dict[str, str]]] = {
    "Documentos Académicos y de Política": [
        {"titulo": "Hanisch, M., et al. (2023), Digital governance: A conceptual framework. Journal of Business Research.", "url": "https://www.sciencedirect.com/journal/journal-of-business-research"},
        {"titulo": "Yang, C., et al. (2024), Government in the digital age. Technological Forecasting & Social Change.", "url": "https://www.sciencedirect.com/journal/technological-forecasting-and-social-change"},
        {"titulo": "DigComp 2.2: The Digital Competence Framework for Citizens. European Commission.", "url": "https://publications.jrc.ec.europa.eu/repository/handle/JRC128415"},
    ],
    "Estrategias y Reportes de Organizaciones Clave": [
        {"titulo": "ILO (2021), Governance of social protection systems (Module #2: ICT & Data).", "url": "https://www.social-protection.org/gimi/ShowRessource.action?ressource.ressourceId=58623"},
        {"titulo": "WHO, Governance for Digital Health (Global Strategy 2020–2025).", "url": "https://www.who.int/publications/i/item/9789240020663"},
        {"titulo": "UN, Roadmap for Digital Cooperation.", "url": "https://www.un.org/en/content/digital-cooperation-roadmap/"},
    ],
    "Casos de Estudio y Multimedia": [
        {"titulo": "What digital success look like - Measuring Government Digitalisation.", "url": "https://knowledge.csc.gov.sg/ethos-issue-21/what-digital-success-looks-like-measuring-evaluating-government-digitalisation/"},
        {"titulo": "UNU, Digital Governance in the Age of AI. YouTube video.", "url": "https://unu.edu/cpr"},
    ],
    "Organizaciones y Portales Fuente": [
        {"titulo": "International Labour Organization (ILO)", "url": "https://www.ilo.org/"},
        {"titulo": "GovTech Singapore", "url": "https://www.tech.gov.sg/"},
        {"titulo": "Digital Agency of Japan", "url": "https://www.digital.go.jp/en/"},
    ]
}

# --- Localización para Biblioteca App ---
L10N_BIBLIOTECA: Dict[str, Dict[str, str]] = {
    'es': {
        'TITULO': "📚 Biblioteca de Referencias en Gobernanza Digital - {superapp_name}",
        'INFO': "Fuentes fundamentales utilizadas para los módulos de {superapp_name}.",
        'WELCOME_MSG': "Bienvenido, {user_name}. Referencias para tu avance.",
        'CATEGORY_1': "Documentos Académicos y de Política",
        'CATEGORY_2': "Estrategias y Reportes de Organizaciones Clave",
        'CATEGORY_3': "Casos de Estudio y Multimedia",
        'CATEGORY_4': "Organizaciones y Portales Fuente",
    },
    'en': {
        'TITULO': "📚 Digital Governance Reference Library - {superapp_name}",
        'INFO': "Fundamental sources used for {superapp_name} modules.",
        'WELCOME_MSG': "Welcome, {user_name}. References for your learning.",
        'CATEGORY_1': "Academic and Policy Documents",
        'CATEGORY_2': "Key Organization Strategies and Reports",
        'CATEGORY_3': "Case Studies and Multimedia",
        'CATEGORY_4': "Source Organizations and Portals",
    },
    'fr': {
        'TITULO': "📚 Bibliothèque de Gouvernance Numérique - {superapp_name}",
        'INFO': "Sources fondamentales pour les modules de {superapp_name}.",
        'WELCOME_MSG': "Bienvenue, {user_name}. Références pour votre avancement.",
        'CATEGORY_1': "Documents Académiques et de Politique",
        'CATEGORY_2': "Stratégies et Rapports d'Organisations Clés",
        'CATEGORY_3': "Études de Cas et Multimédia",
        'CATEGORY_4': "Organisations et Portails Source",
    }
}

# ====================================================================
# --- 2. FUNCIONES DE SOPORTE ---
# ====================================================================

def map_lang_to_code(lang_full: str) -> str:
    """Mapea el nombre completo del idioma al código de dos letras."""
    mapping = {'español': 'es', 'english': 'en', 'français': 'fr'}
    return mapping.get(str(lang_full).lower(), 'es')

# ====================================================================
# --- 3. PUNTO DE ENTRADA PRINCIPAL ---
# ====================================================================

def run(st_context=None, **kwargs: Any):
    """
    Punto de entrada para el orquestador.
    st_context: Recibe el objeto 'st' pasado posicionalmente por la Super App.
    kwargs: Recibe name, lang, location y otros parámetros.
    """
    # 1. Recuperación de parámetros con valores por defecto seguros
    user_name = kwargs.get('name', 'Usuario')
    location = kwargs.get('location', 'Mundo')
    superapp_name = kwargs.get('superapp_name', 'Toolkit DGI')
    lang_full = kwargs.get('lang', 'Español')
    
    # 2. Configuración del idioma
    lang_code = map_lang_to_code(lang_full)
    strings = L10N_BIBLIOTECA.get(lang_code, L10N_BIBLIOTECA['es'])

    # 3. Interfaz de usuario
    st.title(strings['TITULO'].format(superapp_name=superapp_name))
    st.markdown("---")
    
    st.markdown(f"**{strings['WELCOME_MSG'].format(user_name=user_name, location=location)}**")
    st.info(strings['INFO'].format(superapp_name=superapp_name))
    
    # 4. Renderizado dinámico de categorías por idioma
    categorias_map = [
        ("Documentos Académicos y de Política", 'CATEGORY_1'),
        ("Estrategias y Reportes de Organizaciones Clave", 'CATEGORY_2'),
        ("Casos de Estudio y Multimedia", 'CATEGORY_3'),
        ("Organizaciones y Portales Fuente", 'CATEGORY_4'),
    ]
    
    for key_fuente, key_l10n in categorias_map:
        if key_fuente in FUENTES_BIBLIOTECA:
            st.header(f"➡️ {strings[key_l10n]}")
            for fuente in FUENTES_BIBLIOTECA[key_fuente]:
                st.markdown(f"- [{fuente['titulo']}]({fuente['url']})")
            st.markdown("---")

if __name__ == '__main__':
    # Permite ejecución independiente para pruebas
    run(name="Admin", lang="Español", location="Local")