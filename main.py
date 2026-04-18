from fastapi import FastAPI

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "AI CRM System is running"}

# Log interaction (dummy)
@app.post("/log")
def log_interaction():
    return {"status": "Interaction logged successfully"}

# Get interactions (dummy data)
@app.get("/interactions")
def get_interactions():
    data = [
        {
            "id": 1,
            "doctor_name": "Dr Sharma",
            "notes": "Discussed diabetes medicine",
            "summary": "Doctor showed interest"
        }
    ]
    return {"data": data}
