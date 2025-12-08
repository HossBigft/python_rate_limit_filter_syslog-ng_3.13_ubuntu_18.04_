from line_profiler import LineProfiler
from rate_limiter import RateLimiter

def run_test():
    rl = RateLimiter()
    rl.init({"max_logs_per_second": 10000})

    msg = {"PROGRAM": "cwjbaqkj.com [Thu Dec  4 19:12:43 +05 2025] [error] [pid 19652] sapi_apache2.c(325): [client 127.0.0.1:0] PHP Warning: mysql_query(): Access denied for user ''@'localhost' (using password: NO) in /home/c/clientid/example/functions_rc/functions-inner.php on line 299"}
    for _ in range(2000000):
        rl.parse(msg)

lp = LineProfiler()
lp.add_function(RateLimiter.parse)
lp.run('run_test()')
lp.print_stats()