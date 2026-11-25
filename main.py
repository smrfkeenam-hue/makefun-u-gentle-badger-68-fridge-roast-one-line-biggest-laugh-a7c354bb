"""Fridge Roast: one line roasting a smart fridge.

The joke aims at the fridge itself: a 3 a.m. firmware update, a
twenty-minute reboot that kills the ice cream, and an ice maker that
now holds cubes hostage until its app gets five stars.
"""

import os

ENTRY = "My fridge pushed a firmware update at 3 a.m., rebooted for twenty minutes while the ice cream surrendered, and now the ice maker only works if I rate its app five stars."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
