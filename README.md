# update-version

A minimalist Python script to update your project's version through a `version.txt` file.

---

## Installation

You can install it through `pip`:

```sh
pip install update-version
```

This script will install the following python packages as dependencies:

- `argparse`
- `argcomplete`

---

## Usage

```
update-version [-h] [-v] [-V] [-P] [-L] [-D] [-e] [-p] [-m] [-M] [-d]
                    [-r <MAJOR>.<MINOR>.<PATCH>[-<EXTRA>]]
                    [path]
```

This script can be used for two types of versioning:

- `X.Y.Z`
- `X.Y.Z-N`

Where `X` is the major component, `Y` is the minor component and `Z` is the patch component.

If using `N` you will need to pass the `-d` option to the script.

<!-- vim: set ts=2 sts=2 sw=2 et ai si sta: -->
