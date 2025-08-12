# 2D Gravitational Physics Simulator


## 🚀 About The Project

This project is an interactive 2D space simulation built in Python and Pygame that models celestial mechanics. It provides a dynamic environment where users can launch spacecraft and observe their trajectories as they are influenced by the gravitational pull of a central planet, all calculated in real-time based on Newtonian physics.

This project began as a personal challenge to apply the mathematical and physical principles I learned during my JEE preparation into a functional, interactive software application.


<h3>Features</h3>

- <b>Gravitational Physics Simulation:</b> Simulates gravitational attraction between a spacecraft and a planet based on Newton's law of gravitation 
- <b>Interactive User Interface</b> Users can launch spacecraft by clicking on the screen, and setting their initial direction.
- <b>Visual Feedback: </b>Provides visual feedback with images for spacecraft and planets, along with sound effects upon collision.
---

## ✨ Key Concepts Demonstrated

This project is not just a simple game, but an implementation of a core physics engine. The key skills demonstrated are:

* **Math-to-Code Translation:** Translating the abstract mathematical formula for Newton's Law of Universal Gravitation ($F = G \frac{m_1 m_2}{r^2}$) into a working physics model.
* **Vector Mathematics:** Utilizing vector-based calculations for position, velocity, and acceleration to accurately model the forces and update object trajectories each frame.
* **Object-Oriented Programming (OOP):** Structuring the simulation with distinct classes for celestial bodies (Planet, Spacecraft), each with its own properties and methods.
* **Real-Time Simulation Loop:** Managing game state, handling user input (mouse clicks), and updating physics calculations within an efficient main loop.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Library:** Pygame
* **Core Concepts:** Object-Oriented Programming (OOP), Vector Mathematics, Physics Simulation

---

## ⚙️ Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python 3.8+ and pip installed on your system.

### Installation

1.  Clone the repository:
    ```sh
    git clone [https://github.com/Yashwanss/2D-GravitySimulator.git](https://github.com/Yashwanss/2D-GravitySimulator.git)
    ```
2.  Navigate into the project directory:
    ```sh
    cd 2D-GravitySimulator
    ```
3.  Install the necessary packages:
    ```sh
    pip install pygame
    ```

### Running the Simulation

Execute the `main.py` file to start the simulation:
```sh
python main.py
```


## Acknowledgments

- Thanks to [Pygame](https://www.pygame.org/) for providing the library to create this simulation.
- Inspiration is drawn from physics simulations and space exploration concepts.

## 📖 Usage

   - Simply click anywhere on the screen to launch a spacecraft from that position.

   - The spacecraft's initial velocity is determined by the vector from the screen center to your mouse click.

   - Observe how the spacecraft's path bends as it interacts with the planet's gravitational field.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Yashwanss/2D-GravitySimulator/issues).
