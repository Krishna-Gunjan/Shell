# Shell
This project implements a simple command-line shell. The shell grants the users the ability to execute both built-in commands and external programs.

# Features
  1. ## Built-in Commands:

       a. **echo:** Prints the provided arguments to the standard output.
     
       b. **exit:** Exits the shell with an optional exit code.
     
       c. **type:** Displays whether a command is a shell built-in or an external program and shows the path to the external program if found.
     
       d. **pwd:** Prints the current working directory.
     
       e. **cd:** Changes the current working directory to the specified path.
     
       f. **dir:** Displays all the Files and Folders in the specified location.
     
       g. **copy:** Copies all the Files and Folders name in the specified Location.
     
       h. **append:** Open files in another directory as if they were located in the current directory.
     
       i. **clear:** Clears the screen

  3. External Commands:
       The shell can execute any external command available in the system's PATH.

# Project Structure

  1. **Main Shell Class:**

        Shell: Coordinates command execution, handles user input, and manages built-in commands.

  2. **Command Interface:**

        Command: An abstract base class with an execute method that all command classes implement.

  3. **Built-in Command Classes (Derived Class from Command Class):**

        a. EchoCommand
     
        b. ExitCommand
     
        c. TypeCommand
     
        d. PwdCommand
     
        e. CdCommand

        f. DirCommand

        g. CopyCommand

        h. AppendCommand

        i. ClearCommand
