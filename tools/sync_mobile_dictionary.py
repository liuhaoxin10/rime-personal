#!/usr/bin/env python3
"""Copy dictionary data to mobile without copying any desktop input settings."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
MOBILE = ROOT / "mobile"


def main():
    target = MOBILE / "cn_dicts"
    target.mkdir(parents=True, exist_ok=True)
    paths = sorted((ROOT / "cn_dicts").glob("*.dict.yaml"))
    paths.append(ROOT / "custom_rime_ice.dict.yaml")
    for path in paths:
        if path.is_symlink():
            raise ValueError(f"Dictionary must be an ordinary file: {path}")
        destination = MOBILE / path.relative_to(ROOT)
        shutil.copy2(path, destination)
    print(f"Synced {len(paths)} dictionary files; mobile input settings were not copied.")


if __name__ == "__main__":
    main()
