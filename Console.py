#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2012, <Zerstoren>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import sublime
import sublime_plugin
import subprocess
import os

class Console(sublime_plugin.TextCommand):
    """
    This class - is listener subline text commands
    """

    terminal = 'gnome-terminal'
    execCommand = '-e'

    def run(self, edit):
        """
        Run analyze commands, to create console
        """
        
        # Catch file path, and clear bad url
        self.filePath = self.view.file_name().replace(' ', '\ ')
        # Get file name
        self.fileName = self.filePath.split('/')[-1]

        try:
            # check, is file withot or with extension
            self.ext = self.fileName.split('.')[-1]
        except Exception as e:
            self.ext = ''

        # Run save command, before run test
        sublime.active_window().run_command('save')

        # If extenstion as php, htm or html. Run this command in console
        if self.ext == 'php' or self.ext == 'htm' or self.ext == 'html':
            self.consolePHPexecute()
        elif self.ext == 'py':
            self.consolePyexecute()

    def consolePHPexecute(self):
        """
        Open the terminal for PHP
        """
        path = os.path.realpath('')  # get absolute path for current dir
        args = [self.terminal, self.execCommand, "python %s/_exec.py php '%s'" 
            % (path, self.filePath)]
        subprocess.Popen(args)

    def consolePyexecute(self):
        """
        Open the terminal for Python
        """
        path = os.path.realpath('')
        args = [self.terminal, self.execCommand, 
            "python %s/_exec.py python '%s'" % (path, self.filePath)]
        subprocess.Popen(args)