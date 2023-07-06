# ReadMe

NotePad is a simple and easy-to-use online note-taking and task management application that allows you to keep track of your thoughts, ideas, tasks, and team collaborations all in one place. It was built with:

- Python 3.11
- Django 4.2.2
- HTML 5
- CSS 3
- PostgreSQL (for efficient data storage and retrieval)

### Features

1. **User Management**
    - The app is built with Django and integrates with Django's built-in User model for authentication and user management.

2. **Teams**
    - Users can create Teams, which can be managed by a single owner. The owner can add members to the team via the TeamMember model. This allows for collaborative note-taking and task management among team members.

3. **Notes**
    - Users can create Notes that have a title and content. Notes are associated with a user and optionally a team and a category. This means that notes can be shared with all the members of a team, and they can be organized into different categories for better organization.

4. **Categories**
    - Notes can be categorized using the Category model. Each category has a title and a description.

5. **Todo Lists and Todo Items**
    - Users can create Todo Lists, each of which can contain multiple Todo Items. Todo Lists are associated with a user and optionally a team. This allows users to manage their tasks and also share task lists with their teams. Todo Items have a title and a status indicating whether the task has been completed.

6. **Timestamps**
    - All major models (Notes, Todo Lists) include timestamps for creation and last modification, allowing users to keep track of when a note was written or a task was last updated.

### Usage

You will need to sign up and log in to create notes, todo lists, and teams. This app allows for collaborative work, enabling team members to share, edit, and manage notes and todo lists together for efficient team coordination.

### Models

Here is a brief description of the models used in the app:

- **User:** Django's built-in user model. It's used for authentication and as a foreign key in other models.
- **Team:** Represents a team of users. Has a name, description, an owner, and multiple members.
- **TeamMember:** Represents a user's membership in a team.
- **Category:** Represents a category that can be associated with a note.
- **Note:** Represents a note. Has content, associated user, optional category, optional team, and timestamps.
- **TodoList:** Represents a list of tasks. Has associated user, optional team, and timestamps.
- **TodoItem:** Represents a task in a todo list. Has a title and a completion status.

Please refer to the [code](https://github.com/reneczka/notepad) for more details about these models and how they are used in the app.
