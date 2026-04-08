import pytest
from datetime import datetime
from src.core.repository import InMemoryRepository
from src.core.services import UserService, TaskService, ProjectService


@pytest.fixture
def repository():
    return InMemoryRepository()


@pytest.fixture
def user_service(repository):
    return UserService(repository)


@pytest.fixture
def task_service(repository):
    return TaskService(repository)


@pytest.fixture
def project_service(repository):
    return ProjectService(repository)


def test_user_service_create_user(user_service):
    user = user_service.create_user("testuser", "test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_user_service_duplicate_username(user_service):
    user_service.create_user("testuser", "test@example.com")
    
    with pytest.raises(ValueError, match="User with username 'testuser' already exists"):
        user_service.create_user("testuser", "another@example.com")


def test_user_service_get_user(user_service):
    created_user = user_service.create_user("testuser", "test@example.com")
    retrieved_user = user_service.get_user(created_user.id)
    assert retrieved_user == created_user


def test_user_service_list_users(user_service):
    user1 = user_service.create_user("user1", "user1@example.com")
    user2 = user_service.create_user("user2", "user2@example.com")
    
    users = user_service.list_users()
    assert len(users) == 2
    assert user1 in users
    assert user2 in users


def test_task_service_create_task(user_service, task_service):
    user = user_service.create_user("testuser", "test@example.com")
    task = task_service.create_task("Test Task", "Description", user.id)
    
    assert task.title == "Test Task"
    assert task.description == "Description"
    assert task.user_id == user.id


def test_task_service_create_task_invalid_user(task_service):
    with pytest.raises(ValueError, match="User with id 999 not found"):
        task_service.create_task("Test Task", "Description", 999)


def test_task_service_complete_task(user_service, task_service):
    user = user_service.create_user("testuser", "test@example.com")
    task = task_service.create_task("Test Task", "Description", user.id)
    
    completed_task = task_service.complete_task(task.id)
    assert completed_task.completed is True


def test_task_service_list_tasks_by_user(user_service, task_service):
    user1 = user_service.create_user("user1", "user1@example.com")
    user2 = user_service.create_user("user2", "user2@example.com")
    
    task1 = task_service.create_task("Task 1", "Description 1", user1.id)
    task2 = task_service.create_task("Task 2", "Description 2", user1.id)
    task3 = task_service.create_task("Task 3", "Description 3", user2.id)
    
    user1_tasks = task_service.list_tasks_by_user(user1.id)
    assert len(user1_tasks) == 2
    assert task1 in user1_tasks
    assert task2 in user1_tasks
    assert task3 not in user1_tasks


def test_project_service_create_project(user_service, project_service):
    user = user_service.create_user("testuser", "test@example.com")
    project = project_service.create_project("Test Project", "Description", user.id)
    
    assert project.name == "Test Project"
    assert project.description == "Description"
    assert project.owner_id == user.id


def test_project_service_create_project_invalid_user(project_service):
    with pytest.raises(ValueError, match="User with id 999 not found"):
        project_service.create_project("Test Project", "Description", 999)


def test_project_service_list_projects_by_owner(user_service, project_service):
    user1 = user_service.create_user("user1", "user1@example.com")
    user2 = user_service.create_user("user2", "user2@example.com")
    
    project1 = project_service.create_project("Project 1", "Description 1", user1.id)
    project2 = project_service.create_project("Project 2", "Description 2", user1.id)
    project3 = project_service.create_project("Project 3", "Description 3", user2.id)
    
    user1_projects = project_service.list_projects_by_owner(user1.id)
    assert len(user1_projects) == 2
    assert project1 in user1_projects
    assert project2 in user1_projects
    assert project3 not in user1_projects
