import numpy as np

dlt = 1e-1
i = 3

if i == 1:
    #-------------------------------------------------Vela 1985-------------
    numdays = 1000

    E = 1.16e-21
    rho_n = 0.1
    
    # pre-glitch, unit: muHz
    nu_g0       =   11.2016866562e2
    Omega       =   2.0 * np.pi * nu_g0

    # unit: muHz
    dlt_nu      =   17.9
    dlt_nu_p    =   15.1 
    dlt_nu_1    =   2.76
    dlt_nu_2    =   0.066
    # dlt_nu_3    =   12.8
    # dlt_nu_4    =   12.8

    # scaled to dlt_nu
    dlt_nu_list = np.array([dlt_nu_1, dlt_nu_2]) / dlt_nu

    # unit: d
    t_1         =   332.0
    t_2         =   6.5
    # t_3         =   233
    # t_4         =   233
    t_list      = np.array([t_1, t_2])
elif i == 2:
    #-------------------------------------------------Vela 1988-------------
    numdays = 120

    E = 3.05e-15
    rho_n = 0.01
    
    # pre-glitch, unit: muHz
    nu_g0       =   11.2e5
    Omega       =   2.0 * np.pi * nu_g0

    # unit: muHz
    dlt_nu      =   20.2
    dlt_nu_p    =   19.7 
    dlt_nu_1    =   0.376
    dlt_nu_2    =   0.086
    dlt_nu_3    =   0.108
    # dlt_nu_4    =   12.8

    # scaled to dlt_nu
    dlt_nu_list = np.array([dlt_nu_1, dlt_nu_2, dlt_nu_3]) / dlt_nu

    # unit: d
    t_1         =   96
    t_2         =   4
    t_3         =   0.4
    # t_4         =   233
    t_list      = np.array([t_1, t_2, t_3])
elif i == 3:
    #-------------------------------------------------Crab 1975-------------
    numdays = 200
    
    E = 8.44e-23
    rho_n = 0.01
    
    # pre-glitch, unit: muHz
    nu_g0       =   29.9e5
    Omega       =   2.0 * np.pi * nu_g0

    # unit: muHz
    dlt_nu      =   1.32
    dlt_nu_p    =   1.02 
    dlt_nu_1    =   -0.71
    dlt_nu_2    =   1.01
    # dlt_nu_3    =   12.8
    # dlt_nu_4    =   12.8

    # scaled to dlt_nu
    dlt_nu_list = np.array([dlt_nu_1, dlt_nu_2]) / dlt_nu

    # unit: d
    t_1         =   97
    t_2         =   18
    # t_3         =   233
    # t_4         =   233
    t_list      = np.array([t_1, t_2])
elif i == 4:
    #-------------------------------------------------SGR 1935-anti-glitch-------
    numdays = 120

    E = 1.16e-21
    rho_n = 0.1
    
    # pre-glitch, unit: Hz
    nu_g0       =   0.308e-1
    Omega       =   2.0 * np.pi * nu_g0

    # unit: muHz
    dlt_nu      =   19.8
    dlt_nu_p    =   23.2 
    dlt_nu_1    =   -5.88
    dlt_nu_2    =   2.50
    # dlt_nu_3    =   0.108
    # dlt_nu_4    =   12.8

    # scaled to dlt_nu
    dlt_nu_list = np.array([dlt_nu_1, dlt_nu_2]) / dlt_nu

    # unit: d
    t_1         =   8
    t_2         =   131
    # t_3         =   0.4
    # t_4         =   233
    t_list      = np.array([t_1, t_2])
elif i == 5:
    #-------------------------------------------------SGR 1935-glitch-2022------
    numdays = 20

    E = 1.16e-21
    rho_n = 0.1
    
    # pre-glitch, unit: Hz
    nu_g0       =   0.308
    Omega       =   2.0 * np.pi * nu_g0

    # unit: muHz
    dlt_nu      =   49
    dlt_nu_p    =   0.
    dlt_nu_1    =   30
    dlt_nu_2    =   19
    # dlt_nu_3    =   0.108
    # dlt_nu_4    =   12.8

    # scaled to dlt_nu
    dlt_nu_list = np.array([dlt_nu_1, dlt_nu_1]) / dlt_nu

    # unit: d
    t_1         =   25./108
    t_2         =   95./648
    # t_3         =   0.4
    # t_4         =   233
    t_list      = np.array([t_1, t_2])