#!/usr/bin/env python3
import streamlit as st
import os
import fitz  # pymupdf
from research_workflow import run_research_workflow
from memory_agent import memory_store

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
ARCH_IMG = os.path.join(ASSETS_DIR, 'architecture.png')

st.set_page_config(page_title="Research Assistant", layout="wide")
st.title("🔎 Research Assistant with Memory & Multi-Agent Workflow")
st.caption("Strands agents: Researcher → Analyst → Writer | Memory: store & reuse | Docker-ready")

with st.expander("📐 Show Architecture Diagram", expanded=True):
    st.image(ARCH_IMG, caption="Workflow: Researcher → Analyst → Writer with Memory, UI & PDF Export")

query = st.text_input("Enter your research query or claim to verify:")

# Run button
run_col, pdf_col = st.columns([3, 1])
with run_col:
    run_clicked = st.button("Run Workflow", type="primary")

# Progress container
progress = st.empty()
report_area = st.empty()

# Function to export PDF including diagram

def export_pdf(report_text, include_diagram=True):
    pdf_path = os.path.join(os.getcwd(), "report.pdf")
    doc = fitz.open()
    # Page 1: Text report
    page = doc.new_page()
    text_rect = fitz.Rect(50, 50, 550, 770)
    page.insert_textbox(text_rect, report_text, fontsize=11, fontname="helv")
    # Page 2: Architecture diagram
    if include_diagram and os.path.exists(ARCH_IMG):
        page2 = doc.new_page()
        img_rect = fitz.Rect(50, 50, 550, 770)
        page2.insert_image(img_rect, filename=ARCH_IMG)
    doc.save(pdf_path)
    doc.close()
    return pdf_path

if run_clicked and query:
    progress.info("Step 1: Checking memory for prior research…")
    report = run_research_workflow(query)
    progress.success("Workflow complete.")
    report_area.text_area("Final Report", str(report), height=350)
    pdf_file = export_pdf(str(report), include_diagram=True)
    with pdf_col:
        st.download_button("📄 Download PDF", open(pdf_file, "rb"), file_name="report.pdf")

st.sidebar.title("💾 Memory")
if st.sidebar.button("Show Stored Memories"):
    st.sidebar.write(memory_store)
