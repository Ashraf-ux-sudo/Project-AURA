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
            "name": "AURA",
            "version": "1.0",
            "status": "active",
            "user_name": ""
        }  
       
       

if memory["user_name"] == "":
    memory["user_name"] = input("Enter your name: ")
save_memory(memory)


memory = load_memory()

print(f"AURA Name: {memory['name']}\nAURA Version: {memory['version']}\nAURA Status: {memory['status']}\nUser: {memory['user_name']}")    




    