import streamlit as st

# -----------------------------------------------------
# PAGE SETUP
# -----------------------------------------------------
st.set_page_config(page_title="Needs Criteria — Clinical & Functional", layout="wide")

# --- COLOR SYSTEM (Purple-based theme) ---
DARK_PURPLE = "#4C1D95"
MID_PURPLE = "#6D28D9"
LIGHT_PURPLE = "#EDE9FE"
PILL_MUST_BG = "#F3E8FF"
PILL_NICE_BG = "#E0E7FF"
TEXT_COLOR = "#1E1B4B"
SUBTEXT_COLOR = "#42307D"
BORDER_COLOR = "#C4B5FD"

# -----------------------------------------------------
# GLOBAL CSS STYLES
# -----------------------------------------------------
CUSTOM_CSS = f"""
<style>
body {{
  background: linear-gradient(120deg, #f8f5ff 0%, #faf7ff 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: {TEXT_COLOR};
}}
.slide {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.2rem 1.4rem;
}}
.slide h1 {{
  font-size: 2.6rem;
  font-weight: 800;
  margin-bottom: 0.3rem;
  background: linear-gradient(90deg, {DARK_PURPLE}, {MID_PURPLE});
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.slide h3 {{
  font-size: 1.2rem;
  font-weight: 500;
  color: {SUBTEXT_COLOR};
  margin-bottom: 1rem;
}}
.grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.6rem;
}}
.card {{
  background-color: white;
  border: 1px solid {BORDER_COLOR};
  border-radius: 16px;
  padding: 1.2rem 1.4rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  transition: transform 0.25s ease;
}}
.card:hover {{
  transform: translateY(-3px);
}}
.card h2 {{
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: {DARK_PURPLE};
  display: flex;
  align-items: center;
  gap: 0.5rem;
}}
.pill {{
  display: flex;
  align-items: flex-start;
  padding: 0.75rem 1rem;
  margin-bottom: 0.6rem;
  border-radius: 10px;
  line-height: 1.35;
  transition: all 0.25s ease;
  font-size: 1.05rem;
  font-weight: 450;
}}
.pill.must {{
  background-color: {PILL_MUST_BG};
  border-left: 6px solid {MID_PURPLE};
}}
.pill.nice {{
  background-color: {PILL_NICE_BG};
  border-left: 6px solid {DARK_PURPLE};
}}
.pill strong {{
  font-weight: 600;
  color: {DARK_PURPLE};
}}
footer {{
  font-size: 0.85rem;
  margin-top: 1rem;
  color: {SUBTEXT_COLOR};
  text-align: center;
}}
@media (max-width: 980px) {{
  .grid {{ grid-template-columns: 1fr; }}
  .slide h1 {{ font-size: 2.1rem; }}
}}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------------------------------
# PAGE HEADER
# -----------------------------------------------------
st.markdown("""
<div class="slide">
  <h1>Needs Criteria — Clinical & Functional</h1>
  <h3>Distinguishing measurable <b>Must-Haves</b> from aspirational <b>Nice-to-Haves</b></h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# CONTENT
# -----------------------------------------------------
must_haves = [
    "<strong>Accurate mid-case forecast</strong>: Mean absolute error ≤ 5–7 min by 50 % elapsed time; calibration slope 0.9–1.1.",
    "<strong>Live data fusion</strong>: Integrate anesthesia timestamps, device events, and EHR logs with <10 s latency.",
    "<strong>Generalizability</strong>: Validated across ≥3 surgical services (general, ortho, vascular).",
    "<strong>Human-in-the-loop</strong>: Clinician override allowed; interface shows P10–P90 confidence band.",
    "<strong>Safety guardrails</strong>: Forecasts recommend only (no auto-rebook); full audit trail of adjustments."
]

nice_haves = [
    "<strong>Case-mix context</strong>: Incorporate BMI, ASA class, resident level, and implant SKU metadata.",
    "<strong>Explainability</strong>: ‘Top drivers’ visualization (e.g., bleed score↑, scope changes↑).",
    "<strong>Team prompts</strong>: Predictive turnover and ‘call next patient’ alerts.",
    "<strong>Learning mode</strong>: Nightly service-specific fine-tuning with seasonal adaptation.",
    "<strong>Dashboard widgets</strong>: Real-time room status, ETA to close, variance vs plan."
]

# Two-column grid
st.markdown('<div class="slide"><div class="grid">', unsafe_allow_html=True)

# LEFT COLUMN: MUST-HAVES
st.markdown('<div class="card"><h2>Must-Have</h2>', unsafe_allow_html=True)
for item in must_haves:
    st.markdown(f'<div class="pill must">{item}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# RIGHT COLUMN: NICE-TO-HAVES
st.markdown('<div class="card"><h2>Nice-to-Have</h2>', unsafe_allow_html=True)
for item in nice_haves:
    st.markdown(f'<div class="pill nice">{item}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Close grid container
st.markdown('</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------
st.markdown("""
<footer>
Criteria v1.1 · Surgical Innovation Team · Color scheme #4C1D95 #6D28D9 #E0E7FF — Designed Oct 2025
</footer>
""", unsafe_allow_html=True)
