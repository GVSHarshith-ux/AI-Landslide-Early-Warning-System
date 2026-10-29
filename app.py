from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AI-Based Real-Time Landslide Early Warning System")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Landslide Early Warning & GIS Defense Platform</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            body { background-color: #0b0f19; color: #e2e8f0; display: flex; height: 100vh; overflow: hidden; }
            
            /* Sidebar */
            .sidebar { width: 280px; background: #111827; border-right: 1px solid #1f2937; display: flex; flex-direction: column; }
            .logo-container { padding: 20px; border-bottom: 1px solid #1f2937; }
            .logo-title { font-size: 16px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px; }
            .sub-title { font-size: 11px; color: #94a3b8; margin-top: 4px; }
            
            .nav-list { list-style: none; padding: 15px 10px; flex-grow: 1; }
            .nav-item { padding: 12px 16px; margin-bottom: 6px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-size: 14px; font-weight: 500; transition: all 0.2s; }
            .nav-item:hover, .nav-item.active { background: #1e293b; color: #38bdf8; border-left: 4px solid #38bdf8; }
            
            .user-info { padding: 15px; border-top: 1px solid #1f2937; font-size: 12px; color: #64748b; }
            .user-info span { color: #f3f4f6; font-weight: 600; display: block; margin-top: 2px; }

            /* Main Content Container */
            .main-content { flex-grow: 1; padding: 24px; overflow-y: auto; background: #0b0f19; }
            .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
            .page-title { font-size: 22px; font-weight: 700; color: #f8fafc; }
            .badge { background: #0284c7; color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
            .badge-danger { background: #dc2626; }
            
            /* Grid & Cards */
            .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
            .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 20px; }
            .card-title { font-size: 12px; color: #94a3b8; font-weight: 600; text-transform: uppercase; }
            .card-value { font-size: 26px; font-weight: 700; color: #f8fafc; margin-top: 8px; }
            
            /* GIS Map Simulation Container */
            .map-box { height: 380px; background: #151e2e; border: 1px solid #334155; border-radius: 12px; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center; }
            .map-overlay { position: absolute; top: 15px; left: 15px; background: rgba(15, 23, 42, 0.85); padding: 12px 16px; border-radius: 8px; border: 1px solid #334155; font-size: 13px; }
            
            /* Table Styling */
            table { width: 100%; border-collapse: collapse; margin-top: 15px; }
            th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid #334155; font-size: 13px; }
            th { background: #0f172a; color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 11px; }
            tr:hover { background: #1e293b; }
            
            /* Chat Interface */
            .chat-container { height: 420px; display: flex; flex-direction: column; background: #1e293b; border: 1px solid #334155; border-radius: 12px; }
            .chat-messages { flex-grow: 1; padding: 20px; overflow-y: auto; }
            .message { margin-bottom: 15px; padding: 12px 16px; border-radius: 8px; max-width: 80%; font-size: 13px; }
            .msg-user { background: #0284c7; color: white; margin-left: auto; }
            .msg-ai { background: #0f172a; border: 1px solid #334155; color: #e2e8f0; }
            .chat-input { display: flex; padding: 15px; border-top: 1px solid #334155; }
            .chat-input input { flex-grow: 1; background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 10px; color: white; outline: none; }
            .chat-input button { background: #0284c7; color: white; border: none; padding: 10px 20px; margin-left: 10px; border-radius: 6px; cursor: pointer; font-weight: 600; }

            /* Modal Popup */
            .modal-backdrop { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); justify-content: center; align-items: center; z-index: 100; }
            .modal { background: #1e293b; border: 1px solid #334155; border-radius: 12px; width: 550px; padding: 24px; }
            .tab-content { display: none; }
            .tab-content.active { display: block; }
        </style>
    </head>
    <body>

        <!-- Sidebar Navigation -->
        <div class="sidebar">
            <div class="logo-container">
                <div class="logo-title">Landslide AI SOC</div>
                <div class="sub-title">Early Warning System (R24 Regulation)</div>
            </div>
            <ul class="nav-list">
                <li class="nav-item active" onclick="switchTab('tab-51', this)">5.1 Web Application Portal</li>
                <li class="nav-item" onclick="switchTab('tab-52', this)">5.2 GIS Dashboard Overview</li>
                <li class="nav-item" onclick="switchTab('tab-53', this)">5.3 Heavy Rainfall Trigger</li>
                <li class="nav-item" onclick="switchTab('tab-54', this)">5.4 Soil Moisture Anomaly</li>
                <li class="nav-item" onclick="switchTab('tab-55', this)">5.5 Incident Containment</li>
                <li class="nav-item" onclick="switchTab('tab-56', this)">5.6 AI SecOps Chatbot</li>
                <li class="nav-item" onclick="switchTab('tab-57', this)">5.7 Analytics & PDF Report</li>
                <li class="nav-item" onclick="switchTab('tab-58', this)">5.8 Audit Logs & Inspector</li>
            </ul>
            <div class="user-info">
                Logged in as:
                <span>G. V. S. Harshith (2411CS040051)</span>
            </div>
        </div>

        <!-- Main Workspace -->
        <div class="main-content">

            <!-- 5.1 Public Web Portal -->
            <div id="tab-51" class="tab-content active">
                <div class="top-bar">
                    <div class="page-title">Citizen Public Hazard Portal</div>
                    <span class="badge">Live Public Node</span>
                </div>
                <div class="card" style="margin-bottom: 20px;">
                    <h3>Search High-Risk Slopes & Hilly Regions</h3>
                    <p style="color: #94a3b8; font-size: 13px; margin: 10px 0;">Enter District, Sector ID, or Highway stretch to check real-time stability parameters.</p>
                    <input type="text" placeholder="Search Sector (e.g. Sector 04 - Western Ghats Highway)..." style="width: 100%; padding: 12px; background: #0f172a; border: 1px solid #334155; border-radius: 6px; color: white;">
                </div>
                <div class="map-box">
                    <div class="map-overlay">
                        <b>Regional Hazard Map View</b><br>
                        Active Zones Monitored: 24 | Normal Status
                    </div>
                    <div style="text-align: center; color: #64748b;">
                        <svg width="64" height="64" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                        <p style="margin-top: 10px; font-weight: 600;">Interactive GIS Terrain Topography View Layer</p>
                    </div>
                </div>
            </div>

            <!-- 5.2 GIS Dashboard Overview -->
            <div id="tab-52" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">GIS Early Warning Command Dashboard</div>
                    <span class="badge">Telemetry Ingestion Active</span>
                </div>
                <div class="grid">
                    <div class="card"><div class="card-title">IoT Nodes Active</div><div class="card-value">128 / 128</div></div>
                    <div class="card"><div class="card-title">Telemetry Ingested</div><div class="card-value">42,850</div></div>
                    <div class="card"><div class="card-title">Model Status</div><div class="card-value" style="color:#10b981;">CNN-LSTM Live</div></div>
                    <div class="card"><div class="card-title">Active Risk Flag</div><div class="card-value">0 Flags</div></div>
                </div>
                <div class="map-box">
                    <div class="map-overlay"><b>Multi-Sensor GIS Overlay</b><br>Rainfall + Soil VWC % + Satellite DEM</div>
                    <p style="color: #38bdf8; font-weight: 600;">[ All Slope Sectors Normal (Green Status) ]</p>
                </div>
            </div>

            <!-- 5.3 Heavy Rainfall Trigger -->
            <div id="tab-53" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">Sensor Threshold Breach Simulation</div>
                    <span class="badge badge-danger">CRITICAL THRESHOLD BREACH</span>
                </div>
                <div class="card" style="border: 2px solid #ef4444; background: rgba(239, 68, 68, 0.1); margin-bottom: 20px;">
                    <h3 style="color: #ef4444;">[ALERT] Heavy Rainfall Anomaly Detected in Sector 04</h3>
                    <p style="font-size: 13px; margin-top: 5px;">Precipitation Rate: <b>85.4 mm/h</b> (Threshold: > 50 mm/h) | Predicted Risk Score: <b>94 / 100</b></p>
                </div>
                <div class="grid">
                    <div class="card"><div class="card-title">Trigger Sensor</div><div class="card-value">Rain Gauge #04</div></div>
                    <div class="card"><div class="card-title">Cumulative Rain</div><div class="card-value" style="color:#ef4444;">124.5 mm</div></div>
                    <div class="card"><div class="card-title">Slope Displacement</div><div class="card-value" style="color:#f59e0b;">+3.2 mm</div></div>
                    <div class="card"><div class="card-title">Risk Level</div><div class="card-value" style="color:#ef4444;">CRITICAL</div></div>
                </div>
            </div>

            <!-- 5.4 Soil Moisture Anomaly -->
            <div id="tab-54" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">Pore-Water Pressure & Soil Saturation Anomaly</div>
                    <span class="badge badge-danger">VOLUMETRIC WATER BREACH</span>
                </div>
                <div class="card" style="margin-bottom: 20px;">
                    <h3>Soil Moisture Content (VWC %) Sensor Stream</h3>
                    <p style="color: #94a3b8; font-size: 13px;">Volumetric Water Content spiked from 18% to <b>48.2% VWC</b> within 15 minutes.</p>
                    <div style="height: 120px; background: #0f172a; border-radius: 8px; margin-top: 15px; display: flex; align-items: flex-end; padding: 10px; gap: 8px;">
                        <div style="height: 20%; width: 10%; background: #38bdf8;"></div>
                        <div style="height: 25%; width: 10%; background: #38bdf8;"></div>
                        <div style="height: 30%; width: 10%; background: #38bdf8;"></div>
                        <div style="height: 40%; width: 10%; background: #38bdf8;"></div>
                        <div style="height: 95%; width: 10%; background: #ef4444;"></div>
                        <div style="height: 98%; width: 10%; background: #ef4444;"></div>
                    </div>
                </div>
            </div>

            <!-- 5.5 Incident Containment -->
            <div id="tab-55" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">Incident Containment & Action Control</div>
                    <span class="badge">Mitigation Active</span>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Incident ID</th>
                            <th>Target Sector</th>
                            <th>Trigger Type</th>
                            <th>Severity Risk</th>
                            <th>Automated Response</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>INC-20261005-LS01</td>
                            <td>Sector 04 (Highway Slope)</td>
                            <td>Rainfall + Saturation</td>
                            <td><span style="color:#ef4444; font-weight:700;">CRITICAL (94%)</span></td>
                            <td>Multi-lingual SMS & App Push Broadcast Delivered</td>
                            <td><button style="background:#dc2626; color:white; border:none; padding:6px 12px; border-radius:4px; cursor:pointer;" onclick="this.innerText='Acknowledged'">Acknowledge</button></td>
                        </tr>
                        <tr>
                            <td>INC-20261005-LS02</td>
                            <td>Sector 02 (Hill Road)</td>
                            <td>Tilt Anomaly Shift</td>
                            <td><span style="color:#f59e0b; font-weight:700;">HIGH (78%)</span></td>
                            <td>District Authority Alert Sent</td>
                            <td><button style="background:#0284c7; color:white; border:none; padding:6px 12px; border-radius:4px; cursor:pointer;" onclick="this.innerText='Clear Alert'">Clear Alert</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 5.6 AI Chatbot -->
            <div id="tab-56" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">AI SecOps Natural Language Assistant</div>
                    <span class="badge">LLM Agent Online</span>
                </div>
                <div class="chat-container">
                    <div class="chat-messages">
                        <div class="message msg-user">Tell me about the recent risk assessment for Sector 04 highway slope.</div>
                        <div class="message msg-ai">
                            <b>AI Landslide Assistant Forensics:</b><br>
                            • <b>Sector ID:</b> Sector 04 Highway Slope<br>
                            • <b>Risk Status:</b> CRITICAL (94/100)<br>
                            • <b>Triggering Factor:</b> Intense rainfall burst (85.4 mm/h) combined with 48.2% Soil VWC.<br>
                            • <b>LSTM Time-to-Failure Prediction:</b> ~2.5 Hours if saturation continues.<br>
                            • <b>Recommended Action:</b> Issue immediate automated SMS traffic advisories to divert vehicles from Sector 04 highway corridor.
                        </div>
                    </div>
                    <div class="chat-input">
                        <input type="text" value="Explain recent soil moisture anomaly patterns..." readonly>
                        <button>Send</button>
                    </div>
                </div>
            </div>

            <!-- 5.7 Analytics & PDF Report -->
            <div id="tab-57" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">Security Analytics & PDF Report Generator</div>
                    <button style="background:#10b981; color:white; border:none; padding:10px 18px; border-radius:6px; font-weight:600; cursor:pointer;" onclick="alert('Downloading Landslide_Risk_Audit_Report.pdf')">Download Comprehensive PDF Report</button>
                </div>
                <div class="card" style="margin-bottom: 20px;">
                    <h3>7-Day Telemetry vs Landslide Risk Velocity Timeline</h3>
                    <div style="height: 150px; background: #0f172a; border-radius: 8px; margin-top: 15px; display: flex; align-items: flex-end; padding: 15px; justify-content: space-around;">
                        <div style="height: 20%; width: 40px; background: #0284c7; text-align: center; font-size: 10px; color: white;">Mon</div>
                        <div style="height: 30%; width: 40px; background: #0284c7; text-align: center; font-size: 10px; color: white;">Tue</div>
                        <div style="height: 25%; width: 40px; background: #0284c7; text-align: center; font-size: 10px; color: white;">Wed</div>
                        <div style="height: 40%; width: 40px; background: #0284c7; text-align: center; font-size: 10px; color: white;">Thu</div>
                        <div style="height: 85%; width: 40px; background: #ef4444; text-align: center; font-size: 10px; color: white;">Fri</div>
                        <div style="height: 95%; width: 40px; background: #ef4444; text-align: center; font-size: 10px; color: white;">Today</div>
                    </div>
                </div>
            </div>

            <!-- 5.8 Audit Logs & Inspector Modal -->
            <div id="tab-58" class="tab-content">
                <div class="top-bar">
                    <div class="page-title">Real-Time Telemetry Audit Stream</div>
                    <button style="background:#0284c7; color:white; border:none; padding:8px 14px; border-radius:6px;" onclick="document.getElementById('modal').style.display='flex'">Inspect Selected Evidence Log</button>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>Source Node</th>
                            <th>Sensor Endpoint</th>
                            <th>Value Payload</th>
                            <th>Anomaly Classification</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>2026-10-13 13:45:12</td>
                            <td>IoT-Node-04</td>
                            <td>/api/telemetry/rainfall</td>
                            <td>85.4 mm/h</td>
                            <td><span style="color:#ef4444;">CRITICAL BREACH</span></td>
                        </tr>
                        <tr>
                            <td>2026-10-13 13:45:10</td>
                            <td>IoT-Node-04</td>
                            <td>/api/telemetry/soil-vwc</td>
                            <td>48.2 % VWC</td>
                            <td><span style="color:#ef4444;">ANOMALOUS SPIKE</span></td>
                        </tr>
                        <tr>
                            <td>2026-10-13 13:44:00</td>
                            <td>Citizen App</td>
                            <td>/api/reports/photo-evidence</td>
                            <td>Slope Crack Image (Geo-tagged)</td>
                            <td><span style="color:#f59e0b;">EVIDENCE ATTACHED</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>

        <!-- Forensic Modal Popup -->
        <div id="modal" class="modal-backdrop">
            <div class="modal">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                    <h3>Geo-Tagged Field Forensics & Evidence Inspector</h3>
                    <span style="cursor:pointer; font-weight:bold;" onclick="document.getElementById('modal').style.display='none'">✕</span>
                </div>
                <p style="font-size:13px; color:#94a3b8; margin-bottom:10px;">Submitted by Official / Citizen Field App</p>
                <div style="background:#0f172a; padding:15px; border-radius:8px; font-size:12px; font-family:monospace; color:#38bdf8;">
                    Source Node: Citizen Field Report #2411CS040051<br>
                    Coordinates: Lat 17.5449° N, Long 78.4832° E<br>
                    Elevation: 542m above MSL<br>
                    Field Observation: Longitudinal tension crack observed on road embankment following heavy rain.<br>
                    AI Spatial Anomaly Score: HIGH (88/100)
                </div>
            </div>
        </div>

        <script>
            function switchTab(tabId, element) {
                document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
                document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
                document.getElementById(tabId).classList.add('active');
                element.classList.add('active');
            }
        </script>
    </body>
    </html>
    """