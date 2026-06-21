import json
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class OAuthToken:
    access_token: str
    scope: str

def authenticate(client_id: str, client_secret: str, auth_code: str) -> OAuthToken:
    """Simulated OAuth authentication"""
    if not all([client_id, client_secret, auth_code]):
        raise ValueError("Missing authentication parameters")
    return OAuthToken(f"{client_id}:{auth_code}", "repo")

def fetch_profile(token: OAuthToken) -> Dict[str, Any]:
    """Fetch user profile information"""
    if not token.access_token or not token.scope:
        raise ValueError("Invalid OAuth token")
    # Simulated profile data
    return {"login": "alice_id", "public_repos": 3}

def list_repositories(user_id: str) -> List[str]:
    """List available repositories"""
    if user_id == "unknown_user":
        raise ValueError("User not found")
    # Simulated repository data
    return ["repo1", "repo2", "repo3"]

def select_repositories(user_id: str, repository_names: List[str]) -> set:
    """Select repositories to track"""
    available_repos = list_repositories(user_id)
    selected_repos = set()
    for repo in repository_names:
        if repo not in available_repos:
            raise ValueError(f"Repository '{repo}' not found")
        selected_repos.add(repo)
    return selected_repos
