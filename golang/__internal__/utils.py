#!/usr/bin/env python
# coding=utf-8
# Created by @menduo @ 2024/2/5
import os


def adjust_filepath(filepath: str):
    if filepath.startswith("~"):
        filepath = os.path.expanduser(filepath)
    return filepath
