"""Day 7 helper: turn the day-6 CSV into Blender keyframes.

How to use, inside Blender:
  1. Save your .blend file first (this script looks for the CSV next to
     it), and copy your brick_positions.csv into that same folder. If you
     lost yesterday's file, use the sample CSV that ships with this script.
  2. Click your brick object in the viewport so it is the active object.
  3. Open the Scripting tab, click Open, pick this file, press Run.
  4. Press Spacebar over the timeline: the brick slides.

The CSV has one row every 0.1 s of simulation time. At 24 frames per
second, time t lands on frame 1 + t * 24, so 10 s becomes 240 frames.
"""

import csv
from pathlib import Path

import bpy

FPS = 24
CSV_NAME = "brick_positions.csv"

csv_path = Path(bpy.path.abspath("//")) / CSV_NAME
if not csv_path.is_file():
    raise FileNotFoundError(
        f"Could not find {CSV_NAME} next to your .blend file (looked at {csv_path}). "
        "Save the .blend file first, then copy the CSV into the same folder."
    )

brick = bpy.context.active_object
if brick is None:
    raise RuntimeError("Click your brick object in the viewport first, then run the script.")

scene = bpy.context.scene
scene.render.fps = FPS

last_frame = 1
with open(csv_path, newline="") as f:
    for row in csv.DictReader(f):
        t = float(row["t"])
        x = float(row["x"])
        frame = 1 + round(t * FPS)
        brick.location.x = x
        brick.keyframe_insert(data_path="location", frame=frame)
        last_frame = max(last_frame, frame)

scene.frame_start = 1
scene.frame_end = last_frame
print(f"Keyframed '{brick.name}' from frame 1 to frame {last_frame}. Press Spacebar to play.")
