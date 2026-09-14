#!/bin/bash

power_in_microwatts=$(cat /sys/class/power_supply/BAT1/power_now)
power_in_watts=$((power_in_microwatts/1000000))
echo "$power_in_watts Watts"