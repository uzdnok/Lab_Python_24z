import functools
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Setting up a random number generator with a fixed state for reproducibility.
rng = np.random.default_rng(seed=19680801)
# Fixing bin edges.
HIST_BINS = np.linspace(0, 100, 100)

# Histogram our data with numpy.
#data = rng.standard_normal(1000)
data = rng.binomial(100, 0.5, 500)
n, _ = np.histogram(data, HIST_BINS)
num_of_frames = 200


def animate(frame_number, bar_container, ax):
    # Simulate new data coming in.
    #data = rng.standard_normal(1000)
    data = rng.binomial(100, 0.5, 10 * (frame_number + 1))
    n, _ = np.histogram(data, HIST_BINS)

    # Update the height of the bars.
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    # Dynamically update the y-axis if necessary.
    ax.set_ylim(0, np.max(n) * 1.1)  # Update y-axis based on the new data

    progress_text = f"Progress: {frame_number + 1} / {num_of_frames}"
    text_artist.set_text(progress_text)

    return bar_container.patches, text_artist


# Output generated via `matplotlib.animation.Animation.to_jshtml`.

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                              ec="blue", fc="black", alpha=0.5)
text_artist = ax.text(0.95, 0.95, "", transform=ax.transAxes, ha="right", va="top",
                      fontsize=12, color="red")
ax.set_ylim(0, 60)  # Set a safe upper limit for y-axis initially.

# Define the animation function.
anim = functools.partial(animate, bar_container=bar_container, ax=ax)

# Create the animation object with blit=False to redraw the whole plot.
ani = animation.FuncAnimation(fig, anim, frames=num_of_frames, repeat=False, blit=False)
ani.save('histogram_animation.gif', writer='pillow', fps=10)
plt.show()
