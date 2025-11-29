#!/usr/bin/env python3
import sys
import time

output_file_path = "/var/log/rate_limit_test"
MAX_LINES_PER_SECOND = 10

last_time = time.time()
lines_this_second = 0

with open(output_file_path, "a") as f_out:
    for line in sys.stdin:
        current_time = time.time()
        if current_time - last_time >= 1:
            last_time = current_time
            lines_this_second = 0

        if lines_this_second < MAX_LINES_PER_SECOND:
            f_out.write(line)
            f_out.flush()
            lines_this_second += 1
        # Excess lines are silently dropped