#!/usr/bin/env python3

import os
import itertools
import unittest
import subprocess


ALGORITHMS_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseTestHandler(unittest.TestCase):

    ext = None

    def __init__(self, src_file):
        super().__init__()
        self._src_file = src_file
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

    ext = '.py'

    def __init__(self, src_file):
        super().__init__(src_file)

    def runTest(self):
        with open(self._in_file) as stdin_fd:
            with open(self._tmp_file, 'w') as stdout_fd:
                subprocess.call(['python', self._src_file],
                                stdin=stdin_fd, stdout=stdout_fd)
        self.compareOutput()


def main():
    handlers = {}
    for handler_cls in BaseTestHandler.__subclasses__():
        handlers[handler_cls.ext] = handler_cls
    suite = unittest.TestSuite()
    for dirpath, dirnames, filenames in os.walk(ALGORITHMS_DIR):
        if dirpath != ALGORITHMS_DIR:
            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext in handlers:
                    src_file = os.path.join(dirpath, filename)
                    handler = handlers[ext](src_file)
                    suite.addTest(handler)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    main()
