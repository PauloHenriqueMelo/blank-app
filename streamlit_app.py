# app.py
import streamlit as st
import pandas as pd

# -------------- PAGE SETUP --------------
st.set_page_config(page_title="AI Screening Metrics", page_icon="📊", layout="centered")

# ---- Minimal CSS (purple theme + table polish) ----
st.markdown("""
<style>
:root { --purple:#6A0DAD; --lav:#F3EAFD; --ink:#3C1361; }
.main > div { padding-top: 1rem; }
.header-card {
  background: linear-gradient(135deg, var(--purple) 0%, #8B5CF6 100%);
  color: #fff; padding: 18px 20px; border-radius: 14px;
  box-shadow: 0 10px 24px rgba(106,13,173,0.25); margin-bottom: 16px;
}
.header-title { font-size: 1.15rem; font-weight: 800; letter-spacing: .2px; }
.header-sub { opacity:.95; font-size:.85rem; margin-top:6px; }

.pretty-table { width:100%; border-collapse:separate; border-spacing:0; }
.pretty-table thead th {
  background: var(--lav); color: var(--ink); font-weight:800; font-size:14px;
  text-align:left; padding:14px 16px; border-bottom:1px solid #E7DDFC;
}
.pretty-table tbody td {
  font-size:14px; color:#1F2937; padding:12px 16px; border-bottom:1px solid #F1F0F5;
  vertical-align:middle;
}
.pretty-table tbody tr:nth-child(even) { background: #FAF7FF; }
.metric-name { font-weight:800; color:#4B0082; }
.badge {
  display:inline-block; padding:6px 10px; border-radius:10px;
  background: var(--lav); color:#4B0082; font-weight:800; font-variant-numeric:tabular-nums;
}
.progress-cell { width: 260px; }
.progress-wrap {
  width:100%; height:14px; background:#EEE8F7; border-radius:999px; overflow:hidden;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
}
.progress-bar { height:100%; background: linear-gradient(90deg, var(--purple), #8B5CF6); width:0%; }
.pct-text { min-width:64px; text-align:right; font-weight:800; color:var(--ink); font-variant-numeric:tabular-nums; }
.note { margin-top:10px; font-size:12px; color:#6B7280; }
.small { color:#6B7280; font-size:12px; }
</style>
""", unsafe_allow_html=True)

# -------------- SIDEBAR INPUTS --------------
st.sidebar.header("Inputs")
TP = st.sidebar.number_input("True Positive (TP)", min_value=0, value=30, step=1)
TN = st.sidebar.number_input("True Negative (TN)", min_value=0, value=3234, step=1)
FP = st.sidebar.number_input("False Positive (FP)", min_value=0, value=86, step=1)
FN = st.sidebar.number_input("False Negative (FN)", min_value=0, value=2, step=1)
decimals = st.sidebar.slider("Percentage decimals", 0, 4, 2, 1)

# -------------- METRIC CALCS --------------
total = TP + TN + FP + FN
def safe_div(n, d): return n / d if d else 0.0
sensitivity = safe_div(TP, TP + FN)         # recall
specificity = safe_div(TN, TN + FP)
accuracy    = safe_div(TP + TN, total)
precision   = safe_div(TP, TP + FP)

pct = lambda x: f"{x*100:.{decimals}f}%"

# -------------- HEADER --------------
st.markdown(f"""
<div class="header-card">
  <div class="header-title">📊 AI Screening Confusion Matrix & Performance Metrics</div>
  <div class="header-sub">N = {total:,} (TP={TP:,}, TN={TN:,}, FP={FP:,}, FN={FN:,})</div>
</div>
""", unsafe_allow_html=True)

# -------------- DATA (for download/export) --------------
rows = [
    ("True Positive (TP)",  "AI = 1 and Human = 1", f"{TP:,}", None, None),
    ("True Negative (TN)",  "AI = 0 and Human = 0", f"{TN:,}", None, None),
    ("False Positive (FP)", "AI = 1 but Human = 0", f"{FP:,}", None, None),
    ("False Negative (FN)", "AI = 0 but Human = 1", f"{FN:,}", None, None),
    ("Sensitivity (Recall)", "TP / (TP + FN)", None, sensitivity, pct(sensitivity)),
    ("Specificity",          "TN / (TN + FP)", None, specificity, pct(specificity)),
    ("Accuracy",             "(TP + TN) / (TP + TN + FP + FN)", None, accuracy, pct(accuracy)),
    ("Precision (PPV)",      "TP / (TP + FP)", None, precision, pct(precision)),
]
df = pd.DataFrame(rows, columns=["Metric", "Meaning", "Count", "Percent_Value", "Percent_Label"])

# -------------- PRETTY TABLE (HTML) --------------
def render_table(df: pd.DataFrame) -> str:
    html = """
<table class="pretty-table">
  <thead>
    <tr>
      <th style="width: 26%;">Metric</th>
      <th style="width: 36%;">Meaning</th>
      <th style="width: 18%;">Value</th>
      <th style="width: 20%;">% (formatted)</th>
    </tr>
  </thead>
  <tbody>
"""
    for _, r in df.iterrows():
        name = r["Metric"]
        meaning = r["Meaning"]
        count = r["Count"]
        pval = r["Percent_Value"]
        plabel = r["Percent_Label"]

        if pd.isna(pval):  # count rows
            html += f"""
    <tr>
      <td class="metric-name">{name}</td>
      <td>{meaning}</td>
      <td><span class="badge">{count}</span></td>
      <td class="small">—</td>
    </tr>
"""
        else:  # percentage rows
            width = max(0, min(100, round(pval * 100, 2)))
            html += f"""
    <tr>
      <td class="metric-name">{name}</td>
      <td>{meaning}</td>
      <td><span class="badge">{plabel}</span></td>
      <td class="progress-cell">
        <div style="display:flex; align-items:center; gap:10px;">
          <div class="progress-wrap">
            <div class="progress-bar" style="width:{width}%"></div>
          </div>
          <div class="pct-text">{plabel}</div>
        </div>
      </td>
    </tr>
"""
    html += """
  </tbody>
</table>
<div class="note">Higher is better for Sensitivity, Specificity, Accuracy, and Precision. Bars capped at 100%.</div>
"""
    return html

st.markdown(render_table(df), unsafe_allow_html=True)

# -------------- OPTIONAL: raw dataframe + download --------------
with st.expander("Show raw data / download"):
    st.dataframe(
        df.assign(
            Count=df["Count"].fillna("—"),
            Percent_Value=df["Percent_Value"].map(lambda x: round(x, decimals) if pd.notna(x) else "—"),
        ),
        hide_index=True,
        use_container_width=True
    )
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", data=csv, file_name="ai_screening_metrics.csv", mime="text/csv")

# -------------- FOOTER NOTE --------------
st.caption("Tip: adjust TP/TN/FP/FN in the sidebar to recompute all metrics instantly.")
