class PDController:
    # A class is used to that the controller can retain its previous error between time steps

    def __init__(self):
        # Initialize PD controller gains and previous error each time a new PDController object is created
        self.kp = 0.15
        self.kd = 0.6
        self.previous_error = 0.0

    def __call__(self, reference, observation):     #makes the controller object callable like a function
        # Calculate the error and derivative based on the reference and observation
        error = reference - observation
        derivative = error - self.previous_error

        self.previous_error = error # Update the previous error for the next time step

        action = self.kp * error + self.kd * derivative
        return action       # Output the control action