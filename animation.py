import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Box import Box

def prepare_animation_data(Box1: "Box", Box2: "Box", fps: int = 60):
    """
    Prepares animation data for the given Box objects and frames per second (fps).
    This function generates position data points based on the calculated frames per collision interval.

    Args:
        Box1 (Box): The first box object.
        Box2 (Box): The second box object.
        fps (int): The frames per second (fps) for the animation.

    Returns:
        tuple: A tuple containing:
            - x1 (list of float): A list of positions of Box1 over time.
            - x2 (list of float): A list of positions of Box2 over time.
            - collision_frames (list of int): A list containing the number of frames allocated for each collision interval.
    """

    times = Box1.times
    v1_arr = np.array(Box1.v_hist)
    v2_arr = np.array(Box2.v_hist)
    dt_arr = np.diff(times)
    x1 = []
    x2 = []
    x_hist1 = np.array(Box1.x_hist) 
    x_hist2 = np.array(Box2.x_hist)
    collision_frames = []

    # calculate positional frames and track interval frames
    for i, dt in enumerate(dt_arr, start=1):
        frames = int(dt * fps)
        if len(collision_frames) == 0:
            collision_frames.append(frames)
        else:
            collision_frames.append(collision_frames[-1] + frames)
        x1 += np.linspace(x_hist1[i-1], x_hist1[i], frames + 1)[:-1].tolist()
        x2 += np.linspace(x_hist2[i-1], x_hist2[i], frames + 1)[:-1].tolist()

    x1 += np.linspace(x_hist1[-1], x_hist1[-1] + v1_arr[-1] * 5, 5 * fps).tolist()
    x2 += np.linspace(x_hist2[-1], x_hist2[-1] + v2_arr[-1] * 5, 5 * fps).tolist()

    print()
    print(f"Total Motion Duration: {(x2[-1] - x_hist2[-1])/v2_arr[-1] + times[-1]:.2f} seconds")
    print(f"Total Animation Duration: {len(x1)/fps:.2f} seconds")


    return x1, x2, collision_frames


def animate_simulation(Box1: "Box", Box2: "Box", ylim: tuple = (0, 3), left_bound: float = 0, fps: int = 60, save: bool = False, filename: str = "Output/animation.mp4"):
    """
    Create an animation of the colliding boxes that counts the number of collisions.

    Args:
        Box1 (Box): First box.
        Box2 (Box): Second Box.
        side_length (float, optional): side_length of Box1 and Box2 depending on its mass (default value 1 m).
        y_lim (tuple, optional): y-axis boundaries (default value (0,3) m).
        left_bound (float, optional): left wall boundary in meters (default value 0 m).
        fps (int, optional): fps for animation (default value 60 fps).
        save (bool, optional): save animation locally as a video (default value False).
        filename (str, optional): filename for locally saved animation (default value "animation.mp4")
    
    Returns:
        HTML: HTML format of the animation to view in Jupyter notebook.
    """
    # Create figure and set size, aspect ratio, and visuals
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.tight_layout()
    ax.set_ylim(ylim)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(rf"Colliding Blocks with $m$ = {Box1.m: .1e}kg and $M$ = {Box2.m: .1e}kg")
    ax.spines["right"].set_visible(False)  
    ax.spines["top"].set_visible(False)  
    ax.set_yticks([])  
    ax.set_yticklabels([])
    ax.minorticks_on()  
    ax.set_xlabel('Position (m)')


    # calculate animation data from simulation
    side_length = Box1.l
    side_length2 = Box2.l
    x01 = Box1.x0
    x02 = Box2.x0
    collision_count = 0
    x1, x2, collision_frames = prepare_animation_data(Box1, Box2, fps=fps)

    max_x = np.max([np.max(x1), np.max(x2)])
    ax.set_xlim(left_bound, max_x + side_length2)

    # First box
    box1 = plt.Polygon([[x01, 0], [x01 + side_length, 0], [x01 + side_length, side_length], [x01, side_length]], closed=True, color='b', alpha=0.5)
    ax.add_patch(box1)

    # Second box
    box2 = plt.Polygon([[x02, 0], [x02 + side_length2, 0], [x02 + side_length2, side_length2], [x02, side_length2]], closed=True, color='r', alpha=0.5)
    ax.add_patch(box2)

    text_box = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    def animate(i: int):
        """
        Animate helper function to draw each frame.

        Args:
            i (int): frame index.

        Returns:
            None
        """
        nonlocal collision_count
        box1.set_xy([[x1[i], 0], [x1[i] + side_length, 0], [x1[i] + side_length, side_length], [x1[i], side_length]])
        box2.set_xy([[x2[i], 0], [x2[i] + side_length2, 0], [x2[i] + side_length2, side_length2], [x2[i], side_length2]])

        if i in collision_frames:
            if i == 0 and collision_count > 0:
                pass
            else:
                collision_count += collision_frames.count(i)

        text_box.set_text(f"Collisions: {collision_count}")

        return box1, box2, text_box


    ani = animation.FuncAnimation(fig, animate, frames=len(x1), interval=1000/fps, blit=True)
    duration = (len(x1) * (1000 / fps)) / 1000

    if save:
        ani.save(filename, writer="ffmpeg", fps=fps)
        print(f"Save successful as {filename}")
        collision_count = 0


    output = ani.to_jshtml()

    return output