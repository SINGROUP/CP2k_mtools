# -*- coding: utf-8 -*-
#! /usr/bin/env python

from subprocess import check_output, CalledProcessError

class CP2K_restart:
    def __init__(self):
        self.project_name = None
        self.working_directory = None
        self.cp2k_command = None
        self.restart_file = None


    def get_output_path(self):
        return self.working_directory + "/" + self.project_name + ".out"


    def get_restart_file_path(self):
        if self.restart_file is None:
            return self.working_directory + "/" + self.project_name + "-1.restart"
        else:
            return self.restart_file


    def run(self):
        output_file = self.get_output_path()
        restart_file = self.get_restart_file_path()
        command_string = self.cp2k_command + " -i {}".format(restart_file) + \
                            " -o {}".format(output_file)
        print ">> Running CP2K (restarting from previous calculation):"
        print "   -CP2K command: {}".format(command_string)
        try:
            check_output(command_string, shell=True, cwd=self.working_directory)
        except CalledProcessError:
            print "Error occured during CP2K calculation."
            raise
        print ">> CP2K calculation finished succesfully!"
