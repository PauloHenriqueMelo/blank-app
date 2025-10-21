# app.py
import streamlit as st
from graphviz import Digraph

st.set_page_config(page_title="Interdisciplinary Collaboration Map", layout="wide")

# ---------- THEME ----------
st.markdown("""
<style>
.stApp {
  background: linear-gradient(135deg, #ede9fe 0%, #f5f3ff 50%, #fafafa 100%);
  color: #1e1b4b;
  font-family: 'Inter', -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
}
h1 {
  text-align:center;
  font-weight:800;
  font-size:2.2rem;
  color:#4c1d95;
  margin-top:10px;
  text-shadow:0 2px 8px rgba(76,29,149,0.1);
}
p.subtitle {
  text-align:center;
  color:#5b21b6;
  font-size:1rem;
  margin-bottom:2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Interdisciplinary Solution Development</h1>", unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">A unified approach where Biochemist, Vascular Surgeon, and Medical Graduate converge to develop a novel health-technology solution.</p>',
    unsafe_allow_html=True,
)

# ---------- GRAPH ----------
graph = Digraph("Collaboration", format="png")
graph.attr(bgcolor="transparent")
graph.attr(rankdir="TB", nodesep="1.0", splines="spline")

# Style defaults
graph.attr("node", shape="roundrect", style="filled", fontsize="12", fontname="Inter")

# Biochemist cluster
with graph.subgraph(name="cluster_bio") as c:
    c.attr(label="Biochemist", fontsize="16", fontcolor="#4c1d95", color="#c4b5fd", style="filled", fillcolor="#f3e8ff")
    c.node("B1", "Biomarker discovery", fillcolor="#ddd6fe")
    c.node("B2", "Assay development (ELISA, LC-MS)", fillcolor="#e9d5ff")
    c.node("B3", "Molecular pathway analysis", fillcolor="#f3e8ff")

# Vascular Surgeon cluster
with graph.subgraph(name="cluster_surg") as c:
    c.attr(label="Vascular Surgeon", fontsize="16", fontcolor="#4c1d95", color="#c4b5fd", style="filled", fillcolor="#ede9fe")
    c.node("S1", "Clinical needs assessment", fillcolor="#ddd6fe")
    c.node("S2", "Operative workflow insight", fillcolor="#e9d5ff")
    c.node("S3", "Procedure outcome metrics", fillcolor="#f3e8ff")

# Medical Graduate cluster
with graph.subgraph(name="cluster_grad") as c:
    c.attr(label="Medical Graduate", fontsize="16", fontcolor="#4c1d95", color="#c4b5fd", style="filled", fillcolor="#f3e8ff")
    c.node("M1", "Clinical data analysis", fillcolor="#ddd6fe")
    c.node("M2", "Patient-centric design thinking", fillcolor="#e9d5ff")
    c.node("M3", "Scientific communication", fillcolor="#f3e8ff")

# Central unified solution
graph.node("U", "Integrated Health Solution\n(Biomarker-driven vascular care)", shape="rect",
           fillcolor="#c4b5fd", fontcolor="white", style="filled,bold", color="#6d28d9", fontsize="13")

# Connect the disciplines
for n in ["B1", "B2", "B3"]:
    graph.edge(n, "U", color="#8b5cf6")
for n in ["S1", "S2", "S3"]:
    graph.edge(n, "U", color="#8b5cf6")
for n in ["M1", "M2", "M3"]:
    graph.edge(n, "U", color="#8b5cf6")

st.graphviz_chart(graph, use_container_width=True)

# ---------- TEXT SUMMARY ----------
st.markdown("### Collaborative Synergy")
st.write(
"""
- **Biochemist** provides molecular insight, assay design, and validation of biomarkers for vascular pathophysiology.  
- **Vascular Surgeon** defines clinical relevance, ensures procedural applicability, and guides translational feasibility.  
- **Medical Graduate** bridges data analysis, ethical research methodology, and patient-oriented evaluation.  

Together, they co-develop **a biomarker-integrated, clinically validated vascular diagnostic or monitoring system** that unites laboratory innovation with surgical practice and real-world patient outcomes.
"""
)
