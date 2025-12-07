---
marp: true
theme: default
paginate: true
math: mathjax
size: 16:9
style: |
  /* Custom Theme Specification */
  section {
    background-color: #fcfcfc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 24px;
    color: #333;
  }
  h1 {
    color: #2c3e50;
    font-size: 48px;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
  }
  h2 {
    color: #2980b9;
  }
  /* Custom Class for code slides */
  section.technical {
    background-color: #282c34;
    color: #abb2bf;
  }
  section.technical h1, section.technical h2 {
    color: #61afef;
    border-color: #61afef;
  }
  /* Footer Styling */
  footer {
    position: absolute;
    bottom: 20px;
    left: 40px;
    font-size: 14px;
    color: #7f8c8d;
  }
---

# Product Nebula
## API & Architecture Documentation
### Technical Overview Q4 2025

<br>

**Author:** Technical Writing Team
**Contact:** 24f3001410@ds.study.iitm.ac.in

---

# Agenda

1. System Architecture Overview
2. Core Algorithms & Complexity
3. Database Schema Changes
4. Deployment Pipeline

> "Good documentation is like a love letter that you write to your future self."

---

![bg brightness:0.4](https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)

# 1. System Architecture

This release focuses on **microservices decoupling**. 

We are moving away from the monolith to ensure:
* Higher Availability
* Independent Scaling
* Fault Isolation

---

# 2. Algorithmic Complexity

We have optimized the search algorithm. The previous implementation had a complexity of $O(n^2)$, which caused latency spikes during high traffic.

The new **Binary Search Tree** implementation ensures logarithmic time complexity.

### Performance Equation

The total time complexity $T(n)$ for the new query engine is defined as:

$$
T(n) = \sum_{i=1}^{k} \log(n_i) + O(1)
$$

Where:
* $k$ is the number of concurrent shards.
* $n$ is the dataset size.

---

# 3. Implementation Details

We utilize **directive-based styling** (like this dark slide) to highlight code-heavy sections.

```python
def optimize_query(data: list) -> int:
    """
    Optimized search using bisect module.
    Complexity: O(log n)
    """
    import bisect
    
    data.sort()  # Timsort O(n log n)
    breakpoint = bisect.bisect_left(data, 100)
    
    return breakpoint
