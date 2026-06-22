import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from collections import defaultdict

@dataclass
class Commit:
    date: str
    languages: list
    frameworks: list

class GitHubSkillsMap:
    def __init__(self):
        self.cache = {}
        self.cache_expiration = 24 * 60 * 60  # 24 hours

    def get_snapshot(self, username):
        if username in self.cache:
            snapshot, expiration = self.cache[username]
            if datetime.now().timestamp() < expiration:
                return snapshot
        commits = self.get_commits(username)
        snapshot = self.generate_snapshot(commits)
        self.cache[username] = (snapshot, datetime.now().timestamp() + self.cache_expiration)
        return snapshot

    def get_commits(self, username):
        # Simulate fetching commits from GitHub API
        # For demonstration purposes, return some sample data
        return [
            Commit("2022-01-01", ["Python", "JavaScript"], ["Django", "React"]),
            Commit("2022-01-02", ["Python", "Java"], ["Django", "Spring"]),
            Commit("2022-01-03", ["JavaScript", "C++"], ["React", "Qt"]),
        ]

    def generate_snapshot(self, commits):
        commits_per_day = defaultdict(int)
        languages = defaultdict(int)
        frameworks = defaultdict(int)
        for commit in commits:
            date = datetime.strptime(commit.date, "%Y-%m-%d").date()
            commits_per_day[date] += 1
            for language in commit.languages:
                languages[language] += 1
            for framework in commit.frameworks:
                frameworks[framework] += 1
        top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        framework_badges = sorted(frameworks.items(), key=lambda x: x[1], reverse=True)
        return {
            "commits_per_day": dict(commits_per_day),
            "top_languages": top_languages,
            "framework_badges": framework_badges,
        }

    def render_snapshot(self, snapshot):
        # Simulate rendering the snapshot as a bar chart and list of languages and frameworks
        # For demonstration purposes, return a simple string representation
        return f"Commits per day: {snapshot['commits_per_day']}\nTop languages: {snapshot['top_languages']}\nFramework badges: {snapshot['framework_badges']}"
