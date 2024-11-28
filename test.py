import requests
import json

BASE = "http://127.0.0.1:5000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("///////////////////")

# test for RegisterUser
print("Testing RegisterUser...")
response = requests.post(f"{BASE}/user", json={
    "name": "Vaibhav Achuthananda",
    "age": 23
})
print_response(response)
user_id = response.json()["id"]

# test for GetUser
print("Testing GetUser...")
response = requests.get(f"{BASE}/user/{user_id}")
print_response(response)

# test for AddWorkout
print("Testing AddWorkout...")
response = requests.put(f"{BASE}/workouts/{user_id}", json={
    "date": "2024-10-20",
    "time": "39:27",
    "distance": "3mi"
})
print_response(response)

# test for ListWorkouts
print("Testing ListWorkouts...")
response = requests.get(f"{BASE}/workouts/{user_id}")
print_response(response)

# test for ListUsers
print("Testing for ListUsers...")
response = requests.get(f"{BASE}/users")
print_response(response)

# adding an extra user for following
print("Testing RegisterUser AGAIN...")
response = requests.post(f"{BASE}/user", json={
    "name": "Rocco Polimeni",
    "age": 27
})
print_response(response)
second_user_id = response.json()["id"]

# test for FollowFriend
print("Testing for FollowFriend...")
response = requests.put(f"{BASE}/follow-list/{user_id}", json={
    "follow_id": second_user_id
})
print_response(response)

# test for ShowFriendWorkouts
print("Testing ShowFriendWorkouts...")
response = requests.get(f"{BASE}/follow-list/{user_id}/{second_user_id}")
print_response(response)
