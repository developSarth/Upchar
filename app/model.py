from fastapi import FastAPI, APIRouter
import requests
router = APIRouter()

GRADIO_URL = "https://21bb33197abeb1410f.gradio.live"

@router.post("/ask")
def ask_agent(payload: dict):
    user_query = payload["query"]

    # Send request to Gradio API
    gradio_payload = {
        "data": [user_query]   # depends on Gradio input structure
    }

    response = requests.post(GRADIO_URL, json=gradio_payload)
    gradio_output = response.json()

    # Extract the model output
    output_text = gradio_output["data"][0]

    return {"response": output_text}