import streamlit as st

st.set_page_config(page_title="Needs Criteria — Dual Tables", layout="wide")

# -------------------- THEME COLORS (purple) --------------------
PURPLE_DARK = "#4C1D95"
PURPLE = "#6D28D9"
PURPLE_MID = "#7C3AED"
INDIGO_TEXT = "#1E1B4B"
LAVENDER_BG = "#F8F5FF"
CARD_BG = "#FFFFFF"
MUST_BG = "#F3E8FF"     # light violet
NICE_BG = "#E0E7FF"     # light periwinkle
BORDER = "#DDD6FE"

# -------------------- GLOBAL CSS --------------------
CSS = f"""
<style>
:root {{
  --purple-dark: {PURPLE_DARK};
  --purple: {PURPLE};
  --indigo-text: {INDIGO_TEXT};
  --lavender: {LAVENDER_BG};
  --card: {CARD_BG};
  --must: {MUST_BG};
  --nice: {NICE_BG};
  --border: {BORDER};
}}

body {{
  background: linear-gradient(120deg, var(--lavender), #FBFAFF);
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  color: var(--indigo-text);
}}

.slide-wrap {{
  max-width: 1240px;
  margin: 0 auto;
  padding: 8px 12px 0 12px;
}}

.header {{
  display:flex;
  align-items:baseline;
  justify-content:space-between;
  margin-bottom: 8px;
}}
.title {{
  font-weight: 800;
  font-size: 32px;
  letter-spacing: -0.2px;
  background: linear-gradient(90deg, var(--purple-dark), {PURPLE_MID});
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.dual {{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  align-items:start;
}}

.card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  box-shadow: 0 6px 18px rgba(76,29,149,0.06);
  overflow:hidden;
}}

.card-header {{
  display:flex;
  align-items:center;
  gap:10px;
  padding: 12px 16px;
  font-weight: 750;
  font-size: 22px;
  color: var(--purple-dark);
  background: linear-gradient(180deg, #F5F0FF, #F8F6FF);
  border-bottom: 1px solid var(--border);
}}

.icon-check {{
  width:18px; height:18px; display:inline-block; background: var(--purple);
  -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 16.2 4.8 12 3.4 13.4 9 19 21 7 19.6 5.6z" fill="black"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 16.2 4.8 12 3.4 13.4 9 19 21 7 19.6 5.6z" fill="black"/></svg>') no-repeat center/contain;
}}

.icon-diamond {{
  width:18px; height:18px; display:inline-block; background: var(--purple);
  -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 3 21 12 12 21 3 12 12 3z" fill="black"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 3 21 12 12 21 3 12 12 3z" fill="black"/></svg>') no-repeat center/contain;
}}

.rows {{
  display:flex;
  flex-direction:column;
  padding: 10px 12px 14px 12px;
  gap: 10px;
}}

.row {{
  display:grid;
  grid-template-columns: 220px 1fr;   /* fixed label column; fluid text column */
  align-items:start;
  gap: 14px;
  background: var(--must);
  border-left: 6px solid var(--purple);
  border-radius: 12px;
  padding: 10px 12px;
  line-height: 1.35;
  font-size: 16.5px;
}}
.row + .row {{ margin-top: 2px; }}

.row .label {{
  font-weight: 650;
  color: var(--purple-dark);
  word-break: break-word;
}}
.row .text {{
  font-weight: 430;
}}

.card.nice .row {{
  background: var(--nice);
  border-left-color: var(--purple-dark);
}}

.note {{
  padding: 6px 12px 12px 12px;
  font-size: 12.5px;
  color:#4B5563;
}}

@media (max-width: 1100px) {{
  .dual {{ grid-template-columns: 1fr; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -------------------- PAGE HEADER --------------------
st.markdown("""
<div class="slide-wrap">
  <div class="header">
    <div class="title">Needs Criteria — Clinical & Functional</div>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------- DATA --------------------
must_rows = [
    ("Accurate mid-case forecast",
     "Mean absolute error ≤ 5–7 min at the 50% elapsed mark; calibration slope 0.9–1.1."),
    ("Live data fusion",
     "Integrate anesthesia timestamps, device events, and EHR OpTime/SurgiNet logs with < 10 s latency."),
    ("Generalizability",
     "Validated across ≥ 3 surgical services (general, orthopedic, vascular) with non-inferiority per service."),
    ("Human-in-the-loop",
     "Clinician override available; interface shows P10–P90 confidence band."),
    ("Safety guardrails",
     "Recommendations only (no auto re-booking/cancellation); comprehensive audit trail for changes.")
]

nice_rows = [
    ("Case-mix context",
     "Optional inputs: BMI, ASA class, resident level, implant SKU metadata."),
    ("Explainability",
     "Compact ‘Top drivers’ attribution (e.g., bleed score↑, scope exchanges↑)."),
    ("Team prompts",
     "Predictive turnover and ‘call next patient’ alerts when thresholds are crossed."),
    ("Learning mode",
     "Nightly service-specific fine-tuning; seasonal pattern adaptation."),
    ("Dashboard widgets",
     "Tiles for room status, ETA-to-close, and variance vs plan.")
]

# -------------------- RENDER DUAL CARDS --------------------
st.markdown('<div class="slide-wrap"><div class="dual">', unsafe_allow_html=True)

# Must-have card
st.markdown('<div class="card must">', unsafe_allow_html=True)
st.markdown('<div class="card-header"><span class="icon-check"></span>Must-Have</div>', unsafe_allow_html=True)
st.markdown('<div class="rows">', unsafe_allow_html=True)
for label, text in must_rows:
    st.markdown(f'''
    <div class="row">
      <div class="label">{label}</div>
      <div class="text">{text}</div>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) # rows
st.markdown('<div class="note">Specs are concise; left column is fixed width to keep alignment “justified”.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) # card

# Nice-to-have card
st.markdown('<div class="card nice">', unsafe_allow_html=True)
st.markdown('<div class="card-header"><span class="icon-diamond"></span>Nice-to-Have</div>', unsafe_allow_html=True)
st.markdown('<div class="rows">', unsafe_allow_html=True)
for label, text in nice_rows:
    st.markdown(f'''
    <div class="row">
      <div class="label">{label}</div>
      <div class="text">{text}</div>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) # rows
st.markdown('<div class="note">Room for expansion (e.g., predictive staffing, cross-site benchmarking) without clutter.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) # card

st.markdown('</div></div>', unsafe_allow_html=True)  # dual + wrap close
