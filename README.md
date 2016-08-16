# arkiv

A simple cli application for creating & extracting tarballs. Technically it is a ui wrapper for [python-osutil](https://github.com/PencilShavings/python-osutil)'s targz function.

## Usage

Create archive:
```bash
arkiv create $HOME/Desktop/
```

Extract archive:
```bash
arkiv extract $HOME/Desktop.tar.gz
```

Simple yet effective. See --help for more information on usage.

## Dependencies

arkiv requires the following:

- Python 2
- python-osutil
- python-argh

Python Modules can be installed via pip:
```bash
pip install --user argh osutil
```
---

## Installation
Download the source:
```bash
git clone https://github.com/PencilShavings/arkiv.git
```

OR just download the script:

```bash
wget -N https://raw.githubusercontent.com/PencilShavings/arkiv/master/arkiv.py
```

Recommend to rename arkiv.py to just arkiv & place it somewhere in your PATH for a more cohesive cli experience.

NOTE: If you download just the script, don't forget to make it executable.
