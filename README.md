# 🧠 AI Proposal Automation System

This project aims to build an intelligent automation system that reads and analyzes RFPs (Request for Proposals), conducts real-time research, and generates customized proposal documents—designed for consultants, agencies, and professionals who need to respond quickly and persuasively to complex business opportunities.

---

## 🔍 Overview

- **Input**: Raw RFP text, preferred proposal tone, key terms to emphasize, optional client name and title
- **Processing**: RFP summarization, needs extraction, slide-type recommendation, research question generation
- **Research**: Google search & GPT-based document summarization (RAG-style)
- **Output**: Drafted proposal slides with components like titles, graphs, SWOT tables, timelines, and more

---

## 🧭 User Input Flow

| Field | Description |
|-------|-------------|
| RFP Document | Full RFP text or uploaded file |
| Proposal Tone | Formal / Trustworthy / Concise / Creative |
| Emphasis Keywords | List of business terms to highlight |
| Client Name (Optional) | Used for cover and body personalization |
| Project Title (Optional) | Displayed on the proposal cover page |

---

## 🧠 Intelligence Workflow

### 1. RFP Analysis
- Summarize the RFP and extract structured client needs using LLM
- Map extracted needs to pre-defined proposal slide types

### 2. Slide Planning
- Define required components per slide (e.g., title, graph, table)
- Generate tailored research questions for each content section

### 3. Research (RAG Architecture)
- Use Google Search (or SerpAPI) to retrieve top 5–10 results per question
- GPT evaluates accuracy and relevance, summarizes findings, and cites sources
- Re-search if confidence score is low (retry max 10 times)

### 4. Slide Generation
- Automatically assemble slides with data-driven text, graphs, and formatting
- Tone and keywords adjusted to match user selection

---

## 🖥️ Output Format

- 📝 **PowerPoint Draft**: Slide deck including visual elements (charts, tables, SWOT, etc.)
- 📄 **Reference Document**: Source list for each research-based slide (optional)
- 📑 **Executive Summary PDF**: Concise one-page summary (optional)

---

## 📊 Supported Slide Types

- Cover Page, Table of Contents, Project Understanding  
- Client Needs Summary, Market Overview, Growth Trend Analysis  
- Drivers & Challenges, Competitive Benchmarking, SWOT Analysis  
- Solution Overview, Strategic Recommendations, Implementation Plan  
- Timeline & Milestones, Risk Management, Expected Benefits  
- Budget Estimation, Team Introduction, Differentiation, Closing Summary, Q&A

> All slide types are matched with LLM-driven logic and built from research-backed inputs.

---

## ⚙️ Tech Stack

- `Python`, `LangChain`, `OpenAI GPT API`  
- `Google Search` / `SerpAPI` for real-time content retrieval  
- `PPTX Generation Libraries` for automated document creation  
- Optional: `Streamlit` or `Gradio` for front-end interface (planned)

---

## 🚧 Status

Currently in MVP development phase.  
RFP parsing and research modules are operational.  
Next steps: visualization engine integration and output formatting polish.

---

## 💡 Why This Matters

Responding to RFPs is a high-effort, high-stakes task.  
This system transforms the manual hours spent on market research, structure building, and writing—into a guided, intelligent process that empowers professionals to focus on strategy, not slides.

---

## 👤 Author

Hyun Jun Lee  
📫 hyunjun960214@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/hyunjun-lee-a37448212/)  
