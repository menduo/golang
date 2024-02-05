#!/usr/bin/env python
# coding=utf-8
# Created by @menduo @ 2024/2/5
import os


class Env:
    GOROOT = os.getenv("GOROOT")
    GOPATH = os.getenv("GOPATH")
    GOBIN = os.getenv("GOBIN")
    GOOS = os.getenv("GOOS")
    GOARCH = os.getenv("GOARCH")
    GOPRIVATE = os.getenv("GOPRIVATE")

    __kvs__ = {

    }

    def __init__(self):
        pass

    def set(self, key, value):
        return

    def get(self, key=""):
        pass

    def export(self):
        pass

    def prefix(self):
        pass

    def __str__(self):
        return f"GOROOT: {self.GOROOT}\nGOPATH: {self.GOPATH}\nGOOS: {self.GOOS}\nGOARCH: {self.GOARCH}\nGOPRIVATE: {self.GOPRIVATE}\n"

    def __repr__(self):
        return self.__str__()
