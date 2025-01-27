import os

import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_chat_message(message,agent_id, user_id="harshit@lyzr.ai", api_key=os.getenv("LYZR_KEY")):
    session_id = "123"
    url = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    payload = {
        "user_id": user_id,
        "agent_id": agent_id,
        "session_id": session_id,
        "message": message
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    message = "A services company who is a pega systems partner and based in Malaysia with <200 employees"
    response = send_chat_message(message, "67910862095151a92a1fd78e")
    print(response)
