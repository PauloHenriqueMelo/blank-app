# app.py
import streamlit as st

st.set_page_config(page_title="AI Screening — Examples", layout="wide")

# ---------- DATA (5 items) ----------
items = [
    {
        "title": "Clinical-grade human dental pulp stem cells improve adult hippocampal neural regeneration and cognitive deficits in Alzheimer's disease",
        "just":  "Study does not use AI and involves adult Alzheimer’s disease (non-pediatric surgical pathology).",
        "ai": 0, "orig": 0
    },
    {
        "title": "Construction of a prognostic prediction model for colorectal cancer based on 5-year clinical follow-up data",
        "just":  "Adult colorectal cancer population; not pediatric surgical pathology, so excluded.",
        "ai": 0, "orig": 0
    },
    {
        "title": "Pathological image analysis using the GPU: Stroma classification for neuroblastoma",
        "just":  "Develops histopathology image classification for pediatric neuroblastoma (AI + pediatric surgical pathology).",
        "ai": 1, "orig": 0
    },
    {
        "title": "Computer-assisted analysis of medulloblastoma: A cytologic study",
        "just":  "Uses clustering/discriminant analysis on pediatric medulloblastoma cytology.",
        "ai": 1, "orig": 0
    },
    {
        "title": "Deep Learning and Multidisciplinary Imaging in Pediatric Surgical Oncology: A Scoping Review",
        "just":  "Scoping review summarizes studies but does not develop/use/validate an AI model.",
        "ai": 0, "orig": 1
    },
]

def label(x): return "Include" if x == 1 else "Exclude"
def agree(a, b): return a == b

# ---------- STYLE ----------
st.markdown("""
<style>
:root{
  --bg: #ffffff; --ink:#1f2937; --muted:#6b7280; --card:#ffffff;
  --ac1:#6A0DAD; --ac2:#8B5CF6; --ok:#16a34a; --bad:#dc2626;
  --chip:#f3eafd; --bubble:#f9f7ff; --line:#efe7fb;
  --shadow: 0 8px 24px rgba(0,0,0,0.08);
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#0e1117; --ink:#e5e7eb; --muted:#9ca3af; --card:#111418;
    --chip:#2a2140; --bubble:#1a1530; --line:#2a2140; --shadow: 0 8px 24px rgba(0,0,0,0.55);
  }
}
.block-container{padding-top:1rem; padding-bottom:2rem;}
.grid{
  display:grid; gap:16px;
  grid-template-columns: repeat(12, minmax(0,1fr));
}
.card{
  grid-column: span 12;
  background: var(--card); border-radius:18px; box-shadow: var(--shadow);
  border:1px solid var(--line); padding:16px 16px 14px; position:relative;
}
@media (min-width: 900px){
  .card{ grid-column: span 6; }
}
@media (min-width: 1400px){
  .card{ grid-column: span 4; }
}
.leftbar{
  position:absolute; left:0; top:0; bottom:0; width:6px;
  background: linear-gradient(180deg, var(--ac1), var(--ac2));
  border-top-left-radius:18px; border-bottom-left-radius:18px;
}
.title{ font-weight:800; color:var(--ink); font-size:16px; margin-left:10px; }
.row{ display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-top:8px; }
.chip{
  background: var(--chip); color:#4b0082; font-weight:800;
  padding:6px 10px; border-radius:999px; font-size:13px;
}
.bubble{
  background: var(--bubble); border:1px dashed var(--line);
  padding:10px 12px; border-radius:12px; color:var(--ink); font-size:14px;
}
.kv{ display:flex; align-items:center; gap:6px; }
.k{ color:var(--muted); font-weight:600; font-size:12px; }
.v{ font-weight:700; color:var(--ink); }
.agree{
  margin-left:auto; font-weight:900; display:flex; align-items:center; gap:6px;
  padding:6px 10px; border-radius:10px; font-size:13px;
}
.agree.ok{ background:rgba(22,163,74,.12); color:var(--ok); border:1px solid rgba(22,163,74,.35); }
.agree.bad{ background:rgba(220,38,38,.10); color:var(--bad); border:1px solid rgba(220,38,38,.35); }

.sep{ height:10px; }
</style>
""", unsafe_allow_html=True)

# ---------- RENDER ----------
cards = ['<div class="grid">']
for it in items:
    is_agree = agree(it["ai"], it["orig"])
    cards.append(f"""
    <div class="card">
      <div class="leftbar"></div>
      <div class="title">🧾 {it['title']}</div>

      <div class="sep"></div>

      <div class="bubble">💬 {it['just']}</div>

      <div class="row" style="margin-top:10px;">
        <div class="kv">
          <div class="k">AI decision</div>
          <div class="chip">{label(it['ai'])}</div>
        </div>
        <div class="kv">
          <div class="k">Original</div>
          <div class="chip">{label(it['orig'])}</div>
        </div>

        <div class="agree {'ok' if is_agree else 'bad'}">
          {'✅ Agree' if is_agree else '❌ Disagree'}
        </div>
      </div>
    </div>
    """)
cards.append("</div>")

st.components.v1.html("".join(cards), height=800, scrolling=True)
