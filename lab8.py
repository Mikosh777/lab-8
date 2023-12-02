import requests
import random


# 1.1: GET Request
post_id = 1 
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{post_id}")

if response.status_code >= 400:
    print(f"Error: {response.status_code} - {response.text}")
else:
    print("Response content:")
    print(response.json())

# 1.2: Create a ToDo class
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# 1.3: Create a new object of class ToDo
new_todo = ToDo(userId=1, id=post_id, title="Sample Title", completed=False)

# 1.4: POST Request
new_todo_payload = {
    "userId": new_todo.userId,
    "id": new_todo.id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo_payload)

if post_response.status_code >= 400:
    print(f"Error: {post_response.status_code} - {post_response.text}")
else:
    print("Post Response content:")
    print(post_response.json())

# 1.5: Edit some data of your attributes of your todo item
new_todo.title = "Updated Title"

# 1.6: PUT Request
put_payload = {
    "userId": new_todo.userId,
    "id": new_todo.id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

chosen_id = 2  
put_response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{chosen_id}", json=put_payload)

if put_response.status_code >= 400:
    print(f"Error: {put_response.status_code} - {put_response.text}")
else:
    print("Put Response content:")
    print(put_response.json())


                    #Task 2
                    
# Task 2.1: Random Character Request
random_character_id = random.randint(1, 826)
character_response = requests.get(f"https://rickandmortyapi.com/api/character/{random_character_id}")

if character_response.status_code == 200:
    random_character_data = character_response.json()
    print("Random Character JSON response:")
    print(random_character_data)
else:
    print(f"Failed to fetch character with ID: {random_character_id}")

# Task 2.2: Response Output
if random_character_data:
    print("Keys in the JSON structure:")
    print(random_character_data.keys())

# Task 2.3: Save to File
if random_character_data:
    with open(f"info_character_{random_character_id}.json", "w") as file:
        file.write(str(random_character_data))

# Task 2.4: Episode List
if random_character_data:
    episode_urls = random_character_data.get("episode", [])
    episode_ids = [url.split("/")[-1] for url in episode_urls]
    with open(f"all_episodes_with_character_{random_character_id}.txt", "a") as file:
        for episode_id in episode_ids:
            file.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")

# Task 2.5: Episode Response Structure
episode_1_response = requests.get("https://rickandmortyapi.com/api/episode/1")
if episode_1_response.status_code == 200:
    episode_1_data = episode_1_response.json()
    print("Episode 1 Response Structure:")
    print(episode_1_data)
else:
    print("Failed to fetch episode 1 data")

# Task 2.6: Episode Class Creation
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url

    def get_episode_info(self):
        return f"Episode {self.episode}: {self.name} - Air date: {self.air_date}"

# Task 2.7: Episode Data Retrieval
episodes_data = []
for episode_id in episode_ids:
    episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    if episode_response.status_code == 200:
        episode_data = episode_response.json()
        episode = Episode(
            id=episode_data['id'],
            name=episode_data['name'],
            air_date=episode_data['air_date'],
            episode=episode_data['episode'],
            characters=episode_data['characters'],
            url=episode_data['url']
        )
        episodes_data.append(episode)
    else:
        print(f"Failed to fetch episode with ID: {episode_id}")

# Task 2.8: Class Methods
for episode in episodes_data:
    print(episode.get_episode_info())

# Task 2.9: Character Response Structure
character_1_response = requests.get("https://rickandmortyapi.com/api/character/1")
if character_1_response.status_code == 200:
    character_1_data = character_1_response.json()
    print("Character 1 Response Structure:")
    print(character_1_data)
else:
    print("Failed to fetch character 1 data")

# Task 2.10: Character Class Creation
class Character:
    def __init__(self, id, name, status, species, gender, origin, location, image, episode_urls):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode_urls = episode_urls

    def get_character_info(self):
        return f"{self.name} - {self.status} - Species: {self.species} - Gender: {self.gender}"

# Task 2.11: Character Object Creation
if character_1_data:
    character_1 = Character(
        id=character_1_data['id'],
        name=character_1_data['name'],
        status=character_1_data['status'],
        species=character_1_data['species'],
        gender=character_1_data['gender'],
        origin=character_1_data['origin'],
        location=character_1_data['location'],
        image=character_1_data['image'],
        episode_urls=character_1_data['episode']
    )

# Task 2.12: Character Class Methods
if character_1:
    print(character_1.get_character_info())
