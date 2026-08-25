import requests

pokemon = "Charizard"

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}") 

if response.status_code == 200:
    json_file = response.json()
    print(f"Name : {json_file["name"]}")
    print(f"ID   : {json_file["id"]}")

    for stat in json_file["stats"]:
        stat_name = stat["stat"]["name"]
        base_stat = stat["base_stat"]
        print(f"{stat_name}: {base_stat}")
    
else:
    print(f"{pokemon} pokemon not found 😥")


    
