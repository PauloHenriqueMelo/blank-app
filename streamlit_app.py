# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Screening — Labeled Examples", page_icon="🧪", layout="wide")

# ----------------------- DATA (5 EXAMPLES) -----------------------
# Only title, AI justification, AI decision, original decision, and agreement
rows = [
    {
        "Title": "Clinical-grade human dental pulp stem cells improve adult hippocampal neural regeneration and cognitive deficits in Alzheimer's disease",
        "AI_Justification": "Study does not use AI and involves adult Alzheimer’s disease (non-pediatric surgical pathology).",
        "AI_Decision": 0,
        "Original_Decision": 0
    },
    {
        "Title": "Construction of a prognostic prediction model for colorectal cancer based on 5-year clinical follow-up data",
        "AI_Justification": "Adult colorectal cancer population; not pediatric surgical pathology, so excluded.",
        "AI_Decision": 0,
        "Original_Decision": 0
    },
    {
        "Title": "Pathological image analysis using the GPU: Stroma classification for neuroblastoma",
        "AI_Justification": "Develops histopathology image classification for pediatric neuroblastoma (AI + pediatric surgical pathology).",
        "AI_Decision": 1,
        "Original_Decision": 0   # from your example
    },
    {
        "Title": "Computer-assisted analysis of medulloblastoma: A cytologic study",
        "AI_Justification": "Uses clustering/discriminant analysis on pediatric medulloblastoma cytology.",
        "AI_Decision": 1,
        "Original_Decision": 0   # from your example
    },
    {
        "Title": "Deep Learning and Multidisciplinary Imaging in Pediatric Surgical Oncology: A Scoping Review",
        "AI_Justification": "Scoping review summarizes studies but does not develop/use/validate an AI model.",
        "AI_Decision": 0,
        "Original_Decision": 1   # from your example
    },
]

df = pd.DataFrame(rows)

# Derive readable labels and agreement flag
label = {1: "Include", 0: "Exclude"}
df["AI Decision"] = df["AI_Decision"].map(label)
df["Original Decision"] = df["Original_Decision"].map(label)
df["Agreement"] = df.apply(lambda r: "✅ Agree" if r["AI_Decision"] == r["Original_Decision"] else "❌ Disagree", axis=1)

# Final view dataframe with only requested columns
view = df[["Title", "AI_Justification", "AI Decision", "Original Decision", "Agreement"]].rename(
    columns={"AI_Justification": "AI Justification"}
)

# ----------------------- STYLES -----------------------
st.markdown("""
<style>
:root { --purple:#6A0DAD; --lav:#F3EAFD; --ink:#3C1361; }
.card {
  background: linear-gradient(135deg, var(--purple) 0%, #8B5CF6 100%);
  color: #fff; padding: 16px 18px; border-radius: 14px;
  box-shadow: 0 10px 24px rgba(106,13,173,0.25); margin: 8px 0 18px 0;
}
.card h1 { font-size: 1.1rem; margin: 0; font-weight: 800; letter-spacing: .2px; }
.card p { margin: 6px 0 0 0; opacity: .95; }

.tbl-wrap {
  background: #fff; border-radius: 14px; overflow: hidden;
  box-shadow: 0 10px 24px rgba(0,0,0,.06);
}
.tbl {
  width: 100%; border-collapse: separate; border-spacing: 0;
  font-family: Inter, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}
.tbl thead th {
  background: var(--lav); color: var(--ink); font-weight: 800; font-size: 14px;
  text-align: left; padding: 14px 16px; border-bottom: 1px solid #E7DDFC;
}
.tbl tbody td {
  font-size: 14px; color: #1F2937; padding: 12px 16px; border-bottom: 1px solid #F1F0F5; vertical-align: top;
}
.tbl tbody tr:nth-child(even) { background: #FAF7FF; }
.title { font-weight: 700; color: #4B0082; }
.badge {
  display: inline-block; padding: 6px 10px; border-radius: 10px; background: #F3EAFD; color:#4B0082;
  font-weight: 800; font-variant-numeric: tabular-nums;
}
.badge.red { background: #FDECEC; color: #9B1C1C; }
.badge.green { background: #E9FBEE; color: #116329; }
.small { color:#6B7280; font-size:12px; }
</style>
""", unsafe_allow_html=True)

# ----------------------- HEADER -----------------------
st.markdown(f"""
<div class="card">
  <h1>🧪 AI Screening — Labeled Examples (5)</h1>
  <p class="small">Columns: Title · AI Justification · AI Decision · Original Decision · Agreement</p>
</div>
""", unsafe_allow_html=True)

# ----------------------- HTML TABLE RENDER -----------------------
def render_table(df_view: pd.DataFrame) -> str:
    # Build table head
    html = """
<div class="tbl-wrap">
<table class="tbl">
  <thead>
    <tr>
      <th style="width:28%;">Title</th>
      <th style="width:42%;">AI Justification</th>
      <th style="width:10%;">AI Decision</th>
      <th style="width:12%;">Original Decision</th>
      <th style="width:8%;">Agreement</th>
    </tr>
  </thead>
  <tbody>
"""
    # Rows
    for _, r in df_view.iterrows():
        agree = r["Agreement"].startswith("✅")
        agree_badge = f"<span class='badge {'green' if agree else 'red'}'>{r['Agreement']}</span>"
        html += f"""
    <tr>
      <td class="title">{r['Title']}</td>
      <td>{r['AI Justification']}</td>
      <td><span class="badge">{r['AI Decision']}</span></td>
      <td><span class="badge">{r['Original Decision']}</span></td>
      <td>{agree_badge}</td>
    </tr>
"""
    html += """
  </tbody>
</table>
</div>
"""
    return html

# Render as real HTML so styling is preserved
st.components.v1.html(render_table(view), height=520, scrolling=True)

# Optional: raw data download
with st.expander("Download data (CSV)"):
    st.dataframe(view, use_container_width=True, hide_index=True)
    st.download_button(
        "Download CSV",
        data=view.to_csv(index=False).encode("utf-8"),
        file_name="ai_screening_labeled_examples.csv",
        mime="text/csv"
    )
