import streamlit as st

st.set_page_config(page_title="Needs Criteria — Slide 1", page_icon="🧠", layout="wide")

# ---------- THEME / STYLES ----------
PRIMARY_GREEN = "#208A3E"
PRIMARY_BLUE = "#2E6DFF"
PILL_GREEN_BG = "#E9F6EE"
PILL_BLUE_BG = "#EAF2FF"
TEXT_COLOR = "#0F172A"  # slate-900
SUBTEXT_COLOR = "#334155"  # slate-700
RULE_COLOR = "#E5E7EB"  # gray-200

CUSTOM_CSS = f"""
<style>
/* page padding */
.main > div {{ padding-top: 10px; }}

.slide-container {{
  max-width: 1200px;
  margin: 0 auto;
}}

.slide-title {{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-weight: 700;
  font-size: 38px;
  line-height: 1.1;
  letter-spacing: -0.3px;
  color: {TEXT_COLOR};
  margin: 6px 0 2px 0;
}}

.slide-subtitle {{
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-weight: 500;
  font-size: 18px;
  color: {SUBTEXT_COLOR};
  margin-bottom: 18px;
}}

.rule {{
  height: 1px;
  background: {RULE_COLOR};
  margin: 8px 0 24px 0;
  border-radius: 1px;
}}

.columns-wrap {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}}

.col-card {{
  border: 1px solid {RULE_COLOR};
  border-radius: 16px;
  padding: 18px 18px 14px 18px;
  background: white;
  box-shadow: 0 0 0 rgba(0,0,0,0);
}}

.col-title {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-weight: 700;
  font-size: 26px;
  color: {TEXT_COLOR};
}}

.icon-must {{
  width: 18px; height: 18px; display:inline-block;
  background: {PRIMARY_GREEN};
  -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="black" d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>') no-repeat center / contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="black" d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>') no-repeat center / contain;
}}

.icon-nice {{
  width: 18px; height: 18px; display:inline-block;
  background: {PRIMARY_BLUE};
  -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8" fill="black"/></svg>') no-repeat center / contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8" fill="black"/></svg>') no-repeat center / contain;
}}

.pill {{
  display: flex;
  align-items: flex-start;
  gap: 10px;
  border-radius: 10px;
  padding: 10px 12px;
  margin: 10px 0;
  line-height: 1.25;
  font-size: 19px;
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  color: {TEXT_COLOR};
}}

.pill.must {{
  background: {PILL_GREEN_BG};
  border: 1px solid rgba(32,138,62,0.08);
}}

.pill.nice {{
  background: {PILL_BLUE_BG};
  border: 1px solid rgba(46,109,255,0.10);
}}

.pill strong {{ font-weight: 700; }}

.footer-note {{
  margin-top: 16px;
  font-size: 14px;
  color: {SUBTEXT_COLOR};
}}
@media (max-width: 980px) {{
  .columns-wrap {{ grid-template-columns: 1fr; }}
  .slide-title {{ font-size: 32px; }}
}}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- PAGE HEADER ----------
st.markdown(
    """
    <div class="slide-container">
      <div class="slide-title">Needs Criteria — Clinical & Functional</div>
      <div class="slide-subtitle">Must-Have vs Nice-to-Have (color-coded; concise, measurable, deployable)</div>
      <div class="rule"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENT DEFINITIONS ----------
must_haves = [
    "<strong>Accurate mid-case forecast</strong>: MAE ≤ 5–7 min by 50% elapsed; calibration slope 0.9–1.1.",
    "<strong>Live data fusion</strong>: anesthesia timestamps, device events, EHR OpTime/SurgiNet, nurse charting with &lt;10-sec latency.",
    "<strong>Generalizability</strong>: validated in ≥3 services (general, ortho, vascular) with non-inferiority per service.",
    "<strong>Human-in-the-loop</strong>: surgeon/anesthetist override; forecast shows confidence band (P10–P90).",
    "<strong>Safety guardrails</strong>: recommend only (no auto-book/cancel); full audit trail of changes."
]

nice_to_haves = [
    "<strong>Case-mix context</strong>: BMI, ASA, resident level, implant SKU when available.",
    "<strong>Explainability</strong>: quick ‘Top drivers’ (e.g., bleed score ↑, scope exchanges ↑).",
    "<strong>Team prompts</strong>: turnover & ‘call next patient’ alerts on threshold crossings.",
    "<strong>Learning mode</strong>: nightly service-specific fine-tuning; seasonal patterns.",
    "<strong>Dashboard widgets</strong>: room status, ETA to close, variance vs plan."
]

# ---------- RENDER 2-COLUMN SLIDE ----------
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown(
        """
        <div class="slide-container">
          <div class="col-card">
            <div class="col-title"><span class="icon-must"></span>Must-Have</div>
        """,
        unsafe_allow_html=True
    )
    for item in must_haves:
        st.markdown(
            f"""
            <div class="pill must">
              <span class="icon-must"></span>
              <div>{item}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div></div>", unsafe_allow_html=True)

with col_right:
    st.markdown(
        """
        <div class="slide-container">
          <div class="col-card">
            <div class="col-title"><span class="icon-nice"></span>Nice-to-Have</div>
        """,
        unsafe_allow_html=True
    )
    for item in nice_to_haves:
        st.markdown(
            f"""
            <div class="pill nice">
              <span class="icon-nice"></span>
              <div>{item}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    """
    <div class="slide-container footer-note">
      <div>Criteria v1.0 — Oct 2025 · Icons: check = must-have, dot = nice-to-have · Colors follow WCAG-AA contrast.</div>
    </div>
    """,
    unsafe_allow_html=True
)
