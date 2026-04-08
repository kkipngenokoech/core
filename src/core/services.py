from typing import List, Optional
from datetime import datetime
from .models import User, Task, Project
from .repository import InMemoryRepository


class UserService:
    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    def create_user(self, username: str, email: str) -> User:
        existing_user = self.repository.get_user_by_username(username)
        if existing_user:
            raise ValueError(f"User with username '{username}' already exists")
        return self.repository.create_user(username, email)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_user(user_id)

    def list_users(self) -> List[User]:
        return self.repository.list_users()


class TaskService:
    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    def create_task(self, title: str, description: str, user_id: int, due_date: Optional[datetime] = None) -> Task:
        user = self.repository.get_user(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        return self.repository.create_task(title, description, user_id, due_date)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repository.get_task(task_id)

    def list_tasks_by_user(self, user_id: int) -> List[Task]:
        return self.repository.list_tasks_by_user(user_id)

    def complete_task(self, task_id: int) -> Optional[Task]:
        return self.repository.update_task(task_id, completed=True)

    def update_task(self, task_id: int, **kwargs) -> Optional[Task]:
        return self.repository.update_task(task_id, **kwargs)


class ProjectService:
    def __init__(self, repository: InMemoryRepository):
        self.repository = repository

    def create_project(self, name: str, description: str, owner_id: int) -> Project:
        user = self.repository.get_user(owner_id)
        if not user:
            raise ValueError(f"User with id {owner_id} not found")
        return self.repository.create_project(name, description, owner_id)

    def get_project(self, project_id: int) -> Optional[Project]:
        return self.repository.get_project(project_id)

    def list_projects_by_owner(self, owner_id: int) -> List[Project]:
        return self.repository.list_projects_by_owner(owner_id)
