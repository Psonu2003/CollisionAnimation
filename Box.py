class Box(object):
    """
    Class that defines a Box with position, velocity, mass, and length.

    Parameters:
        x0 (float, optional): Initial position in meters (defaults to 5 m).
        m (float, optional): Mass in kg (defaults to 1 kg).
        v0 (float, optional): Initial velocity of the box (defaults to 0 m/s).
        l (float, optional): Length of the box (defaults to 1 m).

    Raises:
        ValueError: If mass m is less than or equal to 0 kg.
        ValueError: If length l is less than or equal to 0 m.
        Exception: If the current box overlaps with another box.
    """
    def __init__(self, x0: float = 5, m: float = 1, v0: float = 0, l: float = 1):
        self.x = float(x0)
        if (m <= 0):
            raise ValueError("Mass must be greater than 0.")
        if (l <= 0):
            raise ValueError("Length must be greater than 0.")
        
        self.m = float(m)
        self.l = float(l)
        self.v = float(v0)
        self.v0 = v0
        self.x0 = x0
        
        self.p = self.m * self.v
        self.x_hist = [self.x]
        self.v_hist = [self.v]
        self.p_hist = [self.p]
        self.times = [0.0]
    
    def update(self, v: float, x: float, t: float):
        """
        Updates Box attributes. 

        Args:
            v (float): velocity (m/s).
            x (float): position (m).
            t (float): time (s).
        Returns:
            None
        Raises:
            ValueError: If time t is less than 0.
        """
        if t < 0:
            raise ValueError('Time must be greater than or equal to 0 s.')

        self.x = float(x)
        self.v = float(v)
        self.p = self.m * self.v

        self.x_hist.append(self.x)
        self.v_hist.append(self.v)
        self.p_hist.append(self.p)
        self.times.append(float(t) + self.times[-1])

    def check_overlap(self, Box2: "Box"):
        """
        Checks if two boxes overlap each other.

        Args:
            Box2 (Box): Other box object.
        
        Returns:
            None
        
        Raises:
            Exception: If the current box overlaps with the other.
        """
        x1 = self.x0
        x2 = Box2.x0

        l1 = self.l
        l2 = Box2.l

        if (x2 < x1+l1 <= x2+l2):
            raise Exception("Simulation failed. Boxes overlap!")

    def __str__(self):
        return f'x = {self.x} m, m = {self.m} kg, v = {self.v} m/s, p = {self.p} kg•m/s'