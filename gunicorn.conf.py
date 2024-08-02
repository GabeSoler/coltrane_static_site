import multiprocessing

def when_ready(server):
    # touch app-initialized when ready
    open("/tmp/app-initialized", "w").close()

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

bind = "0.0.0.0:80"
workers = multiprocessing.cpu_count() * 2 + 1

workers = 2


bind = "unix:///tmp/nginx.socket"
workers = 3