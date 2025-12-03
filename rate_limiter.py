#!/usr/bin/env python
import time

class DomainTracker:
    def __init__(self):
        self.counter = 0  # type: int
        self.first_sighting = time.time()  # type: float

    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0
        self.first_sighting = time.time()


class RateLimiter(object):
    def __init__(self):
        self.max_lines_per_second = 10
        self.domains = {}  # type: dict[str, DomainTracker]

    def init(self, options):
        if "max_logs_per_second" in options:
            self.max_lines_per_second = int(options["max_logs_per_second"])
        return True

    def deinit(self):
        pass

    def parse(self, log_message):
        current_time = time.time()  # type: float
        site_domain = log_message["PROGRAM"]  # type: str

        if site_domain not in self.domains.keys():
            self.domains[site_domain] = DomainTracker()

        tracker = self.domains[site_domain]

        if current_time - tracker.first_sighting >= 1:
            tracker.reset()

        tracker.increment()

        return tracker.counter <= self.max_lines_per_second
