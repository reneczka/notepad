# Notepad Application

This is a Django-based web application designed to help users manage their notes, to-do lists, and team collaborations. It supports category-based organization, team-based note sharing, and advanced to-do list management with customizable items.

[Live demo](https://note-pad-1jg9.onrender.com) (note: please wait up to 1 minute for the cold start)

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Schema](#database-schema)

## Features

- **User Authentication**: Includes user registration, login, and logout functionality.
- **Notes Management**: Users can create, edit, delete, and organize notes by category.
- **To-Do List Management**: Create and manage to-do lists and their items.
- **Team Collaboration**: Allows users to create teams, join or leave teams, and share notes and to-do lists within teams.
- **Category Organization**: Notes can be organized into categories for better management.
- **Responsive Design**: Uses Django templates to ensure the app is user-friendly.

## Technologies Used

- **Django**: Web framework for building the application.
- **PostgreSQL**: Database for storing application data.
- **HTML/CSS**: For front-end design.
- **Python**: Core programming language.

## Project Structure

```
NOTEPAD/
├── notepad/
│   ├── settings.py - Project settings
│   ├── urls.py - URL routing for the project
├── notepad_app/
│   ├── forms.py — Forms for user interaction
│   ├── models.py - Database models
│   └── views.py — Application views for handling requests
├── static/css/ - HTML templates for rendering the web pages
│   └── styles.css - Custom CSS styles
├── templates/
├── .env — Stores environment variables
├── pyproject.toml - Project configuration and dependencies
└── README.md — Project documentation
```

## Setup and Installation

To set up and run the Notepad project, follow these steps:

1. **Clone the repository and enter the project directory:**

   ```
   git clone https://github.com/reneczka/notepad.git
   cd notepad
   ```

2. **Set up the environment:**

   ```
    python -m venv venv
    source venv/bin/activate  
   ```

3. **Install required Python packages:**

   ```
    pip install -r requirements.txt
   ```

4. **Set up the `.env` file:**

    Create a .env file in the project root directory to store sensitive data like database credentials. Follow the format of the .env.example file included in the repository.

5. **Apply database migrations::**

   ```
    python manage.py makemigrations
    python manage.py migrate
   ```
6. **Create a superuser:**

   ```
    python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```
    python manage.py runserver
   ```

8. **Access the application:**

    Open your browser and navigate to http://127.0.0.1:8000 to start using the application. Log in using the superuser credentials to access the admin panel at http://127.0.0.1:8000/admin.


## Usage

1. **User Authentication**:
   - Register a new account or log in to access the application.
   - Logout is available in the navigation menu.

2. **Homepage**:
   - The homepage (`/`) displays an overview of all notes and categories.
   - Quickly navigate to specific categories or notes.

3. **Notes Management**:
   - **Create Note**: Go to `/note/create/` to add a new note. Assign a category or team if applicable.
   - **View Note**: Access detailed note information at `/note/<note_id>/`.
   - **Edit Note**: Update note details at `/note/<note_id>/update/`.
   - **Delete Note**: Remove a note at `/note/<note_id>/delete/`.

4. **Category Management**:
   - **View Categories**: Visit `/category/` for a list of all categories.
   - **Create Category**: Add a new category at `/category/create/`.
   - **Edit Category**: Update a category at `/category/<category_id>/update/`.
   - **Delete Category**: Remove a category at `/category/<category_id>/delete/`.

5. **To-Do List Management**:
   - **View To-Do Lists**: Visit `/todolists/` for a list of all to-do lists.
   - **Create To-Do List**: Add a new to-do list at `/todolist/create/`.
   - **View To-Do List**: Access detailed to-do list information at `/todolist/<list_id>/`.
   - **Edit To-Do List**: Update a to-do list at `/todolist/<list_id>/update/`.
   - **Delete To-Do List**: Remove a to-do list at `/todolist/<list_id>/delete/`.

6. **To-Do Item Management**:
   - **Create To-Do Item**: Add a new item to a list at `/todoitem/<list_id>/create/`.
   - **Edit To-Do Item**: Update an item's details at `/todoitem/<item_id>/update/`.
   - **Delete To-Do Item**: Remove an item at `/todoitem/<item_id>/delete/`.

7. **Team Management**:
   - **Create Team**: Add a new team at `/team/create/`.
   - **View Teams**: See a list of all teams at `/team/list/`.
   - **View Team**: Access detailed team information at `/team/<team_id>/`.
   - **Join Team**: Join a team at `/team/<team_id>/join/`.
   - **Leave Team**: Leave a team at `/team/<team_id>/leave/`.
   - **Delete Team**: Remove a team at `/team/<team_id>/delete/`.


## Database Schema

### Users and Authentication

The project uses Django's built-in **User model** for authentication and user management.

---

### Key Tables

### Users and Authentication

The project uses Django's built-in **User model** for authentication and user management.

---

### Key Tables

#### Notes Table

| Column       | Type        | Description                           |
| ------------ | ----------- | ------------------------------------- |
| id           | Integer     | Primary key, auto-increment           |
| title        | String      | Note title                           |
| content      | Text        | Note content                         |
| user         | ForeignKey  | Reference to the user who owns the note |
| category     | ForeignKey  | Reference to the associated category (nullable) |
| team         | ForeignKey  | Reference to the associated team (nullable) |
| created_at   | DateTime    | Timestamp when the note was created   |
| updated_at   | DateTime    | Timestamp when the note was last updated |

---

#### Categories Table

| Column       | Type        | Description                           |
| ------------ | ----------- | ------------------------------------- |
| id           | Integer     | Primary key, auto-increment           |
| title        | String      | Title of the category                |
| description  | Text        | Additional details about the category |

---

#### To-Do List Table

| Column       | Type        | Description                           |
| ------------ | ----------- | ------------------------------------- |
| id           | Integer     | Primary key, auto-increment           |
| title        | String      | Title of the to-do list              |
| user         | ForeignKey  | Reference to the user who owns the to-do list |
| team         | ForeignKey  | Reference to the associated team (nullable) |
| created_at   | DateTime    | Timestamp when the to-do list was created |
| modified_at  | DateTime    | Timestamp when the to-do list was last modified |

---

#### To-Do Items Table

| Column       | Type        | Description                           |
| ------------ | ----------- | ------------------------------------- |
| id           | Integer     | Primary key, auto-increment           |
| title        | String      | Title of the to-do item              |
| todo_list    | ForeignKey  | Reference to the associated to-do list |
| completed    | Boolean     | Status of the to-do item             |
