

import time
import json
from contextlib import contextmanager

_global_timing_stack = []
_global_times_dict = {
    "sums":{},
    "counts":{}
}
_global_timing_keys = []

def print_time_statistics(verbose=True):
    global _global_timing_stack
    global _global_times_dict
    global _global_timing_keys
    if verbose:
        print(json.dumps(_global_times_dict))
    if len(_global_timing_stack) != 0:
        print(f"Warning: bug in the timing utils, the stack at statistics printing time {time.time()}:\n" + str(_global_timing_stack))
    
    max_key_length = max(map(len, _global_timing_keys))
    print(" " * (max_key_length - len("func / stat")) + " func / stat | runtime(sc) | enters  | average runtime (ms)")
    sum_runtime = 0
    short_runtimes = []
    for key in sorted(_global_timing_keys):
        runtime = _global_times_dict["sums"][key]
        count = _global_times_dict["counts"][key]
        avg = runtime / count * 1000
        sum_runtime += runtime
        if runtime < 0.1:
            short_runtimes.append(key)
            continue
        print(f"{key}:" + " " * (max_key_length - len(key)) + f" | {runtime:11.2f} | {count:7.0f} | {avg:9.4f}")
    print(f"{sum_runtime=}")
    if verbose:
        print(f"{short_runtimes=}")

def start_timing(key):
    global _global_timing_stack
    global _global_times_dict
    global _global_timing_keys
    if key not in _global_timing_keys:
        _global_timing_keys.append(key)
        _global_times_dict["sums"][key] = 0.0
        _global_times_dict["counts"][key] = 0
    _global_timing_stack.append([key, time.time(), 0.0])

def finish_timing():
    key, start_time, recursive_time = _global_timing_stack.pop(-1)
    time_spent = time.time() - start_time - recursive_time
    _global_times_dict["sums"][key] += time_spent
    _global_times_dict["counts"][key] += 1
    if _global_timing_stack:
        _global_timing_stack[-1][2] += time.time() - start_time

@contextmanager
def timing_manager(key):
    start_timing(key)
    yield
    finish_timing()

@contextmanager
def time_without_stack(marker):
    start = time.time()
    yield
    print(f"Timing for {marker=} was {time.time()-start:.2f} (sec)")