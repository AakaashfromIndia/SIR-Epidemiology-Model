# SIR Epidemiology Model Simulation

![SIR Epidemology - Made with Clipchamp](https://github.com/user-attachments/assets/5fab5d6f-3aa6-4374-aa39-7623c0c83ce9)

## Overview

This project provides an interactive simulation of the **SIR epidemiological model**, widely used for modeling the spread of infectious diseases in a closed population. The model segments the population into three categories: **Susceptible (S)**, **Infected (I)**, and **Recovered (R)**, and tracks their dynamics over time using the classic SIR differential equations.
<img width="850" height="1036" alt="SIR-model-Schematic-representation-differential-equations-and-plot-for-the-basic-SIR" src="https://github.com/user-attachments/assets/de3910d8-340a-4713-be23-af0956910f5c" />

The simulation features real-time visualization with sliders to adjust initial epidemic conditions and disease transmission parameters.

## Sliders

- Total population (N)
- Initial number of infected (I₀)
- Initial number of recovered (R₀)
- Infection rate (β)
- Recovery rate (γ)

## How It Works

- SIR Model Equations:
  <img width="850" height="525" alt="image" src="https://github.com/user-attachments/assets/24d054ac-99ee-441d-ab4b-0cf608b14892" />
- The simulation uses `odeint` from `scipy.integrate` to solve the coupled ordinary differential equations for given initial conditions and parameters.
- Visualization updates in real time to show:
  - Susceptible (blue curve)
  - Infected (red curve)
  - Recovered (green curve)
- Sliders below the plot allow you to interactively adjust parameters and observe different epidemic curves.

## Usage

1. **Clone the repository or save the script:**
   - Save the provided Python script (`SIR-Epidemology.py`) to your local directory.

2. **Install dependencies:**
   ```bash
   pip install numpy matplotlib scipy
   ```

3. **Run the simulation:**
   ```bash
   python SIR-Epidemology.py
   ```

4. **Adjust parameters:** Use the sliders in the GUI to modify population size, initial conditions, infection rate, and recovery rate.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy
