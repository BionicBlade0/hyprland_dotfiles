import subprocess

lid_status: bytes = subprocess.check_output(
    "cat /proc/acpi/button/lid/LID0/state", shell=True
)

if lid_status == b"state:      closed\n":
    subprocess.call("hyprctl keyword monitor 'eDP-1, disable'", shell=True)
else:
    subprocess.call("hyprctl keyword monitor 'eDP-1, preferred, auto, 1'", shell=True)
