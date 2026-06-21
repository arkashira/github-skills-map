import pytest
from github_skills_map import (
    authenticate,
    fetch_profile,
    list_repositories,
    select_repositories,
    OAuthToken,
)

def test_authenticate_happy_path():
    token = authenticate("alice_id", "secret", "authcode123")
    assert isinstance(token, OAuthToken)
    assert token.access_token == "alice_id:authcode123"
    assert token.scope == "repo"

def test_authenticate_missing_params():
    with pytest.raises(ValueError):
        authenticate("", "secret", "code")

def test_fetch_profile_happy_path():
    token = authenticate("alice_id", "secret", "code")
    profile = fetch_profile(token)
    assert profile["login"] == "alice_id"
    assert profile["public_repos"] == 3

def test_fetch_profile_invalid_token():
    with pytest.raises(ValueError):
        fetch_profile(OAuthToken("", ""))

def test_list_repositories_happy_path():
    repos = list_repositories("alice_id")
    assert repos == ["repo1", "repo2", "repo3"]

def test_list_repositories_user_not_found():
    with pytest.raises(ValueError):
        list_repositories("unknown_user")

def test_select_repositories_happy_path():
    selected = select_repositories("alice_id", ["repo1", "repo3"])
    assert set(selected) == {"repo1", "repo3"}

def test_select_repositories_missing_repo():
    with pytest.raises(ValueError) as exc:
        select_repositories("alice_id", ["repo1", "nonexistent"])
    assert "nonexistent" in str(exc.value)
