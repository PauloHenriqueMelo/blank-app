# app.py
import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="AI Screening Metrics", page_icon="📊", layout="centered")

# --- Sidebar inputs ---
st.sidebar.header("Inputs")
TP = st.sidebar.number_input("True Positive (TP)", min_value=0, value=30, step=1)
TN = st.sidebar.number_input("True Negative (TN)", min_value=0, value=3234, step=1)
FP = st.sidebar.number_input("False Positive (FP)", min_value=0, value=86, step=1)
FN = st.sidebar.number_input("False Negative (FN)", min_value=0, value=2, step=1)
decimals = st.sidebar.slider("Percentage decimals", 0, 4, 2, 1)

# --- Metrics ---
total = TP + TN + FP + FN
def safe_div(n, d): return n / d if d else 0.0
sensitivity = safe_div(TP, TP + FN)          # 0.9375
specificity = safe_div(TN, TN + FP)          # 0.974096...
accuracy    = safe_div(TP + TN, total)       # 0.973747...
precision   = safe_div(TP, TP + FP)          # 0.258620...

fmt_pct = lambda x: f"{x*100:.{decimals}f}%"

rows = [
    ("True Positive (TP)",  "AI = 1 and Human = 1", f"{TP:,}", None, None),
    ("True Negative (TN)",  "AI = 0 and Human = 0", f"{TN:,}", None, None),
    ("False Positive (FP)", "AI = 1 but Human = 0", f"{FP:,}", None, None),
    ("False Negative (FN)", "AI = 0 but Human = 1", f"{FN:,}", None, None),
    ("Sensitivity (Recall)", "TP / (TP + FN)", None, sensitivity, fmt_pct(sensitivity)),
    ("Specificity",          "TN / (TN + FP)", None, specificity, fmt_pct(specificity)),
    ("Accuracy",             "(TP + TN) / (TP + TN + FP + FN)", None, accuracy, fmt_pct(accuracy)),
    ("Precision (PPV)",      "TP / (TP + FP)", None, precision, fmt_pct(precision)),
]
df = pd.DataFrame(rows, columns=["Metric","Meaning","Count","Percent_Value","Percent_Label"])

# --- Build HTML ---
def render_html(df: pd.DataFrame) -> str:
    header = f"""
<div style="font-family: Inter, -apple-system, Segoe UI, Roboto, Arial, sans-serif;">
  <div style="background: linear-gradient(135deg,#6A0DAD 0%,#8B5CF6 100%);
              color:#fff;padding:18px 20px;border-radius:14px;
              box-shadow:0 10px 24px rgba(106,13,173,.25);margin-bottom:14px;">
    <div style="font-size:18px;font-weight:800;letter-spacing:.2px;">
      📊 AI Screening Confusion Matrix & Performance Metrics
    </div>
    <div style="opacity:.95;font-size:13px;margin-top:6px;">
      N = {total:,} (TP={TP:,}, TN={TN:,}, FP={FP:,}, FN={FN:,})
    </div>
  </div>
  <style>
    .tbl {{ width:100%; border-collapse:separate; border-spacing:0; border-radius:14px; overflow:hidden;
           box-shadow:0 10px 24px rgba(0,0,0,.06); background:#fff; }}
    thead th {{ background:#F3EAFD; color:#3C1361; font-weight:800; font-size:14px; text-align:left;
               padding:14px 16px; border-bottom:1px solid #E7DDFC; }}
    tbody td {{ font-size:14px; color:#1F2937; padding:12px 16px; border-bottom:1px solid #F1F0F5; }}
    tbody tr:nth-child(even) {{ background:#FAF7FF; }}
    .name {{ font-weight:800; color:#4B0082; }}
    .badge {{ display:inline-block; padding:6px 10px; border-radius:10px; background:#F3EAFD; color:#4B0082;
              font-weight:800; font-variant-numeric:tabular-nums; }}
    .pwrap {{ width:100%; height:14px; background:#EEE8F7; border-radius:999px; overflow:hidden;
              box-shadow:inset 0 1px 2px rgba(0,0,0,.05); }}
    .pbar {{ height:100%; background:linear-gradient(90deg,#6A0DAD,#8B5CF6); width:0%; }}
    .pct {{ min-width:64px; text-align:right; font-weight:800; color:#3C1361; font-variant-numeric:tabular-nums; }}
    .muted {{ color:#6B7280; font-size:12px; }}
  </style>
  <table class="tbl">
    <thead>
      <tr>
        <th style="width:26%;">Metric</th>
        <th style="width:36%;">Meaning</th>
        <th style="width:18%;">Value</th>
        <th style="width:20%;">% (2 decimals)</th>
      </tr>
    </thead>
    <tbody>
"""
    body = []
    for _, r in df.iterrows():
        if pd.isna(r["Percent_Value"]):
            body.append(f"""
      <tr>
        <td class="name">{r['Metric']}</td>
        <td>{r['Meaning']}</td>
        <td><span class="badge">{r['Count']}</span></td>
        <td class="muted">—</td>
      </tr>""")
        else:
            width = max(0, min(100, round(float(r["Percent_Value"])*100, 2)))
            body.append(f"""
      <tr>
        <td class="name">{r['Metric']}</td>
        <td>{r['Meaning']}</td>
        <td><span class="badge">{r['Percent_Label']}</span></td>
        <td>
          <div style="display:flex; align-items:center; gap:10px;">
            <div class="pwrap"><div class="pbar" style="width:{width}%"></div></div>
            <div class="pct">{r['Percent_Label']}</div>
          </div>
        </td>
      </tr>""")
    footer = """
    </tbody>
  </table>
  <div class="muted" style="margin-top:10px;">
    Higher is better for Sensitivity, Specificity, Accuracy, and Precision. Bars capped at 100%.
  </div>
</div>
"""
    return header + "\n".join(body) + footer

html = render_html(df)

# --- Render as real HTML (NOT markdown) ---
st.components.v1.html(html, height=560, scrolling=True)

# Optional: raw data + download
with st.expander("Show raw data / download"):
    st.dataframe(
        df.assign(Count=df["Count"].fillna("—"),
                  Percent_Value=df["Percent_Value"].map(lambda x: round(x, decimals) if pd.notna(x) else "—")),
        use_container_width=True, hide_index=True
    )
    st.download_button("Download CSV",
                       data=df.to_csv(index=False).encode("utf-8"),
                       file_name="ai_screening_metrics.csv",
                       mime="text/csv")
