# SmartPMO – AI Project & Resource Intelligence Dashboard

Ein interaktives IT-Consulting Management-Dashboard, entwickelt mit **Python**, **Streamlit** und **Plotly**.

**SmartPMO** unterstützt Project Management Offices (PMO) und IT-Beratungen dabei, Multi-Projekt-Portfolios zu überwachen, die Berater-Auslastung zu analysieren, Budgetrisiken durch automatisierte KI-Regeln frühzeitig zu erkennen und What-If-Szenariosimulationen durchzuführen.

---

##  Live Demo & Portfolio
* **Portfolio Website:** [mein-portfolio-oumaima.streamlit.app](https://mein-portfolio-oumaima.streamlit.app)
* **Tech Stack:** `Python 3.12` | `Streamlit` | `Pandas` | `Plotly` | `NumPy`

---

##  Kernfunktionen

### 1. Executive Summary & Portfolio KPIs
* **Echtzeit-Übersicht:** Aggregierte Kennzahlen zu Gesamtbudget, Ist-Kosten, durchschnittlichem Projektfortschritt und kritischen Risikowarnungen.
* **Dynamische Budget- vs. Kosten-Diagramme:** Interaktive Plotly-Balkendiagramme zum direkten Vergleich von geplantem Budget und Ist-Kosten pro Projekt.

### 2. KI-Risikoanalyse (Rule Engine)
* **Automatisierte Risikoerkennung:** Vergleicht den relativen Budgetverbrauch mit dem tatsächlichen Projektfortschritt.
* **Frühwarnsystem:**
  *  **High Risk:** Budgetüberschreitung (Kosten > 100%).
  *  **Medium Risk:** Kosten laufen dem Fortschritt davon (Ist-Kosten % > Fortschritt % + 15%).
  *  **Low Risk:** Projekt liegt im geplanten Rahmen.

### 3. Ressourcen- & Kapazitäts-Tracking
* **Auslastungsanalyse:** Visualisiert die Auslastung der Berater im Vergleich zur Soll-Kapazität (100%).
* **Status-Indikatoren:** Hebt überlastete Berater und verfügbare Kapazitäten  direkt hervor.

### 4. Interaktiver What-If Szenario-Simulator
* **Finanzielle Auswirkungsberechnung:** Berechnet Zusatzkosten bei Projektverzögerungen basierend auf Teamgröße, Verzögerungswochen und Tagessätzen (€).
* **Live-Budgetprognose:** Berechnet dynamisch die erwarteten Gesamtkosten und verbleibenden Puffer neu.

### 5. Dynamische Dateneingabe
* Integriertes Formular zum Hinzufügen neuer Projekte im laufenden Betrieb unter Nutzung von Streamlit `session_state`.

---

##  Projektstruktur

```text
SmartPMO-Analytics/
│
├── app.py              # Hauptanwendung (UI, Analytics & Simulation)
├── requirements.txt    # Python-Abhängigkeiten
└── README.md           # Projektdokumentation
