#!/usr/bin/env python3
"""Package the independent Zihao mobile or desktop Rime source profile."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {
    "LICENSE",
    "custom_phrase.txt",
    "personal_phrase_t9.txt",
    "default.yaml",
    "default.custom.yaml",
    "rime_ice.custom.yaml",
    "melt_eng.custom.yaml",
    "t9.custom.yaml",
    "symbols_v.yaml",
    "symbols_caps_v.yaml",
}
SOURCE_DIRS = {"cn_dicts", "en_dicts", "lua", "opencc"}
SOURCE_SUFFIXES = {".yaml", ".txt", ".lua", ".json"}


def source_files(profile_root):
    for path in sorted(profile_root.iterdir()):
        if path.is_file() and (
            path.name in ROOT_FILES
            or path.name.endswith((".schema.yaml", ".dict.yaml"))
        ):
            yield path
    for directory in sorted(SOURCE_DIRS):
        for path in sorted((profile_root / directory).rglob("*")):
            if not path.is_file() or path.is_symlink():
                continue
            if any(part.startswith(".") or ".userdb" in part for part in path.relative_to(profile_root).parts):
                continue
            if path.suffix in SOURCE_SUFFIXES or path.relative_to(profile_root).as_posix() == "lua/lunar.db":
                yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=("mobile", "desktop"), default="mobile")
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "rime-personal.zip")
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    profile_root = ROOT / "mobile" if args.profile == "mobile" else ROOT
    paths = list(source_files(profile_root))
    with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths:
            archive.write(path, path.relative_to(profile_root).as_posix())
    print(f"Packaged {args.profile}: {len(paths)} source files: {output} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
