from DSR_ROBOT2 import movel, posx

Y_START = 0.000000
Y_Z_TOTAL_OFFSET = -0.600000
Y_INTERPOLATION_LENGTH = 99.997000

def calc_z_offset(dy):
    if Y_INTERPOLATION_LENGTH <= 0:
        return 0.0
    ratio = (Y_START - dy) / Y_INTERPOLATION_LENGTH
    ratio = max(0.0, min(1.0, ratio))
    return Y_Z_TOTAL_OFFSET * ratio

def draw(cx, cy, cz):
    PEN_RPY = (0.0, 180.0, 90.0)
    vel = 100
    acc = 100

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.125
    dy = -0.184
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.125
    dy = -0.184
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.965
    dy = -0.708
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.814
    dy = -4.058
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.167
    dy = -15.386
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.557
    dy = -19.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.036
    dy = -22.776
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.793
    dy = -28.190
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.793
    dy = -31.622
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.385
    dy = -37.101
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.680
    dy = -42.079
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.579
    dy = -42.591
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.047
    dy = -43.063
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.285
    dy = -49.300
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.186
    dy = -52.936
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.030
    dy = -54.892
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.635
    dy = -55.857
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.342
    dy = -64.244
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.888
    dy = -71.403
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.889
    dy = -75.489
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.513
    dy = -76.563
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.926
    dy = -76.911
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.358
    dy = -76.568
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.054
    dy = -74.593
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.011
    dy = -70.105
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.728
    dy = -65.206
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.407
    dy = -61.914
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.203
    dy = -59.175
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.460
    dy = -45.989
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.129
    dy = -45.572
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 74.790
    dy = -38.178
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 77.085
    dy = -33.199
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 77.618
    dy = -28.516
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 77.264
    dy = -25.594
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.829
    dy = -20.772
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.143
    dy = -15.748
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.460
    dy = -12.360
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.542
    dy = -5.114
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.919
    dy = -1.960
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.218
    dy = -1.073
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.276
    dy = -0.720
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.965
    dy = -1.063
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.892
    dy = -3.364
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.423
    dy = -1.780
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.840
    dy = -0.895
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.302
    dy = -0.008
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.302
    dy = -0.008
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.302
    dy = -3.026
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.302
    dy = -3.026
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.368
    dy = -3.026
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.368
    dy = -3.026
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.548
    dy = -2.844
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.548
    dy = -2.844
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.564
    dy = -3.486
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.474
    dy = -5.509
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.474
    dy = -5.509
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.921
    dy = -7.432
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.921
    dy = -7.432
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.454
    dy = -5.169
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.454
    dy = -5.169
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.577
    dy = -4.447
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.577
    dy = -4.447
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.465
    dy = -4.447
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.465
    dy = -4.447
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.643
    dy = -4.267
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.643
    dy = -4.267
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.596
    dy = -5.333
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.514
    dy = -7.866
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.585
    dy = -10.045
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 67.191
    dy = -14.974
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.438
    dy = -24.119
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.868
    dy = -27.494
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.905
    dy = -30.124
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.307
    dy = -31.451
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.307
    dy = -31.451
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.535
    dy = -36.948
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.535
    dy = -36.948
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.196
    dy = -36.474
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.134
    dy = -35.212
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 67.069
    dy = -33.035
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.367
    dy = -29.665
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.367
    dy = -29.665
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.004
    dy = -27.538
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.004
    dy = -27.538
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.334
    dy = -29.359
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.146
    dy = -30.895
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.296
    dy = -30.678
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.767
    dy = -29.378
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.234
    dy = -28.236
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.645
    dy = -27.554
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.415
    dy = -17.839
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.823
    dy = -13.799
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.370
    dy = -10.887
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.396
    dy = -8.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.334
    dy = -8.531
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.334
    dy = -8.531
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.272
    dy = -9.586
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.272
    dy = -9.586
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.797
    dy = -6.897
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.387
    dy = -6.021
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.387
    dy = -6.021
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.210
    dy = -6.223
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.210
    dy = -6.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.144
    dy = -6.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.144
    dy = -6.223
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.836
    dy = -7.290
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.836
    dy = -7.290
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.448
    dy = -9.998
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.393
    dy = -13.319
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.587
    dy = -24.641
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.877
    dy = -28.532
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.218
    dy = -28.779
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.218
    dy = -28.779
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.688
    dy = -29.137
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.688
    dy = -29.137
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.174
    dy = -30.710
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.544
    dy = -29.690
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.531
    dy = -31.104
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.835
    dy = -30.420
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.411
    dy = -29.621
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.266
    dy = -28.838
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.659
    dy = -27.532
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.659
    dy = -27.532
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.480
    dy = -27.713
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.480
    dy = -27.713
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.237
    dy = -27.713
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.237
    dy = -27.713
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.970
    dy = -30.908
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.970
    dy = -30.908
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.773
    dy = -34.181
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.414
    dy = -36.210
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.817
    dy = -38.380
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.190
    dy = -38.910
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.190
    dy = -38.910
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.913
    dy = -38.546
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.913
    dy = -38.546
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.841
    dy = -42.650
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.212
    dy = -47.674
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.526
    dy = -48.146
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.697
    dy = -44.800
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.764
    dy = -42.812
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.764
    dy = -42.812
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.616
    dy = -48.273
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.616
    dy = -48.273
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.883
    dy = -48.853
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.441
    dy = -48.586
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.319
    dy = -47.910
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.319
    dy = -47.910
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.370
    dy = -49.209
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.370
    dy = -49.209
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.708
    dy = -50.637
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.708
    dy = -50.637
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.892
    dy = -52.408
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.892
    dy = -52.408
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.476
    dy = -55.400
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.476
    dy = -55.400
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.357
    dy = -64.478
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.357
    dy = -64.478
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.890
    dy = -70.060
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.596
    dy = -71.004
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.815
    dy = -73.468
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.794
    dy = -77.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -84.013
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -84.013
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.783
    dy = -76.584
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.783
    dy = -76.584
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.053
    dy = -72.819
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.053
    dy = -72.819
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.885
    dy = -71.044
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.885
    dy = -71.044
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.878
    dy = -72.573
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.095
    dy = -74.707
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.770
    dy = -79.682
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.479
    dy = -85.018
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.846
    dy = -89.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.760
    dy = -93.765
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.582
    dy = -98.211
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.081
    dy = -99.655
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.466
    dy = -99.997
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.836
    dy = -98.682
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.847
    dy = -96.254
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.829
    dy = -92.483
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.121
    dy = -87.700
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.443
    dy = -82.633
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.019
    dy = -74.681
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 67.668
    dy = -73.297
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.309
    dy = -71.747
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.009
    dy = -70.516
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.009
    dy = -70.516
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.186
    dy = -70.340
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.186
    dy = -70.340
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 76.675
    dy = -75.445
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.008
    dy = -79.777
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 98.938
    dy = -84.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 98.938
    dy = -84.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.372
    dy = -76.552
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.372
    dy = -76.552
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.025
    dy = -71.931
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.025
    dy = -71.931
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.834
    dy = -63.044
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.834
    dy = -63.044
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.239
    dy = -63.781
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.324
    dy = -63.740
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.789
    dy = -63.042
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.789
    dy = -63.042
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.604
    dy = -60.393
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.604
    dy = -60.393
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.716
    dy = -60.393
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.716
    dy = -60.393
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.512
    dy = -60.543
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.512
    dy = -60.543
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.771
    dy = -60.626
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.771
    dy = -60.626
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.731
    dy = -58.476
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.731
    dy = -58.476
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.322
    dy = -57.570
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.322
    dy = -57.570
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.263
    dy = -56.675
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.263
    dy = -56.675
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.210
    dy = -57.197
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.010
    dy = -56.643
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.070
    dy = -57.939
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.070
    dy = -57.939
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.087
    dy = -59.666
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.087
    dy = -59.666
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.134
    dy = -60.067
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.134
    dy = -60.067
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.845
    dy = -59.788
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.845
    dy = -59.788
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.932
    dy = -59.825
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.932
    dy = -59.825
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.735
    dy = -60.038
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.735
    dy = -60.038
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.492
    dy = -60.038
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.492
    dy = -60.038
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.492
    dy = -60.215
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.492
    dy = -60.215
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.604
    dy = -60.215
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.604
    dy = -60.215
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.442
    dy = -51.342
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.442
    dy = -51.342
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.444
    dy = -51.112
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.237
    dy = -49.590
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.245
    dy = -47.670
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.790
    dy = -46.373
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.790
    dy = -46.373
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.027
    dy = -49.549
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.027
    dy = -49.549
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.077
    dy = -49.666
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.286
    dy = -51.007
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.380
    dy = -50.925
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.568
    dy = -49.552
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.318
    dy = -49.901
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.318
    dy = -49.901
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.635
    dy = -51.191
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.635
    dy = -51.191
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.646
    dy = -50.774
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.403
    dy = -49.483
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.197
    dy = -47.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.301
    dy = -46.085
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.301
    dy = -46.085
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.415
    dy = -48.670
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.415
    dy = -48.670
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.846
    dy = -47.867
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.938
    dy = -44.997
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.173
    dy = -37.140
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.883
    dy = -33.040
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.883
    dy = -33.040
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.047
    dy = -36.942
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.047
    dy = -36.942
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.414
    dy = -35.412
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.729
    dy = -36.986
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.669
    dy = -37.191
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.774
    dy = -35.711
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.771
    dy = -34.643
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.771
    dy = -34.643
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.360
    dy = -34.071
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.360
    dy = -34.071
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.132
    dy = -34.756
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.941
    dy = -36.292
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.941
    dy = -36.292
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.210
    dy = -36.777
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.210
    dy = -36.777
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.297
    dy = -45.649
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.297
    dy = -45.649
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.499
    dy = -37.125
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.499
    dy = -37.125
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.521
    dy = -35.051
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.385
    dy = -34.254
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.385
    dy = -34.254
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.191
    dy = -34.462
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.191
    dy = -34.462
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.125
    dy = -34.462
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.125
    dy = -34.462
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.845
    dy = -34.838
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.845
    dy = -34.838
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.416
    dy = -34.818
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.149
    dy = -37.003
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.837
    dy = -37.621
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.321
    dy = -36.404
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.358
    dy = -34.970
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.358
    dy = -34.970
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.006
    dy = -35.348
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.006
    dy = -35.348
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.398
    dy = -36.574
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.398
    dy = -36.574
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.653
    dy = -31.975
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.653
    dy = -31.975
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.928
    dy = -31.499
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.931
    dy = -29.025
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.207
    dy = -26.463
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.989
    dy = -15.860
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.417
    dy = -11.519
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.319
    dy = -7.054
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.171
    dy = -3.915
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.171
    dy = -3.915
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

