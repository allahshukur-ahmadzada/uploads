#!/usr/bin/env python3

# Simple Checkmk local check script

# Define the service name and dummy status message
service_name = "Dummy_Service"
status_message = "OK - This is a dummy check."

# Output the check result
# Format: <return_code> <service_name> - <status_output>
print(f"0 {service_name} - {status_message}")
