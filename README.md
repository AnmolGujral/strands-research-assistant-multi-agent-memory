# 🔎 Strands Research Assistant with Memory and Multi-Agent Workflow

## ✨ Overview
This project demonstrates an **Agentic Workflow** using Strands Agents combined with **memory capabilities** and an interactive **Streamlit UI**. It enables:
- Multi-step research workflows
- Memory-based personalization
- PDF report generation (includes architecture diagram)
- Dockerized deployment for easy scalability

## ✅ Features
- Enter a query → See workflow steps in UI
- View stored memories in sidebar
- Download report as PDF
- Reuse previous research from memory

## 📐 Architecture Diagram
- Displayed directly in the **Streamlit UI** (expandable section).
- **Included in the downloadable PDF report** as a dedicated page.

---

## ▶️ Run Locally
```shell
unzip research_assistant_project.zip
cd research_assistant_project
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Run with Docker
```shell
docker build -t research-assistant .
docker run -p 8501:8501 research-assistant
```
