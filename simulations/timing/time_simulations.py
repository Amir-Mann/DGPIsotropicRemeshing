

import argparse
import os
import time

def run_commands(commands, reps=1):
    for command in commands:
        print(f"\nRunning command: {command}")
        start_time = time.time()
        for _ in range(reps):
        	os.system(command)
        end_time = time.time()
        
        elapsed_time = (end_time - start_time) / reps
        print(f"Execution time for '{command}': {elapsed_time:.2f} seconds. Over {reps} runs.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a list of commands and measure their execution time.")
    parser.add_argument('commands', nargs='+', type=str, help='List of commands to execute')
    parser.add_argument('-r', '--reps', type=int, default=1, help='Repetitions per command')
    
    args = parser.parse_args()
    
    run_commands(args.commands, reps=args.reps)
