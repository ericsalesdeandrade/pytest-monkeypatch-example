import os
import pytest


def get_app_mode():
    """Fetches the application mode from the APP_MODE environment variable."""
    app_mode = os.getenv("APP_MODE")
    if not app_mode:
        raise OSError("APP_MODE environment variable is not set.")
    return app_mode.lower()


def test_get_app_mode(monkeypatch):
    """Test behavior when APP_MODE is set."""
    monkeypatch.setenv("APP_MODE", "Production")
    assert get_app_mode() == "production"


def test_missing_app_mode(monkeypatch):
    """Test behavior when APP_MODE is not set."""
    monkeypatch.delenv("APP_MODE", raising=False)

    with pytest.raises(OSError, match="APP_MODE environment variable is not set."):
        get_app_mode()
