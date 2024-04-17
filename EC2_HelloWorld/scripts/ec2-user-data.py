#!/usr/bin/python3
import subprocess

# Update system packages
subprocess.run(["yum", "update", "-y"])

# Install Apache HTTP server
subprocess.run(["yum", "install", "-y", "httpd"])

# Start Apache server
subprocess.run(["systemctl", "start", "httpd"])

# Enable Apache server to start on boot
subprocess.run(["systemctl", "enable", "httpd"])

# Create index.html file with "Hello, World"
with open('/var/www/html/index.html', 'w') as f:
    f.write("<h1>Hello, World from {}</h1>".format(subprocess.check_output(["hostname", "-f"]).decode().strip()))