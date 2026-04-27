"""
Convert the project report from Markdown to a self-contained, print-ready HTML page,
then open it in the default browser for PDF export via Ctrl+P.
"""
import markdown
import webbrowser
import os

REPORT_MD = r"C:\Users\Tan Wei Feng\.gemini\antigravity\brain\c150bf9b-5287-47cc-8019-05bfdb895c4a\project_report.md"
OUTPUT_HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Project_Report.html")

# Read the markdown source
with open(REPORT_MD, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert to HTML with extensions for tables, fenced code, etc.
html_body = markdown.markdown(
    md_content,
    extensions=['tables', 'fenced_code', 'codehilite', 'toc', 'nl2br'],
    extension_configs={
        'codehilite': {'css_class': 'highlight', 'guess_lang': False},
    }
)

# Wrap in a full, styled HTML document
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CineMatch - Project Report</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

  :root {{
    --bg: #ffffff;
    --text: #1a1a2e;
    --text-secondary: #4a4a6a;
    --accent: #e94560;
    --accent-light: #fff0f3;
    --border: #e8e8f0;
    --code-bg: #f6f8fa;
    --table-header: #1a1a2e;
    --table-stripe: #f9f9fc;
  }}

  @media print {{
    body {{ font-size: 10pt; }}
    .no-print {{ display: none !important; }}
    h1, h2, h3 {{ page-break-after: avoid; }}
    table, pre, blockquote {{ page-break-inside: avoid; }}
    @page {{ margin: 1.5cm 2cm; }}
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.75;
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 32px 80px;
  }}

  /* --- Headings --- */
  h1 {{
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--text);
    margin: 48px 0 8px;
    letter-spacing: -0.5px;
  }}
  h1:first-child {{ margin-top: 0; }}

  h2 {{
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--accent);
    margin: 40px 0 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid var(--border);
  }}

  h3 {{
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--text);
    margin: 28px 0 12px;
  }}

  h4 {{
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin: 20px 0 8px;
  }}

  p {{
    margin: 12px 0;
    color: var(--text);
  }}

  strong {{ color: var(--text); }}

  /* --- Horizontal Rules --- */
  hr {{
    border: none;
    border-top: 2px solid var(--border);
    margin: 40px 0;
  }}

  /* --- Tables --- */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 24px;
    font-size: 0.9rem;
  }}

  thead th {{
    background: var(--table-header);
    color: #fff;
    font-weight: 600;
    text-align: left;
    padding: 10px 14px;
  }}

  thead th:first-child {{ border-radius: 6px 0 0 0; }}
  thead th:last-child {{ border-radius: 0 6px 0 0; }}

  tbody td {{
    padding: 9px 14px;
    border-bottom: 1px solid var(--border);
  }}

  tbody tr:nth-child(even) {{ background: var(--table-stripe); }}
  tbody tr:hover {{ background: var(--accent-light); }}

  /* --- Code --- */
  code {{
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.85em;
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 4px;
    color: var(--accent);
  }}

  pre {{
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
    overflow-x: auto;
    margin: 16px 0;
    font-size: 0.85rem;
    line-height: 1.6;
  }}

  pre code {{
    background: none;
    padding: 0;
    color: var(--text);
  }}

  /* --- Blockquotes (alerts) --- */
  blockquote {{
    border-left: 4px solid var(--accent);
    background: var(--accent-light);
    padding: 14px 20px;
    margin: 16px 0;
    border-radius: 0 8px 8px 0;
  }}

  blockquote p {{ margin: 4px 0; color: var(--text); }}

  /* --- Lists --- */
  ul, ol {{
    margin: 10px 0 10px 24px;
  }}

  li {{
    margin: 4px 0;
  }}

  /* --- Print button --- */
  .print-bar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--table-header);
    color: #fff;
    padding: 10px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 999;
    box-shadow: 0 2px 12px rgba(0,0,0,0.15);
  }}

  .print-bar span {{ font-weight: 600; font-size: 0.9rem; }}

  .print-btn {{
    background: var(--accent);
    color: #fff;
    border: none;
    padding: 8px 24px;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    border-radius: 6px;
    cursor: pointer;
    transition: 0.2s;
  }}

  .print-btn:hover {{ opacity: 0.85; }}
</style>
</head>
<body>

<div class="print-bar no-print">
  <span>CineMatch Project Report</span>
  <button class="print-btn" onclick="window.print()">Save as PDF (Ctrl+P)</button>
</div>

<div style="height: 48px;" class="no-print"></div>

{html_body}

</body>
</html>"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_doc)

print(f"Report saved to: {OUTPUT_HTML}")
print("Opening in browser... Use Ctrl+P > 'Save as PDF' to export.")
webbrowser.open(f'file:///{OUTPUT_HTML.replace(os.sep, "/")}')
