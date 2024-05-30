# Shell
This project implements a simple command-line shell in Python. The shell allows users to execute both built-in commands and external programs, similar to what you would find in Unix-like shell environments. The implementation adheres to the SOLID principles, ensuring the code is modular, maintainable, and extensible.

# Features
  1. Built-in Commands:
       a. echo: Prints the provided arguments to the standard output.
       b. exit: Exits the shell with an optional exit code.
       c. type: Displays whether a command is a shell built-in or an external program and shows the path to the external program if found.
       d. pwd: Prints the current working directory.
       e. cd: Changes the current working directory to the specified path.

  2. External Commands:
       The shell can execute any external command available in the system's PATH.

# SOLID Principles
   1. Single Responsibility Principle (SRP):
         Each command is implemented as a separate class responsible only for executing that specific command.
         The Shell class is responsible for interpreting user input and coordinating the execution of commands.

   2. Open/Closed Principle (OCP):
         The design allows new commands to be added easily by creating new classes that implement the Command interface without modifying existing code.

   3. Liskov Substitution Principle (LSP):

         All command classes adhere to the Command interface, allowing them to be used interchangeably within the shell.

   4. Interface Segregation Principle (ISP):

        The Command interface is kept simple with a single execute method, ensuring that implementing classes are not burdened with unnecessary methods.

   5. Dependency Inversion Principle (DIP):

        The TypeCommand class depends on an abstraction (the Command interface) rather than a concrete implementation, allowing it to interact with any command.

# Project Structure

  1. Main Shell Class:

        Shell: Coordinates command execution, handles user input, and manages built-in commands.

  2. Command Interface:

        Command: An abstract base class with an execute method that all command classes implement.

  3. Built-in Command Classes:

        a. EchoCommand: Implements the echo command.
        b. ExitCommand: Implements the exit command.
        c. TypeCommand: Implements the type command, checking if a command is built-in or external.
        d. PwdCommand: Implements the pwd command.
        e. CdCommand: Implements the cd command.
