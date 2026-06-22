from github_skills_map import GitHubSkillsMap, Commit
import pytest
from datetime import datetime

def test_get_snapshot():
    github_skills_map = GitHubSkillsMap()
    commits = [
        Commit("2022-01-01", ["Python", "JavaScript"], ["Django", "React"]),
        Commit("2022-01-02", ["Python", "Java"], ["Django", "Spring"]),
        Commit("2022-01-03", ["JavaScript", "C++"], ["React", "Qt"]),
    ]
    snapshot = github_skills_map.get_snapshot("username")
    assert isinstance(snapshot, dict)
    assert "commits_per_day" in snapshot
    assert "top_languages" in snapshot
    assert "framework_badges" in snapshot

def test_get_commits():
    github_skills_map = GitHubSkillsMap()
    commits = github_skills_map.get_commits("username")
    assert isinstance(commits, list)
    assert all(isinstance(commit, Commit) for commit in commits)

def test_generate_snapshot():
    github_skills_map = GitHubSkillsMap()
    commits = [
        Commit("2022-01-01", ["Python", "JavaScript"], ["Django", "React"]),
        Commit("2022-01-02", ["Python", "Java"], ["Django", "Spring"]),
        Commit("2022-01-03", ["JavaScript", "C++"], ["React", "Qt"]),
    ]
    snapshot = github_skills_map.generate_snapshot(commits)
    assert isinstance(snapshot, dict)
    assert "commits_per_day" in snapshot
    assert "top_languages" in snapshot
    assert "framework_badges" in snapshot

def test_render_snapshot():
    github_skills_map = GitHubSkillsMap()
    snapshot = {
        "commits_per_day": {"2022-01-01": 1, "2022-01-02": 1, "2022-01-03": 1},
        "top_languages": [("Python", 2), ("JavaScript", 2), ("Java", 1), ("C++", 1)],
        "framework_badges": [("Django", 2), ("React", 2), ("Spring", 1), ("Qt", 1)],
    }
    rendered_snapshot = github_skills_map.render_snapshot(snapshot)
    assert isinstance(rendered_snapshot, str)

def test_cache_expiration():
    github_skills_map = GitHubSkillsMap()
    github_skills_map.cache = {"username": ("snapshot", datetime.now().timestamp() - 25 * 60 * 60)}  # expired cache
    snapshot = github_skills_map.get_snapshot("username")
    assert isinstance(snapshot, dict)
    assert "commits_per_day" in snapshot
    assert "top_languages" in snapshot
    assert "framework_badges" in snapshot
