# Forecast + Alerting Pipeline (Intern Assessment – Logic Leap AI)

## 📁 Project Structure
logic_leap_project/
├── notebooks/ # EDA, feature exploration, modeling, anomaly
│ ├── eda.ipynb
│ ├── feature_engineering.ipynb
│ ├── forecasting.ipynb
│ └── anomaly_detection.ipynb
├── src/ # Clean, reproducible logic
│ ├── loader.py
│ ├── features.py
│ ├── models.py
│ └── anomaly.py
├── app/ # CLI interface using Typer
│ └── main.py
├── outputs/ # Generated outputs
│ ├── forecast_units_produced_S1.csv
│ ├── forecast_power_kwh_S1.csv
│ └── alerts.csv
├── requirements.txt


## 🚀 How to Run

### ⚙️ Install Dependencies
```bash
pip install -r requirements.txt

🧠 Run Forecast
python app/main.py forecast --site-id S1 --target units_produced
python app/main.py forecast --site-id S1 --target power_kwh

⚠️ Run Anomaly Detection
python app/main.py anomalies

