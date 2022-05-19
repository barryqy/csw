#!/usr/bin/env python
import functions


# Check creds
functions.check_API_creds()

# Get all sensors
sensors = functions.get_sensors()

# Print sensors
functions.print_sensors(sensors)

