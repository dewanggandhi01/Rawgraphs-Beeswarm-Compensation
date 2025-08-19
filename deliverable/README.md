# RAWGraphs Beeswarm Plot — Compensation Analysis

**Email (required):** 23f2004781@ds.study.iitm.ac.in

This repository contains a publication-ready **Beeswarm Plot** created in **RAWGraphs** to analyze employee salary distribution across departments and experience levels.

## Files
- `chart.png` — Exported from RAWGraphs (PNG, between 300×300 and 512×512 px).
- `README.md` — This file with required email.
- *(Optional)* `beeswarm_compensation_data.csv` — Sample data used to generate the plot.

## How to Reproduce
1. Open https://rawgraphs.io/ (or RAWGraphs 2.0 app).
2. Copy-paste the CSV data from `beeswarm_compensation_data.csv`.
3. Choose **Beeswarm Plot**.
4. Map the fields:
   - **Value / X**: `salary` (continuous)
   - **Groups / Y**: `department` (categorical)
   - **Color**: `level` (categorical)
   - **Labels**: *(optional)* `department`
5. Customize:
   - Title: *Salary Distribution by Department & Level*
   - Legend: ON
   - Axes labels: X=`Salary (USD)`, Y=`Department`
   - Color palette: Professional palette (e.g., Set2 or Set3)
   - Dot radius: 3–6 (per preference)
6. Export:
   - Format: **PNG**
   - Size: **512×512 px** (or any size between 300×300 and 512×512)
   - Download as `chart.png`

## Validation URL (RAW README)
Use the **raw** URL format (replace with your details):
```
https://raw.githubusercontent.com/<username>/<repo>/<branch>/<folder>/README.md
```
Example:
```
https://raw.githubusercontent.com/dewanggandhi01/rawgraphs-beeswarm-compensation/main/deliverable/README.md
```
