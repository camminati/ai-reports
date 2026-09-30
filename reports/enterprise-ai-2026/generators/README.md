# Generators (archive)

The Python scripts that produced the slides during the original work. They are kept for
provenance only. **The HTML files in `../slides/` are the source of truth.** Later edits
were made directly on the slides and by targeted scripts, so re-running the older
generators (`b1`–`b10`, `fix*`, `b8`) would overwrite those edits.

* `lib.py`: palette, fonts and layout helpers used by the generators
* `srcmap.py`, `srcbuild*.py`, `srcpub.py`: source extraction, ordering, numbering and layout
  of the source slides (`srcbuild3.py` is the last version)
* `chk2.py`, `ovf.py`: the original layout checkers (superseded by `tools/check_layout.py`)
* `sem.py`, `mck.py`, `med.py`, `leg.py`: one-off edits (forecast colours, McKinsey
  corrections, media slides, legends), already applied

Paths inside the scripts point to the original working directory and will need adjusting.
