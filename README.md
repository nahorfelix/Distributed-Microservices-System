[![CI/CD Pipeline](https://github.com/nahorfelix/Distributed-Microservices-System/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/nahorfelix/Distributed-Microservices-System/actions)
##   T&T Group Enterprise Suite
A distributed system designed to manage employee check-ins and check-outs with a focus on high performance and security.
##   🚀 Key Engineering Features
Microservices Architecture: Decoupled services for Authentication and Attendance tracking.
Stateless Security: Implemented JWT (JSON Web Tokens) for secure, distributed authorization.
Polyglot Backend: * Auth Service: Built with Flask for robust identity management.
Attendance Service: Built with FastAPI for high-concurrency, asynchronous performance.
Cross-Origin Communication: Securely integrated via CORS policies.
##   🛠️ Tech Stack
Frontend: React (State Management & Hooks)
Backend: Python (FastAPI, Flask)
Database: SQLite (Relational Storage)
DevOps: GitHub Actions (CI/CD Pipeline)

##    How to Run
1. **Clone the repo:** `git clone https://github.com/nahorfelix/Distributed-Microservices-System.git`
2. **Start Auth Service:** - `cd auth-service`
   - `pip install -r requirements.txt`
   - `python app.py`
3. **Start Attendance Service:**
   - `cd attendance-service`
   - `pip install -r requirements.txt`
   - `python -m uvicorn main:app --port 5002`
4. **View Dashboard:** Open `dashboard-ui/index.html` in your browser.
