import sys
import os
import subprocess
from abc import ABC, abstractmethod
import pyperclip

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class EchoCommand(Command):
    def execute(self, args):
        print(" ".join(args))

class ExitCommand(Command):
    def execute(self, args):
        try:
            exit_code = int(args[0]) if args else 0
        except ValueError:
            exit_code = 0
        sys.exit(exit_code)

class TypeCommand(Command):
    def __init__(self, builtins):
        self.builtins = builtins

    def execute(self, args):
        if not args:
            return
        command = args[0]
        if command in self.builtins:
            print(f"{command} is a shell builtin")
        elif command_path := self.find_command_in_path(command):
            print(f"{command} is {command_path}")
        else:
            print(f"{command} not found")

    def find_command_in_path(self, command):
        path_dirs = os.environ.get("PATH", "").split(os.pathsep)
        for dir in path_dirs:
            potential_path = os.path.join(dir, command)
            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                return potential_path
        return None

class PwdCommand(Command):
    def execute(self, args):
        print(os.getcwd())

class CdCommand(Command):
    def execute(self, args):
        global CURRENT_PATH
        path = ''.join(args)
        path = os.path.expanduser(path)
        try:
            os.chdir(path)
            CURRENT_PATH = path
        except FileNotFoundError:
            print(f"cd: {path}: No such file or directory")

class DirCommand(Command):
    def execute(self, args=None):
        global CURRENT_PATH
        if args:
            dir_list = os.listdir(''.join(args))
        else:
            dir_list = os.listdir(CURRENT_PATH)
        for dir in dir_list:
            print(dir) 
        return dir_list 

class CopyCommand(Command):
    def execute(self, args):
        global CURRENT_PATH
        if args:
            dir_list = os.listdir(''.join(args))
        else:
            dir_list = os.listdir(CURRENT_PATH)
        pyperclip.copy('\n'.join(dir_list))

class AppendCommand(Command):
    def execute(self, args):
        try:
            with open(''.join(args)) as file:
                print(file.read())
        except FileNotFoundError:
            print(f"{''.join(args)} not found")

class ClearCommand(Command):
    def execute(self, args):
        os.system('cls')

class Shell:
    def __init__(self):
        self.builtins = {}
        self.builtins["echo"] = EchoCommand()
        self.builtins["exit"] = ExitCommand()
        self.builtins["type"] = TypeCommand(self.builtins)
        self.builtins["pwd"] = PwdCommand()
        self.builtins["cd"] = CdCommand()
        self.builtins["dir"] = DirCommand()
        self.builtins["copy"] = CopyCommand()
        self.builtins['append'] = AppendCommand()
        self.builtins['clear'] = ClearCommand()

    def execute_command(self, command_line):
        parts = command_line.split()
        if not parts:
            return
        cmd_name = parts[0]
        cmd_args = parts[1:]
        if cmd_name in self.builtins:
            self.builtins[cmd_name].execute(cmd_args)
        else:
            self.run_external_program(cmd_name, cmd_args)

    def run_external_program(self, program_name, program_args):
        try:
            result = subprocess.run([program_name] + program_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    print(line)
            else:
                for line in result.stderr.splitlines():
                    print(line, end="")
        except FileNotFoundError:
            print(f"{program_name}: command not found")
            
    def run(self):
        global CURRENT_PATH
        CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
        while True:
            sys.stdout.write(f"$ {CURRENT_PATH}>")
            sys.stdout.flush()
            try:
                command_line = input().strip()
                self.execute_command(command_line)
            except (EOFError, KeyboardInterrupt):
                print()
                break

if __name__ == "__main__":
    shell = Shell()
    shell.run()
