# Strava Lite

## Project Description

Strava Lite is a Flask-based RESTful API service that allows users to track their running workouts. Users can create accounts, log their runs with details like date, time, and distance, and view their workout history. The application also includes social features where users can follow other runners and view their workouts.

### Key Features

- User Management (Create, Read, Update, Delete)
- Workout Tracking
- Social Following System
- Friend Workout Viewing
- RESTful API Design

### API Endpoints

- `POST /user` - Register a new user
- `GET /user/<user_id>` - Get user details
- `DELETE /user/<user_id>` - Remove a user
- `GET /users` - List all users
- `PUT /workouts/<user_id>` - Add a workout
- `GET /workouts/<user_id>` - List user's workouts
- `PUT /follow-list/<user_id>` - Follow another user
- `GET /follow-list/<user_id>/<follow_id>` - View friend's workouts

## Dependencies

The project requires the following Python packages:

- Flask==2.3.2
- Flask-RESTful==0.3.9
- requests==2.32.3

These can be installed using `pip install -r requirements.txt`
