#!/usr/bin/env python
import time

class TokenBucket:
    __slots__ = ('rate', 'tokens', 'last_sighting')
    def __init__(self, last_sighting, rate=10000):
        self.rate = rate   # type: int
        self.tokens = 0.0  # type: float
        self.last_sighting =  last_sighting# type: float
           


class RateLimiter(object):
    __slots__ = ('max_lines_per_second', 'domains')
    
    def __init__(self):
        self.max_lines_per_second = 10
        self.domains = {}  # type: dict[str, TokenBucket]
        
    def init(self, options):
        if "max_logs_per_second" in options:
            self.max_lines_per_second = int(options["max_logs_per_second"])
        return True


    def parse(self, log_message):
        now = time.time()
        site_domain = log_message["PROGRAM"]  # type: str
        if site_domain not in self.domains:
            self.domains[site_domain] = TokenBucket(rate=self.max_lines_per_second, last_sighting=now)
        bucket = self.domains[site_domain]  # type: TokenBucket
        elapsed = now - bucket.last_sighting
        
        if elapsed >= 1.0:
            bucket.tokens = min(bucket.rate, bucket.tokens + int(elapsed) * bucket.rate)
            bucket.last_sighting = now
        
        if bucket.tokens >= 1.0:
            bucket.tokens -= 1.0
            return True
        
        return False
    