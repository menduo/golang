#!/usr/bin/env python
# coding=utf-8
# Created by @menduo @ 2024/2/5
import os
import tempfile
from subprocess import check_output

from golang.__internal__.env import Env


def run_code(code: str, env: Env = None):
    file = tempfile.mktemp(suffix=".go")
    with open(file, "w") as f:
        f.write(code)
    output = check_output(["go", "run", file])
    return output


def run_file(filepath: str, env: Env = None, workdir: str = None):
    if workdir:
        os.chdir(workdir)
    pass


__all__ = ["run_code", "run_file", ]
