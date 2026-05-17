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

    dx = 26.559
    dy = -11.160
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.559
    dy = -11.160
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.235
    dy = -10.543
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.492
    dy = -9.136
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.671
    dy = -2.729
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.544
    dy = -0.118
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.544
    dy = -0.118
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.308
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.308
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.540
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.540
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.188
    dy = -0.116
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.188
    dy = -0.116
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.995
    dy = -2.289
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.763
    dy = -0.118
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.763
    dy = -0.118
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.528
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.528
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.347
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.347
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.995
    dy = -0.117
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.995
    dy = -0.117
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.347
    dy = -1.528
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.466
    dy = -4.447
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.738
    dy = -5.219
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.044
    dy = -7.370
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.980
    dy = -8.850
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.104
    dy = -15.641
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.030
    dy = -17.190
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.010
    dy = -17.739
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.269
    dy = -17.267
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.269
    dy = -17.267
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.504
    dy = -17.620
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.504
    dy = -17.620
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.094
    dy = -21.084
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.900
    dy = -27.934
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.195
    dy = -30.517
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.893
    dy = -30.805
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.091
    dy = -31.594
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.218
    dy = -37.825
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.218
    dy = -37.825
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.213
    dy = -36.417
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.213
    dy = -36.417
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.738
    dy = -29.299
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.342
    dy = -23.725
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.342
    dy = -23.725
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.101
    dy = -21.618
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.101
    dy = -21.618
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.699
    dy = -28.073
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.699
    dy = -28.073
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.707
    dy = -28.294
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.707
    dy = -28.294
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.048
    dy = -28.775
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.048
    dy = -28.775
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.453
    dy = -28.332
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.453
    dy = -28.332
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.176
    dy = -27.592
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.176
    dy = -27.592
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.638
    dy = -25.256
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.638
    dy = -25.256
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.972
    dy = -27.133
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.542
    dy = -27.601
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.460
    dy = -27.245
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.455
    dy = -27.639
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.229
    dy = -27.105
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.940
    dy = -26.078
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.940
    dy = -26.078
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.940
    dy = -25.606
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.940
    dy = -25.606
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.512
    dy = -25.104
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.349
    dy = -21.142
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.349
    dy = -21.142
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.342
    dy = -18.440
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.342
    dy = -18.440
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.237
    dy = -20.996
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.319
    dy = -24.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.537
    dy = -25.608
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.899
    dy = -25.594
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.830
    dy = -22.118
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.825
    dy = -19.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.825
    dy = -19.616
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.475
    dy = -19.616
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.475
    dy = -19.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.773
    dy = -15.744
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.060
    dy = -12.805
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.060
    dy = -12.805
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.078
    dy = -13.035
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.078
    dy = -13.035
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.296
    dy = -11.384
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.073
    dy = -10.802
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.073
    dy = -10.802
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.397
    dy = -11.032
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.397
    dy = -11.032
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.340
    dy = -12.695
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.079
    dy = -14.685
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.079
    dy = -14.685
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.491
    dy = -16.915
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.491
    dy = -16.915
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.304
    dy = -20.848
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.520
    dy = -24.029
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.507
    dy = -26.810
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.949
    dy = -28.191
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.957
    dy = -28.429
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.957
    dy = -28.429
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.198
    dy = -28.190
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.198
    dy = -28.190
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.080
    dy = -27.486
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.080
    dy = -27.486
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.600
    dy = -25.610
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.600
    dy = -25.610
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.004
    dy = -27.308
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.939
    dy = -27.146
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.692
    dy = -27.578
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.283
    dy = -27.500
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.300
    dy = -26.953
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.303
    dy = -25.845
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.303
    dy = -25.845
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.304
    dy = -24.551
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.304
    dy = -24.551
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.151
    dy = -25.730
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.783
    dy = -25.259
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.969
    dy = -25.481
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.607
    dy = -24.902
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.844
    dy = -23.159
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.913
    dy = -18.492
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.209
    dy = -14.805
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.569
    dy = -13.387
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.190
    dy = -13.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.850
    dy = -16.803
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.295
    dy = -20.403
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.835
    dy = -23.264
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.165
    dy = -24.407
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.611
    dy = -22.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.550
    dy = -26.441
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.374
    dy = -27.475
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.909
    dy = -28.187
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.001
    dy = -24.072
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.699
    dy = -19.238
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.394
    dy = -16.343
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.068
    dy = -12.269
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.000
    dy = -9.985
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.000
    dy = -9.985
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.771
    dy = -6.577
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.771
    dy = -6.577
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.130
    dy = -6.218
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.130
    dy = -6.218
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.410
    dy = -5.749
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.410
    dy = -5.749
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.065
    dy = -6.643
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.946
    dy = -10.704
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.785
    dy = -12.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.410
    dy = -13.031
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.333
    dy = -13.040
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.333
    dy = -13.040
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.628
    dy = -13.275
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.628
    dy = -13.275
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.318
    dy = -14.269
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.394
    dy = -14.455
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.637
    dy = -13.870
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.037
    dy = -12.458
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.037
    dy = -12.458
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.985
    dy = -18.560
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.985
    dy = -18.560
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.128
    dy = -21.964
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.710
    dy = -23.822
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.538
    dy = -24.555
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.277
    dy = -21.848
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.277
    dy = -21.848
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.094
    dy = -30.894
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.094
    dy = -30.894
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.911
    dy = -33.670
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.276
    dy = -40.074
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.206
    dy = -42.023
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.540
    dy = -43.119
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.885
    dy = -43.114
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.624
    dy = -42.386
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.982
    dy = -41.231
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.982
    dy = -41.231
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.395
    dy = -43.345
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.395
    dy = -43.345
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.803
    dy = -50.684
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.358
    dy = -55.785
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.762
    dy = -58.155
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.061
    dy = -58.153
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.527
    dy = -56.972
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.534
    dy = -52.399
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.202
    dy = -49.021
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.605
    dy = -49.167
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.841
    dy = -52.256
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.486
    dy = -54.858
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.200
    dy = -55.564
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.787
    dy = -59.205
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.556
    dy = -61.905
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.556
    dy = -61.905
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.026
    dy = -60.260
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.026
    dy = -60.260
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.075
    dy = -61.917
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.441
    dy = -59.714
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.487
    dy = -52.509
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.487
    dy = -52.509
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.975
    dy = -48.742
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.975
    dy = -48.742
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.661
    dy = -44.758
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.661
    dy = -44.758
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.238
    dy = -45.585
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.238
    dy = -45.585
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.511
    dy = -46.861
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.511
    dy = -46.861
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.730
    dy = -43.463
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.730
    dy = -43.463
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.321
    dy = -46.125
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.362
    dy = -49.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.966
    dy = -50.631
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.175
    dy = -50.748
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.878
    dy = -50.277
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.230
    dy = -47.667
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.091
    dy = -45.695
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.341
    dy = -42.771
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.240
    dy = -41.669
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.857
    dy = -40.288
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 3.535
    dy = -37.472
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 3.535
    dy = -37.472
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.881
    dy = -34.418
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.881
    dy = -34.418
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.649
    dy = -27.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.368
    dy = -25.266
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.538
    dy = -25.554
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.793
    dy = -27.372
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.038
    dy = -26.309
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.423
    dy = -25.605
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.917
    dy = -21.848
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.917
    dy = -21.848
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.041
    dy = -21.725
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.041
    dy = -21.725
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.692
    dy = -21.724
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.891
    dy = -23.150
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.148
    dy = -29.200
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.465
    dy = -29.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.549
    dy = -29.243
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.549
    dy = -29.243
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.218
    dy = -28.998
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.218
    dy = -28.998
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.453
    dy = -27.236
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.453
    dy = -27.236
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.283
    dy = -30.413
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.283
    dy = -30.413
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.905
    dy = -30.769
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.905
    dy = -30.769
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.241
    dy = -31.005
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.241
    dy = -31.005
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.851
    dy = -34.170
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.501
    dy = -36.184
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.501
    dy = -36.184
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.885
    dy = -37.903
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.885
    dy = -37.903
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.519
    dy = -40.411
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.519
    dy = -40.411
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.728
    dy = -41.113
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.728
    dy = -41.113
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.542
    dy = -44.680
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.489
    dy = -45.364
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.371
    dy = -45.161
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.639
    dy = -47.458
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.668
    dy = -49.193
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.564
    dy = -49.584
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.856
    dy = -48.748
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.856
    dy = -48.748
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.796
    dy = -49.219
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.796
    dy = -49.219
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.452
    dy = -53.949
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.147
    dy = -59.213
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.166
    dy = -62.532
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.749
    dy = -64.255
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.479
    dy = -64.261
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.791
    dy = -63.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.796
    dy = -60.537
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.863
    dy = -55.509
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.100
    dy = -50.863
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.100
    dy = -50.863
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.463
    dy = -52.264
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.463
    dy = -52.264
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.523
    dy = -52.148
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.523
    dy = -52.148
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.756
    dy = -50.394
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.756
    dy = -50.394
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.290
    dy = -52.038
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.181
    dy = -51.178
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.230
    dy = -49.531
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.702
    dy = -47.270
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.116
    dy = -47.222
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.116
    dy = -47.222
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.234
    dy = -46.633
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.234
    dy = -46.633
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.123
    dy = -47.252
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.006
    dy = -47.736
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.938
    dy = -48.372
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 2.587
    dy = -50.696
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.011
    dy = -57.562
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.011
    dy = -57.562
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.012
    dy = -57.793
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.012
    dy = -57.793
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -59.070
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.647
    dy = -60.025
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.027
    dy = -60.184
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.011
    dy = -59.559
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.011
    dy = -59.559
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.766
    dy = -59.349
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.766
    dy = -59.349
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.382
    dy = -57.879
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.382
    dy = -57.879
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.465
    dy = -57.916
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.465
    dy = -57.916
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.477
    dy = -59.086
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.403
    dy = -58.145
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.403
    dy = -58.145
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.448
    dy = -58.492
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.448
    dy = -58.492
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.203
    dy = -64.078
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.524
    dy = -64.370
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.464
    dy = -64.950
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.076
    dy = -66.379
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.230
    dy = -64.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.229
    dy = -64.257
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.229
    dy = -64.257
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.346
    dy = -65.194
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.346
    dy = -65.194
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.985
    dy = -70.595
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.156
    dy = -72.476
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.660
    dy = -72.592
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.934
    dy = -71.888
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.764
    dy = -71.098
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.211
    dy = -70.589
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.192
    dy = -68.691
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.819
    dy = -66.487
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.819
    dy = -66.487
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.552
    dy = -67.752
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.552
    dy = -67.752
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.350
    dy = -67.192
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.350
    dy = -67.192
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.301
    dy = -67.286
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.301
    dy = -67.286
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.112
    dy = -69.051
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.112
    dy = -69.051
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.125
    dy = -70.584
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.125
    dy = -70.584
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.710
    dy = -71.299
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.710
    dy = -71.299
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.041
    dy = -64.724
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.041
    dy = -64.724
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.249
    dy = -65.128
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.614
    dy = -66.409
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.681
    dy = -69.189
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.681
    dy = -69.189
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.096
    dy = -67.421
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.096
    dy = -67.421
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.352
    dy = -65.406
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.352
    dy = -65.406
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.023
    dy = -62.022
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.023
    dy = -62.022
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.725
    dy = -64.880
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.284
    dy = -69.118
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.315
    dy = -70.524
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.798
    dy = -71.936
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.469
    dy = -72.358
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.340
    dy = -71.507
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.115
    dy = -67.570
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.801
    dy = -69.527
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.025
    dy = -72.656
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.106
    dy = -73.073
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.690
    dy = -74.123
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.737
    dy = -76.242
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.890
    dy = -77.501
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.711
    dy = -77.763
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.114
    dy = -77.127
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.582
    dy = -73.970
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.041
    dy = -71.416
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.546
    dy = -74.027
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.711
    dy = -77.634
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.812
    dy = -83.577
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.297
    dy = -99.964
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.297
    dy = -99.964
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.244
    dy = -84.459
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.244
    dy = -84.459
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.433
    dy = -86.404
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.270
    dy = -86.493
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.248
    dy = -83.541
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.184
    dy = -81.582
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.836
    dy = -80.463
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.836
    dy = -80.463
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.006
    dy = -81.289
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.006
    dy = -81.289
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.643
    dy = -79.893
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.399
    dy = -79.324
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.186
    dy = -77.410
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.893
    dy = -75.999
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.893
    dy = -75.999
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.716
    dy = -73.415
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.716
    dy = -73.415
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.943
    dy = -75.254
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.767
    dy = -76.828
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.767
    dy = -76.828
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.473
    dy = -73.296
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.473
    dy = -73.296
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.352
    dy = -71.773
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.352
    dy = -71.773
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.407
    dy = -70.480
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.407
    dy = -70.480
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.753
    dy = -66.341
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.330
    dy = -64.563
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.883
    dy = -64.595
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.221
    dy = -65.266
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.690
    dy = -70.704
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.146
    dy = -70.950
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.625
    dy = -70.442
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.693
    dy = -67.163
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.928
    dy = -64.137
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.928
    dy = -64.137
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.875
    dy = -64.957
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.875
    dy = -64.957
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.743
    dy = -63.084
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.743
    dy = -63.084
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.932
    dy = -71.067
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.932
    dy = -71.067
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.387
    dy = -82.617
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.389
    dy = -99.965
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.389
    dy = -99.965
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.409
    dy = -100.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.409
    dy = -100.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.757
    dy = -98.233
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.757
    dy = -98.233
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.726
    dy = -97.735
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.726
    dy = -97.735
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.393
    dy = -82.194
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.263
    dy = -75.303
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.712
    dy = -72.794
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.085
    dy = -70.040
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.748
    dy = -62.845
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.809
    dy = -51.685
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.809
    dy = -51.685
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.334
    dy = -51.419
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.334
    dy = -51.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.931
    dy = -51.089
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 53.931
    dy = -51.089
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.601
    dy = -46.278
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.601
    dy = -46.278
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.884
    dy = -44.533
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.884
    dy = -44.533
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.352
    dy = -46.403
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.352
    dy = -46.403
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.245
    dy = -47.459
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.118
    dy = -47.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.305
    dy = -46.399
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.305
    dy = -46.399
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.238
    dy = -49.246
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.238
    dy = -49.246
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.484
    dy = -49.579
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.417
    dy = -49.256
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.417
    dy = -49.256
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.183
    dy = -41.607
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.183
    dy = -41.607
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.537
    dy = -42.516
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.654
    dy = -41.701
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.654
    dy = -41.701
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.300
    dy = -41.697
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.300
    dy = -41.697
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.064
    dy = -39.996
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.480
    dy = -32.465
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.009
    dy = -29.953
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.009
    dy = -29.953
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.155
    dy = -32.432
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.155
    dy = -32.432
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.201
    dy = -31.387
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.767
    dy = -30.792
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.767
    dy = -30.792
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.073
    dy = -30.894
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.073
    dy = -30.894
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.652
    dy = -30.986
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.247
    dy = -32.784
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.379
    dy = -34.285
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.702
    dy = -34.291
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.820
    dy = -33.502
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.751
    dy = -31.601
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.608
    dy = -32.422
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.608
    dy = -32.422
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.800
    dy = -31.486
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.800
    dy = -31.486
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.030
    dy = -31.243
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.030
    dy = -31.243
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.369
    dy = -31.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.369
    dy = -31.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.956
    dy = -31.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.956
    dy = -31.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.024
    dy = -34.300
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.024
    dy = -34.300
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.718
    dy = -40.988
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.653
    dy = -40.529
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.092
    dy = -42.892
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.596
    dy = -43.343
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.573
    dy = -42.959
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.611
    dy = -41.353
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.611
    dy = -41.353
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.330
    dy = -42.006
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.330
    dy = -42.006
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.307
    dy = -42.692
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.769
    dy = -42.655
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.572
    dy = -42.033
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.572
    dy = -42.033
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.485
    dy = -42.871
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.485
    dy = -42.871
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.240
    dy = -45.080
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.240
    dy = -45.080
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.741
    dy = -44.168
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.741
    dy = -44.168
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.384
    dy = -45.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.263
    dy = -46.661
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.450
    dy = -46.581
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.038
    dy = -45.633
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.925
    dy = -44.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.541
    dy = -43.930
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.745
    dy = -42.878
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.745
    dy = -42.878
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.950
    dy = -43.813
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.950
    dy = -43.813
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.827
    dy = -42.105
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.628
    dy = -41.706
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.628
    dy = -41.706
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.631
    dy = -42.049
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.631
    dy = -42.049
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.784
    dy = -42.764
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.784
    dy = -42.764
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.806
    dy = -38.294
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.806
    dy = -38.294
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.012
    dy = -38.892
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.987
    dy = -40.009
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.608
    dy = -40.797
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.714
    dy = -40.732
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.005
    dy = -39.101
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.921
    dy = -38.180
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.921
    dy = -38.180
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.088
    dy = -36.415
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.088
    dy = -36.415
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.284
    dy = -37.019
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.270
    dy = -38.120
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.975
    dy = -38.924
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.997
    dy = -38.511
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.973
    dy = -36.710
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.207
    dy = -36.296
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.207
    dy = -36.296
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.071
    dy = -26.100
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.071
    dy = -26.100
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.789
    dy = -25.756
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.789
    dy = -25.756
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.704
    dy = -34.535
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.704
    dy = -34.535
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.273
    dy = -35.820
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 3.630
    dy = -37.345
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.128
    dy = -39.577
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.635
    dy = -42.945
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.321
    dy = -45.968
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.343
    dy = -47.499
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.280
    dy = -48.039
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.455
    dy = -47.044
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.102
    dy = -44.197
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.803
    dy = -41.812
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.031
    dy = -41.935
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.399
    dy = -41.233
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.244
    dy = -38.590
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.730
    dy = -37.593
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.902
    dy = -35.916
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.863
    dy = -33.542
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.149
    dy = -30.268
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.101
    dy = -29.133
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.736
    dy = -29.131
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.607
    dy = -26.658
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.378
    dy = -22.459
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.080
    dy = -19.318
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.856
    dy = -17.494
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.089
    dy = -15.044
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.384
    dy = -12.102
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.794
    dy = -11.277
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.794
    dy = -11.277
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.497
    dy = -13.161
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.497
    dy = -13.161
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.829
    dy = -13.078
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.430
    dy = -11.917
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.313
    dy = -7.369
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.955
    dy = -5.281
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.955
    dy = -5.281
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.010
    dy = -4.941
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.010
    dy = -4.941
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.073
    dy = -5.044
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.073
    dy = -5.044
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.599
    dy = -7.284
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.599
    dy = -7.284
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.163
    dy = -5.497
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.061
    dy = -2.467
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.061
    dy = -2.467
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.585
    dy = -31.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.585
    dy = -31.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.172
    dy = -31.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.172
    dy = -31.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.285
    dy = -30.901
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.285
    dy = -30.901
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.032
    dy = -31.070
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.814
    dy = -32.422
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.814
    dy = -32.422
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.875
    dy = -31.129
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.875
    dy = -31.129
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.275
    dy = -32.485
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.800
    dy = -34.072
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.146
    dy = -33.897
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.409
    dy = -32.306
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.409
    dy = -32.306
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.942
    dy = -32.553
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.942
    dy = -32.553
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.475
    dy = -31.166
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.475
    dy = -31.166
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.624
    dy = -32.891
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.624
    dy = -32.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.746
    dy = -33.522
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.921
    dy = -35.068
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.858
    dy = -37.981
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.156
    dy = -39.238
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.156
    dy = -39.238
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.087
    dy = -60.156
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.087
    dy = -60.156
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.093
    dy = -61.766
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.093
    dy = -61.766
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.318
    dy = -61.551
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.318
    dy = -61.551
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.343
    dy = -63.534
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.125
    dy = -66.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.846
    dy = -69.396
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.369
    dy = -72.118
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.453
    dy = -73.300
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.650
    dy = -71.686
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.012
    dy = -71.653
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.039
    dy = -70.968
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.888
    dy = -66.345
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.822
    dy = -64.406
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.069
    dy = -63.154
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.311
    dy = -62.718
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.447
    dy = -63.779
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.932
    dy = -66.852
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.418
    dy = -71.184
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.404
    dy = -74.474
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.404
    dy = -74.474
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.537
    dy = -86.690
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.537
    dy = -86.690
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.028
    dy = -90.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.953
    dy = -92.977
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.642
    dy = -99.964
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.642
    dy = -99.964
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.054
    dy = -54.734
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.054
    dy = -54.734
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.353
    dy = -52.637
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.353
    dy = -52.637
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.755
    dy = -58.733
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.755
    dy = -58.733
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.568
    dy = -58.030
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.239
    dy = -54.438
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.622
    dy = -54.445
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.269
    dy = -55.564
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.765
    dy = -59.194
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.560
    dy = -57.913
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 3.395
    dy = -57.553
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 1.210
    dy = -58.852
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 2.002
    dy = -55.594
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.467
    dy = -50.852
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.357
    dy = -49.688
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.357
    dy = -49.688
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.153
    dy = -49.209
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.153
    dy = -49.209
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.663
    dy = -49.567
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.166
    dy = -49.269
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.935
    dy = -48.617
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.935
    dy = -48.617
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.232
    dy = -46.533
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.232
    dy = -46.533
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.866
    dy = -46.663
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.858
    dy = -48.072
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.412
    dy = -50.153
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.412
    dy = -50.153
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.717
    dy = -51.211
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.717
    dy = -51.211
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.834
    dy = -54.269
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.834
    dy = -54.269
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

