import streamlit as st

st.set_page_config(page_title="Needs Criteria — Data, IT, Privacy & Ops", layout="wide")

# -------------------- PURPLE THEME --------------------
PURPLE_DARK = "#4C1D95"
PURPLE = "#6D28D9"
PURPLE_MID = "#7C3AED"
LAVENDER = "#F8F5FF"
CARD = "#FFFFFF"
BORDER = "#DDD6FE"
TEXT = "#1E1B4B"
SUBTEXT = "#4B5563"
CHIP_BG = "#F3E8FF"       # bullets
CHIP_BG_2 = "#EDE9FE"     # alt bullets

# -------------------- GLOBAL CSS --------------------
CSS = f"""
<style>
body {{
  background: radial-gradient(1200px 600px at 20% -20%, #FBFAFF 0%, {LAVENDER} 60%, #FFFFFF 100%);
  color: {TEXT};
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
}}
.container {{
  max-width: 1280px;
  margin: 0 auto;
  padding: 10px 14px 0 14px;
}}
.title {{
  font-weight: 800;
  font-size: 32px;
  letter-spacing: -0.2px;
  background: linear-gradient(90deg, {PURPLE_DARK}, {PURPLE_MID});
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 2px;
}}
.subtitle {{
  color: {SUBTEXT};
  font-size: 15px;
  margin-bottom: 12px;
}}
.grid4 {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}}
.card {{
  background: {CARD};
  border: 1px solid {BORDER};
  border-radius: 14px;
  box-shadow: 0 8px 18px rgba(76,29,149,0.06);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  min-height: 360px;
}}
.ribbon {{
  height: 6px;
  background: linear-gradient(90deg, {PURPLE_DARK}, {PURPLE});
}}
.header {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border-bottom: 1px solid {BORDER};
}}
.header h2 {{
  font-size: 22px;
  font-weight: 700;
  color: {PURPLE_DARK};
  margin: 0;
}}
.icon {{
  width: 18px; height: 18px; display:inline-block; background: {PURPLE};
}}
/* monoline SVG masks for icons */
.icon-db {{
  -webkit-mask: url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 3c-4.97 0-9 1.79-9 4v10c0 2.21 4.03 4 9 4s9-1.79 9-4V7c0-2.21-4.03-4-9-4Zm0 2c3.87 0 7 .9 7 2s-3.13 2-7 2-7-.9-7-2 3.13-2 7-2Zm-7 5c1.66 1.02 4.7 1.5 7 1.5S17.34 11.02 19 10v3c0 1.1-3.13 2-7 2s-7-.9-7-2V10Zm0 6c1.66 1.02 4.7 1.5 7 1.5s5.34-.48 7-1.5v2c0 1.1-3.13 2-7 2s-7-.9-7-2v-2Z"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 1.79-9 4v10c0 2.21 4.03 4 9 4s9-1.79 9-4V7c0-2.21-4.03-4-9-4Zm0 2c3.87 0 7 .9 7 2s-3.13 2-7 2-7-.9-7-2 3.13-2 7-2Zm-7 5c1.66 1.02 4.7 1.5 7 1.5S17.34 11.02 19 10v3c0 1.1-3.13 2-7 2s-7-.9-7-2V10Zm0 6c1.66 1.02 4.7 1.5 7 1.5s5.34-.48 7-1.5v2c0 1.1-3.13 2-7 2s-7-.9-7-2v-2Z"/></svg>') no-repeat center/contain;
}}
.icon-plug {{
  -webkit-mask: url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M7 2h2v6H7V2Zm8 0h2v6h-2V2ZM6 9h12v2a6 6 0 0 1-6 6H9a3 3 0 0 0-3 3v2H4v-2a5 5 0 0 1 5-5h3a4 4 0 0 0 4-4V9H6Z"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7 2h2v6H7V2Zm8 0h2v6h-2V2ZM6 9h12v2a6 6 0 0 1-6 6H9a3 3 0 0 0-3 3v2H4v-2a5 5 0 0 1 5-5h3a4 4 0 0 0 4-4V9H6Z"/></svg>') no-repeat center/contain;
}}
.icon-shield {{
  -webkit-mask: url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 2 4 5v6c0 5 3.4 9.6 8 11 4.6-1.4 8-6 8-11V5l-8-3Zm-1 13-3-3 1.4-1.4L11 12.2l3.6-3.6L16 10l-5 5Z"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2 4 5v6c0 5 3.4 9.6 8 11 4.6-1.4 8-6 8-11V5l-8-3Zm-1 13-3-3 1.4-1.4L11 12.2l3.6-3.6L16 10l-5 5Z"/></svg>') no-repeat center/contain;
}}
.icon-people {{
  -webkit-mask: url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M9 11a4 4 0 1 0-0.001-8.001A4 4 0 0 0 9 11Zm8 5c0-2.8-4.7-3.5-8-3.5S1 13.2 1 16v3h16v-3Zm5-10h-2l-1 3h-3l1 2-1 3h3l1 3h2l-1-3h3l-1-3h-3l1-3Z"/></svg>') no-repeat center/contain;
          mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 11a4 4 0 1 0-0.001-8.001A4 4 0 0 0 9 11Zm8 5c0-2.8-4.7-3.5-8-3.5S1 13.2 1 16v3h16v-3Zm5-10h-2l-1 3h-3l1 2-1 3h3l1 3h2l-1-3h3l-1-3h-3l1-3Z"/></svg>') no-repeat center/contain;
}}
.body {{
  padding: 10px 12px 14px 12px;
  display:flex; flex-direction:column; gap:10px;
}}
.chip {{
  background: {CHIP_BG};
  border: 1px solid {BORDER};
  border-radius: 10px;
  padding: 8px 10px;
  font-size: 15.8px;
  line-height: 1.25;
}}
.chip:nth-child(2n) {{ background: {CHIP_BG_2}; }}
.chip b {{ font-weight: 700; color: {PURPLE_DARK}; }}
.footer-strip {{
  margin-top: 14px;
  background: linear-gradient(90deg, {CHIP_BG_2}, {CHIP_BG});
  border: 1px dashed {BORDER};
  border-radius: 12px;
  padding: 10px 14px;
  font-size: 15.5px;
}}
.smallnote {{ color:{SUBTEXT}; font-size:12.5px; padding-top:4px; }}
@media (max-width: 1200px) {{
  .grid4 {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 680px) {{
  .grid4 {{ grid-template-columns: 1fr; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown(f"""
