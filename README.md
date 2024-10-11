# Custom-logger

The attached python script (process_logger.txt) attempts to run multiple processes, capture their output, and log it to separate files. However, there are several issues with this code.
Your task is to identify the problems and explain in your reply to us. Then improve/extend the script addressing the mentioned problems and the following requirements:

- Write the child process output into temporary files instead of hardcoded filenames, ensure proper cleanup of the logfiles and error handling. Think of real-life use-cases when we’d like to keep the temporary logs rather than clean them up.

- Use python logging to decorate the child process output with timestamps, log-levels and process IDs.

- Implement logging to stdout handler, which will print just the output lines that contain the strings provided by user as arguments. Think of grep-like filter just for stdout.

- Improve thread synchronization and think whether we can utilize threads better, not just for reading and writing the output. Assume the processes are independent of each other, and time of completion may vary.

- Comments/doc-strings and debugging print-outs in the code are very welcome. You also may elaborate in Readme.md file and attach it to your code files.

