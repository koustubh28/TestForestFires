# Forest Fires Prediction Web Application

A complete end-to-end Machine Learning web application that predicts the burned area of forest fires based on meteorological data. The application is built using **Python**, **Flask**, and deployed on **Render**.

## 🚀 Live Demo
*https://testforestfires-zegj.onrender.com/predictdata*

---

## 🛠️ Tech Stack & Architecture

*   **Frontend:** HTML5, CSS3 (Clean, responsive user interface)
*   **Backend Framework:** Flask (Python)
*   **Machine Learning:** Jupyter Notebooks for EDA, Feature Engineering, and Model Training (Regression/Classification models)
*   **Deployment & Cloud:** Render (`.ebextensions` configured for automated environment provisioning)

---

## 📁 Repository Structure

*   `application.py` — The core Flask application entry point.
*   `.ebextensions/` — Configuration files for deployment.
*   `models/` — Serialized, trained Machine Learning models ready for production inference.
*   `notebooks/` — Jupyter Notebooks detailing the Data Analysis, Visualization, and Model Development lifecycle.
*   `templates/` — HTML templates rendering the web application UI.
*   `requirements.txt` — Managed Python package dependencies.

---

## ⚙️ Local Setup & Installation

Follow these steps to run the web application locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/koustubh28/TestForestFires.git](https://github.com/koustubh28/TestForestFires.git)
   cd TestForestFires
