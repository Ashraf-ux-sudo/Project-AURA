import json

   
def load_memory(filename="aura_memory.json"):
    try:
        with open(filename, "r") as file:
            memory = json.load(file)
        return memory
    except FileNotFoundError:
        return {
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


def save_memory(memory):
    with open("aura_memory.json", "w") as file:
        json.dump(memory, file, indent=4)
def main():
    memory = load_memory()

    if memory["user"]["name"] == "":
        memory["user"]["name"] = input("Enter your name: ")
        save_memory(memory)
    if memory["user"]["favourite_language"] == "":
        memory["user"]["favourite_language"] = input("Enter your favourite programming language: ")
        save_memory(memory)

    print(f"AURA Name: {memory['aura']['name']}\nAURA Version: {memory['aura']['version']}\nAURA Status: {memory['aura']['status']}\nUser: {memory['user']['name']}\nFavourite Language: {memory['user']['favourite_language']}")
if __name__ == "__main__":
    main()