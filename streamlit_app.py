import streamlit as st

# -------------------------------------------------------------------
# PAGE SETUP
# -------------------------------------------------------------------
st.set_page_config(page_title="Definition of Outcome — Surgical Innovation", layout="wide")

# -------------------- PURPLE THEME --------------------
PURPLE_DARK = "#4C1D95"
PURPLE = "#6D28D9"
PURPLE_MID = "#7C3AED"
INDIGO = "#1E1B4B"
LAVENDER = "#F8F5FF"
CARD = "#FFFFFF"
BORDER = "#DDD6FE"
SUBTEXT = "#475569"

# -------------------- GLOBAL CSS --------------------
CSS = f"""
<style>
body {{
  background: radial-gradient(1200px 600px at 10% -10%, #FBFAFF 0%, {LAVENDER} 65%, #FFFFFF 100%);
  color: {INDIGO};
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
}}

.wrap {{
  max-width: 1280px;
  margin: 0 auto;
  padding: 10px 14px 0 14px;
}}

.title {{
  font-weight: 850;
  font-size: 34px;
  letter-spacing: -0.2px;
  background: linear-gradient(90deg, {PURPLE_DARK}, {PURPLE_MID});
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 4px;
}}
.subtitle {{
  color: {SUBTEXT};
  font-size: 15px;
  margin-bottom: 12px;
}}

.kpi-grid {{
  display:grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}}

.kpi {{
  background:{CARD};
  border: 1px solid {BORDER};
  border-radius: 16px;
  overflow:hidden;
  box-shadow: 0 10px 22px rgba(76,29,149,0.07);
}}
.kpi .ribbon {{
  height: 6px;
  background: linear-gradient(90deg, {PURPLE_DARK}, {PURPLE});
}}
.kpi .body {{
  padding: 12px 14px 14px 14px;
}}

.kpi .label {{
  display:flex; align-items:center; gap:10px;
  color:{PURPLE_DARK};
  font-weight: 760; font-size: 18px;
  margin-bottom: 8px;
}}
/* monochrome metric icon */
.icon-metric {{
  width:18px; height:18px; background:{PURPLE};
  -webkit-mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M3 3h4v18H3V3Zm7 8h4v10h-4V11Zm7-6h4v16h-4V5Z"/></svg>') no-repeat center/contain;
          mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M3 3h4v18H3V3Zm7 8h4v10h-4V11Zm7-6h4v16h-4V5Z"/></svg>') no-repeat center/contain;
}}

.kpi .numbers {{
  display:grid;
  grid-template-columns: 1fr 36px 1fr;
  align-items:center;
  gap: 8px;
}}
.kpi .val {{
  background:#F3E8FF;
  border:1px solid {BORDER};
  border-radius: 12px;
  padding: 10px;
  text-align:center;
}}
.kpi .val .top {{ font-size:24px; font-weight:820; color:{PURPLE_DARK}; }}
.kpi .val .sub {{ font-size:12.5px; color:{SUBTEXT}; margin-top:2px; }}

.kpi .arrow {{
  height: 46px;
  display:flex; align-items:center; justify-content:center;
}}
/* rightward arrow */
.kpi .arrow::before {{
  content:"";
  width:24px; height:24px; background:{PURPLE};
  -webkit-mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M13 5l7 7-7 7v-4H4v-6h9V5z"/></svg>') no-repeat center/contain;
          mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M13 5l7 7-7 7v-4H4v-6h9V5z"/></svg>') no-repeat center/contain;
}}

.kpi .delta {{
  margin-top: 10px;
  display:flex; align-items:center; justify-content:space-between;
  font-size: 13px; color:{SUBTEXT};
}}
.kpi .delta .gain {{
  font-weight: 760; color:{PURPLE_DARK}; background:#EDE9FE; border:1px solid {BORDER}; border-radius:8px; padding:4px 8px;
}}

.panel-grid {{
  display:grid;
  grid-template-columns: 2fr 1fr;
  gap: 14px;
  margin-top: 14px;
}}

.panel {{
  background:{CARD};
  border:1px solid {BORDER};
  border-radius: 14px;
  box-shadow: 0 8px 18px rgba(76,29,149,0.06);
  padding: 12px 14px;
}}

.panel h3 {{
  margin: 2px 0 8px 0;
  font-size: 20px;
  color:{PURPLE_DARK};
  font-weight: 760;
}}
.table {{
  width:100%;
  border-collapse: separate;
  border-spacing: 0 8px;
  font-size: 15px;
}}
.tr {{
  display:grid;
  grid-template-columns: 180px 1fr 130px 150px 130px;
  gap: 10px;
  background:#F8F6FF;
  border:1px solid {BORDER};
  padding: 8px 10px;
  border-radius: 10px;
}
.th {{ font-weight:760; color:{INDIGO}; background:transparent; }}
.small {{ color:{SUBTEXT}; font-size:12.5px; }}

.meaning {{
  display:grid; grid-template-columns: repeat(3, 1fr); gap: 12px;
}}
.tile {{
  background:{CARD}; border:1px solid {BORDER}; border-radius: 12px; padding: 12px;
}}
.tile h4 {{ margin:0 0 6px 0; font-size: 17px; color:{PURPLE_DARK}; font-weight:760; }}
.tile p {{ margin:0; font-size: 15px; line-height:1.35; color:{INDIGO}; }}

.icon-clin, .icon-pat, .icon-eco {{
  width:18px; height:18px; background:{PURPLE};
  display:inline-block; vertical-align:-3px; margin-right:6px;
}}
.icon-clin {{
  -webkit-mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 2l4 4-4 4-4-4 4-4Zm-8 18v-6h4v6H4Zm6 0v-8h4v8h-4Zm6 0v-4h4v4h-4Z"/></svg>') no-repeat center/contain;
          mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 2l4 4-4 4-4-4 4-4Zm-8 18v-6h4v6H4Zm6 0v-8h4v8h-4Zm6 0v-4h4v4h-4Z"/></svg>') no-repeat center/contain;
}}
.icon-pat {{
  -webkit-mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 12a4 4 0 1 0-4-4 4 4 0 0 0 4 4Zm-6 7a6 6 0 0 1 12 0v1H6Z"/></svg>') no-repeat center/contain;
          mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M12 12a4 4 0 1 0-4-4 4 4 0 0 0 4 4Zm-6 7a6 6 0 0 1 12 0v1H6Z"/></svg>') no-repeat center/contain;
}}
.icon-eco {{
  -webkit-mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M3 12c4-6 14-6 18 0-4 6-14 6-18 0Zm8 8h2v-4h-2v4Zm-6-2h2v-2H5v2Zm12 0h2v-2h-2v2Z"/></svg>') no-repeat center/contain;
          mask:url('data:image/svg+xml;utf8,\
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">\
  <path d="M3 12c4-6 14-6 18 0-4 6-14 6-18 0Zm8 8h2v-4h-2v4Zm-6-2h2v-2H5v2Zm12 0h2v-2h-2v2Z"/></svg>') no-repeat center/contain;
}}

.footer-note {{
  margin-top: 10px;
  font-size: 12.5px;
  color:{SUBTEXT};
}}
@media (max-width: 1100px) {{
  .kpi-grid {{ grid-template-columns: 1fr; }}
  .panel-grid {{ grid-template-columns: 1fr; }}
  .meaning {{ grid-template-columns: 1fr; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -------------------------------------------------------------------
# HEADER
# -------------------------------------------------------------------
st.markdown(f"""
<div class="wrap">
  <div class="title">Definition of Outcome</div>
  <div class="subtitle">Quantifiable targets, verification, and why it matters</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# KPI CARDS — BASELINE → TARGET with delta
