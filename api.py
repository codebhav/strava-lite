from flask_restful import Resource, reqparse
from uuid import uuid4 as generateID

users = {}

register_user_parser = (reqparse.RequestParser()
                        .add_argument("name", type=str, required=True)
                        .add_argument("age", type=int, required=False)
                        )


class RegisterUser(Resource):
    def post(self):
        name, age = register_user_parser.parse_args().values()
        id = str(generateID())
        users[id] = {
            "id": id,
            "name": name,
            "age": age,
            "workouts": [],
            "following": set()
        }
        return {
            "id": id,
            "name": name,
            "age": age,
        }, 200


class GetUser(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"message": "User not found"}, 404
        return {
            "id": user["id"],
            "name": user["name"],
            "age": user["age"],
        }, 200


class RemoveUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {}, 200
        return {"message": "User not found"}, 404


class ListUsers(Resource):
    def get(self):
        return {
            "users": [
                {
                    "id": user["id"],
                    "name": user["name"],
                    "age": user["age"]
                } for user in users.values()]
        }, 200

add_workout_parser = (reqparse.RequestParser()
    .add_argument("date", type=str, required=True)
    .add_argument("time", type=str, required=True)
    .add_argument("distance", type=str, required=True)
)

class AddWorkout(Resource):
    def put(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        
        date, time, distance = add_workout_parser.parse_args().values()
        workout = {
            "date": date,
            "distance": distance,
            "time": time,
        }
        users[user_id]["workouts"].append(workout)
        return workout, 200

class ListWorkouts(Resource):
    def get(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        return {"workouts": users[user_id]["workouts"]}, 200

follow_friend_parser = (reqparse.RequestParser()
    .add_argument("follow_id", type=str, required=True)
)

class FollowFriend(Resource):
    def put(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
    
        follow_id = follow_friend_parser.parse_args()["follow_id"]
    
        if follow_id not in users:
            return {"message": "User to follow not found"}, 404
    
        users[user_id]["following"].add(follow_id)
        return {"following": list(users[user_id]["following"])}, 200


class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        if user_id not in users or follow_id not in users:
            return {"message": "User not found"}, 404

        if follow_id not in users[user_id]["following"]:
            return {"message": "Not following this user"}, 403

        return {"workouts": users[follow_id]["workouts"]}, 200
