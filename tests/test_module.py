from pathlib import Path


def get_ssh_path():
    return Path.home() / ".ssh"


def test_get_ssh_path(monkeypatch):
    def mockreturn():
        return Path("/tmp")

    monkeypatch.setattr(Path, "home", mockreturn)
    assert get_ssh_path() == Path("/tmp/.ssh")

    # Optional: reset the monkeypatch if needed for rest of the test
    monkeypatch.delattr(Path, "home")
