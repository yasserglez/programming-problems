#!/usr/bin/env python3

import contextlib
import os
import subprocess
import sys
import unittest
from itertools import zip_longest


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseTestHandler(unittest.TestCase):

    extensions = None

    def __init__(self, src_file):
        super().__init__()
        self._src_file = src_file
        self._src_dir = os.path.dirname(self._src_file)
        basename = os.path.splitext(self._src_file)[0]
        self._in_file = basename + '.in'
        self._out_file = basename + '.out'
        self._tmp_file = basename + '.tmp'

    def __str__(self):
        return self._src_file[len(ROOT_DIR) + 1:]

    def setUp(self):  # Compile.
        pass

    @contextlib.contextmanager
    def _src_dir_as_cwd(self):
        prev_cwd = os.getcwd()
        os.chdir(self._src_dir)
        try:
            yield
        finally:
            os.chdir(prev_cwd)

    def runTest(self, args):
        # Run the program.
        if os.path.isfile(self._in_file):
            stdin_fd = open(self._in_file)
        else:
            stdin_fd = None
        with self._src_dir_as_cwd():
            with open(self._tmp_file, 'w') as stdout_fd:
                subprocess.call(args, stdin=stdin_fd, stdout=stdout_fd)
        if stdin_fd:
            stdin_fd.close()
        # Compare the output.
        self.compareOutput()

    def compareOutput(self):
        with open(self._tmp_file) as tmp_fd:
            with open(self._out_file) as out_fd:
                for out_line, tmp_line in zip_longest(out_fd, tmp_fd):
                    if out_line != tmp_line:
                        self.fail("output doesn't match")

    def tearDown(self):  # Cleaning up.
        if os.path.isfile(self._tmp_file):
            os.remove(self._tmp_file)

    @classmethod
    def iter_handlers(cls):
        stack = [cls]
        while stack:
            cls = stack.pop()
            if cls.extensions:
                yield cls
            for subcls in cls.__subclasses__():
                stack.append(subcls)


class PythonTestHandler(BaseTestHandler):

    extensions = ('.py', )

    def runTest(self):
        super().runTest(['python3', self._src_file])


class RTestHandler(BaseTestHandler):

    extensions = ('.R', '.r')

    def runTest(self):
        super().runTest(['Rscript', '--vanilla', self._src_file])


class GCCTestHandler(BaseTestHandler):

    def __init__(self, src_file):
        super().__init__(src_file)
        self._bin_file = os.path.splitext(self._src_file)[0]

    def runTest(self):
        super().runTest([self._bin_file])

    def tearDown(self):
        super().tearDown()
        if os.path.isfile(self._bin_file):
            os.remove(self._bin_file)


class CTestHandler(GCCTestHandler):

    extensions = ('.c', )

    def setUp(self):
        subprocess.call(['gcc', '-ansi',
                         '-D_POSIX_C_SOURCE=200809L',
                         '-Wall', '-Wextra', '-Werror', '-pedantic',
                         self._src_file, '-o', self._bin_file])


class CPPTestHandler(GCCTestHandler):

    extensions = ('.cpp', '.cc')

    def setUp(self):
        subprocess.call(['g++', '-ansi',
                         '-Wall', '-Wextra', '-Werror', '-pedantic',
                         self._src_file, '-o', self._bin_file])


class JavaTestHandler(BaseTestHandler):

    extensions = ('.java', )

    def setUp(self):
        subprocess.call(['javac', self._src_file])

    def runTest(self):
        classname = os.path.splitext(os.path.basename(self._src_file))[0]
        super().runTest(['java', '-ea', classname])

    def tearDown(self):
        super().tearDown()
        for classfile in (f for f in os.listdir() if f.endswith('.class')):
            os.remove(classfile)


class ScalaTestHandler(BaseTestHandler):

    extensions = ('.scala', )

    def runTest(self):
        super().runTest(['scala', '-howtorun:script', self._src_file])


class SQLTestHandler(BaseTestHandler):

    extensions = ('.sql', )

    def __init__(self, src_file):
        super().__init__(src_file)
        self._db_file = os.path.splitext(self._src_file)[0] + '.db'

    def setUp(self):
        if os.path.isfile(self._in_file):
            stdin_fd = open(self._in_file)
            subprocess.call(['sqlite3', self._db_file], stdin=stdin_fd)
            stdin_fd.close()

    def runTest(self):
        # Run the query.
        with self._src_dir_as_cwd():
            with open(self._src_file) as stdin_fd:
                with open(self._tmp_file, 'w') as stdout_fd:
                    args = ['sqlite3', self._db_file]
                    subprocess.call(args, stdin=stdin_fd, stdout=stdout_fd)
        # Compare the output.
        self.compareOutput()

    def tearDown(self):
        super().tearDown()
        if os.path.isfile(self._db_file):
            os.remove(self._db_file)


def main():
    handlers = {}
    for handler_cls in BaseTestHandler.iter_handlers():
        for extension in handler_cls.extensions:
            handlers[extension] = handler_cls
    suite = unittest.TestSuite()
    for dirpath, _, filenames in sorted(os.walk(ROOT_DIR), key=lambda t: t[0]):
        if dirpath != ROOT_DIR:
            for filename in sorted(filenames):
                extension = os.path.splitext(filename)[1]
                if extension in handlers:
                    src_file = os.path.join(dirpath, filename)
                    handler = handlers[extension](src_file)
                    suite.addTest(handler)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return (0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    sys.exit(main())
