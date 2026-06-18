import pytest
from datetime import datetime
from github_skills_map import (
    generate_github_api_token,
    fetch_user_commits,
    fetch_user_pull_requests,
    calculate_skills,
    display_skills,
    Commit,
    PullRequest,
    Skill,
)

def test_generate_github_api_token():
    username = "testuser"
    password = "testpassword"
    token = generate_github_api_token(username, password)
    assert token == f"token-{username}"

def test_fetch_user_commits():
    username = "testuser"
    token = generate_github_api_token(username, "testpassword")
    commits = fetch_user_commits(username, token)
    assert len(commits) == 2
    assert isinstance(commits[0], Commit)

def test_fetch_user_pull_requests():
    username = "testuser"
    token = generate_github_api_token(username, "testpassword")
    pull_requests = fetch_user_pull_requests(username, token)
    assert len(pull_requests) == 2
    assert isinstance(pull_requests[0], PullRequest)

def test_calculate_skills():
    commits = [
        Commit("abc123", "Initial commit", datetime(2022, 1, 1)),
        Commit("def456", "Added feature", datetime(2022, 1, 15)),
    ]
    pull_requests = [
        PullRequest(1, "Fix bug", "Bug fix", datetime(2022, 1, 10)),
        PullRequest(2, "Add feature", "New feature", datetime(2022, 1, 20)),
    ]
    skills = calculate_skills(commits, pull_requests)
    assert len(skills) == 4
    assert isinstance(skills[0], Skill)

def test_display_skills():
    skills = [
        Skill("Python", 1),
        Skill("JavaScript", 1),
    ]
    displayed_skills = display_skills(skills)
    assert displayed_skills == '[{"name": "Python", "level": 1}, {"name": "JavaScript", "level": 1}]'

def test_edge_case_calculate_skills():
    commits = []
    pull_requests = []
    skills = calculate_skills(commits, pull_requests)
    assert skills == []
