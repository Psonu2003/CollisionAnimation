from time import time
import numpy as np
from typing import Dict, Union
from Box import Box

def format_scientific(value, force=False):
    if value == 0:
        return "0 s"

    exponent = int(np.floor(np.log10(abs(value))))
    coefficient = value / (10**exponent)

    if abs(exponent) > 3 or force:
        # Convert exponent to superscript format
        superscript_map = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
        exponent_str = str(exponent).translate(superscript_map)

        return f"{coefficient:.3f} × 10{exponent_str}"
    else:
        return f"{value:,.3f}"


    
def elastic_collision_sim(Box1: "Box", Box2: "Box", left_bound: float = 0) -> Dict[str, Union[int, float, "Box"]]:
    """
    Simulates perfectly elastic collisions between two boxes in one-dimensional motion.

    The simulation continues until the two boxes no longer collide. 
    The left boundary acts as a perfectly rigid wall.

    Args:
        Box1 (Box): First box object.
        Box2 (Box): Second box object (must be placed to the right of Box1).
        left_bound (float, optional): The x-coordinate of the left boundary (defaults to 0 m).

    Returns:
        dict: A dictionary containing:
            - "Collisions" (int): The total number of collisions before the system stabilizes.
            - "Smallest Interval" (float): The shortest time interval between collisions.
            - "Box 1" (Box): The final state of Box1.
            - "Box 2" (Box): The final state of Box2.

    Raises:
        Exception: If either box is outside the left boundary.
        Exception: If Box2 is not initially placed to the right of Box1.
    """
    start = time()
    Box1.check_overlap(Box2)

    if (Box1.x0 < left_bound) or (Box2.x0 < left_bound):
        raise Exception(f"One or both boxes are outside the left boundary of x = {left_bound}m.")
    
    if (Box2.x0 < Box1.x0):
        raise Exception("Box 2 must be placed to the right of Box 1.")
    
    collisions = 0
    dt_min = 0
    while True:
        m1 = Box1.m
        x1 = Box1.x
        x2 = Box2.x
        l1 = Box1.l
        m2 = Box2.m
        v1 = Box1.v
        v2 = Box2.v

        if v1 < 0:
            dx = abs(x1 - left_bound)
            t = dx / abs(v1)
            v1f = -v1
            v2f = v2
        

        elif v1 < v2 and v2 > 0:
            dt_min = np.min(np.diff(Box1.times))
            duration = time() - start

            print("------------- Simulation Report -------------")
            print(f"Total Collisions   : {collisions:,}")
            print(f"Smallest Interval  : {format_scientific(dt_min, force=True)} s")
            print(f"Simulation Time    : {format_scientific(duration, force=True)} s\n")

            print("Box 1:")
            print(f"  - Position   : {Box1.x:.3f} m")
            print(f"  - Mass       : {format_scientific(Box1.m)} kg")
            print(f"  - Velocity   : {Box1.v:.3f} m/s")
            print(f"  - Momentum   : {Box1.p:.3f} kg·m/s\n")

            print("Box 2:")
            print(f"  - Position   : {Box2.x:.3f} m")
            print(f"  - Mass       : {format_scientific(Box2.m)} kg")
            print(f"  - Velocity   : {Box2.v:.3f} m/s")
            print(f"  - Momentum   : {Box2.p:.3f} kg·m/s")

            break

        else:
            t = (x1 + l1 - x2) / (v2 - v1)
            v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
            v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        
        
        collisions += 1

        Box1.update(v1f, x1 + v1 * t, t)
        Box2.update(v2f, x2 + v2 * t, t)
    
    
    sim_data = {"Collisions": collisions, "Smallest Interval": float(dt_min), "Box 1": Box1, "Box 2": Box2}
    return sim_data