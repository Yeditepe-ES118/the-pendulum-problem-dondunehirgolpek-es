import numpy as np
def find_period(L0, L1):
    g = 9.81 # gravitational acceleration (m/s^2)
    
    # make sure inputs are valid
    if L0 <= 0 or L1 <= 0 :
        print("Lengths must be positive.")
        return
    if L1 <= L0 :
        print("L1 must be greater than L0.")
        return
    
    # create array of lengths from L0 to L1
    lengths = np.arange(int(L0), int(L1) + 1, 1)
    
    # calculate the period for each length
    periods = 2 * np.pi * np.sqrt(lengths / g)
    
    # print results 
    for L, T in zip(lengths, periods):
        print("When L = %.1f m, T = %.1f s" % (L, T))
        
# example run
find_period(2, 10)


