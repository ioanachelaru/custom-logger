# Custom-logger

The script `process_logger.py` attempts to run multiple processes, capture their output, and log it to separate files, while also allowing for filtered stdout output. 

## Description

### ProcessManager
This class is responsible for managing the processes. It accepts a list of commands to run, starts the processes based on those commands, reads their output, and logs it to temporary files.

### ProcessRunner
This class is responsible for running a single process. It accepts a command to run and spawns a new process to run said command.

### Logger
This class is responsible for logging the output of a process to a file. It also allows for filtering the stdout output based on a list of keywords passed down in the `filters.csv` file.

