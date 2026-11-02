"""Render header illustrations to public/images/blog/illustrations/<slug>.svg.

Each drawings/<slug>.py defines TITLE (a plain description, also a good
imageAlt) and shapes() -> list of pen.s(...). Standard library only.

    python3 tools/illustrations/build.py            # all drawings
    python3 tools/illustrations/build.py <slug>...  # just these
"""
import importlib.util, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pen  # noqa: E402

OUT = HERE.parents[1] / "public/images/blog/illustrations"


def render(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    (OUT / f"{path.stem}.svg").write_text(pen.sketch(mod.TITLE, mod.shapes()))
    print("wrote", path.stem)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    names = sys.argv[1:]
    for p in sorted((HERE / "drawings").glob("*.py")):
        if not names or p.stem in names:
            render(p)
