from DSR_ROBOT2 import movel, posx

Y_START = 0.000000
Y_Z_TOTAL_OFFSET = -0.600000
Y_INTERPOLATION_LENGTH = 100.000000

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

    dx = 22.673
    dy = -2.360
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.673
    dy = -2.360
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.234
    dy = -4.979
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.847
    dy = -12.609
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.749
    dy = -16.642
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.960
    dy = -25.254
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.349
    dy = -29.990
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.683
    dy = -38.697
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.417
    dy = -41.311
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.723
    dy = -48.392
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.912
    dy = -51.232
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.480
    dy = -51.124
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.437
    dy = -50.557
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.384
    dy = -45.474
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.103
    dy = -41.395
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.038
    dy = -32.504
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.662
    dy = -32.104
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.678
    dy = -33.159
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.678
    dy = -33.159
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.037
    dy = -32.241
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.037
    dy = -32.241
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.204
    dy = -27.133
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.521
    dy = -20.840
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.551
    dy = -15.042
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.808
    dy = -12.373
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.377
    dy = -12.329
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.154
    dy = -13.876
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.674
    dy = -17.664
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.884
    dy = -19.727
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.803
    dy = -24.234
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.392
    dy = -29.670
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.057
    dy = -29.972
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.581
    dy = -29.452
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.151
    dy = -26.449
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.591
    dy = -20.584
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.174
    dy = -16.454
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.665
    dy = -13.967
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.337
    dy = -9.962
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.337
    dy = -9.962
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.223
    dy = -10.610
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.223
    dy = -10.610
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.099
    dy = -11.923
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.099
    dy = -11.923
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.705
    dy = -9.333
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.705
    dy = -9.333
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.751
    dy = -9.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.751
    dy = -9.173
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.867
    dy = -10.223
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.867
    dy = -10.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.374
    dy = -12.528
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.304
    dy = -18.970
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.433
    dy = -20.878
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.023
    dy = -21.888
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.023
    dy = -21.888
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.776
    dy = -14.549
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.776
    dy = -14.549
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.202
    dy = -10.089
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.721
    dy = -6.554
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.721
    dy = -6.554
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.605
    dy = -5.375
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.605
    dy = -5.375
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.260
    dy = -5.375
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.260
    dy = -5.375
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.037
    dy = -5.135
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.037
    dy = -5.135
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.927
    dy = -5.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.875
    dy = -5.817
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.875
    dy = -5.817
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.279
    dy = -4.473
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.279
    dy = -4.473
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.958
    dy = -4.058
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.958
    dy = -4.058
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.909
    dy = -6.425
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.909
    dy = -6.425
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.667
    dy = -6.813
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.218
    dy = -7.606
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.666
    dy = -9.077
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.982
    dy = -26.739
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.982
    dy = -26.739
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.981
    dy = -27.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.981
    dy = -27.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.558
    dy = -29.138
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.289
    dy = -29.626
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.424
    dy = -28.969
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.877
    dy = -30.276
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.943
    dy = -29.631
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.394
    dy = -28.572
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.656
    dy = -27.129
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.656
    dy = -27.129
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.788
    dy = -26.999
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.788
    dy = -26.999
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.836
    dy = -26.999
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.836
    dy = -26.999
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.718
    dy = -27.003
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.718
    dy = -27.003
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.104
    dy = -26.572
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.944
    dy = -25.275
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.529
    dy = -23.065
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.807
    dy = -20.709
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.807
    dy = -20.709
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.401
    dy = -30.144
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.401
    dy = -30.144
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.143
    dy = -30.672
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.143
    dy = -30.672
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.685
    dy = -32.630
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.685
    dy = -32.630
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.866
    dy = -35.451
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.124
    dy = -37.511
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.467
    dy = -43.381
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.467
    dy = -43.381
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.238
    dy = -45.737
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.238
    dy = -45.737
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.445
    dy = -48.487
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.977
    dy = -49.828
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.028
    dy = -50.588
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.028
    dy = -50.588
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.690
    dy = -49.424
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.690
    dy = -49.424
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.215
    dy = -48.646
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.215
    dy = -48.646
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.338
    dy = -48.756
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.338
    dy = -48.756
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.164
    dy = -50.451
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.384
    dy = -50.191
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.838
    dy = -48.749
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.838
    dy = -48.749
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.972
    dy = -48.626
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.972
    dy = -48.626
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.013
    dy = -48.774
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.013
    dy = -48.774
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.288
    dy = -50.599
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.288
    dy = -50.599
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.519
    dy = -50.051
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.237
    dy = -49.080
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.157
    dy = -46.912
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.461
    dy = -45.348
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.461
    dy = -45.348
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.847
    dy = -36.427
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.847
    dy = -36.427
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.876
    dy = -34.955
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.348
    dy = -34.076
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.348
    dy = -34.076
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.211
    dy = -34.341
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.211
    dy = -34.341
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.661
    dy = -36.271
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.867
    dy = -36.699
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.435
    dy = -35.856
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.631
    dy = -34.080
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.631
    dy = -34.080
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.324
    dy = -34.350
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.324
    dy = -34.350
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.723
    dy = -34.748
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.044
    dy = -34.258
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.925
    dy = -33.671
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.925
    dy = -33.671
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.788
    dy = -33.814
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.788
    dy = -33.814
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.870
    dy = -33.814
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.870
    dy = -33.814
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.010
    dy = -36.692
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.010
    dy = -36.692
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.995
    dy = -35.401
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.995
    dy = -35.401
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.855
    dy = -34.869
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.855
    dy = -34.869
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.872
    dy = -35.550
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.872
    dy = -35.550
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.032
    dy = -34.595
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.032
    dy = -34.595
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.242
    dy = -34.344
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.242
    dy = -34.344
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.731
    dy = -29.627
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.731
    dy = -29.627
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.451
    dy = -31.849
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.451
    dy = -31.849
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.154
    dy = -31.978
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.154
    dy = -31.978
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.742
    dy = -31.969
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.582
    dy = -32.510
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.646
    dy = -42.452
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.155
    dy = -42.495
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.772
    dy = -36.379
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.388
    dy = -25.952
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.187
    dy = -21.451
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.194
    dy = -18.634
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.781
    dy = -16.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.598
    dy = -13.217
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.676
    dy = -8.270
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.545
    dy = -3.143
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.292
    dy = -0.521
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.545
    dy = -0.002
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.545
    dy = -0.002
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.414
    dy = -0.132
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.414
    dy = -0.132
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.628
    dy = -0.132
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.628
    dy = -0.132
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.268
    dy = -0.917
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.268
    dy = -0.917
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.216
    dy = -2.766
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.056
    dy = -1.219
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.653
    dy = -0.919
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.653
    dy = -0.919
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.522
    dy = -1.050
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.522
    dy = -1.050
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.605
    dy = -1.050
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.605
    dy = -1.050
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.474
    dy = -1.181
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.474
    dy = -1.181
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.819
    dy = -1.181
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.819
    dy = -1.181
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.318
    dy = -2.884
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.318
    dy = -2.884
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.467
    dy = -2.883
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.714
    dy = -3.691
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.575
    dy = -6.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.255
    dy = -10.747
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.133
    dy = -15.602
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.875
    dy = -20.226
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.109
    dy = -22.520
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.122
    dy = -23.985
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.122
    dy = -23.985
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.729
    dy = -37.352
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.729
    dy = -37.352
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.228
    dy = -37.710
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.505
    dy = -39.022
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.069
    dy = -49.110
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.075
    dy = -50.724
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.449
    dy = -51.454
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.894
    dy = -42.727
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.894
    dy = -42.727
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.321
    dy = -51.638
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.321
    dy = -51.638
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.877
    dy = -59.107
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.894
    dy = -63.742
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.754
    dy = -70.611
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.332
    dy = -73.134
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.214
    dy = -74.310
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.363
    dy = -74.185
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.823
    dy = -73.538
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.304
    dy = -72.092
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.853
    dy = -66.054
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.853
    dy = -66.054
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.853
    dy = -71.690
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.853
    dy = -71.690
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.255
    dy = -74.399
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.669
    dy = -77.119
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.617
    dy = -80.281
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.355
    dy = -85.935
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.820
    dy = -93.731
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.297
    dy = -99.999
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.297
    dy = -99.999
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.063
    dy = -100.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.063
    dy = -100.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.194
    dy = -85.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.508
    dy = -82.263
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.245
    dy = -75.098
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.245
    dy = -75.098
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.079
    dy = -61.459
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.079
    dy = -61.459
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.434
    dy = -62.002
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.150
    dy = -61.462
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.150
    dy = -61.462
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.440
    dy = -58.358
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.440
    dy = -58.358
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.884
    dy = -58.427
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.884
    dy = -58.427
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.326
    dy = -58.421
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.326
    dy = -58.421
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.475
    dy = -58.470
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.475
    dy = -58.470
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.682
    dy = -58.715
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.682
    dy = -58.715
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.027
    dy = -58.715
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.027
    dy = -58.715
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.242
    dy = -58.946
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.242
    dy = -58.946
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.883
    dy = -58.930
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.883
    dy = -58.930
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.828
    dy = -55.783
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.828
    dy = -55.783
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.142
    dy = -56.227
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.942
    dy = -55.841
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.942
    dy = -55.841
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.044
    dy = -63.827
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.044
    dy = -63.827
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.572
    dy = -69.988
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.963
    dy = -70.381
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.505
    dy = -71.088
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.383
    dy = -75.101
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.132
    dy = -78.811
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.435
    dy = -84.928
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.435
    dy = -84.928
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.831
    dy = -70.510
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.831
    dy = -70.510
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.140
    dy = -77.071
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.234
    dy = -83.080
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.116
    dy = -87.946
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.627
    dy = -92.120
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.871
    dy = -99.999
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.871
    dy = -99.999
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -82.699
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -82.699
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.909
    dy = -78.732
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.545
    dy = -75.242
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.706
    dy = -71.564
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.201
    dy = -65.471
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.311
    dy = -60.920
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.429
    dy = -51.508
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.429
    dy = -51.508
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.837
    dy = -41.023
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.837
    dy = -41.023
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.823
    dy = -39.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.823
    dy = -39.158
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.919
    dy = -36.300
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.919
    dy = -36.300
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.553
    dy = -35.168
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.553
    dy = -35.168
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.573
    dy = -36.325
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.573
    dy = -36.325
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.679
    dy = -37.516
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.679
    dy = -37.516
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.097
    dy = -34.873
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.097
    dy = -34.873
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.015
    dy = -36.271
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.314
    dy = -37.469
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.033
    dy = -36.822
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.366
    dy = -35.128
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.366
    dy = -35.128
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.581
    dy = -36.963
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.581
    dy = -36.963
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.759
    dy = -35.096
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.018
    dy = -34.462
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.209
    dy = -34.472
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.209
    dy = -34.472
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.964
    dy = -34.585
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.964
    dy = -34.585
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.672
    dy = -35.536
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.672
    dy = -35.536
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.397
    dy = -31.456
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.397
    dy = -31.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.174
    dy = -29.755
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.981
    dy = -29.869
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.879
    dy = -30.805
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.229
    dy = -30.564
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.207
    dy = -29.354
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.639
    dy = -28.369
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.367
    dy = -27.648
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.507
    dy = -27.657
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.507
    dy = -27.657
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.161
    dy = -28.558
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.161
    dy = -28.558
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.357
    dy = -30.033
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.184
    dy = -30.669
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.184
    dy = -30.669
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

