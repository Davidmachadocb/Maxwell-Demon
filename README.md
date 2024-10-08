# Maxwell's Demon Simulation

## Overview

This project simulates a **Maxwell's Demon** scenario where particles move within a two-dimensional space, with the goal of observing the evolution of **kinetic energy**, **entropy**, and **temperature** under different collision types (elastic and inelastic). The simulation visualizes the behavior of particles as they interact and pass through a "door," mimicking the thought experiment of Maxwell’s Demon.

The simulation is performed using **Python** with **Matplotlib** for visualization and animations. The project includes various utilities for calculating entropy, temperature, and resolving particle collisions.

## Features

- Simulates particle motion and interactions within a two-dimensional box.
- Visualizes particle movement, collisions, and temperature distribution over time.
- Calculates and plots:
  - **Spatial entropy**
  - **Temperature** for different regions (before and after the door).
- Supports both **elastic** and **inelastic** collisions between particles.

## Requirements

To run the simulation, the following Python libraries are required:

- `numpy`
- `matplotlib`

You can install these dependencies using `pip`:

```bash
pip install numpy matplotlib
```

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Maxwell-Demon.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Maxwell-Demon
   ```

3. Run the simulation script:

   ```bash
   python simulation.py
   ```

   By default, the simulation will use **elastic collisions**. To change the collision type, modify the `collision_type` argument in the script:

   ```python
   run_simulation(collision_type='inelastic')
   ```

## Project Structure

- **`simulation.py`**: Main script that runs the simulation and animates particle behavior, entropy, and temperature evolution over time.
- **`particle.py`**: Defines the `Particle` class with methods for movement and collision detection.
- **`entropy.py`**: Contains utility functions for calculating entropy and temperature in the system, as well as handling collisions between particles.
- **`plots.py`**: Includes plotting functions that generate graphs of entropy and temperature over time.

## Simulation Details

The simulation takes place in a two-dimensional box, where particles are assigned random positions and velocities. The box has a "door" at the center that selectively allows particles to pass through based on their velocity and position. 

The key behaviors modeled are:

- **Collisions**: Particles collide either elastically or inelastically, altering their velocities accordingly.
- **Temperature Zones**: The box is divided into two regions (blue and red zones). The temperature of each zone is calculated based on the average kinetic energy of the particles in that region.
- **Entropy Calculation**: Both **spatial entropy** (based on particle distribution) and **velocity-based entropy** are calculated.

## Output

The simulation produces real-time animations of the particles and, at the end of the simulation, generates plots showing:

- **Entropy over time**.
- **Temperature over time** for the entire box and the two separate regions (blue and red).

## Example Output

- **Entropy and Temperature Graph**: The `plot_entropia_temperatura` function visualizes how entropy and temperature evolve throughout the simulation.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

This project was created as part of a physics assignment exploring concepts related to entropy and thermodynamics. The simulation and calculations are based on the Maxwell's Demon thought experiment.
