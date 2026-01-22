from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os
import pickle

app = FastAPI(
    title="ML Pipeline CI/CD Demo",
    description="A demonstration of CI/CD for Machine Learning models using DVC",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def root():
    model_exists = os.path.exists("model/svm")
    data_exists = os.path.exists("data/raw")
    
    status_model = "Available" if model_exists else "Not pulled (run: dvc pull -r read)"
    status_data = "Available" if data_exists else "Not pulled (run: dvc pull -r read)"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ML Pipeline CI/CD Demo</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 40px 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }}
            .container {{
                background: white;
                border-radius: 16px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }}
            h1 {{
                color: #333;
                margin-bottom: 10px;
            }}
            .subtitle {{
                color: #666;
                font-size: 1.1em;
                margin-bottom: 30px;
            }}
            .section {{
                background: #f8f9fa;
                border-radius: 12px;
                padding: 20px;
                margin: 20px 0;
            }}
            .section h2 {{
                color: #444;
                font-size: 1.2em;
                margin-top: 0;
            }}
            .status {{
                display: flex;
                justify-content: space-between;
                padding: 10px 0;
                border-bottom: 1px solid #eee;
            }}
            .status:last-child {{
                border-bottom: none;
            }}
            .badge {{
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.85em;
                font-weight: 500;
            }}
            .available {{
                background: #d4edda;
                color: #155724;
            }}
            .missing {{
                background: #fff3cd;
                color: #856404;
            }}
            .endpoints {{
                display: grid;
                gap: 10px;
            }}
            .endpoint {{
                background: white;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #e9ecef;
            }}
            .endpoint code {{
                background: #e9ecef;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 0.9em;
            }}
            a {{
                color: #667eea;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .tools {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 15px;
            }}
            .tool {{
                background: #667eea;
                color: white;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 0.85em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ML Pipeline CI/CD Demo</h1>
            <p class="subtitle">Continuous Integration and Deployment for Machine Learning</p>
            
            <div class="section">
                <h2>Project Status</h2>
                <div class="status">
                    <span>Model (SVM)</span>
                    <span class="badge {'available' if model_exists else 'missing'}">{status_model}</span>
                </div>
                <div class="status">
                    <span>Training Data</span>
                    <span class="badge {'available' if data_exists else 'missing'}">{status_data}</span>
                </div>
            </div>
            
            <div class="section">
                <h2>API Endpoints</h2>
                <div class="endpoints">
                    <div class="endpoint">
                        <code>GET /</code> - This page
                    </div>
                    <div class="endpoint">
                        <code>GET /health</code> - Health check endpoint
                    </div>
                    <div class="endpoint">
                        <code>GET /docs</code> - <a href="/docs">Interactive API documentation</a>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>Tools Used</h2>
                <div class="tools">
                    <span class="tool">DVC</span>
                    <span class="tool">CML</span>
                    <span class="tool">MLEM</span>
                    <span class="tool">FastAPI</span>
                    <span class="tool">scikit-learn</span>
                </div>
            </div>
            
            <div class="section">
                <h2>Quick Start</h2>
                <p>To pull the model and data from remote storage:</p>
                <pre style="background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 8px; overflow-x: auto;">dvc pull -r read</pre>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model_available": os.path.exists("model/svm"),
        "data_available": os.path.exists("data/raw")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
