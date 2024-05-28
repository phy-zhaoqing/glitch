from numpy import *
from scipy.integrate import quad
from scipy.misc import derivative

from parameters import *
from fobs import f_obs
# ------------------------------------------function------------------------------------------------------
# formula (11), the radius-dependent time-scales omega_pm^{-1}
# a mixture of the classical Ekman time-scale 
# & the superfluid mutual friction coupling time-scale 
def omega_pm(r, pm):
    z2       =   1. - square(r)
    z_term   =   power(z2, -0.75)

    term1    =   - 0.5 * (beta + z_term)
    term2    =   sqrt(power(term1, 2) - beta * rho_n * z_term)

    if pm == '+':
        result = term1 + term2
    elif pm == '-':
        result = term1 - term2
    else:
        print("An unexpected error occurred:", pm)
        result = None
    return result

#-----------------------------------------------------------------------------------------
# formula (15), defined to calc formula (14)
def gA_to_quad(tau, r):
    tau = array([tau])
    r = array([r])

    omg_p   =   omega_pm(r, '+')
    omg_m   =   omega_pm(r, '-')
    z       =   sqrt(1 - square(r))

    # calc the left vector. & right matrix.
    right_p   = exp(omg_p.T @ tau)
    right_m   = exp(omg_m.T @ tau)
    left =  power(r, 3)/sqrt(z) / (omg_p - omg_m)
    left = diag(left[0])
    return 7.5*(left @ right_p - left @ right_m)

def gA_prime_to_quad(tau, r):
    tau = array([tau])
    r = array([r])

    omg_p   =   omega_pm(r, '+')
    omg_m   =   omega_pm(r, '-')
    z       =   sqrt(1 - square(r))
    # calc the left vector. & right matrix.
    right_p   =   exp(omg_p.T @ tau)
    right_m   =   exp(omg_m.T @ tau)
    left_p = power(r, 3)*omg_p/sqrt(z) / (omg_p - omg_m)
    left_p = diag(left_p[0])
    left_m = power(r, 3)*omg_m/sqrt(z) / (omg_p - omg_m)
    left_m = diag(left_m[0])
    return 7.5*(left_p @ right_p - left_m @ right_m)

# 定义被积函数中 tau 的积分函数
def gA(tau, times=1000):
    return ones(times) @ gA_to_quad(tau,arange(times)/times) / times

# formula (16), defined to calc formula (14)
def gB(tau):
    m, = tau.shape
    delta_tau = tau[1]-tau[0]
    return beta*(convolve(gA(tau),ones(m),'full'))[:m] * delta_tau

def gA_prime(tau,times=1000):
    return ones(times) @ gA_prime_to_quad(tau,arange(times)/times) / times

def gB_prime(tau):
    return beta*gA(tau)

# --------------------------------------------------------------------------------------
# formula (14)-(16), an integral equation for 
# the spin evolution of the crust

# to solve it numerically, guessing an initial 
# trial function for f(tau) (e.g. exponential),
# substituting it into the right-hand side of (14),
# updating f(tau) via underrelaxation (Press et al. 2002),
# and iterating.

def f_term1(tau, f_old):
    m, = tau.shape
    delta_tau = tau[1] - tau[0]
    gAprime = gA_prime(tau) 
    gBprime  = gB_prime(tau)
    return -rho_n*K*(convolve(gAprime+gBprime,f_old,'full'))[:m] * delta_tau

def f_term2(tau):
    return rho_n*K*(gA(tau)*Omega_n0 + gB(tau)*Omega_0) + 1

def f_model(tau, f_old):
    f1=f_term1(tau,f_old)
    f2=f_term2(tau)
    return  f1+f2 

# under relaxation method
def glitch(tau,f_init,tolerance=1e-5,weight=0.5):

    # f=f_ana(tau, coeffs=coeffs) # using coeffs from parameters.py
    f = f_init
    error = 1
    while (abs(error) > tolerance):
        f_old = f
        f_new = f_model(tau, f_old)
        # under relaxation method
        f = (1-weight)*f_old + weight*f_new
        # update the error
        error = mean(abs(f-f_old)) / mean(abs(f_old))
        print(f'(f_old: {f_old}\nf_new: {f_new}\nf: {f}\n)')
        print(error)
    return f

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # variable, unit: d
    t   =   arange(0, N+1, dlt) # parameters from parameters.py
    # Ekman time, scale the time coord.
    tau = sqrt(E) * Omega * t
    

    # y_obs = f_obs(tau)
    # f1 = f_term1(tau,y_obs)
    # f2 = f_term2(tau)
    # # plt.subplot(2,2,1)
    # plt.plot(tau,gA(tau),label='gA')
    # # plt.subplot(2,2,2)
    # plt.plot(tau,gA_prime(tau),'--',label='gA_prime')
    # # plt.subplot(2,2,3)
    # plt.plot(tau,gB(tau),label='gB')
    # # plt.subplot(2,2,4)
    # plt.plot(tau,gB_prime(tau),'--',label='gB_prime')
    # # plt.plot(tau,test)
    # # plt.plot(tau,gA(tau)+gB(tau),label='gA+gB')
    # plt.plot(tau,f1,'--',label='f1')
    # plt.title(f'dlt={dlt}')
    # plt.plot(tau,f2,'--',label='f2')
    # plt.plot(tau,f1+f2,'--',label='f')
    # plt.legend()

    # plot 
    out_path = '../output/'
    # run the model
    y_obs = f_obs(tau)
    y = glitch(tau,y_obs)

    # save as .npy
    save(out_path+f'{glitch_name}_glitch_#_{N/dlt}.npy',y)

    # plot
    plt.plot(t,y_obs/y_obs[0],'r--',label='f_obs')
    plt.plot(t,y/y[0],'b',label='f_model')


    # plt.plot(t,y+y_obs)
    plt.title(f'Crab_1975_glitch, #={N/dlt}')
    plt.legend()
    # plt.axis 刻度
    # plt.save 保存为pdf
    plt.show()