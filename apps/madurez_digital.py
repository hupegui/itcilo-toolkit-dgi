# Madurez digital
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

# ==============================================================================
# 1. BASE DE DATOS - CONTENIDO ORIGINAL PROTEGIDO
# ==============================================================================
DIM_MAP = {
    "Español": ["Propósito", "Datos", "Metodología", "Herramientas", "Personas", "Procesos"],
    "English": ["Purpose", "Data", "Methodology", "Tools", "People", "Processes"],
    "Français": ["Objectif", "Données", "Méthodologie", "Outils", "Personnes", "Processus"]
}

def get_questions_db(is_org, lang):
    dims = DIM_MAP.get(lang, DIM_MAP["English"])
    if is_org:
        if lang == "Español":
            return {
                dims[0]: [("Q1", "Existe una estrategia o visión digital documentada, aunque sea preliminar."), ("Q2", "La estrategia digital se comunica a todo el personal que necesita usarla."), ("Q3", "El personal entiende el propósito y valor estratégico de los proyectos digitales.")],
                dims[1]: [("Q4", "La organización tiene medidas básicas para proteger sistemas y datos contra ciberamenazas."), ("Q5", "Existen reglas claras y accesibles para manejar datos sensibles o personales."), ("Q6", "Se aplican controles básicos para asegurar la fiabilidad de los datos en decisiones oficiales.")],
                dims[2]: [("Q7", "Se involucra a usuarios finales o ciudadanos para probar servicios digitales antes del lanzamiento."), ("Q8", "Se fomenta y existe una forma básica de probar y compartir nuevas ideas de mejora digital."), ("Q9", "Los proyectos siguen un enfoque paso a paso que permite cambios rápidos y aprendizaje.")],
                dims[3]: [("Q10", "Existe una persona o groupo responsable de coordinar que los sistemas digitales funcionen juntos."), ("Q11", "Se documentan costos y riesgos básicos antes de adquirir nuevas herramientas digitales."), ("Q12", "Los sistemas digitales principales pueden compartir datos entre sí fácilmente.")],
                dims[4]: [("Q13", "Diferentes departamentos se reúnen y colaboran activamente en proyectos digitales compartidos."), ("Q14", "Se considera específicamente cómo asegurar que los servicios sean accesibles para todos los ciudadanos."), ("Q15", "Se comunican proactivamente los cambios y progresos para generar confianza.")],
                dims[5]: [("Q16", "Se mapean y simplifican los procesos de trabajo antes de intentar automatizarlos."), ("Q17", "Las reglas básicas para gestionar herramientas e información son claras y accesibles."), ("Q18", "Existen reglas o criterios simples para decidir qué tareas deben automatizarse primero.")]
            }
        elif lang == "Français":
            return {
                dims[0]: [("Q1", "Il existe une stratégie ou une vision numérique documentée, même préliminaire."), ("Q2", "La stratégie numérique est communiquée à tout le personnel qui doit l'utiliser."), ("Q3", "Le personnel comprend l'objectif et la valeur stratégique des projets numériques.")],
                dims[1]: [("Q4", "L'organisation dispose de mesures de base pour protéger les systèmes et les données contre les cybermenaces."), ("Q5", "Il existe des règles claires et accessibles pour la gestion des données sensibles ou personnelles."), ("Q6", "Des contrôles de base sont appliqués pour garantir la fiabilité des données dans les décisions officielles.")],
                dims[2]: [("Q7", "Les utilisateurs finaux ou les citoyens sont impliqués pour tester les services numériques avant leur lancement."), ("Q8", "Il existe une manière de base de tester et de partager de nouvelles idées d'amélioration numérique."), ("Q9", "Les projets suivent une approche étape par étape permettant des changements rapides et un apprentissage.")],
                dims[3]: [("Q10", "Il existe une personne ou un groupe responsable de coordonner le fonctionnement conjoint des systèmes numériques."), ("Q11", "Les coûts et les risques de base sont documentés avant l'acquisition de nouveaux outils numériques."), ("Q12", "Les principaux systèmes numériques peuvent facilement partager des données entre eux.")],
                dims[4]: [("Q13", "Différents départements se réunissent et collaborent activement sur des projets numériques partagés."), ("Q14", "La manière de garantir que les services soient accessibles à tous les citoyens est spécifiquement prise en compte."), ("Q15", "Les changements et les progrès sont communiqués de manière proactive pour instaurer la confiance.")],
                dims[5]: [("Q16", "Les processus de travail sont cartographiés et simplifiés avant de tenter de les automatiser."), ("Q17", "Les règles de base pour la gestion des outils et des informations sont claires et accessibles."), ("Q18", "Il existe des règles ou des critères simples pour décider quelles tâches doivent être automatisées en premier.")]
            }
        else: # English
            return {
                dims[0]: [("Q1", "A digital strategy or vision exists and is documented, even if preliminary."), ("Q2", "The digital strategy is communicated to all staff who need to use it."), ("Q3", "Personnel understand the strategic purpose and value of digital projects.")],
                dims[1]: [("Q4", "The organization has basic measures to protect systems and data against cyber threats."), ("Q5", "Clear and accessible rules exist for handling sensitive or personal data."), ("Q6", "Basic controls are applied to ensure data reliability in official decisions.")],
                dims[2]: [("Q7", "End-users or citizens are involved to test digital services before launch."), ("Q8", "There is a basic way to test and share new ideas for digital improvement."), ("Q9", "Projects follow a step-by-step approach that allows for quick changes and learning.")],
                dims[3]: [("Q10", "There is a person or group responsible for coordinating that digital systems work together."), ("Q11", "Basic costs and risks are documented before acquiring new digital tools."), ("Q12", "Main digital systems can share data with each other easily.")],
                dims[4]: [("Q13", "Different departments meet and actively collaborate on shared digital projects."), ("Q14", "Specific consideration is given to ensuring services are accessible to all citizens."), ("Q15", "Changes and progress are proactively communicated to build trust.")],
                dims[5]: [("Q16", "Work processes are mapped and simplified before attempting to automate them."), ("Q17", "Basic rules for managing tools and information are clear and accessible."), ("Q18", "Simple rules or criteria exist to decide which tasks should be automated first.")]
            }
    else:
        if lang == "Español":
            return {
                dims[0]: [("Q1", "Entiendo cómo mi trabajo apoya los objetivos de mi organización."), ("Q2", "Puedo explicar el propósito de las iniciativas digitales."), ("Q3", "Puedo transmitir la visión digital de la organización.")],
                dims[1]: [("Q4", "Aplico estándares de seguridad a los datos."), ("Q5", "Aplico principios éticos en el manejo de datos."), ("Q6", "Aseguro que los datos que uso son fiables.")],
                dims[2]: [("Q7", "Entiendo el diseño centrado en el usuario."), ("Q8", "Propongo ideas innovadoras."), ("Q9", "Aprendo de los errores en proyectos digitales.")],
                dims[3]: [("Q10", "Entiendo la utilidad de una herramienta digital."), ("Q11", "Considero riesgos y gobernanza al usar herramientas."), ("Q12", "Entiendo conceptos de interoperabilidad.")],
                dims[4]: [("Q13", "Promuevo el trabajo en equipo entre áreas."), ("Q14", "Promuevo la inclusión digital."), ("Q15", "Me comunico eficazmente con stakeholders.")],
                dims[5]: [("Q16", "Sugiero mejoras en los flujos de trabajo."), ("Q17", "Entiendo las reglas de gobernanza."), ("Q18", "Identifico oportunidades de automatización.")]
            }
        elif lang == "Français":
            return {
                dims[0]: [("Q1", "Je comprends comment mon travail soutient les objectifs de mon organisation."), ("Q2", "Je peux expliquer le but des initiatives numériques."), ("Q3", "Je peux transmettre la vision numérique de l'organisation.")],
                dims[1]: [("Q4", "J'applique les normes de sécurité aux données."), ("Q5", "J'applique les principes éthiques dans la gestion des données."), ("Q6", "Je m'assure que les données que j'utilise sont fiables.")],
                dims[2]: [("Q7", "Je comprends la conception centrée sur l'utilisateur."), ("Q8", "Je propose des idées innovantes."), ("Q9", "J'apprends des erreurs dans les projets numériques.")],
                dims[3]: [("Q10", "Je comprends l'utilité d'un outil numérique."), ("Q11", "Je prends en compte les risques et la gouvernance lors de l'utilisation d'outils."), ("Q12", "Je comprends les concepts d'interopérabilité.")],
                dims[4]: [("Q13", "Je favorise le travail d'équipe entre les services."), ("Q14", "Je promeus l'inclusion numérique."), ("Q15", "Je communique efficacement avec les parties prenantes.")],
                dims[5]: [("Q16", "Je suggère des amélioraciones dans les flux de travail."), ("Q17", "Je comprends les reglas de gobernanza."), ("Q18", "J'identifie les opportunités d'automatisation.")]
            }
        else: # English
            return {
                dims[0]: [("Q1", "I understand how my work supports my organization's objectives."), ("Q2", "I can explain the purpose of digital initiatives."), ("Q3", "I can convey the organization's digital vision.")],
                dims[1]: [("Q4", "I apply security standards to data."), ("Q5", "I apply ethical principles in data handling."), ("Q6", "I ensure the data I use is reliable.")],
                dims[2]: [("Q7", "I understand user-centered design."), ("Q8", "I propose innovative ideas."), ("Q9", "I learn from mistakes in digital projects.")],
                dims[3]: [("Q10", "I understand the utility of a digital tools."), ("Q11", "I consider risks and governance when using tools."), ("Q12", "I understand interoperability concepts.")],
                dims[4]: [("Q13", "I promote teamwork between areas."), ("Q14", "I promote digital inclusion."), ("Q15", "I communicate effectively with stakeholders.")],
                dims[5]: [("Q16", "I suggest improvements in workflows."), ("Q17", "I understand governance rules."), ("Q18", "I identify automation opportunities.")]
            }

