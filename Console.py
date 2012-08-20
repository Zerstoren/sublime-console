#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import subprocess
import os

class Console(sublime_plugin.TextCommand):
    def run(self, edit):
        self.filePath = self.view.file_name().replace(' ', '\ ')
        self.fileName = self.filePath.split('/')[-1]
        try:
            self.ext = self.fileName.split('.')[-1]
        except Exception as e:
            self.ext = ''

        sublime.active_window().run_command('save')
        if self.ext == 'php' or self.ext == 'htm' or self.ext == 'html':
            self.consolePHPsyntax()
        elif self.ext == 'py':
            self.consolePySyntax()

    def consolePHPsyntax(self):
        path = os.path.realpath('')
        args = ['gnome-terminal',"-e", "python %s/_exec.py php \'%s\'" % (path, self.filePath)]
        subprocess.Popen(args)

    def consolePySyntax(self):
        path = os.path.realpath('')
        args = ['gnome-terminal',"-e", "python %s/_exec.py python \'%s\'" % (path, self.filePath)]
        subprocess.Popen(args)