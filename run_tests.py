#!/usr/bin/env python3

import os
import itertools
import unittest
import subprocess


ALGORITHMS_DIR = os.path.abspath(os.path.dirname(__file__))


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
        return self._src_file[len(ALGORITHMS_DIR) + 1:]

    def setUp(self):  # compile
        pass

    def runTest(self):  # run program and call compareOutput
        pass

    def compareOutput(self):
        with open(self._out_file) as out_fd:
            with open(self._tmp_file) as tmp_fd:
                for out_line, tmp_line in itertools.zip_longest(out_fd, tmp_fd):
                    if out_line != tmp_line:
                        self.fail("output doesn't match")

    def tearDown(self):  # cleanup
        if os.path.isfile(self._tmp_file):
            os.remove(self._tmp_file)


class PythonTestHandler(BaseTestHandler):

    extensions = ('.py', )

    def runTest(self):
        with open(self._in_file) as stdin_fd:
            with open(self._tmp_file, 'w') as stdout_fd:
                subprocess.call(['python', self._src_file],
                                stdin=stdin_fd, stdout=stdout_fd)
        self.compareOutput()


class GCCTestHandler(BaseTestHandler):

    extensions = ('.c', '.cpp')

    def __init__(self, src_file):
        super().__init__(src_file)
        self._bin_file = os.path.splitext(self._src_file)[0]

    def setUp(self):
        subprocess.call(['gcc' if self._src_file.endswith('.c') else 'g++',
                         self._src_file, '-o', self._bin_file])

    def runTest(self):
        with open(self._in_file) as stdin_fd:
            with open(self._tmp_file, 'w') as stdout_fd:
                subprocess.call([self._bin_file],
                                stdin=stdin_fd, stdout=stdout_fd)
        self.compareOutput()

    def tearDown(self):
        super().tearDown()
        if os.path.isfile(self._bin_file):
            os.remove(self._bin_file)


class JavaTestHandler(BaseTestHandler):

    extensions = ('.java', )

    def setUp(self):
        subprocess.call(['javac', self._src_file])

    def runTest(self):
        classname = os.path.splitext(os.path.basename(self._src_file))[0]
        with open(self._in_file) as stdin_fd:
            with open(self._tmp_file, 'w') as stdout_fd:
                subprocess.call(['java', '-cp', self._src_dir,  classname],
                                stdin=stdin_fd, stdout=stdout_fd)
        self.compareOutput()

    def tearDown(self):
        super().tearDown()
        classfile = os.path.splitext(self._src_file)[0] + '.class'
        if os.path.isfile(classfile):
            os.remove(classfile)


def main():
    handlers = {}
    for handler_cls in BaseTestHandler.__subclasses__():
        for extension in handler_cls.extensions:
            handlers[extension] = handler_cls
    suite = unittest.TestSuite()
    for dirpath, dirnames, filenames in os.walk(ALGORITHMS_DIR):
        if dirpath != ALGORITHMS_DIR:
            for filename in filenames:
                extension = os.path.splitext(filename)[1]
                if extension in handlers:
                    src_file = os.path.join(dirpath, filename)
                    handler = handlers[extension](src_file)
                    suite.addTest(handler)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    main()