def get_maturity_level(score, is_org, lang):
    lvls_map = {
        "Español": ["Nivel 1: Explorador 🔍", "Nivel 2: Ajustado ⚙️", "Nivel 3: Desarrollado 📈", "Nivel 4: Maduro 🏆"] if is_org else ["Explorador 🌱", "Competente 🌿", "Gestor 🏗️", "Maduro 🚀"],
        "Français": ["Niveau 1: Explorateur 🔍", "Niveau 2: Ajusté ⚙️", "Niveau 3: Développé 📈", "Niveau 4: Mature 🏆"] if is_org else ["Explorateur 🌱", "Compétent 🌿", "Gestionnaire 🏗️", "Mature 🚀"],
        "English": ["Level 1: Explorer 🔍", "Level 2: Adjusted ⚙️", "Level 3: Developed 📈", "Level 4: Maduro 🏆"] if is_org else ["Explorer 🌱", "Competent 🌿", "Manager 🏗️", "Mature 🚀"]
    }
    lvls = lvls_map.get(lang, lvls_map["English"])
    thresholds = [2.0, 3.0, 4.0] if is_org else [2.0, 3.5, 4.5]
    if score < thresholds[0]: return lvls[0]
    if score < thresholds[1]: return lvls[1]
    if score < thresholds[2]: return lvls[2]
    return lvls[3]

