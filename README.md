🌌 2D Orbital Simulator (Python + Pygame)

A fun little orbital simulator made using Python and Pygame where celestial bodies interact using gravity and orbit each other in real time.

Started as a small gravity experiment and slowly evolved into a proper physics-heavy simulation project 😆

---

✨ Current Features

- 🌍 True n-body gravity simulation (every body attracts every other body)
- 🪐 Multiple planets orbiting a central sun
- 📈 Leapfrog integration for cleaner and more stable orbits
- 🎥 Camera panning
- 🛸 Zoom controls
- 🌠 Orbit trails
- ⚡ Adjustable simulation speed
- 🖥️ Real-time HUD with simulation stats

---

🧠 Physics Used

The simulator uses Newton's Law of Universal Gravitation:

F = G * (m₁ × m₂) / r²

Each body experiences gravitational attraction from every other body.

Acceleration is calculated using:

a = F / m

To improve long-term orbital stability, the simulator uses Leapfrog Integration (Velocity Verlet style) instead of basic Euler integration.

This helps reduce:

- Orbital drift
- Energy loss/gain over time
- Weird spiraling or unstable orbits

---

☀️ Current Simulation Setup

The current simulation contains:

- ☀️ 1 Sun
- 🪐 5 Planets

Each body stores:

- Position ("x", "y")
- Velocity ("vx", "vy")
- Acceleration ("ax", "ay")
- Mass
- Radius
- Color
- Trail history

---

🎮 Controls

Camera Controls

- W / A / S / D → Move camera
- I → Zoom in
- O → Zoom out

---

📊 HUD Displays

Current HUD shows:

- FPS
- Number of bodies
- Zoom level
- Simulation speed
- Physics integrator

---

🛠️ Built With

- Python 🐍
- Pygame 🎮
- Lots of math and physics 😵‍💫

---

🚀 Planned Additions

- Interactive body creation
- Collision / merger physics
- Follow-body camera
- Barnes–Hut optimization for larger simulations

Still very much a work in progress, but also a really fun project to build and learn from :3
