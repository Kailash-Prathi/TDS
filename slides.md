---
marp: true
theme: default
paginate: true
math: mathjax
size: 16:9
style: |
  /* Custom Theme Specification */
  section {
    font-family: 'Arial', sans-serif;
    font-size: 28px;
    padding: 50px;
    color: #333;
  }
  h1 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
  }
  .highlight-box {
    background-color: #f0f8ff;
    border-left: 5px solid #3498db;
    padding: 15px;
  }
---

# Technical Documentation
## Product Architecture V2

**Author Email:** 24f3001410@ds.study.iitm.ac.in

---

# 1. Custom Styling Directive

This slide uses a **local Marp directive** (`_backgroundColor`) to change the slide color to a light cream, distinct from the global theme.

<div class="highlight-box">
  Directives allow us to style specific slides without affecting the whole presentation.
</div>

---

![bg brightness:0.5](https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

# 2. Visuals & Backgrounds

This slide uses the **image background directive** (`bg`) combined with a brightness filter.

* High Contrast
* Visual Impact
* White Text (via directive)

---

# 3. Algorithmic Complexity

We use mathematical notation to define our system performance.

### Time Complexity Equation
The sorting algorithm runs in log-linear time:

$$
T(n) = n \log n + O(n)
$$

Where $n$ is the number of database records.

---

# Thank You

**Contact:** 24f3001410@ds.study.iitm.ac.in
