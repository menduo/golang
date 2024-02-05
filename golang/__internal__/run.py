#!/usr/bin/env python
# coding=utf-8
# Created by @menduo @ 2024/2/5
import os
import tempfile
from subprocess import check_output

from golang.__internal__.env import Env

from golang.__internal__.utils import adjust_filepath


def run_code(code: str, env: Env = None):
    file = tempfile.mktemp(suffix=".go")
    with open(file, "w") as f:
        f.write(code)
    output = check_output(["go", "run", file])
    return output


def run_file(filepath: str, env: Env = None, chdir: bool = True):
    filepath = adjust_filepath(filepath)
    dirpath, filename = os.path.split(filepath)

    if chdir:
        os.chdir(dirpath)
    if env:
        env.export()

    output = check_output(["go", "run", filename])
    return output


__all__ = ["run_code", "run_file", ]
