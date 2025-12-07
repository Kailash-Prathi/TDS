---
marp: true
theme: default
paginate: true
math: mathjax
size: 16:9
style: |
  /* Global Theme Specification */
  section {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 26px;
    padding: 50px;
    color: #333;
  }
  h1 {
    color: #0056b3;
    border-bottom: 2px solid #0056b3;
  }
  code {
    background-color: #f0f0f0;
    padding: 2px 5px;
    border-radius: 4px;
  }
---

# Technical Documentation: Project API
## Version 2.0 Deployment Strategy

**Maintainer:** Technical Writing Team
**Email:** 24f3001410@ds.study.iitm.ac.in

---

# Agenda

1.  Architecture Overview
2.  Complexity Analysis
3.  Theme & Styling
4.  Version Control

> This documentation is designed to be converted to PDF/HTML via CI/CD.

---

# Custom Styling via Directives

This slide uses **Marp Directives** to override the global theme for a "Dark Mode" effect.

* **Directive Used:** `_backgroundColor: #2c3e50`
* **Directive Used:** `_color: white`

This is useful for emphasis or distinct section breaks in your documentation.

---

![bg right:40%](https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

# Algorithmic Complexity

We utilize a revised sorting mechanism to improve data retrieval speeds.

### Mathematical Model

The time complexity $T(n)$ for the new algorithm is:

$$
O(n \log n)
$$

Where $n$ represents the number of active records in the database.

---

# Maintenance Info

To update this presentation:

1.  Edit `presentation.md`.
2.  Push to the Git repository.
3.  Contact **24f3001410@ds.study.iitm.ac.in** for merge conflicts.
