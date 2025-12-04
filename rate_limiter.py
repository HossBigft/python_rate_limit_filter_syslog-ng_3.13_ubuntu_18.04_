#!/usr/bin/env python
import time

class TokenBucket:
    def __init__(self, rate=10000):
        self.rate = rate   # type: int
        self.tokens = 0.0  # type: float
        self.last_sighting = time.time()  # type: float
           
    def refill_tokens(self):
        now = time.time()
        elapsed = now - self.last_sighting  
        
        if elapsed >= 1:  
            num_refills = int(elapsed)  
            tokens_to_add = num_refills * self.rate  
        
            self.tokens += tokens_to_add
            self.tokens = min(self.rate, self.tokens)
            
            self.last_sighting = now
    
    
    def has_tokens(self, amount):
        return amount <= self.tokens

    def consume(self, amount):
        self.refill_tokens()
        if self.has_tokens(amount):
            self.tokens -= amount
            return True

        return False


class RateLimiter(object):
    def __init__(self):
        self.max_lines_per_second = 10
        self.domains = {}  # type: dict[str, TokenBucket]
    def init(self, options):
        if "max_logs_per_second" in options:
            self.max_lines_per_second = int(options["max_logs_per_second"])
        return True


    def parse(self, log_message):
        site_domain = log_message["PROGRAM"]  # type: str
        if site_domain not in self.domains:
            self.domains[site_domain] = TokenBucket(rate=self.max_lines_per_second)
        bucket = self.domains[site_domain]  # type: TokenBucket
        return bucket.consume(1)
    