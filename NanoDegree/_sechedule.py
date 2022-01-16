import subprocess

# Turn my computer on
subprocess.call(["/usr/bin/systemctl", "start", "laptop-mode.service"])

# Turn my computer off
subprocess.call(["/usr/bin/systemctl", "stop", "laptop-mode.service"])

# Reboot my computer
subprocess.call(["/usr/bin/systemctl", "reboot"])

# Logout of my computer
subprocess.call(["/usr/bin/systemctl", "logout"])