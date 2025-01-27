from fastapi import FastAPI
from agents import send_chat_message
from apollo import search_companies
import json

app = FastAPI()

@app.get("/filtered-orgs")
def get_filtered_orgs(message: str):
    cpr = send_chat_message(message, "67910862095151a92a1fd78e")
    print("cpr done")
    cpr_json = send_chat_message(cpr, "679131c6095151a92a1fded1")
    print("cpr_json done")
    cpr_json_to_dict = send_chat_message(cpr_json, "679223a809418e2c4c0350ac")
    print("cpr_json_to_dict done")
    refined_data = json.loads(cpr_json_to_dict)
    print("refined_data done")
    data = search_companies(refined_data)
    print(data)
    filtered_orgs = []
    for org in data:
        if org.get('website_url') and org.get('linkedin_url'):
            filtered_org = {
                'name': org['name'],
                'website_url': org['website_url'],
                'linkedin_url': org['linkedin_url']
            }
            filtered_orgs.append(filtered_org)
    return filtered_orgs
