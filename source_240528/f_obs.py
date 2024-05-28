import numpy as np
from params import nu_g0,dlt_nu, dlt_nu_p, dlt_nu_list, t_list
from parameters import E

# formula (19)
def f_obs(tau):

    # summation of terms of power law 
    sum = 0.0
    for i in range(len(dlt_nu_list)):
        powerlaw = np.exp(- tau / (np.sqrt(E) * 2.0 * np.pi * nu_g0 * t_list[i]))
        sum     += dlt_nu_list[i] * powerlaw

    # f_obs
    obs = dlt_nu_p / dlt_nu + sum

    return obs