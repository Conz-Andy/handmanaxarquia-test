# Canonical HA mark. The original trace of the low-resolution source left a
# stair-stepped wobble along the bottom edge of the A counter (deviations of about
# one source pixel) and a 19-unit stub at its top-left apex; both are replaced here
# by the straight edges the mark is actually built from. Written into site/images at
# build time so every page — and the inlined data URI — uses the corrected geometry.
from pathlib import Path

MARK = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3300 3672" width="3300" height="3672">\n'
        '<path fill="#FBA917" fill-rule="evenodd" d="M 1476 0 L 901 342 L 894 1474 L 564 1517 '
        'L 561 533 L 0 840 L 0 2735 L 570 3056 L 563 2133 L 884 2054 L 901 3245 L 1667 3671 '
        'L 2386 3245 L 2395 2055 L 2724 2121 L 2726 3054 L 3299 2735 L 3299 845 L 1813 0 '
        'L 1812 2906 L 1639 3011 L 1487 2918 Z M 2393 1008 L 2723 1182 L 2718 1522 L 2389 1459 Z"/>\n'
        '</svg>\n')


def apply(site: Path):
    d = site / "images"
    d.mkdir(parents=True, exist_ok=True)
    (d / "logo_mark.svg").write_text(MARK)
    print("logo mark: straight-edge version written")


if __name__ == "__main__":
    apply(Path(__file__).resolve().parent.parent / "site")
