import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.animation as animation
from matplotlib.cm import plasma
# line chart for mood over the week

days = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
mood = [5, 6, 4, 7, 8, 6, 9]

plt.plot(days, mood, marker="o", color='purple')
plt.title('My Mood Over the Week')
plt.ylabel('Mood Level (1-10)')
plt.grid(True)
plt.show()

# Pie chart for daily routine

labels = ['Sleep', 'School', 'Coding', 'Eating', 'Relaxing']
hours = [8, 6, 4, 2, 4]

plt.pie(hours, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("My Daily Routine")
plt.axis('equal')  # Keeps it a circle
plt.show()

# Random colors for bar chart

categories = ['A', 'B', 'C', 'D', 'E']
values = [random.randint(1, 10) for _ in categories]
colors = ['#'+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in categories]

plt.bar(categories, values, color=colors)
plt.title('Random Color Bars')
plt.show()

# Animated line chart

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # update the data.
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()

# Animated pulsating wave
# This is trippy as hell

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.cos(x))

def update(frame):
    line.set_ydata(np.cos(x + frame / 10) * np.sin(frame / 20))  # pulsating wave
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()

# What.

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame / 10) / np.cos(frame / 5))
    return line,

ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)
plt.show()

# Okay back to normal
# Animated sine and cosine waves with different frequencies

# Set up the plot
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)

# Create TWO lines
line1, = ax.plot(x, np.sin(x), label="wave 1")
line2, = ax.plot(x, np.cos(x), label="wave 2")
ax.legend()

# Update function
def update(frame):
    # Animate both lines differently
    line1.set_ydata(np.sin(x + frame / 10))
    line2.set_ydata(np.cos(x + frame / 20))
    return line1, line2

# Animate it!
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

plt.show()


# Have we reached the fourth dimension yet?
# Animated sine and cosine waves with different frequencies and phase shifts

# Set up the plot
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)

# Create TWO lines
line1, = ax.plot(x, np.sin(x), label="wave 1")
line2, = ax.plot(-x, -np.cos(x), label="wave 2")
ax.legend()

# Update function
def update(frame):
    # Animate both lines differently
    line1.set_ydata(np.sin(x + frame / 10))
    line2.set_ydata(-np.cos(x + frame / 10))
    return line1, line2

# Animate it!
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

plt.show()

# Animated multiple functions with scaling and shifting, still pretty cool

# Create figure and axis
fig, ax = plt.subplots()

# x values
x = np.linspace(0, 2 * np.pi, 200)

# Initial lines for multiple functions
line1, = ax.plot(x, np.sin(x), label='sin(x)')
line2, = ax.plot(x, np.cos(x), label='cos(x)')
line3, = ax.plot(x, np.sin(x) * np.cos(x), label='sin(x)*cos(x)')

# Set axis limits and legend
ax.set_ylim(-2, 2)
ax.legend(loc='upper right')

# Update function for animation
def update(frame):
    shift = frame / 10
    scale = np.cos(frame / 50)

    line1.set_ydata(np.sin(x + shift) / scale)
    line2.set_ydata(np.cos(x + shift) / scale)
    line3.set_ydata((np.sin(x + shift) * np.cos(x + shift)) / scale)
    return line1, line2, line3

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=300, interval=50, blit=True
)

plt.show()

# What is happening here?
# Animated sine, cosine, and tangent functions with limits to prevent overflow

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)  # <- This limits the y-axis to prevent tan(x) from exploding

# x values
x = np.linspace(0, 2 * np.pi, 1000)

# Initialize empty lines for each function
line_sin, = ax.plot([], [], label="sin(x)")
line_cos, = ax.plot([], [], label="cos(x)")
line_tan, = ax.plot([], [], label="tan(x)")

# Add legend
ax.legend()

# Animation init function
def init():
    line_sin.set_data([], [])
    line_cos.set_data([], [])
    line_tan.set_data([], [])
    return line_sin, line_cos, line_tan

# Animation update function
def update(frame):
    x_data = x[:frame]
    sin_data = np.sin(x_data)
    cos_data = np.cos(x_data)
    tan_data = np.tan(x_data)

    line_sin.set_data(x_data, sin_data)
    line_cos.set_data(x_data, cos_data)
    line_tan.set_data(x_data, tan_data)
    return line_sin, line_cos, line_tan

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=len(x), init_func=init, blit=True, interval=10, repeat=False
)

# Show it
plt.show()

# Animated scatter plot with random points
fig, ax = plt.subplots()
x = np.random.rand(100)
y = np.random.rand(100)
sc = ax.scatter(x, y)
def update(frame):
    x = np.random.rand(100)
    y = np.random.rand(100)
    sc.set_offsets(np.c_[x, y])
    return sc,
ani = animation.FuncAnimation(fig, update, frames=100, interval=500, blit=True)
plt.show()

# WARNING: AI GENERATED CODE BELOW

fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 500)

# Create 5 wave lines with different phase shifts
num_lines = 5
lines = [ax.plot(x, np.sin(x + i), lw=2)[0] for i in np.linspace(0, 2*np.pi, num_lines)]

ax.set_ylim(-3, 3)
ax.set_xlim(0, 4 * np.pi)
ax.axis("off")  # Turn off axes for the aesthetic

def update(frame):
    for i, line in enumerate(lines):
        shift = frame / (10 + i*2)
        distortion = np.sin(x * (1.5 + 0.3*i) + shift) * np.cos((frame + i*50) / 25)
        warp = distortion / (np.cos(frame/50 + i) + 1.5)
        line.set_ydata(warp + np.sin(frame/30 + i))  # Wavy offset
        color = plasma((frame % 300 + i*20) / 300)  # trippy color shifts
        line.set_color(color)
    return lines

ani = animation.FuncAnimation(fig, update, frames=600, interval=30, blit=True)
plt.show()
