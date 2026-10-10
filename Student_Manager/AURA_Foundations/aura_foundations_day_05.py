import json
import os

def load_memory():
    with open("aura_memory.json", "r") as file:
        memory = json.load(file)
    return memory  

def save_memory(memory):
    with open("aura_memory.json", "w") as file:
        json.dump(memory, file, indent=4)

if os.path.exists("aura_memory.json"):
    memory = load_memory()
else:
    memory = {
        "aura": {
            "name": "AURA",
            "version": "1.0",
            "status": "learning"
        },
        "user": {
            "name": "",
            "favourite_language": ""
        }
    }

if memory["user"]["name"] == "":
    memory["user"]["name"] = input("Enter your name: ")
    save_memory(memory)
if memory["user"]["favourite_language"] == "":
    memory["user"]["favourite_language"] = input("Enter your favourite programming language: ")
    save_memory(memory)

print(f"AURA Name: {memory['aura']['name']}\nAURA Version: {memory['aura']['version']}\nAURA Status: {memory['aura']['status']}\nUser: {memory['user']['name']}\nFavourite Language: {memory['user']['favourite_language']}")