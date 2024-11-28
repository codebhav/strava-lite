# Strava Lite

## Project Info

**Project Link:** https://github.com/codebhav/strava-lite

**Name:** Vaibhav Achuthananda  
**Email:** vachutha@stevens.edu

**Project Title:** Strava Lite
**Project Description:** Strava Lite is a Flask-based RESTful API service that allows users to track their running workouts. Users can create accounts, log their runs with details like date, time, and distance, and view their workout history. The application also includes social features where users can follow other runners and view their workouts.

## Resolved Issues

1. For the longest time I was struggling with finding a way to loop users for `ListUsers` inside the `return` statement. After serving my time on StackOverflow I figured out I could add the for loop at the end of the dictionary inside the array itself. Bingo!
2. I was trying to parse follow-id like usual `follow_id = follow_friend_parser.parse_args().values()` which would return a dict_values object. But it worked fine after I changed it to `follow_id = follow_friend_parser.parse_args()["follow_id"]` to get the actual string value.
3. Other bugs were pretty minor, it was mostly me forgetting to add a slash before the url in `routes.py` or spelling something incorrectly. Nevertheless, there are no more bugs in the project to the best of my knowledge.
