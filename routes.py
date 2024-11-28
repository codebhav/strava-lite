from flask_restful import Api
from constants import *
from api import *

BASE_USER_ROUTE = "/user"
USER_ID_ROUTE = f"{BASE_USER_ROUTE}/<string:user_id>"
USERS_ROUTE = "/users"
WORKOUTS_ROUTE = "/workouts/<string:user_id>"
FOLLOW_ROUTE = "/follow-list/<string:user_id>"
FRIEND_WORKOUTS_ROUTE = "/follow-list/<string:user_id>/<string:follow_id>"

ROUTES = {
    REGISTER_USER: BASE_USER_ROUTE,
    GET_USER: USER_ID_ROUTE,
    REMOVE_USER: USER_ID_ROUTE,
    LIST_USERS: USERS_ROUTE,
    ADD_WORKOUT: WORKOUTS_ROUTE,
    LIST_WORKOUTS: WORKOUTS_ROUTE,
    FOLLOW_FRIEND: FOLLOW_ROUTE,
    SHOW_FRIEND_WORKOUTS: FRIEND_WORKOUTS_ROUTE
}


METHODS = {
    REGISTER_USER: POST,
    GET_USER: GET,
    REMOVE_USER: DELETE,
    LIST_USERS: GET,
    ADD_WORKOUT: PUT,
    LIST_WORKOUTS: GET,
    FOLLOW_FRIEND: PUT,
    SHOW_FRIEND_WORKOUTS: GET 
}


RESOURCES = {
    REGISTER_USER: RegisterUser,
    GET_USER: GetUser,
    REMOVE_USER: RemoveUser,
    LIST_USERS: ListUsers,
    ADD_WORKOUT: AddWorkout,
    LIST_WORKOUTS: ListWorkouts,
    FOLLOW_FRIEND: FollowFriend,
    SHOW_FRIEND_WORKOUTS: ShowFriendWorkouts
}

def init_routes(api: Api) -> None:
    for [api_name, resource] in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])
