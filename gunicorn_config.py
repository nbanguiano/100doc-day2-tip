bind = "unix:/tmp/day2-tip.sock"  # Unix socket instead of TCP port
workers = 3
timeout = 120
worker_class = 'sync'
forwarded_allow_ips = '*'  # Trust X-Forwarded-* headers
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
accesslog = "access.log"  # Log file for access logs
errorlog = "error.log"    # Log file for error logs

# Set Flask environment
raw_env = ["FLASK_ENV=production"]
