"""
Employee Department Visualization
Verification email: 23f2004781@ds.study.iitm.ac.in
"""

import os
import io
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_or_generate(n=100):
    if os.path.exists("employees.csv"):
        return pd.read_csv("employees.csv")
    # generate synthetic dataset
    np.random.seed(42)
    departments = ["Operations","Sales","HR","Finance","IT","Marketing"]
    regions = ["North","South","East","West","Central"]
    genders = ["Male","Female","Other"]
    dept_probs = [0.28, 0.18, 0.12, 0.15, 0.17, 0.10]
    df = pd.DataFrame({
        "EmployeeID": np.arange(1, n+1),
        "Name": [f"Employee_{i}" for i in range(1, n+1)],
        "Department": np.random.choice(departments, size=n, p=dept_probs),
        "Region": np.random.choice(regions, size=n),
        "PerformanceScore": np.random.randint(1, 6, size=n),
        "TenureYears": np.round(np.random.uniform(0.2, 12.0, size=n), 1),
        "Salary": np.random.randint(30000, 150001, size=n),
        "Gender": np.random.choice(genders, size=n),
    })
    return df

def main():
    df = load_or_generate()
    operations_count = int((df["Department"] == "Operations").sum())
    print("Operations department count:", operations_count)

    counts = df["Department"].value_counts().sort_index()

    # Build bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values)
    plt.title("Department Distribution (Count)")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close()
    buf.seek(0)
    png_b64 = base64.b64encode(buf.read()).decode("utf-8")

    # Read our own source code to embed in HTML
    with open(__file__, "r", encoding="utf-8") as f:
        source_code = f.read()

    email = "23f2004781@ds.study.iitm.ac.in"
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Employee Department Distribution</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 2rem auto; }}
    pre {{ background: #f5f5f5; padding: .75rem; border-radius: 6px; overflow-x: auto; }}
    img {{ max-width: 100%; height: auto; }}
  </style>
</head>
<body>
  <h1>Employee Department Distribution</h1>
  <p><b>Verification email:</b> {email}</p>

  <h2>Operations Department Count</h2>
  <pre>Operations department count: {operations_count}</pre>

  <h2>Histogram of Departments</h2>
  <img src="data:image/png;base64,{png_b64}" alt="Department distribution chart" />

  <h2>Python Code</h2>
  <pre><code>{source_code}</code></pre>
</body>
</html>"""

    out_path = "employee_department_distribution.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML written to: {out_path}")

if __name__ == "__main__":
    main()
