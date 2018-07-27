"""Contains function for calculating distance between two GPS coordinates.
This is only used for some exploratory analysis and not for final analysis."""
from math import atan, atan2, cos, radians, sin, sqrt, tan


def vincenty(coord1, coord2, max_iter=200, tol=10**-12):
    """Calculates vincenty distance between two coordinate points

    Original source:
    https://nathanrooy.github.io/posts/2016-12-18/vincenty-formula-with-python/
    with minor changes

    Parameters
    ----------
    coord1 : tuple of floats, (latitude, longitude)

    coord2 : tuple of floats, (latitude, longitude)

    max_iter : int, optional (default=200)
        Maximum number of iterations. Higher -> slower/more accurate

    tol: float, optional (default=10**-12)
        Tolerance value which stands for successful convergence

    Returns
    -------
    float
        Distance in meters
    """
    # Constants
    a = 6378137  # radius at equator in meters (WGS-84)
    f = 1 / 298.257223563  # flattening of the ellipsoid (WGS-84)
    b = (1 - f) * a

    phi_1, L_1 = coord1
    phi_2, L_2 = coord2

    u_1 = atan((1 - f) * tan(radians(phi_1)))
    u_2 = atan((1 - f) * tan(radians(phi_2)))

    L = radians(L_2 - L_1)

    # set initial value of lambda to L
    Lambda = L

    sin_u1 = sin(u_1)
    cos_u1 = cos(u_1)
    sin_u2 = sin(u_2)
    cos_u2 = cos(u_2)

    # Begin iterations
    iters = 0
    for i in range(0, max_iter):
        iters += 1

        cos_lambda = cos(Lambda)
        sin_lambda = sin(Lambda)
        sin_sigma = sqrt((cos_u2 * sin(Lambda))**2 +
                         (cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lambda)**2)
        cos_sigma = sin_u1 * sin_u2 + cos_u1 * cos_u2 * cos_lambda
        sigma = atan2(sin_sigma, cos_sigma)
        sin_alpha = (cos_u1 * cos_u2 * sin_lambda) / sin_sigma
        cos_sq_alpha = 1 - sin_alpha**2
        cos2_sigma_m = cos_sigma - ((2 * sin_u1 * sin_u2) / cos_sq_alpha)
        C = (f / 16) * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha))
        Lambda_prev = Lambda
        Lambda = L + (1 - C) * f * sin_alpha * (sigma + C * sin_sigma *
                                                (cos2_sigma_m + C * cos_sigma *
                                                 (-1 + 2 * cos2_sigma_m**2)))

        # successful convergence
        diff = abs(Lambda_prev - Lambda)
        if diff <= tol:
            break

    u_sq = cos_sq_alpha * ((a**2 - b**2) / b**2)
    A = 1 + (u_sq / 16384) * (4096 + u_sq * (-768 + u_sq * (320 - 175 * u_sq)))
    B = (u_sq / 1024) * (256 + u_sq * (-128 + u_sq * (74 - 47 * u_sq)))
    delta_sig = B * sin_sigma * (cos2_sigma_m + 0.25 * B *
                                 (cos_sigma * (-1 + 2 * cos2_sigma_m**2) -
                                  (1 / 6) * B * cos2_sigma_m *
                                  (-3 + 4 * sin_sigma**2) *
                                  (-3 + 4 * cos2_sigma_m**2)))
    return b * A * (sigma - delta_sig)
