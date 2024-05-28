from numpy import *

dlt = 5e-3 # 3e-3

i=2

if i==1:
    ## Vela 1988
    glitch_name = 'Vela_1988'
    N = 120

    # pre-glitch, unit: muHz
    nu_g0       =   11.2016866562e5
    Omega       =   2.0 * pi * nu_g0

    # Fig. 2. (a)
    # dimensionless parameters
    K       =   53
    B       =   5e-9
    E       =   3.05e-15

    # viscous, scaled to total density: rho
    rho_n   =   0.01

    # viscous, total mass flux, scaled to dlt_Omega
    Omega_0 =   0.97
    Omega_n0=   0.97

    beta    =   B / sqrt(E)

    coeffs = [20/7*rho_n*K, Omega_n0, Omega_0, beta] # [a_rho_n_K, b_Omega_n0, c_Omega_0, d_beta]

elif i==2:
    #-------------------------------------------------Crab 1975-------------
    glitch_name = 'Crab_1975'
    N = 200
    
    # pre-glitch, unit: muHz
    nu_g0       =   29.9e5
    Omega       =   2.0 * pi * nu_g0

    # Fig. 2. (a)
    # dimensionless parameters
    K       =   2.5e3
    B       =   3.3e-9
    E       =   8.44e-23

    # viscous, scaled to total density: rho
    rho_n   =   0.01

    # viscous, total mass flux, scaled to dlt_Omega
    Omega_0 =   0.77
    Omega_n0=   -2.47

    beta    =   B / sqrt(E)

    coeffs = [20/7*rho_n*K, Omega_n0, Omega_0, beta] # [a_rho_n_K, b_Omega_n0, c_Omega_0, d_beta]