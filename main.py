from Box import Box
from tools import elastic_collision_sim
from animation import  animate_simulation
import matplotlib as mpl

def main():
    folder = "Output"
    filename = "elastic_collision.mp4"

    print()

    print("Welcome to the Elastic Collision Simulation!")
    print("This simulation demonstrates perfectly elastic collisions between two boxes in one-dimensional motion.")
    print("The left boundary acts as a perfectly rigid wall.")
    print("The simulation will continue until the two boxes no longer collide.")
    print("The boxes have the following properties:")
    print("Box: mass (kg), initial position (m), initial velocity (m/s), length (m)")

    print()

    print("===RULES===")
    print("1. Box 1 must be placed to the left of Box 2.")
    print("2. The animation must be less than 500 MB to be embedded in the HTML file.")
    print("3. All boxes must have a mass greater than 0 kg and a length greater than 0 m.")
    print("4. All boxes must be placed to the right of the left boundary (default is 0 m).")
    print("5. The simulation will stop when the two boxes no longer collide.")
    print("6. The left boundary acts as a perfectly rigid wall.")

    print()

    print("===SUGGESTIONS===")
    print("1. The number of collisions only rely on the masses of the boxes.")
    print("So, increasing the distance will make the animation longer than it needs to be.")
    print("2. Try setting mass 1 to 1 kg and let mass 2 be 100^n and vary n by positive integers.")

    print()

    print("==INPUTS===")

    use_default = input("Do you want to use the default values? (yes/no, default is yes): ").strip().lower() or "yes"
    if use_default == "yes":
        print("Using default values...")
        left_bound = 0
        x0_1 = 3
        m1 = 1
        v0_1 = 0
        l1 = 1
        x0_2 = 8
        m2 = 100
        v0_2 = -1
        l2 = 1
        do_animation = True
    elif use_default == "no":
        left_bound = int(input("Enter the left boundary (default is 0 m): ") or 0)
        x0_1 = float(input("Enter the initial position of Box 1 (default is 3 m): ") or 3)
        m1 = float(input("Enter the mass of Box 1 (default is 1 kg): ") or 1)
        v0_1 = float(input("Enter the initial velocity of Box 1 (default is 0 m/s): ") or 0)
        l1 = float(input("Enter the length of Box 1 (default is 1 m): ") or 1)
        x0_2 = float(input("Enter the initial position of Box 2 (default is 8 m): ") or 8)
        m2 = float(input("Enter the mass of Box 2 (default is 100 kg): ") or 100)
        v0_2 = float(input("Enter the initial velocity of Box 2 (default is -1 m/s): ") or -1)
        l2 = float(input("Enter the length of Box 2 (default is 1 m): ") or 1)
        do_animation = input("Do you want to generate an animation? (yes/no, default is yes): ").strip().lower() or "yes"
        if do_animation == "yes":
            do_animation = True
        elif do_animation == "no":
            do_animation = False
        else:
            print("Invalid input. Defaulting to 'yes'.")
            do_animation = True
    else:
        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

    print()

    print("===END OF INPUTS===")

    print()

    print("Starting simulation...")
    Box1 = Box(x0=x0_1, m=m1, v0=v0_1, l=l1)
    Box2 = Box(x0=x0_2, m=m2, v0=v0_2, l=l2)
    sim_data = elastic_collision_sim(Box1, Box2, left_bound=left_bound)


    if do_animation:
        print("Generating animation...")
        mpl.rcParams['animation.embed_limit'] = 500.0

        html_output = animate_simulation(Box1, Box2, fps=60, left_bound=left_bound, save=True, filename=f"{folder}/{filename}")
        with open("html/animation.html", "w") as f:
            f.write(html_output)
        print("html saved to html/animation.html")

if __name__ == "__main__":
    main()