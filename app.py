import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="SmartPMO | AI Project & Resource Analytics",
    page_icon="📊",
    layout="wide"
)

# 2. Header & Titel
st.title("📊 SmartPMO – AI Project & Resource Analytics")
st.caption("IT-Consulting Management Dashboard für Projekt-KPIs, Ressourcen-Auslastung & KI-Risikoanalysen")
st.markdown("---")

# 3. Session State Initialisierung (Dynamische Datenspeicherung)
if "projects_list" not in st.session_state:
    st.session_state.projects_list = [
        {"Projekt-ID": "PRJ-101", "Projektname": "Cloud Migration Azure", "Kunde": "FinTech AG", "Budget (€)": 120000, "Ist-Kosten (€)": 115000, "Fortschritt (%)": 90, "Team-Größe": 5},
        {"Projekt-ID": "PRJ-102", "Projektname": "ERP Rollout Phase 2", "Kunde": "Logistik SE", "Budget (€)": 250000, "Ist-Kosten (€)": 190000, "Fortschritt (%)": 65, "Team-Größe": 8},
        {"Projekt-ID": "PRJ-103", "Projektname": "KI-Chatbot Integration", "Kunde": "Retail Group", "Budget (€)": 85000, "Ist-Kosten (€)": 92000, "Fortschritt (%)": 80, "Team-Größe": 3},
        {"Projekt-ID": "PRJ-104", "Projektname": "BI Dashboard Modernization", "Kunde": "PharmaCare GmbH", "Budget (€)": 45000, "Ist-Kosten (€)": 30000, "Fortschritt (%)": 70, "Team-Größe": 2},
        {"Projekt-ID": "PRJ-105", "Projektname": "Workplace Microsoft Teams", "Kunde": "Automotive Holding", "Budget (€)": 110000, "Ist-Kosten (€)": 60000, "Fortschritt (%)": 40, "Team-Größe": 4}
    ]

if "resources_list" not in st.session_state:
    st.session_state.resources_list = [
        {"Berater": "Max Mustermann", "Rolle": "Senior Cloud Architect", "Auslastung (%)": 110, "Hauptprojekt": "Cloud Migration Azure", "Status": "Überlastet ⚠️"},
        {"Berater": "Oumaima Majda", "Rolle": "IT-Consultant / Data Analyst", "Auslastung (%)": 85, "Hauptprojekt": "KI-Chatbot Integration", "Status": "Optimal ✅"},
        {"Berater": "Laura Schmidt", "Rolle": "Project Manager", "Auslastung (%)": 95, "Hauptprojekt": "ERP Rollout Phase 2", "Status": "Optimal ✅"},
        {"Berater": "Sven Weber", "Rolle": "Full-Stack Developer", "Auslastung (%)": 125, "Hauptprojekt": "Cloud Migration Azure", "Status": "Kritisch Überlastet 🚨"},
        {"Berater": "Anna Becker", "Rolle": "DevOps Engineer", "Auslastung (%)": 70, "Hauptprojekt": "Workplace Microsoft Teams", "Status": "Kapazität frei 🟢"}
    ]

# 4. Formular: Neues Projekt dynamisch hinzufügen
with st.expander("➕ Neues Projekt zum Dashboard hinzufügen"):
    with st.form("new_project_form", clear_on_submit=True):
        col_f1, col_f2, col_f3 = st.columns(3)
        
        with col_f1:
            new_id = st.text_input("Projekt-ID", value=f"PRJ-10{len(st.session_state.projects_list)+1}")
            new_name = st.text_input("Projektname")
            new_client = st.text_input("Kunde / Unternehmen")

        with col_f2:
            new_budget = st.number_input("Budget (€)", min_value=1000, step=5000, value=50000)
            new_cost = st.number_input("Ist-Kosten (€)", min_value=0, step=1000, value=10000)

        with col_f3:
            new_progress = st.slider("Fortschritt (%)", 0, 100, 10)
            new_team = st.number_input("Team-Größe (Personen)", min_value=1, value=3)

        submit_button = st.form_submit_button("🚀 Projekt speichern")

        if submit_button:
            if new_name and new_client:
                st.session_state.projects_list.append({
                    "Projekt-ID": new_id,
                    "Projektname": new_name,
                    "Kunde": new_client,
                    "Budget (€)": new_budget,
                    "Ist-Kosten (€)": new_cost,
                    "Fortschritt (%)": new_progress,
                    "Team-Größe": new_team
                })
                st.success(f"Projekt '{new_name}' wurde erfolgreich hinzugefügt!")
                st.rerun()
            else:
                st.error("Bitte gib mindestens einen Projektnamen und einen Kunden ein!")

# 5. DataFrames erzeugen & KI-Logik anwenden
df_projects = pd.DataFrame(st.session_state.projects_list)
df_resources = pd.DataFrame(st.session_state.resources_list)

