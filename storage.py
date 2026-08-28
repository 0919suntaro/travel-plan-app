import json
from datetime import datetime
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent / "data"
FAVORITES_PATH = DATA_DIR / "favorites.json"


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(exist_ok=True)


def load_favorites() -> list[dict[str, Any]]:
    if not FAVORITES_PATH.exists():
        return []
    try:
        return json.loads(FAVORITES_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_favorites(favorites: list[dict[str, Any]]) -> None:
    _ensure_data_dir()
    FAVORITES_PATH.write_text(
        json.dumps(favorites, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add_favorite(kind: str, title: str, detail: dict[str, Any]) -> None:
    favorites = load_favorites()
    favorites.append(
        {
            "kind": kind,
            "title": title,
            "detail": detail,
            "saved_at": datetime.now().isoformat(timespec="seconds"),
        }
    )
    save_favorites(favorites)


def remove_favorite(index: int) -> None:
    favorites = load_favorites()
    if 0 <= index < len(favorites):
        favorites.pop(index)
        save_favorites(favorites)
