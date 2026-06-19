import pytest
from github_skills_map import fetch_github_data, extract_skills, generate_graph, save_graph, Skill, main
import sys

def test_fetch_github_data():
    data = fetch_github_data("test_user")
    assert len(data) == 3
    assert data[0].name == "Python"
    assert data[0].level == 5

def test_extract_skills():
    data = [Skill("Python", 5), Skill("Java", 3), Skill("C++", 4)]
    skills = extract_skills(data)
    assert skills == data

def test_generate_graph():
    skills = [Skill("Python", 5), Skill("Java", 3), Skill("C++", 4)]
    graph = generate_graph(skills)
    assert graph == "Python: 5\nJava: 3\nC++: 4\n"

def test_save_graph(tmp_path):
    graph = "Python: 5\nJava: 3\nC++: 4\n"
    output_path = tmp_path / "skills.txt"
    save_graph(graph, str(output_path))
    assert output_path.exists()
    with open(output_path, "r") as f:
        assert f.read() == graph

def test_main(tmp_path, capsys):
    output_path = tmp_path / "skills.txt"
    with pytest.raises(SystemExit) as exit_info:
        main(["test_user", "--output", str(output_path)])
    assert exit_info.value.code == 0
    assert output_path.exists()
    with open(output_path, "r") as f:
        assert f.read() == "Python: 5\nJava: 3\nC++: 4\n"
