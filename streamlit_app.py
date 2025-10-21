# app.py
import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title='Addressing "Killer Risks"',
    page_icon="🛡️",
    layout="wide",
)

# ---------- THEME & CSS ----------
CSS = """
<style>
/* Page background */
.stApp {
  background: radial-gradient(1200px 800px at 50% -10%, #1e1b4b 0%, #0b1220 35%, #0b1220 100%);
  color: #e5e7eb;
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial, "Apple Color Emoji","Segoe UI Emoji";
}

/* Section title */
.h1-title {
  text-align:center; 
  font-size: 2.0rem; 
  font-weight: 800; 
  color: #ffffff;
  margin: 0 0 1rem 0;
  text-shadow: 0 6px 24px rgba(88,101,242,0.25);
}

/* Card grid */
.grid { display:grid; gap: 24px; }
@media (min-width: 992px) {
  .grid { grid-template-columns: 1fr 1fr; }
}

/* Risk card */
.card {
  position: relative;
  border-radius: 18px;
  border: 1.5px solid #2b3344;
  background: linear-gradient(180deg, rgba(20,26,41,.7), rgba(14,20,32,.55));
  box-shadow: 0 20px 40px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.03);
  padding: 24px;
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}
.card:hover {
  transform: scale(1.02);
  box-shadow: 0 30px 60px rgba(0,0,0,0.45);
  border-color: #3b3f55;
}

/* Icon badge */
.badge {
  position: absolute;
  top: -12px; left: 18px;
  width: 42px; height: 42px;
  border-radius: 12px;
  display:flex; align-items:center; justify-content:center;
  color:#fff; font-weight:700; font-size: 18px;
  box-shadow: 0 10px 20px rgba(0,0,0,.35);
}

/* Labels */
.label-sm {
  letter-spacing: .12em; 
  font-size: .72rem; 
  font-weight: 700; 
  opacity:.8; 
  margin-bottom: .25rem;
}

/* Risk title */
.risk-title {
  font-size: 1.25rem;
  font-weight: 800;
  margin: .25rem 0 1.25rem 0;
  color: #fff;
}

/* Mitigation box */
.mitig {
  border-radius: 14px;
  padding: 14px 16px;
  background: rgba(38,49,69,.6);
  border: 1px solid rgba(103,232,249,.18);
}
.mitig .label-sm { color: #34d399; }
.mitig p { margin:0; color:#cfd8e3; }

/* Status row */
.status { display:flex; align-items:center; gap:8px; margin-top: 12px; color:#93a3b8; font-size:.78rem; }
.dot { width:8px; height:8px; border-radius:999px; }

/* Animated arrow */
.arrow {
  width: 40px; height: 40px; margin: 14px auto;
  opacity:.9;
}
@keyframes drop {
  0% { transform: translateY(-4px); opacity:.8; }
  50% { transform: translateY(2px); opacity:1; }
  100% { transform: translateY(-4px); opacity:.8; }
}
.arrow path { animation: drop 1.2s infinite ease-in-out; }

/* Footer stat tiles */
.tiles { display:grid; gap: 16px; grid-template-columns: repeat(2, 1fr); }
@media (min-width: 992px) { .tiles { grid-template-columns: repeat(4, 1fr); } }
.tile {
  border-radius: 16px; text-align:center; padding: 16px 10px;
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
}
.tile .big { font-size: 1.6rem; font-weight: 900; margin-bottom: 4px; }
.tile .sub { font-size: .85rem; opacity:.9; }

/* Subtle divider spacing */
.section { margin: 10px 0 26px 0; }

/* Small helper to clamp width of central container */
.maxw { max-width: 1200px; margin: 0 auto; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="h1-title">Addressing "Killer Risks"</div>', unsafe_allow_html=True)

# ---------- DATA ----------
risks = [
    {
        "id": "heterogeneity",
        "title": "Data Heterogeneity",
        "mitigation": "Standardized HL7/FHIR streams",
        "badge": "🧩",
        "badge_color": "#60a5fa",  # blue
        "arrow_color": "#60a5fa",
        "status_color": "#60a5fa",
    },
    {
        "id": "regulatory",
        "title": "Regulatory Hurdles",
        "mitigation": "Class II SaMD; early engagement with Health Canada",
        "badge": "📄",
        "badge_color": "#a78bfa",  # purple
        "arrow_color": "#a78bfa",
        "status_color": "#a78bfa",
    },
    {
        "id": "adoption",
        "title": "Adoption Resistance",
        "mitigation": "Co-design with OR staff during pilot",
        "badge": "👥",
        "badge_color": "#ec4899",  # pink
        "arrow_color": "#ec4899",
        "status_color": "#ec4899",
    },
    {
        "id": "cost",
        "title": "Cost Justification",
        "mitigation": "Demonstrated 6–12 month ROI in simulation",
        "badge": "💵",
        "badge_color": "#10b981",  # emerald
        "arrow_color": "#10b981",
        "status_color": "#10b981",
    },
]

stats = [
    {"big": "100%", "sub": "Data Standardized", "bg": "rgba(59,130,246,.18)", "fg": "#60a5fa", "bd": "rgba(59,130,246,.35)"},
    {"big": "Class II", "sub": "SaMD Pathway", "bg": "rgba(167,139,250,.18)", "fg": "#a78bfa", "bd": "rgba(167,139,250,.35)"},
    {"big": "Co-design", "sub": "With OR Staff", "bg": "rgba(236,72,153,.18)", "fg": "#ec4899", "bd": "rgba(236,72,153,.35)"},
    {"big": "6–12mo", "sub": "ROI Timeline", "bg": "rgba(16,185,129,.18)", "fg": "#10b981", "bd": "rgba(16,185,129,.35)"},
]

# ---------- HELPERS ----------
def risk_card(r):
    arrow_svg = f"""
    <svg class="arrow" viewBox="0 0 40 40" fill="none">
      <path d="M20 10 L20 30 M20 30 L15 25 M20 30 L25 25"
            stroke="{r['arrow_color']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    """
    html = f"""
    <div class="card">
      <div class="badge" style="background:{r['badge_color']}">{r['badge']}</div>
      <div class="label-sm" style="color:#fb7185">RISK</div>
      <div class="risk-title">{r['title']}</div>
      {arrow_svg}
      <div class="mitig">
        <div class="label-sm">MITIGATION STRATEGY</div>
        <p>{r['mitigation']}</p>
      </div>
      <div class="status">
        <span class="dot" style="background:{r['status_color']}"></span>
        <span>Strategy validated</span>
      </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def stat_tile(s):
    html = f"""
    <div class="tile" style="background:{s['bg']}; border-color:{s['bd']}">
      <div class="big" style="color:{s['fg']}">{s['big']}</div>
      <div class="sub" style="color:{s['fg']}">{s['sub']}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ---------- LAYOUT ----------
st.markdown('<div class="maxw">', unsafe_allow_html=True)

# Risk grid
st.markdown('<div class="grid section">', unsafe_allow_html=True)
for i, r in enumerate(risks):
    # Place two per row using columns for consistent spacing within Streamlit's flow
    if i % 2 == 0:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            risk_card(risks[i])
        if i + 1 < len(risks):
            with c2:
                risk_card(risks[i + 1])
st.markdown('</div>', unsafe_allow_html=True)

# Summary tiles
st.markdown('<div class="tiles section">', unsafe_allow_html=True)
for s in stats:
    stat_tile(s)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
