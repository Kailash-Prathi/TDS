---
marp: true
theme: custom
paginate: true
math: katex
---

<!--
  Product documentation presentation (Marp Markdown)
  Author email included: 24f3001410@ds.study.iitm.ac.in
-->

<!-- Custom theme CSS for Marp -->
<style>
/*marp:theme*/
:root{
  --brand: #0b5cff;
  --accent: #00b28a;
  --bg: #0f1724;
  --text: #e6eef8;
  --muted: #9fb1d7;
  --card: rgba(255,255,255,0.03);
  --radius: 14px;
  --mono: 'Fira Code', monospace;
  --ui-font: 'Inter', 'Helvetica Neue', Arial, sans-serif;
}

/* base slide styles */
section {
  font-family: var(--ui-font);
  color: var(--text);
  background-color: var(--bg);
  padding: 48px;
}

/* Title styling */
h1 {
  font-size: 2.4rem;
  margin-bottom: .25rem;
  color: white;
}

/* Subtitles */
h2, h3 {
  color: var(--muted);
}

/* Email (footer-like) */
.email {
  font-family: var(--mono);
  font-size: 0.9rem;
  color: var(--accent);
  margin-top: 8px;
}

/* Card block for content */
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: 0 6px 24px rgba(3,8,23,0.6);
}

/* Code blocks */
pre, code {
  font-family: var(--mono);
  background: rgba(255,255,255,0.02);
  padding: 8px;
  border-radius: 8px;
  color: #e6f2ff;
}

/* Page number styling (if paginate true) */
marp-footer {
  font-size: .9rem;
  color: var(--muted);
}

/* Accent rule */
.rule {
  height: 6px;
  width: 140px;
  background: linear-gradient(90deg, var(--brand), var(--accent));
  border-radius: 6px;
  margin: 12px 0 18px 0;
}

/* Make list items slightly larger and relaxed */
li {
  font-size: 1.05rem;
  line-height: 1.6;
}

/* Centering helper */
.center {
  text-align: center;
}

/* Small note text */
.note {
  color: #bcd7ff;
  font-size: 0.9rem;
}

/* Make display math larger */
.katex-display {
  font-size: 1.25rem;
}

/* Responsive image in slides */
img.responsive {
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 8px 30px rgba(2,6,23,0.6);
}
</style>

---

# Product: Acme Software — Documentation
## Maintainable documentation for developers & users
<div class="rule"></div>

**Technical writer:** Product Documentation Team  
**Contact:** <span class="email">24f3001410@ds.study.iitm.ac.in</span>

<!-- _class: center -->
<!-- _footer: "Acme Software • Internal Documentation" -->

---

<!-- Slide with background image using slide-level frontmatter -->
---
backgroundImage: url('https://picsum.photos/1600/900?grayscale')
backgroundSize: cover
backgroundPosition: center
class: center

# Acme Software — At a glance

> A brief visual overview of the product capabilities and architecture.

<div style="height:16px"></div>

<!-- use a translucent card to make text readable on background -->
<div class="card" style="display:inline-block; max-width:900px;">
**Acme Software** is a modular, extensible platform for processing pipelines, integrations, and analytics.  
Designed for maintainability and version-controlled docs.
</div>

---

# Table of contents
1. Overview & goals  
2. Installation & setup  
3. High-level architecture  
4. Key modules (API, Worker, UI)  
5. Examples / Commands  
6. Appendix: complexity & algorithms

---

# 1. Overview & goals
- Single source of truth in Markdown, source-controlled (Git)
- Convert to HTML/PDF/PPTX via Marp or other static-site generators
- Clear separation: user guide, dev guide, API reference
- Maintainable templates for release notes and changelogs

---

# 2. Installation & setup
### Requirements
- Node.js >= 16 (for build tool)
- Python 3.8+ (CLI tooling)
- PostgreSQL 12+ (optional for local backend)

### Quick install (example)
```bash
# clone repo
git clone git@github.com:your-org/acme.git
cd acme

# install dependencies
npm ci
pip install -r requirements.txt

# start dev environment
docker compose up --build
