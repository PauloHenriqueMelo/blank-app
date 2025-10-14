# app.py
import streamlit as st

st.set_page_config(page_title="AI Screening — Cards", layout="wide")

# ---- Your 5 items ----
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

def lab(v): return "Include" if v == 1 else "Exclude"
def agree(a, b): return a == b

# ---- Render as HTML component (forced readable colors) ----
html_head = """
<div style="all: initial;">
  <style>
    /* App-embedded design system (forced readable colors) */
    .wrap {
      font-family: Inter, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      background: transparent;
    }
    .grid {
      display: grid; gap: 16px;
      grid-template-columns: repeat(12, minmax(0,1fr));
    }
    .card {
      grid-column: span 12;
      background: #ffffff;                /* forced white for readability */
      color: #111827;                     /* dark ink */
      border: 1px solid #E7DDFC;          /* soft lilac line */
      border-radius: 18px;
      box-shadow: 0 10px 28px rgba(106,13,173,0.12);
      padding: 16px 16px 14px;
      position: relative;
    }
    @media (min-width: 1000px){ .card{ grid-column: span 6; } }
    @media (min-width: 1400px){ .card{ grid-column: span 4; } }

    .accent {
      position:absolute; left:0; top:0; bottom:0; width:6px;
      background: linear-gradient(180deg,#6A0DAD,#8B5CF6);
      border-top-left-radius:18px; border-bottom-left-radius:18px;
    }

    .title {
      font-weight: 800; font-size: 16px; line-height: 1.35;
      margin: 0 0 10px 10px; color: #2d1b69;
    }

    /* Dialog bubble for justification */
    .bubble {
      background: #F8F5FF;                /* very light purple */
      border: 1px dashed #D8C9FB;
      color: #2f2f33;
      padding: 12px 14px;
      border-radius: 14px;
      margin: 2px 0 10px 10px;
      position: relative;
    }
    .bubble:before {
      content: ""; position: absolute; left: 20px; top: -8px;
      width: 16px; height: 16px; transform: rotate(45deg);
      background: #F8F5FF; border-left: 1px dashed #D8C9FB; border-top: 1px dashed #D8C9FB;
    }

    /* Chips */
    .row { display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-left:10px; }
    .chip {
      background: #F3EAFD; color: #4B0082; font-weight: 800;
      padding: 6px 10px; border-radius: 999px; font-size: 13px;
      border: 1px solid #E1D6FB;
    }

    /* Agreement badge */
    .agree {
      margin-left: auto; display:flex; align-items:center; gap:8px;
      padding: 6px 10px; border-radius: 12px; font-weight: 900; font-size: 13px;
      border: 1px solid;
    }
    .ok  { color:#166534; background:#E9FBEE; border-color: #A7F3D0; }
    .bad { color:#991B1B; background:#FDECEC; border-color: #FCA5A5; }

    /* Small gray label */
    .k { color:#6B7280; font-size:12px; font-weight:600; }
  </style>
  <div class="wrap">
    <div class="grid">
"""

cards = []
for it in items:
    is_agree = agree(it["ai"], it["orig"])
    cards.append(f"""
      <div class="card">
        <div class="accent"></div>
        <div class="title">🧾 {it['title']}</div>
        <div class="bubble">💬 {it['just']}</div>
        <div class="row">
          <div class="k">AI decision</div>
          <div class="chip">{lab(it['ai'])}</div>
          <div class="k" style="margin-left:12px;">Original</div>
          <div class="chip">{lab(it['orig'])}</div>
          <div class="agree {'ok' if is_agree else 'bad'}">{'✅ Agree' if is_agree else '❌ Disagree'}</div>
        </div>
      </div>
    """)

html_tail = """
    </div>
  </div>
</div>
"""

st.components.v1.html(html_head + "".join(cards) + html_tail, height=860, scrolling=True)
