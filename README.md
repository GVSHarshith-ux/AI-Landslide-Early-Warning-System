# AI-Based Real-Time Landslide Early Warning System

An intelligent GIS platform designed to ingest real-time IoT ground telemetry (tipping bucket rainfall, volumetric soil water content VWC %, MPU6050 tilt/vibration) and Copernicus DEM satellite rasters to forecast micro-sector landslide hazards using hybrid spatial-temporal deep learning (2D ResNet-CNN + BiLSTM).

---

## Project & Developer Metadata

- **Author:** G. V. S. Harshith
- **Roll Number:** `2411CS040051`
- **Email:** `gvsharshith28@gmail.com`
- **GitHub Handle:** [@GVSHarshith-ux](https://github.com/GVSHarshith-ux)
- **Class:** B.Tech III Year — Cyber Security Alpha (Academic Year 2026–2027)
- **Faculty Project Supervisor:** Dr. G. Anand Kumar (Dean-CS, IOT, ECE)
- **Institution:** Department of Cyber Security, Malla Reddy University, Hyderabad, India

---

## Core System Capabilities

1. **Multi-Sensor Telemetry Ingestion:** Continuous 15-second IoT streams collecting rainfall rates, soil moisture VWC %, and structural slope tilt.
2. **Hybrid Spatial-Temporal Deep Learning:**
   - **2D ResNet-CNN:** Extracts geomorphological slope terrain embeddings from satellite DEM rasters.
   - **BiLSTM Sequence Model:** Processes 72-hour historical water saturation vectors to compute hazard failure probability.
3. **Sub-15s Emergency Dispatch:** Triggers automated SMS (Twilio), mobile push alerts (Firebase FCM), and smartwatch notification mirroring.
4. **Interactive GIS Command Dashboard:** Features 8 test case interfaces including hazard heatmaps, pore-water anomaly graphs, incident containment, AI SecOps Chatbot, and automated PDF audit report exports.
5. **Offline Queue Sync:** Local SQLite store-and-forward queue caches citizen reports and ground telemetry during remote mountain power/cellular outages.

---

## Tech Stack & Frameworks

- **Frontend & GIS:** HTML5, CSS3, JavaScript, Leaflet.js
- **Backend Application Engine:** Python 3.10+, FastAPI, Uvicorn ASGI Server
- **AI/ML Core:** PyTorch, Scikit-learn, GeoPandas
- **Databases & Cache:** PostgreSQL / PostGIS, SQLite (Offline Edge Sync)
- **Notification Services:** Twilio API, Firebase Cloud Messaging (FCM)

---

## Quick Start (Local Execution)

```bash
# Clone repository
git clone [https://github.com/GVSHarshith-ux/AI-Landslide-Early-Warning-System.git](https://github.com/GVSHarshith-ux/AI-Landslide-Early-Warning-System.git)
cd AI-Landslide-Early-Warning-System

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch ASGI server
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
