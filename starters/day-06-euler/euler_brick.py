"""Day 6 starter: the sliding brick, simulated with forward Euler.

A brick of mass m = 2 kg sits on ice (no friction). We push it with a
constant force f = 10 N for 10 seconds. This script marches forward in
time with forward Euler, plots position versus time, and saves (t, x)
to a CSV file that tomorrow's Blender movie will read.

Fill in the three TODO lines. Everything else is done for you.

Run it with:
    conda activate camp
    python euler_brick.py
"""

import csv

import matplotlib.pyplot as plt

# --- the physical setup -------------------------------------------------
m = 2.0       # mass of the brick, kg
f = 10.0      # constant push, N
t_end = 10.0  # how long we push, s
h = 0.1       # time step, s (later, try 0.01 and 1.0; what changes?)

# --- the state of the brick at t = 0 ------------------------------------
t = 0.0
x = 0.0       # position, m
v = 0.0       # velocity, m/s

ts = [t]
xs = [x]

# --- the forward Euler loop ---------------------------------------------
while t < t_end - 1e-9:
    a = 0.0        # TODO 1: Newton's second law says m * a = f, so a = ?

    x_new = x      # TODO 2: new position = old position + h * (old velocity)
    v_new = v      # TODO 3: new velocity = old velocity + h * a

    x = x_new
    v = v_new
    t = t + h

    ts.append(t)
    xs.append(x)

# --- check against the exact answer -------------------------------------
# This problem is simple enough to solve with pencil and paper:
# x(t) = 0.5 * (f / m) * t^2. Real simulations rarely have this luxury.
x_exact = 0.5 * (f / m) * t_end**2
print(f"Euler says x({t_end:g}) = {xs[-1]:.2f} m; the exact answer is {x_exact:.2f} m")

# --- save the CSV that feeds tomorrow's Blender movie --------------------
with open("brick_positions.csv", "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["t", "x"])
    for ti, xi in zip(ts, xs):
        writer.writerow([f"{ti:.3f}", f"{xi:.6f}"])
print("Wrote brick_positions.csv (keep it, day 7 needs it)")

# --- plot ----------------------------------------------------------------
plt.plot(ts, xs)
plt.xlabel("time t [s]")
plt.ylabel("position x [m]")
plt.title("Sliding brick, forward Euler")
plt.grid(True)
plt.show()
