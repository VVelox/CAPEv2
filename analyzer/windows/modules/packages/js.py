# Copyright (C) 2015 Optiv, Inc. (brad.spengler@optiv.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from __future__ import absolute_import
import os

from lib.common.abstracts import Package


class JS(Package):
    """JavaScript analysis package."""

    PATHS = [
        ("SystemRoot", "system32", "wscript.exe"),
    ]

    def start(self, path):
        wscript = self.get_path("wscript.exe")
        args = f'"{path}"'
        ext = os.path.splitext(path)[-1].lower()
        if ext != ".js" and ext != ".jse":
            if ext == ".jse" or (os.path.isfile(path) and "#@~^" == open(path, "rt").read(4)):
                if ext != ".jse":
                    os.rename(path, f"{path}.jse")
                    path = f"{path}.jse"
                    ext = ".jse"
            else:
                os.rename(path, f"{path}.js")
                path = f"{path}.js"

        if ext == ".jse":
            # antivm fix
            free = self.options.get("free", False)
            # to not track calcs
            self.options["free"] = 1
            # fuck antivm
            for i in range(20):
                # calc
                calc = os.path.join("C:\\windows", "system32", "calc.exe")
                # cl = Process()
                self.execute(calc, "", path)
            if free is False:
                self.options["free"] = 0

        args = f'"{path}"'
        return self.execute(wscript, args, path)
