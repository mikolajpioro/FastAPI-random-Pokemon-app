from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(id):
    url = f"{base_url}/pokemon/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "sprite": data['sprites']['other']['official-artwork']['front_default']
        }
    else:
        return "Failed"

# function call with a random id
pokemon_info = get_pokemon(random.randint(1, 1025))

if pokemon_info:
    final_info = [
    {"name": pokemon_info["name"], "id": pokemon_info["id"], "sprite": pokemon_info["sprite"]}
]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request, "final_info": final_info})