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

## 🧠 RFP Intelligence Workflow
![image](https://github.com/user-attachments/assets/7a11393f-cbb2-4051-829c-3c3b9f7176bf)

## 1. Client Input
- Upload RFP file (PDF, DOCX)
- Specify proposal tone and direction
- Provide any additional context or preferences

## 2. RFP Analysis
- Parse and extract key RFP requirements
- Generate a concise summary of the RFP
- Organize content for downstream mapping

## 3.1. Slide Framework Design
- Match RFP requirements to corresponding slide templates  
  → 20 standard templates currently available

## 3.2.1. Research Question Generation
- Generate key research questions for each RFP item
- Vary question detail based on subscription plan  
  → (e.g., default vs. advanced tier)

## 3.2.2. Research & Validation
- Use Search APIs (e.g., SERP API) to conduct external research
- Validate content relevance and accuracy via AI Agent
- Fallback to alternative source (e.g., Perplexity API) if needed

## 4. Draft Proposal Generation
- Map researched insights to the appropriate slide templates
- Populate charts and tables based on extracted data
- Incorporate client input to write titles, subtitles, and main content

## 5. Consultant Review
Final review by human consultant to ensure:
- Data accuracy and logical consistency
- Slide formatting and template alignment
- Clarity and professional tone of language

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
