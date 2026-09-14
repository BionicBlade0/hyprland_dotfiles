import os
import random
import subprocess


# HYPRPAPER
WALLPAPER_PATH: str = "/mnt/hiroshi/Documents/Wallpapers/Anime"
# HYPRPAPER_CONFIG_PATH: str = "/home/hiroshi/.config/hypr/hyprpaper.conf"


wallpapers: list[str] = []


def list_files_recursively(path: str) -> None:

    entry: str
    for entry in os.listdir(path):
        full_path: str = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursively(full_path)
        else:
            wallpapers.append(full_path)


list_files_recursively(WALLPAPER_PATH)
wallpaper_count: int = len(wallpapers)

random_number: int = random.randint(0, wallpaper_count - 1)
selected_wallpaper: str = wallpapers[random_number]


subprocess.run(f"hyprctl hyprpaper wallpaper ,{selected_wallpaper}", shell=True)

# HYPRLOCK
HYPRLOCK_CONFIG_PATH: str = "/home/hiroshi/.config/hypr/hyprlock.conf"
hyprlock_config: str = r"""
# # BACKGROUND
background {
    monitor =
    path =
    blur_size = 4
    blur_passes = 2
}

# shape {
#     monitor =
#     size = 3840, 2160
#     color = rgba(0, 0, 0, 0.7)
#     position = 0, 0
# }

# GENERAL
general {
    hide_cursor = true
    disable_loading_bar = true
    # fractional_scaling = 1
}

# INPUT FIELD
input-field {
    monitor =
    dots_size = 0.2
    size = 300, 100
    outer_color = rgba(0, 0, 0, 0)
    inner_color = rgba(0, 0, 0, 0)
    font_color = rgb(255, 255, 255)
    check_color = rgba(0, 0, 0, 0)
    fail_color = rgba(0, 0, 0, 0) # if authentication failed, changes outer_color and fail message color
    halign = center
    valign = center
    position = 0, -100
    placeholder_text =  # Text rendered in the input box when it's empty.
    capslock_color = rgba(0, 0, 0, 0)
    # outline_thickness = 3
}

# DATE
label {
  monitor =
  text = cmd[update:1000] echo "$(date +"%A, %B %d")"
  font_size = 40
  font_family = Fira Code Bold
  position = 0, 200
  halign = center
  valign = center
}

# TIME
label {
  monitor =
  text = cmd[update:1000] echo "$(date +"%-I:%M %p")"
  font_size = 100
  font_family = Fire Code Bold
  position = 0, 100
  halign = center
  valign = center
}"""

hyprlock_config = hyprlock_config.replace("path =", f"path = {selected_wallpaper}")

with open(HYPRLOCK_CONFIG_PATH, "w") as hyprlock_config_file:
    hyprlock_config_file.write(hyprlock_config)
