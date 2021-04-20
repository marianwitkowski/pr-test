"""
 Pull request from oandatest user
"""

from math import pi

def calc_circle_area(r):
    if not type(r) in [int, float]:
        raise TypeError("invalid radius type")
    if r<0:
        raise ValueError("Radius must be positive value")
    return pi*(r**2)

"""
testest
radius = [1, 2, -1, 0]
for r in radius:
    print(f"r={r} area={calc_circle_area(r)}")
"""