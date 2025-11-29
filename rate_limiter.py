#!/usr/bin/env python3
import sys

output_file_path = "/tmp/rate_limit_passed.log"

with open(output_file_path, "a") as f_out:
    for line in sys.stdin:
        f_out.write(line)