import streamlit as st

st.set_page_config(
    page_title='Addressing "Killer Risks"',
    page_icon="🧠",
    layout="wide",
)

# ---------- STYLES ----------
st.markdown("""
<style>
.stApp {
  background: linear-gradient(145deg, #c8b6ff 0%, #e3d7ff 30%, #faf6ff 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen;
  color: #1e1b4b;
}

/* --- MAIN TITLE --- */
.h1-title {
  text-align:center;
  font-size: 2.2rem;
  font-weight: 800;
  color: #312e81;
  margin-top: 1rem;
  margin-bottom: 2rem;
  text-shadow: 0 3px 10px rgba(72,61,139,0.15);
}

/* --- GRID LAYOUT --- */
.grid { display:grid; gap: 24px; }
@media (min-width: 992px) { .grid { grid-template-columns: 1fr 1fr; } }

/* --- CARD --- */
.card {
  position: relative;
  border-radius: 16px;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(140,120,200,0.2);
  box-shadow: 0 12px 30px rgba(80,60,150,0.1);
  padding: 24px;
  transition: all .25s ease;
}
.card:hover {
  transform: scale(1.015);
  box-shadow: 0 18px 40px rgba(80,60,150,0.18);
}

/* --- LABELS --- */
.label-sm {
  letter-spacing: .1em;
  font-size: .7rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #7e22ce;
  margin-bottom: .3rem;
}

/* --- RISK TITLE --- */
.risk-title {
  font-size: 1.3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: #1e1b4b;
}

/* --- MITIGATION BOX --- */
.mitig {
  border-radius: 10px;
  background: rgba(240,238,255,0.8);
  border: 1px solid rgba(140,120,200,0.25);
  padding: 10px 14px;
}
.mitig .label-sm {
  color: #059669;
  font-weight: 700;
}
.mitig p {
  color: #1e1b4b;
  margin: 0;
  font-size: .9rem;
}

/* --- ARROW --- */
.arrow { width: 36px; height: 36px; margin: 0.5rem auto; opacity: .8; }
@keyframes floaty {
  0%,100% { transform: translateY(-3px); }
  50% { transform: translateY(3px); }
}
.arrow path { animation: floaty 1.2s infinite ease-in-out; }

/* --- STATUS --- */
.status {
  display:flex; align-items:center; gap:8px;
  margin-top: 10px;
  color:#334155;
  font-size:.78rem;
}
.dot { width:7px; height:7px; border-radius:50%; }

/* --- SUMMARY TILES --- */
.tiles { display:grid; gap: 16px; grid-template-columns: repeat(2, 1fr); margin-top: 2rem; }
@media (min-width: 992px) { .tiles { grid-template-columns: repeat(4, 1fr); } }

.tile {
  border-radius: 14px;
  text-align:center;
  padding: 16px;
  background: rgba(255,255,255,0.6);
  border: 1px solid rgba(140,120,200,0.25);
  box-shadow: 0 8px 20px rgba(100,80,160,0.08);
}
.tile .big { font-size: 1.5rem; font-weight: 800; margin-bottom: 4px; }
.tile .sub { font-size: .85rem; opacity:.9; }

.maxw { max-width: 1100px; margin: 0 auto; }
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
risks = [
    {
        "title": "Data Heterogeneity",
        "mitigation": "Standardized HL7/FHIR streams",
        "arrow_color": "#3b82f6",
        "status_color": "#3b82f6",
    },
    {
        "title": "Regulatory Hurdles",
        "mitigation": "Class II SaMD; early engagement with Health Canada",
        "arrow_color": "#8b5cf6",
        "status_color": "#8b5cf6",
    },
    {
        "title": "Adoption Resistance",
        "mitigation": "Co-design with OR staff during pilot",
        "arrow_color": "#ec4899",
        "status_color": "#ec4899",
    },
    {
        "title": "Cost Justification",
        "mitigation": "Demonstrated 6–12 month ROI in simulation",
        "arrow_color": "#10b981",
        "status_color": "#10b981",
    },
]

stats = [
    {"big": "100%", "sub": "Data Standardized", "fg": "#3b82f6"},
    {"big": "Class II", "sub": "SaMD Pathway", "fg": "#8b5cf6"},
    {"big": "Co-design", "sub": "With OR Staff", "fg": "#ec4899"},
    {"big": "6–12mo", "sub": "ROI Timeline", "fg": "#10b981"},
]

# ---------- COMPONENTS ----------
def risk_card(r):
    arrow_svg = f"""
    <svg class="arrow" viewBox="0 0 40 40" fill="none">
      <path d="M20 10 L20 30 M20 30 L15 25 M20 30 L25 25"
            stroke="{r['arrow_color']}" stroke-width="3"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    """
    html = f"""
    <div class="card">
      <div class="label-sm">RISK</div>
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
    <div class="tile">
      <div class="big" style="color:{s['fg']}">{s['big']}</div>
      <div class="sub" style="color:{s['fg']}">{s['sub']}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ---------- LAYOUT ----------
st.markdown('<div class="h1-title">Addressing "Killer Risks"</div>', unsafe_allow_html=True)
st.markdown('<div class="maxw">', unsafe_allow_html=True)

# Risk cards grid
for i in range(0, len(risks), 2):
    c1, c2 = st.columns(2, gap="large")
    with c1: risk_card(risks[i])
    if i + 1 < len(risks):
        with c2: risk_card(risks[i + 1])

# Summary tiles
st.markdown('<div class="tiles">', unsafe_allow_html=True)
for s in stats:
    stat_tile(s)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