<div class="container">
  <div class="title">Needs Criteria — Data, IT, Privacy/Regulatory & Operational</div>
  <div class="subtitle">Four-column grid with measurable specs and deployability requirements</div>
</div>
""", unsafe_allow_html=True)

# -------------------- COLUMN CONTENT --------------------
data_bullets = [
    "<b>Coverage:</b> ≥ 95% of elective cases include all required signals.",
    "<b>Latency:</b> event-to-model ingest < 10 s; refresh ≤ 30 s.",
    "<b>Quality:</b> automated checks for missingness, time drift, duplicates; completeness ≥ 98%.",
    "<b>Standards:</b> HL7 v2 / FHIR for EHR; device feeds via vendor APIs or syslog."
]
it_bullets = [
    "<b>EHR interoperability:</b> Epic OpTime / Oracle Health (Cerner) SurgiNet read; write-back notes/flags without altering legal record.",
    "<b>Uptime:</b> ≥ 99.5% during block hours; graceful degradation to planned duration.",
    "<b>Access:</b> SSO (SAML/OAuth2), RBAC least privilege; read-only device interfaces.",
    "<b>Deployment:</b> On-prem or VPC; containerized (K8s/Helm); logs to hospital SIEM."
]
privacy_bullets = [
    "<b>Compliance:</b> PHIPA/PIPEDA & Québec Law 25; align with HIPAA if cross-border.",
    "<b>Security:</b> AES-256 at rest, TLS 1.2+ in transit; field-level access controls.",
    "<b>Governance:</b> Data Processing Agreement; model audit logs & change control.",
    "<b>SaMD:</b> clinical decision support; documented intended use, risk class, post-market surveillance."
]
ops_bullets = [
    "<b>Pilot KPIs:</b> overtime ↓ ≥ 10%, first-case on-time ↑ ≥ 10%, cancellations ↓ ≥ 15%, staff satisfaction +0.5/5.",
    "<b>Training:</b> < 1 h orientation; contextual tooltips; bilingual EN/FR UI.",
    "<b>Support:</b> clinical champion per service; weekly huddles first 8 weeks.",
    "<b>MLOps:</b> drift detection, dataset shift alerts, monthly recalibration."
]

# Helper to render a column card
def render_card(icon_class, title, bullets):
    st.markdown(f'<div class="card"><div class="Ribbon ribbon"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="header"><span class="icon {icon_class}"></span><h2>{title}</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="body">', unsafe_allow_html=True)
    for b in bullets:
        st.markdown(f'<div class="chip">{b}</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------- RENDER GRID --------------------
st.markdown('<div class="container"><div class="grid4">', unsafe_allow_html=True)
render_card("icon-db", "Data (Must)", data_bullets)
render_card("icon-plug", "IT / Integration (Must)", it_bullets)
render_card("icon-shield", "Privacy / Regulatory (Must)", privacy_bullets)
render_card("icon-people", "Adoption & Ops (Must)", ops_bullets)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- FOOTER STRIP: NICE-TO-HAVE --------------------
nice_to_have = (
    "<b>Nice-to-Haves:</b> Federated learning across sites; de-identification for research sandbox. "
    "Predictive staffing & PACU bed ETA; OR block optimization suggestions. "
    "Sustainability KPI (overtime energy use ↓)."
)
st.markdown(f'<div class="footer-strip">{nice_to_have}<div class="smallnote">Designed for Canadian academic centers; no new hardware required.</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # close container
