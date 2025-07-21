import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import odeint

# --- SIR model differential equations ---
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Model parameters (initial)
N0 = 1000     # total population
I0 = 1        # initial infected
R0 = 0        # initial recovered
S0 = N0 - I0 - R0
beta0 = 0.4   # infection rate
gamma0 = 0.1  # recovery rate (1/days)
t_max = 160

# --- Time array ---
t = np.linspace(0, t_max, t_max)

# --- Figure and axes setup ---
fig, ax = plt.subplots(figsize=(9,6))
plt.subplots_adjust(left=0.07, right=0.98, bottom=0.27, top=0.92)
l_s, = ax.plot([], [], 'b-', lw=2, label='Susceptible')
l_i, = ax.plot([], [], 'r-', lw=2, label='Infected')
l_r, = ax.plot([], [], 'g-', lw=2, label='Recovered')
ax.legend()
ax.set_xlabel('Time /days')
ax.set_ylabel('Number of people')
ax.set_title('SIR Model Simulation')
ax.grid(True)

# --- Slider axes positions and colors ---
slider_color = 'whitesmoke'
slider_h = 0.032
slider_y0 = 0.13
slider_x0 = 0.12
slider_gap = 0.33
slider_w = 0.17

slider_defs = [
    # (left, bottom, width, height), min, max, initial, color, label
    ([slider_x0 + 0*slider_gap, slider_y0, slider_w, slider_h],   100,  5000000,    N0, 'tab:blue',   'Population (N)'),
    ([slider_x0 + 1*slider_gap, slider_y0, slider_w, slider_h],     1,   1000000,    I0, 'tab:red',    'Initial Infected'),
    ([slider_x0 + 2*slider_gap, slider_y0, slider_w, slider_h],     0,   500000,    R0, 'tab:green',  'Initial Recovered'),
    ([slider_x0 + 0*slider_gap, slider_y0-0.07, slider_w, slider_h], 0.05, 1.0, beta0, 'tab:orange', 'Infection rate (β)'),
    ([slider_x0 + 1*slider_gap, slider_y0-0.07, slider_w, slider_h], 0.01, 1.0, gamma0, 'tab:cyan', 'Recovery rate (γ)'),
]

sliders = []
for axpos, vmin, vmax, vinit, col, label in slider_defs:
    saxs = fig.add_axes(axpos, facecolor=slider_color)
    s = Slider(saxs, label, vmin, vmax, valinit=vinit, color=col)
    sliders.append(s)

# --- Update function ---
def update(val=None):
    N = sliders[0].val
    I0 = int(sliders[1].val)
    R0 = int(sliders[2].val)
    S0 = N - I0 - R0 if N - I0 - R0 >= 0 else 0
    beta = sliders[3].val
    gamma = sliders[4].val

    y0 = S0, I0, R0
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T

    l_s.set_data(t, S)
    l_i.set_data(t, I)
    l_r.set_data(t, R)
    ax.set_xlim(0, t_max)
    min_y = 0
    max_y = max(N, np.max([S.max(), I.max(), R.max()])) * 1.1
    ax.set_ylim(min_y, max_y)
    fig.canvas.draw_idle()


for s in sliders:
    s.on_changed(update)
update()

plt.show()
