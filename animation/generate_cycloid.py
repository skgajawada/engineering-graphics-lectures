import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters for Cycloid (Diameter D = 50 mm -> Radius r = 25 mm)
r = 25
theta = np.linspace(0, 2 * np.pi, 200)

# Parametric equations for Cycloid
x = r * (theta - np.sin(theta))
y = r * (1 - np.cos(theta))

fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(-5, 170)
ax.set_ylim(-10, 60)
ax.set_aspect('equal')
ax.axis('off')

# Plot static base line and final curve trace
ax.plot([0, 160], [0, 0], color='magenta', linewidth=3, label="Directrix Line")
ax.plot(x, y, color='purple', linewidth=2.5, label="Cycloid Curve")

# Dynamic elements for animation
circle_patch = plt.Circle((0, r), r, color='blue', fill=False, linewidth=2, label="Rolling Circle")
ax.add_patch(circle_patch)
point_dot, = ax.plot([], [], 'ro', markersize=6, label="Tracing Point P")
radius_line, = ax.plot([], [], 'b-', linewidth=1)

def init():
    circle_patch.center = (0, r)
    point_dot.set_data([], [])
    radius_line.set_data([], [])
    return circle_patch, point_dot, radius_line

def animate(i):
    th = theta[i]
    cx = r * th
    cy = r
    circle_patch.center = (cx, cy)
    
    # Tracing point coordinates
    px = r * (th - np.sin(th))
    py = r * (1 - np.cos(th))
    
    point_dot.set_data([px], [py])
    radius_line.set_data([cx, px], [cy, py])
    return circle_patch, point_dot, radius_line

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(theta), interval=40, blit=True)

# Save as a looping GIF
ani.save('cycloid_animation.gif', writer='pillow', fps=30)
print("Cycloid animation GIF generated successfully!")