def calculate_risk(row):
    budget_used = (row["Ist-Kosten (€)"] / row["Budget (€)"]) * 100 if row["Budget (€)"] > 0 else 0
    progress = row["Fortschritt (%)"]
    
    if budget_used > 100:
        return "🚨 Budgetüberschreitung", "High"
    elif budget_used > progress + 15:
        return "⚠️ Kosten laufen Fortschritt davon", "Medium"
    else:
        return "✅ Im Rahmen", "Low"

df_projects[["KI-Risikoanalyse", "Risikostufe"]] = df_projects.apply(calculate_risk, axis=1, result_type="expand")

# 6. Executive Summary KPIs
total_budget = df_projects["Budget (€)"].sum()
total_spent = df_projects["Ist-Kosten (€)"].sum()
avg_progress = df_projects["Fortschritt (%)"].mean()
high_risk_count = len(df_projects[df_projects["Risikostufe"] != "Low"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Gesamtbudget Portfolio", f"{total_budget:,.0f} €".replace(",", "."))
col2.metric("Ist-Kosten Gesamt", f"{total_spent:,.0f} €".replace(",", "."), delta=f"{(total_spent/total_budget)*100 if total_budget > 0 else 0:.1f}% genutzt")
col3.metric("Durchschnittl. Fortschritt", f"{avg_progress:.1f} %")
col4.metric("Kritische Projekte (KI-Warnung)", f"{high_risk_count} Projekte", delta_color="inverse")

st.markdown("---")

# 7. Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📌 Portfolio & KI-Risikoanalyse", "👥 Ressourcen & Auslastung", "🔮 What-If Simulator"])

# --- TAB 1: PORTFOLIO & RISIKO ---
with tab1:
    st.subheader("Projekt-Portfolio Übersicht")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        fig_budget = go.Figure(data=[
            go.Bar(name='Budget (€)', x=df_projects['Projektname'], y=df_projects['Budget (€)'], marker_color='#0052CC'),
            go.Bar(name='Ist-Kosten (€)', x=df_projects['Projektname'], y=df_projects['Ist-Kosten (€)'], marker_color='#FF4B4B')
        ])
        fig_budget.update_layout(barmode='group', title="Budget vs. Ist-Kosten je Projekt", height=350)
        st.plotly_chart(fig_budget, use_container_width=True)
        
    with col_chart2:
        fig_progress = px.bar(df_projects, x='Fortschritt (%)', y='Projektname', orientation='h',
                              color='Risikostufe', color_discrete_map={'Low': '#2E7D32', 'Medium': '#ED6C02', 'High': '#D32F2F'},
                              title="Fortschritt & KI-Risikoeinstufung")
        fig_progress.update_layout(height=350)
        st.plotly_chart(fig_progress, use_container_width=True)

    st.subheader("📋 Detaillierte Projektliste mit KI-Bewertung")
    st.dataframe(df_projects[["Projekt-ID", "Projektname", "Kunde", "Budget (€)", "Ist-Kosten (€)", "Fortschritt (%)", "KI-Risikoanalyse"]], use_container_width=True)

# --- TAB 2: RESSOURCEN ---
with tab2:
    st.subheader("Ressourcen-Auslastung im IT-Consulting")
    
    fig_res = px.bar(df_resources, x='Berater', y='Auslastung (%)', color='Status',
                     color_discrete_map={'Optimal ✅': '#2E7D32', 'Überlastet ⚠️': '#ED6C02', 'Kritisch Überlastet 🚨': '#D32F2F', 'Kapazität frei 🟢': '#0288D1'},
                     title="Auslastung der Berater in % (Soll: 100%)")
    fig_res.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text="Max. Soll-Kapazität (100%)")
    st.plotly_chart(fig_res, use_container_width=True)
    
    st.subheader("Team-Übersicht")
    st.table(df_resources)

# --- TAB 3: SIMULATOR ---
with tab3:
    st.subheader("🔮 Interaktiver Szenario-Simulator")
    st.write("Simulieren Sie Kosten- und Budgetauswirkungen bei Projektverzögerungen:")
    
    selected_proj = st.selectbox("Wähle ein Projekt zur Simulation:", df_projects["Projektname"])
    delay_weeks = st.slider("Projektverzögerung in Wochen:", 0, 12, 2)
    daily_rate = st.number_input("Durchschnittlicher Tagessatz des Teams (€):", value=800, step=100)
    
    proj_row = df_projects[df_projects["Projektname"] == selected_proj].iloc[0]
    extra_cost = delay_weeks * 5 * daily_rate * (proj_row["Team-Größe"] * 0.5)
    new_total_cost = proj_row["Ist-Kosten (€)"] + extra_cost
    budget_diff = proj_row["Budget (€)"] - new_total_cost
    
    st.markdown("### 📈 Simulationsergebnis:")
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Zusätzliche Personalkosten", f"+ {extra_cost:,.0f} €".replace(",", "."))
    res_col2.metric("Neuer Erwarteter Endpreis", f"{new_total_cost:,.0f} €".replace(",", "."), 
                    delta=f"{budget_diff:,.0f} € Restbudget".replace(",", "."),
                    delta_color="normal" if budget_diff >= 0 else "inverse")