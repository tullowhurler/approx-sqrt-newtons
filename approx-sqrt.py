def sqrt(x):
    # Intial guess 
    z = 1.0 
    # keep getting better estimate for the square root 
    # of x, until you are within two decimal places.
    while abs(z*z - x) >= 0.01: 
        # get a better approximation for the square root. 
        z -= (z*z - x) / (2*z)
    # return z. 
    return z



sqrt(8.0)