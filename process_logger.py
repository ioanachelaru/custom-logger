from ProcessManager import ProcessManager

def main():
    cmds = [
        """python -c "import sys, time; print('Starting'); sys.stderr.write('Warning: this is a test\\n'); time.sleep(1); print('A process'); sys.stderr.write('Error: something went wrong\\n'); time.sleep(1); print('Finishing')" """,
        """python -c "import sys, time; print('Another start'); sys.stderr.write('Another warning\\n'); time.sleep(2); print('Another process'); sys.stderr.write('Another error message\\n')" """
    ]

    process_manager = ProcessManager(cmds)
    process_manager.run()


if __name__ == "__main__":
    main()