# Perfectly Elastic Collision Simulator

This repo provides a simulation of two colliding blocks where the user can control their masses, positions, and initial velocities. There is a immovable barrier to the left of both boxes that perfectly reflects any momentum transfers from the box. The purpose of this simulation is to demonstrate a unique phenomena based on the mass ratios of Box 1 and 2. When $\mathrm{Box 1}/\mathrm{Box 1} = 0.01^n$ where $n$ is some positive integer, then the number of collisions will match the digits of $\pi$. The number of digits the collisions will match $\pi$ to is $n$ digits. Other than this, the repo can serve as a general purpose perfect elastic collision simulator with an immovable and indestructable wall. 

# How to use
First, clone this repo onto your local machine. Then, run the following commands in the cloned repository directory

```bash
python -m venv collision-venv
```

This will create the `collision-venv` virtual environment.

For Windows,

```bash
collision-venv\Scripts\activate.bat
```

and for Mac/Linux,

```bash
source ./collision-venv/bin/activate
```

After the virtual environment is activated, do

```bash
pip install -r requirements.txt
```
this will automatically install all of the required libraries.

Now, run `main.py` using

```bash
python main.py
```

or 

```bash
python3 main.py
```

or 

```bash
py main.py
```

If it's easier to use the `input.in` file to feed in the input values, then do 

```bash
python main.py < input.in
```
This will feed all the inputs into the `main.py` without the user needing to type them in each time. 

# Tips
Just note that if you do choose to save the animation that it could take a few minutes to complete. Do not terminate the program even if you see a message saying that the animation is saved. The simulation will terminate on its own and this will allow the video and HTML to be properly created. 

## Contact
If you have any questions, please contact me at [pratham.gujar30@gmail.com](mailto:pratham.gujar30@gmail.com). 