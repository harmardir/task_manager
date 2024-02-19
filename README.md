## Task Manager
The Task Manager app is a simple Django project demonstrating the use of Celery, Celery Beat, and Redis for handling asynchronous tasks and scheduled periodic tasks.

### Features:
- Allows users to create tasks via a Django model.
- Utilizes Celery to execute asynchronous tasks in the background.
- Uses Celery Beat for scheduling and executing periodic tasks.
- Redis is employed as the message broker and result backend for Celery.

### Setup Instructions:
- Install Django, Celery, and Redis.
- Clone the repository.
- Configure Celery in `settings.py` and set up Celery Beat schedules.
- Run Celery worker and Celery Beat.
- Start the Django development server.
- Access the app through the browser and create tasks to see asynchronous and periodic task execution.

### Project Structure:
- task_manager/: Django project folder.
- tasks/: Django app for managing tasks.
- models.py: Defines the Task model.
- tasks.py: Defines Celery tasks.
- celery.py: Celery configuration file.
- settings.py: Django settings file.

### Dependencies:
- Django
- Celery
- Redis

### Usage:
- Create tasks via the Django admin or programmatically.
- Tasks will be executed asynchronously using Celery.
- Periodic tasks are scheduled and executed by Celery Beat.
- Monitor task execution in the console logs.
