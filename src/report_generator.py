import os
import json
from datetime import datetime
from src.gemini_utils import SESSION_TRACKER

REPORT_PATH = "report.html"

def generate_visual_report(metrics: list) -> str:
    """Genera un reporte HTML con gráficos y tabla detallada."""
    # REPORT_PATH is now relative to current working directory
    # No need to create directory as it goes to root of project or where script runs
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Cálculos básicos
    total = len(metrics)
    included = len([m for m in metrics if m['status'] == 'INCLUDED'])
    filtered = len([m for m in metrics if m['status'] == 'FILTERED'])
    duplicates = len([m for m in metrics if m['status'] == 'DUPLICATE'])
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nubenetes Curation Health Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f7f6; color: #333; margin: 0; padding: 20px; }}
            .container {{ max-width: 1200px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .summary-cards {{ display: flex; gap: 20px; margin: 20px 0; }}
            .card {{ flex: 1; padding: 20px; border-radius: 8px; text-align: center; color: white; }}
            .card.total {{ background: #34495e; }}
            .card.included {{ background: #27ae60; }}
            .card.filtered {{ background: #e67e22; }}
            .card.duplicates {{ background: #2980b9; }}
            .charts-container {{ display: flex; gap: 40px; margin: 40px 0; flex-wrap: wrap; }}
            .chart-box {{ flex: 1; min-width: 300px; height: 350px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 30px; }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; font-size: 14px; }}
            th {{ background: #f8f9fa; color: #2c3e50; }}
            tr:hover {{ background: #f1f1f1; }}
            .status-tag {{ padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }}
            .status-INCLUDED {{ background: #d4edda; color: #155724; }}
            .status-FILTERED {{ background: #fff3cd; color: #856404; }}
            .status-DUPLICATE {{ background: #d1ecf1; color: #0c5460; }}
            .stars {{ color: #f1c40f; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💎 Nubenetes Curation Dashboard</h1>
            <p><strong>Run Timestamp:</strong> {timestamp}</p>
            
            <div class="summary-cards">
                <div class="card total"><h3>{total}</h3><p>Processed</p></div>
                <div class="card included"><h3>{included}</h3><p>Included</p></div>
                <div class="card filtered"><h3>{filtered}</h3><p>Filtered</p></div>
                <div class="card duplicates"><h3>{duplicates}</h3><p>Duplicates</p></div>
            </div>

            <div class="charts-container">
                <div class="chart-box"><canvas id="decisionChart"></canvas></div>
                <div class="chart-box"><canvas id="sourceChart"></canvas></div>
            </div>

            <h2>🧠 AI Intelligence & Infrastructure</h2>
            <div style="background: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
                <div style="display: flex; gap: 40px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 250px;">
                        <h4>🤖 Model Usage</h4>
                        <ul style="list-style: none; padding: 0;">
                            {''.join([f"<li><code>{m}</code>: <b>{c}</b> calls</li>" for m, c in SESSION_TRACKER.model_usage.items()]) or "<li>No AI calls recorded</li>"}
                        </ul>
                    </div>
                    <div style="flex: 2; min-width: 300px;">
                        <h4>🔑 API Key Health</h4>
                        <table style="width: 100%; color: white; border: none;">
                            <tr><th>Key</th><th>Type</th><th>Usage</th><th>Failures</th></tr>
                            {''.join([f"<tr><td>{idx+1}</td><td>{s['type']}</td><td>{s['calls']}</td><td>{s['429s']}/{s['404s']}</td></tr>" for idx, s in SESSION_TRACKER.key_stats.items()])}
                        </table>
                    </div>
                </div>
            </div>

            <h2>📋 Detailed Curation Matrix</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Status</th>
                        <th>Title</th>
                        <th>Primary Category</th>
                        <th>Impact</th>
                        <th>Source</th>
                        <th>Reason</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    sources = {}
    for i, m in enumerate(metrics, 1):
        status_class = f"status-{m['status']}"
        stars = "🌟" if m.get('impact_score', 0) > 80 else ""
        impact = f"{m.get('impact_score', 0)} {stars}"
        
        sources[m['source']] = sources.get(m['source'], 0) + 1
        
        html += f"""
                    <tr>
                        <td>{i}</td>
                        <td><span class="status-tag {status_class}">{m['status']}</span></td>
                        <td><a href="{m['url']}" target="_blank">{m.get('title', 'N/A')[:60]}...</a></td>
                        <td><code>{m['category']}</code></td>
                        <td class="stars">{impact}</td>
                        <td>{m['source']}</td>
                        <td>{m['reason']}</td>
                    </tr>
        """
        
    html += f"""
                </tbody>
            </table>
        </div>

        <script>
            // Decision Chart
            const ctx1 = document.getElementById('decisionChart').getContext('2d');
            new Chart(ctx1, {{
                type: 'pie',
                data: {{
                    labels: ['Included', 'Filtered', 'Duplicate'],
                    datasets: [{{
                        data: [{included}, {filtered}, {duplicates}],
                        backgroundColor: ['#27ae60', '#e67e22', '#2980b9']
                    }}]
                }},
                options: {{ plugins: {{ title: {{ display: true, text: 'Decision Distribution' }} }} }}
            }});

            // Source Chart
            const ctx2 = document.getElementById('sourceChart').getContext('2d');
            new Chart(ctx2, {{
                type: 'bar',
                data: {{
                    labels: {list(sources.keys())},
                    datasets: [{{
                        label: 'Links by Source',
                        data: {list(sources.values())},
                        backgroundColor: '#34495e'
                    }}]
                }},
                options: {{ plugins: {{ title: {{ display: true, text: 'Extraction Sources' }} }} }}
            }});
        </script>
    </body>
    </html>
    """
    
    with open(REPORT_PATH, "w") as f:
        f.write(html)
        
    return REPORT_PATH
