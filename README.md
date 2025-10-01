# 📘 OriGen.AI – Backend Technical Test

## 📂 Project Structure
```
origen-ai-backend-test/
├── part_a/ # Part A: Simulation Scheduler API
│ ├── app/
│ ├── docker-compose.yml
│ ├── Dockerfile
│ └── requirements.txt
│
├── coding_test_part_b/ # Part B: Proprietary Library Obfuscator
│ ├── proprietary_lib/
│ ├── main.py
│ ├── obfuscate_proprietary_lib.py
│ └── backup_originals/
│
└── README.md

```

---

## 🚀 Part A – Simulation Scheduler API

### 🔧 Requirements
- **Python 3.11+**
- **PostgreSQL 15**
- **Docker & Docker Compose** (recommended for containerized setup)

---

### ▶️ Run Locally

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r part_a/requirements.txt

```

### ▶️ Run PostgreSQL:
```bash
docker run --name origen-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=origen \
  -p 5432:5432 -d postgres:15
```
2. Export Database URL:
```
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/origen"

```
3. Start API server:

```
cd part_a
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
### ▶️ Run with Docker Compose

```bash
cd part_a
docker compose up --build
```

### Available:
```
Swagger UI → http://localhost:8000/docs

Redoc → http://localhost:8000/redoc
```
### Endpoints

1. List Machines
```
curl -X 'GET' \
  'http://localhost:8000/api/machines' \
  -H 'accept: application/json'

  Response : 
  [
  {
    "id": 1,
    "name": "m-1.large",
    "description": "GPU machine type 1",
    "created_at": "2025-10-01T01:41:22.799174+00:00"
  },
  {
    "id": 2,
    "name": "m-2.xlarge",
    "description": "GPU machine type 2",
    "created_at": "2025-10-01T01:41:22.799485+00:00"
  },
  {
    "id": 3,
    "name": "cpu.medium",
    "description": "CPU machine example",
    "created_at": "2025-10-01T01:41:22.799602+00:00"
  }
]
```
2. Create Simulation
```
curl -X 'POST' \
  'http://localhost:8000/api/simulations' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "test-sim2",
    "machine_id": 1
}
'
Response : 
{
  "id": 4,
  "name": "test-sim2",
  "machine_id": 1,
  "status": "pending",
  "created_at": "2025-10-01T02:33:00.104622+00:00",
  "updated_at": "2025-10-01T02:33:00.104622+00:00"
}
```
3. List Simulations
```
curl -X 'GET' \
  'http://localhost:8000/api/simulations?status=pending&order_by=created_at' \
  -H 'accept: application/json'
  

Response : 
[
  {
    "id": 1,
    "name": "sim-docker",
    "machine_id": 1,
    "status": "pending",
    "created_at": "2025-10-01T01:42:20.900980+00:00",
    "updated_at": "2025-10-01T01:42:20.900980+00:00"
  },
  {
    "id": 3,
    "name": "test-sim",
    "machine_id": 1,
    "status": "pending",
    "created_at": "2025-10-01T02:01:52.092298+00:00",
    "updated_at": "2025-10-01T02:01:52.092298+00:00"
  },
  {
    "id": 4,
    "name": "test-sim2",
    "machine_id": 1,
    "status": "pending",
    "created_at": "2025-10-01T02:33:00.104622+00:00",
    "updated_at": "2025-10-01T02:33:00.104622+00:00"
  }
]

```
4. Simulation Details

```
curl -X 'GET' \
  'http://localhost:8000/api/simulations/3' \
  -H 'accept: application/json'

Response : 

{
  "id": 3,
  "name": "test-sim",
  "machine_id": 1,
  "status": "pending",
  "created_at": "2025-10-01T02:01:52.092298+00:00",
  "updated_at": "2025-10-01T02:01:52.092298+00:00",
  "convergence": []
}

```
5. Streaming Endpoint (watch convergence)
```
curl -X 'GET' \
  'http://localhost:8000/api/simulations/2/stream' \
  -H 'accept: application/json'

Response :
data: {"seconds": 10, "loss": 0.7569}

data: {"seconds": 20, "loss": 0.6663}

data: {"seconds": 30, "loss": 0.7221}

data: {"seconds": 40, "loss": 0.7301}

data: {"seconds": 50, "loss": 0.4976}

data: {"seconds": 60, "loss": 0.4918}

data: {"seconds": 70, "loss": 0.4601}

data: {"seconds": 80, "loss": 0.4747}

data: {"seconds": 90, "loss": 0.4625}

data: {"seconds": 100, "loss": 0.4805}

data: {"seconds": 110, "loss": 0.6736}

data: {"seconds": 120, "loss": 0.3494}

data: {"seconds": 130, "loss": 0.3109}

data: {"seconds": 140, "loss": 0.3571}

data: {"seconds": 150, "loss": 0.3054}

data: {"seconds": 160, "loss": 0.4909}

data: {"seconds": 170, "loss": 0.3521}

data: {"seconds": 180, "loss": 0.4897}

data: {"seconds": 190, "loss": 0.5357}

event: finished
data: {}


```


### 🔒 Part B – Proprietary Library Obfuscator

This part demonstrates creating a small proprietary_lib, obfuscating its source files and verifying the hardened package still runs unchanged main.py.

### ▶️ Run Locally
```
cd coding_test_part_b

python obfuscate_proprietary_lib.py ./proprietary_lib

```
```
Files to obfuscate:
   proprietary_lib/analysis.py
   proprietary_lib/transformations.py
Proceed to obfuscate 2 files and backup originals to: backup_originals/<timestamp>
Type 'yes' to continue:
```
### ▶️ Verify Execution
```
python main.py
```
### Expected output:
```
11.9127
```