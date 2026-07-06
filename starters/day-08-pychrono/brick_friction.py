"""Day 8 starter: the same sliding brick, now in PyChrono with friction.

Monday's setup returns: a 2 kg brick pushed with a constant 10 N for
10 seconds. But the ice is gone. The brick now rests on a floor with real
contact and friction, and the physics engine (not your Euler loop) does
the integration, the contact detection, and the friction.

Run it with:
    conda activate camp
    python brick_friction.py

Things to try (one number flips the story):
  - MU = 0.6: friction can resist more than the 10 N push; the brick
    never moves.
  - MU = 0.0: Monday's ice comes back; expect about 250 m at t = 10 s.

The brick slides out of the camera view after a few seconds; that is
fine. The plot at the end tells the whole 10-second story.
"""

import matplotlib.pyplot as plt
import pychrono as chrono
import pychrono.irrlicht as chronoirr

MU = 0.3       # friction coefficient between brick and floor
M = 2.0        # brick mass, kg
F_PUSH = 10.0  # constant push along +x, N
T_END = 10.0   # simulation length, s

# The system: the world that holds the bodies, forces, and contacts
sys = chrono.ChSystemNSC()
sys.SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)
sys.SetGravitationalAcceleration(chrono.ChVector3d(0, -9.81, 0))

# One shared contact material; it carries the friction coefficient
mat = chrono.ChContactMaterialNSC()
mat.SetFriction(MU)

# The floor: a long fixed box whose top surface sits at y = 0
floor = chrono.ChBodyEasyBox(300, 0.2, 4, 1000, True, True, mat)
floor.SetPos(chrono.ChVector3d(140, -0.1, 0))
floor.SetFixed(True)
floor.GetVisualShape(0).SetTexture(chrono.GetChronoDataFile("textures/concrete.jpg"))
sys.Add(floor)

# The brick: 0.4 x 0.2 x 0.2 m box; density chosen so its mass is M = 2 kg
brick_density = M / (0.4 * 0.2 * 0.2)
brick = chrono.ChBodyEasyBox(0.4, 0.2, 0.2, brick_density, True, True, mat)
brick.SetPos(chrono.ChVector3d(0, 0.1, 0))
sys.Add(brick)

# The constant push along +x. Order matters: attach the force to the
# body first, then configure it.
push = chrono.ChForce()
brick.AddForce(push)
push.SetF_x(chrono.ChFunctionConst(F_PUSH))

# Live 3D visualization
vis = chronoirr.ChVisualSystemIrrlicht()
vis.AttachSystem(sys)
vis.SetWindowSize(1024, 768)
vis.SetWindowTitle("Day 8: sliding brick with friction")
vis.Initialize()
vis.AddSkyBox()
vis.AddCamera(chrono.ChVector3d(-2, 1.5, -4), chrono.ChVector3d(2, 0.1, 0))
vis.AddTypicalLights()

# March forward in time; the engine handles contact and friction each step
ts = []
xs = []
while vis.Run() and sys.GetChTime() < T_END:
    vis.BeginScene()
    vis.Render()
    vis.EndScene()
    sys.DoStepDynamics(5e-3)
    ts.append(sys.GetChTime())
    xs.append(brick.GetPos().x)

print(f"At t = {sys.GetChTime():.2f} s the brick is at x = {brick.GetPos().x:.2f} m")
print("Monday's frictionless answer was 250 m. Friction is the difference.")

# Compare against Monday: the exact frictionless curve x(t) = 0.5*(f/m)*t^2
plt.plot(ts, xs, label=f"PyChrono, friction MU = {MU}")
plt.plot(ts, [0.5 * (F_PUSH / M) * t**2 for t in ts], "--", label="Monday: no friction (exact)")
plt.xlabel("time t [s]")
plt.ylabel("position x [m]")
plt.title("The same brick, with and without friction")
plt.legend()
plt.grid(True)
plt.show()