# -------------------------------------------------------------------
st.markdown('<div class="wrap"><div class="kpi-grid">', unsafe_allow_html=True)

# KPI 1
st.markdown(f"""
<div class="kpi">
  <div class="ribbon"></div>
  <div class="body">
    <div class="label"><span class="icon-metric"></span>Forecast Error (Primary)</div>
    <div class="numbers">
      <div class="val"><div class="top">±25 min</div><div class="sub">Baseline MAE</div></div>
      <div class="arrow"></div>
      <div class="val"><div class="top">±5 min</div><div class="sub">Target (mid-case)</div></div>
    </div>
    <div class="delta">
      <div class="small">Measured at 50% elapsed time; calibrated slope 0.9–1.1</div>
      <div class="gain">−80% error</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# KPI 2
st.markdown(f"""
<div class="kpi">
  <div class="ribbon"></div>
  <div class="body">
    <div class="label"><span class="icon-metric"></span>OR Overtime</div>
    <div class="numbers">
      <div class="val"><div class="top">Baseline</div><div class="sub">Avg monthly hours</div></div>
      <div class="arrow"></div>
      <div class="val"><div class="top">↓ ≥10%</div><div class="sub">Within 6 months</div></div>
    </div>
    <div class="delta">
      <div class="small">Unit: total overtime hours across elective rooms</div>
      <div class="gain">Operational gain</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# KPI 3
st.markdown(f"""
<div class="kpi">
  <div class="ribbon"></div>
  <div class="body">
    <div class="label"><span class="icon-metric"></span>Patient Cancellations</div>
    <div class="numbers">
      <div class="val"><div class="top">Baseline</div><div class="sub">% of elective cases</div></div>
      <div class="arrow"></div>
      <div class="val"><div class="top">↓ ≥15%</div><div class="sub">After deployment</div></div>
    </div>
    <div class="delta">
      <div class="small">Denominator: scheduled elective cases per month</div>
      <div class="gain">Access improvement</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# VERIFICATION PANEL (how we’ll measure / prove it)
# -------------------------------------------------------------------
st.markdown('<div class="wrap"><div class="panel-grid">', unsafe_allow_html=True)

# Left: verification table
st.markdown(f"""
<div class="panel">
  <h3>Verification & Acceptance Tests</h3>
  <div class="tr th">
    <div>Metric</div><div>Definition</div><div>Target</div><div>Data Source</div><div>Window</div>
  </div>
  <div class="tr">
    <div>Forecast Error</div>
    <div>MAE between forecasted remaining time at 50% elapsed and actual remaining time; assess calibration slope/intercept.</div>
    <div><b>≤ 5–7 min</b>; slope 0.9–1.1</div>
    <div>Model logs + OR timeline (EHR OpTime/SurgiNet)</div>
    <div>First <b>200 cases</b> per service</div>
  </div>
  <div class="tr">
    <div>OR Overtime</div>
    <div>Total hours finishing after scheduled end across elective rooms.</div>
    <div><b>≥ 10% reduction</b></div>
    <div>Payroll/OR admin reports</div>
    <div>Baseline 6 weeks → Follow-up 6 months</div>
  </div>
  <div class="tr">
    <div>Cancellations</div>
    <div>Cancelled elective cases / scheduled elective cases.</div>
    <div><b>≥ 15% reduction</b></div>
    <div>EHR scheduling + daily OR list</div>
    <div>Monthly, rolling 3-month average</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Right: meaning tiles
st.markdown(f"""
<div class="panel">
  <h3>Meaningfulness</h3>
  <div class="meaning">
    <div class="tile">
      <h4><span class="icon-clin"></span>Clinical</h4>
      <p>Fewer late finishes and recovery crunches ⇒ lower staff fatigue and more predictable turnover.</p>
    </div>
    <div class="tile">
      <h4><span class="icon-pat"></span>Patient</h4>
      <p>Reduced delays and cancellations ⇒ shorter waits and improved experience on day of surgery.</p>
    </div>
    <div class="tile">
      <h4><span class="icon-eco"></span>Economic</h4>
      <p>Overtime hours reduced and throughput stabilized ⇒ annual savings that scale to millions in tertiary centers.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# FOOTER
# -------------------------------------------------------------------