# ==============================================================================
# 2. FUNCIÓN PRINCIPAL
# ==============================================================================
def run(st, name="", lang="Español", location="", **kwargs):
    ui_map = {
        "Español": {
            "main_title": "Evaluación de la Madurez Digital",
            "btn_ind": "👤 INDIVIDUAL", "btn_org": "🏢 ORGANIZACIONAL",
            "pdp": "Generar Plan", "pdo": "Generar Plan",
            "score": "Puntaje Global", "rec": "💡 Recomendaciones Estratégicas", "btn_down": "📥 Descargar Reporte Completo (.txt)",
            "err": "⚠️ Por favor, responda todas las preguntas.", "clean": "🧹 Limpiar",
            "intro_org": "Para llevar a su organización al siguiente nivel, siga estas recomendaciones:",
            "intro_ind": "Para avanzar en su desarrollo profesional digital, siga estas recomendaciones:"
        },
        "English": {
            "main_title": "Digital Maturity Assessment",
            "btn_ind": "👤 INDIVIDUAL", "btn_org": "🏢 ORGANIZATIONAL",
            "pdp": "Generate Plan", "pdo": "Generate Plan",
            "score": "Global Score", "rec": "💡 Strategic Recommendations", "btn_down": "📥 Download Full Report (.txt)",
            "err": "⚠️ Please answer all questions.", "clean": "🧹 Clear",
            "intro_org": "To move your organization to the next maturity level, follow these targeted recommendations:",
            "intro_ind": "To advance your personal digital maturity, follow these targeted recommendations:"
        },
        "Français": {
            "main_title": "Évaluation de la Maturité Numérique",
            "btn_ind": "👤 INDIVIDUEL", "btn_org": "🏢 ORGANISATIONNEL",
            "pdp": "Générer le Plan", "pdo": "Générer le Plan",
            "score": "Score Global", "rec": "💡 Recommandations Stratégiques", "btn_down": "📥 Télécharger le Rapport Complet (.txt)",
            "err": "⚠️ Veuillez répondre à toutes les questions.", "clean": "🧹 Effacer",
            "intro_org": "Pour faire passer votre organisation au niveau supérieur, suivez ces recommandations :",
            "intro_ind": "Pour faire progresser votre maturité numérique personnelle, suivez ces recommandations :"
        }
    }
    ui = ui_map.get(lang, ui_map["Español"])

    if "mad_mode" not in st.session_state: st.session_state.mad_mode = None
    if "res_ready" not in st.session_state: st.session_state.res_ready = False
    if "reset_key" not in st.session_state: st.session_state.reset_key = 0

    st.title(f"🚀 {ui['main_title']}")
    
    c1, c2 = st.columns(2)
    if c1.button(ui["btn_ind"], key="btn_ind_mode", use_container_width=True): 
        st.session_state.mad_mode, st.session_state.res_ready, st.session_state.reset_key = "IND", False, st.session_state.reset_key + 1
        st.rerun()
    if c2.button(ui["btn_org"], key="btn_org_mode", use_container_width=True): 
        st.session_state.mad_mode, st.session_state.res_ready, st.session_state.reset_key = "ORG", False, st.session_state.reset_key + 1
        st.rerun()

    if st.session_state.mad_mode:
        is_org = st.session_state.mad_mode == "ORG"
        q_db = get_questions_db(is_org, lang)
        st.divider()
        st.subheader(ui["btn_org"] if is_org else ui["btn_ind"])

        with st.form(key=f"f_{st.session_state.reset_key}"):
            responses = {}
            for dim, qs in q_db.items():
                st.markdown(f"### {dim}")
                for q_id, q_txt in qs:
                    with st.container(border=True):
                        col_t, col_o = st.columns([0.6, 0.4])
                        col_t.markdown(f"**{q_id}**: {q_txt}")
                        responses[q_id] = col_o.radio(
                            f"R_{q_id}_{st.session_state.reset_key}", 
                            [1, 2, 3, 4, 5], index=None, horizontal=True, label_visibility="collapsed"
                        )
            
            col_gen, col_clr = st.columns([0.7, 0.3])
            submit_label = ui['pdo'] if is_org else ui['pdp']
            
            if col_gen.form_submit_button(submit_label, use_container_width=True, type="primary"):
                if None in responses.values(): 
                    st.error(ui["err"])
                else: 
                    st.session_state.res_ready, st.session_state.final_res = True, responses

            if col_clr.form_submit_button(ui["clean"], use_container_width=True):
                st.session_state.res_ready = False
                st.session_state.reset_key += 1
                st.rerun()

        if st.session_state.res_ready:
            data = st.session_state.final_res
            res_list = [{"Dim": d, "Val": np.mean([data[q[0]] for q in qs])} for d, qs in q_db.items()]
            df_res = pd.DataFrame(res_list)
            avg = df_res["Val"].mean()
            nivel_global = get_maturity_level(avg, is_org, lang)
            fecha = datetime.now().strftime('%d/%m/%Y')

            st.markdown("---")
            st.markdown(f"#### {ui['score']}: {avg:.2f} | {nivel_global}")

            chart = alt.Chart(df_res).mark_bar().encode(
                x=alt.X("Val:Q", scale=alt.Scale(domain=[0, 5])),
                y=alt.Y("Dim:N", sort=None),
                color=alt.Color("Val:Q", scale=alt.Scale(scheme="blues"), legend=None),
                tooltip=["Dim", "Val"]
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)

            st.subheader(ui['rec'])
            
            # Matriz de Recomendaciones Completa (Previamente definida)
            if is_org:
                recs_db = {
                    "Español": {
                        "1-2": ("Nivel 1 → Nivel 2", ["Asignar Responsabilidad: Nombre un 'Líder Digital' o un pequeño comité.", "Redactar Políticas Básicas: Pasar de acuerdos verbales a directrices escritas.", "Inventariar sus Activos: Liste todas las herramientas y fuentes de datos actuales."]),
                        "2-3": ("Nivel 2 → Nivel 3", ["Estandarizar Procesos: Cree 'Procedimientos Operativos Estándar' (SOP) compartidos.", "Mejorar la Comunicación: Establezca una cadencia de reuniones regulares TI-Negocio.", "Formalizar la Retroalimentación: Implemente una fase obligatoria de pruebas de usuario."]),
                        "3-4": ("Nivel 3 → Nivel 4", ["Automatizar el Cumplimiento: Use software para supervisar privacidad y salud del sistema.", "Invertir en Alfabetización Digital: Cree una cultura 'digital-first' en toda la plantilla.", "Benchmarking Externo: Compare su rendimiento con los estándares internacionales."])
                    },
                    "English": {
                        "1-2": ("Level 1 → Level 2", ["Assign Ownership...", "Draft Basic Policies...", "Inventory Your Assets..."]),
                        "2-3": ("Level 2 → Level 3", ["Standardize Processes...", "Enhance Communication...", "Formalize Feedback..."]),
                        "3-4": ("Level 3 → Level 4", ["Automate Compliance...", "Invest in Digital Literacy...", "External Benchmarking..."])
                    },
                    "Français": {
                        "1-2": ("Niveau 1 → Niveau 2", ["Attribuer la Responsabilité...", "Rédiger des Politiques de Base...", "Inventorier vos Actifs..."]),
                        "2-3": ("Niveau 2 → Niveau 3", ["Standardiser les Processus...", "Améliorer la Communication...", "Formaliser les Retours..."]),
                        "3-4": ("Niveau 3 → Niveau 4", ["Automatiser la Conformité...", "Investir dans la Culture Numérique...", "Analyse Comparative Externe..."])
                    }
                }
            else:
                recs_db = {
                    "Español": {
                        "1-2": ("Explorador → Competente", ["Educación: Inscribirse en cursos de alfabetización digital y ética.", "Observación: Hacer shadowing a un Líder Digital.", "Inventario: Documentar flujos de trabajo personales para detectar hábitos ad-hoc."]),
                        "2-3": ("Competente → Gestor", ["Responsabilidad: Liderar un proyecto de documentación de procesos.", "Habilidades: Certificaciones en Agile o Diseño Centrado en el Usuario.", "Estandarización: Pasar de 'hacer' a 'definir' cómo deben hacerse las cosas."]),
                        "3-4": ("Gestor → Maduro", ["Mentoría: Mentorizar a exploradores sobre la visión digital.", "Políticas: Participar en el diseño de políticas de gobernanza.", "Tendencias: Investigar y reportar sobre IA y riesgos de gobernanza."]),
                        "4+": ("Maduro → Liderazgo", ["Asesoría: Actuar como asesor permanente del CIO.", "Difusión: Publicar sobre éxitos y fracasos del viaje digital.", "Predicción: Sugerir cambios estratégicos basados en datos del sistema."])
                    },
                    "English": {
                        "1-2": ("Explorer → Competent", ["Education: Foundational courses...", "Observation: Shadow a champion...", "Inventory: Document workflow..."]),
                        "2-3": ("Competent → Manager", ["Responsibility: Lead documentation...", "Skill Up: Agile/UCD certs...", "Standardization: Define tasks..."]),
                        "3-4": ("Manager → Mature", ["Mentorship: Help explorers...", "Policy: Task force participation...", "Trends: AI/Risk research..."]),
                        "4+": ("Mature → Leadership", ["Guide: Permanent advisor...", "Thought Leadership: Articles...", "Predictive: Data-driven strategy..."])
                    },
                    "Français": {
                        "1-2": ("Explorateur → Compétent", ["Éducation : Cours de base...", "Observation : Suivre un champion...", "Inventaire : Documenter les flux..."]),
                        "2-3": ("Compétent → Gestionnaire", ["Responsabilité : Diriger la documentation...", "Compétences : Certifs Agile/UCD...", "Standardisation : Définir les tâches..."]),
                        "3-4": ("Gestionnaire → Mature", ["Mentorat : Aider les explorateurs...", "Politiques : Groupes de travail...", "Tendances : Recherche IA/Risques..."]),
                        "4+": ("Mature → Leadership", ["Guide : Conseiller permanent...", "Leadership : Articles...", "Prédictive : Stratégie via données..."])
                    }
                }

            lang_recs = recs_db.get(lang, recs_db.get("English"))
            low_dims = df_res.sort_values(by="Val").head(3)
            report_recs = []

            for _, row in low_dims.iterrows():
                v = row['Val']
                if is_org:
                    k = "1-2" if v < 2.0 else "2-3" if v < 3.0 else "3-4"
                else:
                    k = "1-2" if v < 2.0 else "2-3" if v < 3.5 else "3-4" if v < 4.5 else "4+"
                
                lbl, bpts = lang_recs[k]
                report_recs.append(f"Dimension: {row['Dim']} ({v:.2f})\nGoal: {lbl}\n- " + "\n- ".join(bpts))
                with st.expander(f"📍 {row['Dim']} ({v:.1f}) | {lbl}"):
                    for r in bpts: st.write(f"· {r}")

            # ==============================================================================
            # CONSTRUCCIÓN DEL REPORTE DETALLADO (.TXT)
            # ==============================================================================
            report_txt = f"=== REPORTE DE MADUREZ DIGITAL ===\n"
            report_txt += f"Nombre: {name}\n"
            report_txt += f"Lugar: {location}\n"
            report_txt += f"Fecha: {fecha}\n"
            report_txt += f"Tipo de Evaluación: {'Organizacional' if is_org else 'Individual'}\n"
            report_txt += f"-------------------------------------------\n"
            report_txt += f"RESULTADO GLOBAL: {avg:.2f} / 5.0\n"
            report_txt += f"NIVEL DE MADUREZ: {nivel_global}\n"
            report_txt += f"-------------------------------------------\n\n"
            
            report_txt += f"DETALLE POR DIMENSIONES:\n"
            for _, row in df_res.iterrows():
                dim_lvl = get_maturity_level(row['Val'], is_org, lang)
                report_txt += f"- {row['Dim']}: {row['Val']:.2f} ({dim_lvl})\n"
            
            report_txt += f"\nRECOMENDACIONES ESTRATÉGICAS:\n"
            report_txt += "\n".join(report_recs)
            
            report_txt += f"\n\n-------------------------------------------\n"
            report_txt += f"RESPUESTAS DETALLADAS DEL CUESTIONARIO:\n"
            for dim, qs in q_db.items():
                report_txt += f"\n[{dim}]\n"
                for q_id, q_txt in qs:
                    val = data.get(q_id, "N/A")
                    report_txt += f"{q_id}. {q_txt} -> RESPUESTA: {val}\n"
            
            st.download_button(
                ui['btn_down'], 
                report_txt, 
                f"Reporte_Madurez_{name.replace(' ','_')}_{fecha.replace('/','-')}.txt", 
                use_container_width=True
            )