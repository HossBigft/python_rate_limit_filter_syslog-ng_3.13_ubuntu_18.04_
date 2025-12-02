#!/usr/bin/env python3
import time

class RateLimiter(object):
    def __init__(self):
        self.max_lines_per_second = 10
        self.last_time = time.time()
        self.lines_this_second = 0
    
    def init(self, options):
        if "max_logs_per_second" in options:
            self.max_lines_per_second = int(options["max_logs_per_second"])
        return True
    
    def deinit(self):
        pass
    
    def parse(self, log_message):
        current_time = time.time()
        
        if current_time - self.last_time >= 1:
            self.last_time = current_time
            self.lines_this_second = 0
        
        if self.lines_this_second < self.max_lines_per_second:
            self.lines_this_second += 1
            return True  
        
        return False
