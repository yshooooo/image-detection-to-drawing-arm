from DSR_ROBOT2 import movel, posx

Y_START = 0.000000
Y_Z_TOTAL_OFFSET = -0.900000
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

    dx = 23.242
    dy = -19.881
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.242
    dy = -19.881
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.081
    dy = -23.260
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.246
    dy = -25.518
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.551
    dy = -28.493
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.151
    dy = -35.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.466
    dy = -32.695
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.466
    dy = -32.695
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.271
    dy = -34.226
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.271
    dy = -34.226
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.792
    dy = -35.151
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.099
    dy = -37.481
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.203
    dy = -39.115
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.130
    dy = -40.458
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.905
    dy = -42.213
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.658
    dy = -43.724
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.956
    dy = -44.919
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.956
    dy = -44.919
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.477
    dy = -48.636
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.477
    dy = -48.636
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.331
    dy = -39.416
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.331
    dy = -39.416
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.739
    dy = -39.229
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.739
    dy = -39.229
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.325
    dy = -38.103
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.318
    dy = -35.527
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.318
    dy = -35.527
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.075
    dy = -36.391
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.075
    dy = -36.391
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.604
    dy = -34.862
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.604
    dy = -34.862
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.995
    dy = -34.519
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.995
    dy = -34.519
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.639
    dy = -34.711
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.028
    dy = -36.317
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.270
    dy = -37.333
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.876
    dy = -36.836
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.273
    dy = -36.107
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.075
    dy = -35.141
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.075
    dy = -35.141
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.406
    dy = -33.979
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.406
    dy = -33.979
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.382
    dy = -34.068
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.676
    dy = -35.235
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.892
    dy = -36.787
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.892
    dy = -36.787
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.112
    dy = -34.531
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.112
    dy = -34.531
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.726
    dy = -38.487
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.801
    dy = -45.894
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.801
    dy = -45.894
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.931
    dy = -45.867
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.931
    dy = -45.867
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.328
    dy = -47.407
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.983
    dy = -48.863
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.718
    dy = -48.967
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.493
    dy = -50.482
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.330
    dy = -50.393
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.132
    dy = -49.073
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.351
    dy = -48.540
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.434
    dy = -46.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.434
    dy = -46.173
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.626
    dy = -52.612
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.626
    dy = -52.612
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.193
    dy = -54.252
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.959
    dy = -54.744
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.959
    dy = -54.744
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.787
    dy = -54.120
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.787
    dy = -54.120
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.919
    dy = -55.190
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.433
    dy = -55.991
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.567
    dy = -55.960
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.121
    dy = -55.232
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.889
    dy = -54.426
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.889
    dy = -54.426
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.805
    dy = -52.624
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.805
    dy = -52.624
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.195
    dy = -54.027
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.164
    dy = -55.670
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.164
    dy = -55.670
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.499
    dy = -58.334
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.499
    dy = -58.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.985
    dy = -58.735
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.167
    dy = -58.150
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.167
    dy = -58.150
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.363
    dy = -57.803
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.363
    dy = -57.803
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.056
    dy = -62.824
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.601
    dy = -63.329
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.395
    dy = -63.243
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.225
    dy = -62.339
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.213
    dy = -60.536
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.213
    dy = -60.536
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.461
    dy = -61.170
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.461
    dy = -61.170
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.433
    dy = -66.038
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.652
    dy = -66.336
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.573
    dy = -63.609
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 56.573
    dy = -63.609
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.045
    dy = -63.608
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.045
    dy = -63.608
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.668
    dy = -65.849
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.345
    dy = -66.604
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.931
    dy = -70.612
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.818
    dy = -75.505
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.830
    dy = -81.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.171
    dy = -82.977
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.494
    dy = -93.322
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.663
    dy = -100.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.663
    dy = -100.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.191
    dy = -92.966
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.191
    dy = -92.966
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.432
    dy = -82.160
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.771
    dy = -75.966
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.824
    dy = -70.034
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.824
    dy = -70.034
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.601
    dy = -64.835
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.601
    dy = -64.835
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.529
    dy = -69.355
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.403
    dy = -72.522
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.534
    dy = -76.659
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.473
    dy = -85.079
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.307
    dy = -87.641
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 3.059
    dy = -91.253
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -100.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -100.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.173
    dy = -89.292
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.173
    dy = -89.292
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.804
    dy = -87.771
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.804
    dy = -87.771
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.745
    dy = -89.908
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.745
    dy = -89.908
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.936
    dy = -82.870
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.922
    dy = -86.879
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.766
    dy = -87.283
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.239
    dy = -77.369
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.239
    dy = -77.369
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.056
    dy = -79.202
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.056
    dy = -79.202
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.364
    dy = -80.731
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.364
    dy = -80.731
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.308
    dy = -83.181
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.308
    dy = -83.181
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.954
    dy = -82.590
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.536
    dy = -83.224
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.640
    dy = -92.658
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.450
    dy = -92.393
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.065
    dy = -90.510
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.884
    dy = -81.867
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.861
    dy = -72.314
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.632
    dy = -72.179
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.779
    dy = -73.095
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.662
    dy = -75.822
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.181
    dy = -76.434
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.392
    dy = -75.276
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.875
    dy = -73.812
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.775
    dy = -72.804
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.799
    dy = -71.867
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.992
    dy = -71.026
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.171
    dy = -68.388
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.968
    dy = -63.899
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.586
    dy = -62.363
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.207
    dy = -60.121
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.740
    dy = -55.538
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.773
    dy = -52.982
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.836
    dy = -50.458
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.310
    dy = -48.931
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.310
    dy = -48.931
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.399
    dy = -47.402
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.399
    dy = -47.402
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.331
    dy = -48.632
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.143
    dy = -47.241
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.979
    dy = -43.437
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.979
    dy = -43.437
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.256
    dy = -42.461
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.256
    dy = -42.461
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.641
    dy = -43.014
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.635
    dy = -38.547
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.635
    dy = -38.547
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.263
    dy = -37.917
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.263
    dy = -37.917
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.840
    dy = -38.369
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 74.252
    dy = -41.368
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.991
    dy = -41.817
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.112
    dy = -41.852
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.112
    dy = -41.852
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 74.663
    dy = -41.849
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 74.663
    dy = -41.849
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.623
    dy = -43.773
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 80.153
    dy = -44.344
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.493
    dy = -45.250
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.493
    dy = -45.250
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.374
    dy = -43.164
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.374
    dy = -43.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.141
    dy = -43.202
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.691
    dy = -43.702
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.205
    dy = -46.157
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.356
    dy = -51.089
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.945
    dy = -51.629
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.376
    dy = -51.297
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.376
    dy = -51.297
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.243
    dy = -51.981
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.243
    dy = -51.981
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 88.273
    dy = -52.940
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.466
    dy = -54.420
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.318
    dy = -55.036
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.871
    dy = -56.428
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 83.200
    dy = -58.056
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.400
    dy = -58.566
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.059
    dy = -60.171
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.966
    dy = -62.595
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.155
    dy = -63.914
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.545
    dy = -63.941
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.545
    dy = -63.941
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.063
    dy = -66.058
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.063
    dy = -66.058
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.578
    dy = -68.237
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.578
    dy = -68.237
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 76.423
    dy = -69.704
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 76.423
    dy = -69.704
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.985
    dy = -72.648
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.263
    dy = -73.489
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.363
    dy = -73.704
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.363
    dy = -73.704
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.503
    dy = -75.268
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.503
    dy = -75.268
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.567
    dy = -77.869
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.191
    dy = -76.782
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.191
    dy = -76.782
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.982
    dy = -78.272
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.982
    dy = -78.272
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.149
    dy = -79.769
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.919
    dy = -81.017
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.919
    dy = -81.017
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.390
    dy = -81.662
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 73.390
    dy = -81.662
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.919
    dy = -81.430
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.779
    dy = -82.414
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.666
    dy = -83.173
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.405
    dy = -84.124
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 75.794
    dy = -84.103
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 77.153
    dy = -83.747
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 77.736
    dy = -81.682
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.590
    dy = -80.843
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.213
    dy = -81.357
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.954
    dy = -81.049
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.804
    dy = -78.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 91.474
    dy = -77.176
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.218
    dy = -76.756
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.218
    dy = -76.756
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 88.921
    dy = -75.721
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 88.921
    dy = -75.721
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.878
    dy = -76.263
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.537
    dy = -76.822
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.474
    dy = -76.970
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.474
    dy = -76.970
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.173
    dy = -75.439
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.173
    dy = -75.439
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.093
    dy = -75.868
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.063
    dy = -76.491
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 86.446
    dy = -76.795
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.373
    dy = -75.915
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.373
    dy = -75.915
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.869
    dy = -74.619
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.869
    dy = -74.619
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.238
    dy = -75.569
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.673
    dy = -74.956
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.098
    dy = -73.677
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.779
    dy = -74.307
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.226
    dy = -73.981
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.904
    dy = -71.116
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.599
    dy = -70.383
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 80.984
    dy = -70.042
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 80.188
    dy = -67.793
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.655
    dy = -67.744
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 82.976
    dy = -68.524
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.340
    dy = -67.857
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.429
    dy = -69.159
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.431
    dy = -67.703
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.266
    dy = -67.547
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 91.546
    dy = -68.190
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 92.058
    dy = -67.873
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.975
    dy = -65.002
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.275
    dy = -62.804
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.656
    dy = -61.482
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.322
    dy = -60.849
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.322
    dy = -60.849
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.028
    dy = -61.145
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.028
    dy = -61.145
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 83.036
    dy = -63.561
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.993
    dy = -65.183
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.885
    dy = -65.949
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.804
    dy = -67.595
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.804
    dy = -67.595
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.291
    dy = -70.674
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.291
    dy = -70.674
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.914
    dy = -72.203
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.914
    dy = -72.203
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.996
    dy = -74.613
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.996
    dy = -74.613
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.986
    dy = -75.836
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 81.986
    dy = -75.836
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 80.431
    dy = -78.901
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 80.431
    dy = -78.901
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.504
    dy = -80.426
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 79.504
    dy = -80.426
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.901
    dy = -81.647
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 78.901
    dy = -81.647
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 83.408
    dy = -84.712
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 85.537
    dy = -87.126
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.711
    dy = -91.167
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.196
    dy = -99.750
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.837
    dy = -99.987
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 90.837
    dy = -99.987
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.290
    dy = -72.481
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.290
    dy = -72.481
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.953
    dy = -70.354
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.953
    dy = -70.354
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.794
    dy = -70.973
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.794
    dy = -70.973
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.974
    dy = -66.685
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.974
    dy = -66.685
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.252
    dy = -66.330
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.252
    dy = -66.330
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.939
    dy = -69.736
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.128
    dy = -71.820
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.128
    dy = -71.820
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.471
    dy = -56.215
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 69.471
    dy = -56.215
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 68.435
    dy = -56.317
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.015
    dy = -54.548
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.015
    dy = -54.548
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.840
    dy = -50.305
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.840
    dy = -50.305
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.442
    dy = -51.351
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.802
    dy = -52.032
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.481
    dy = -52.210
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.057
    dy = -51.784
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 66.005
    dy = -50.299
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.066
    dy = -50.109
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.066
    dy = -50.109
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.623
    dy = -53.106
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.623
    dy = -53.106
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 70.893
    dy = -54.103
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.248
    dy = -54.873
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.090
    dy = -55.192
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.824
    dy = -54.853
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 72.774
    dy = -53.161
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.779
    dy = -52.890
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 71.779
    dy = -52.890
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.797
    dy = -58.153
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 84.797
    dy = -58.153
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 87.927
    dy = -56.828
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.587
    dy = -54.702
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 89.587
    dy = -54.702
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.301
    dy = -44.879
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.301
    dy = -44.879
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.599
    dy = -43.593
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.082
    dy = -41.900
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.771
    dy = -40.188
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.702
    dy = -39.036
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.702
    dy = -39.036
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.727
    dy = -39.156
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.727
    dy = -39.156
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.502
    dy = -48.632
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.502
    dy = -48.632
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.623
    dy = -37.869
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.623
    dy = -37.869
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.574
    dy = -38.695
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.081
    dy = -38.842
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.651
    dy = -38.428
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.789
    dy = -37.570
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.789
    dy = -37.570
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.319
    dy = -35.442
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.319
    dy = -35.442
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.684
    dy = -32.694
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.684
    dy = -32.694
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.614
    dy = -35.157
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.614
    dy = -35.157
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.210
    dy = -34.407
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.753
    dy = -34.855
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.845
    dy = -37.613
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.701
    dy = -36.849
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 58.430
    dy = -29.391
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.671
    dy = -26.154
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.494
    dy = -20.548
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.457
    dy = -14.470
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 51.191
    dy = -12.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.460
    dy = -11.925
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.460
    dy = -11.925
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.151
    dy = -12.238
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.151
    dy = -12.238
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.200
    dy = -15.352
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 41.648
    dy = -17.432
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.090
    dy = -18.653
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.105
    dy = -19.263
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.105
    dy = -19.263
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.626
    dy = -18.523
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.626
    dy = -18.523
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.026
    dy = -15.986
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.874
    dy = -15.406
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.776
    dy = -15.227
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.776
    dy = -15.227
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.683
    dy = -17.456
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.683
    dy = -17.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.961
    dy = -20.209
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.860
    dy = -24.381
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.860
    dy = -24.381
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.629
    dy = -23.547
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.629
    dy = -23.547
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.629
    dy = -22.018
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.629
    dy = -22.018
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.529
    dy = -29.340
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.529
    dy = -29.340
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.359
    dy = -30.016
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.773
    dy = -30.704
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.281
    dy = -31.411
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.941
    dy = -32.038
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.093
    dy = -31.155
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.322
    dy = -32.130
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.736
    dy = -31.834
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.942
    dy = -31.146
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.215
    dy = -29.673
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.215
    dy = -29.673
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.435
    dy = -36.418
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.435
    dy = -36.418
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.825
    dy = -35.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.524
    dy = -34.352
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.524
    dy = -34.352
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.783
    dy = -33.958
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.783
    dy = -33.958
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.853
    dy = -34.260
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.275
    dy = -36.128
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.275
    dy = -36.128
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.401
    dy = -34.452
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.401
    dy = -34.452
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.383
    dy = -36.361
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.938
    dy = -37.061
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.349
    dy = -36.539
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.897
    dy = -34.786
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.897
    dy = -34.786
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.701
    dy = -29.041
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 47.701
    dy = -29.041
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.599
    dy = -29.593
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.840
    dy = -30.720
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 42.887
    dy = -31.477
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.902
    dy = -30.883
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.331
    dy = -31.850
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 52.575
    dy = -31.309
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.993
    dy = -29.587
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.008
    dy = -28.754
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.008
    dy = -28.754
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.920
    dy = -0.308
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.920
    dy = -0.308
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.309
    dy = -1.198
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.929
    dy = -4.687
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.119
    dy = -8.041
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.746
    dy = -12.241
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.628
    dy = -16.793
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.988
    dy = -20.611
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.581
    dy = -26.338
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.450
    dy = -32.021
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.968
    dy = -32.417
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.385
    dy = -32.097
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.462
    dy = -33.630
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.818
    dy = -35.069
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.831
    dy = -38.504
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.983
    dy = -46.877
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.150
    dy = -49.026
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.776
    dy = -49.250
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.502
    dy = -48.910
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.756
    dy = -55.339
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.968
    dy = -60.056
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.812
    dy = -64.549
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.640
    dy = -64.632
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.729
    dy = -67.466
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.305
    dy = -69.122
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 40.998
    dy = -69.408
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 46.301
    dy = -67.808
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 49.272
    dy = -65.108
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 55.352
    dy = -57.083
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.171
    dy = -49.167
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.364
    dy = -49.228
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.443
    dy = -48.058
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.074
    dy = -46.789
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.114
    dy = -43.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.896
    dy = -42.502
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.249
    dy = -41.962
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.840
    dy = -39.998
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 65.154
    dy = -34.993
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 64.522
    dy = -33.550
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.416
    dy = -32.416
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.701
    dy = -32.091
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.083
    dy = -32.443
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 60.861
    dy = -31.817
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 62.045
    dy = -29.082
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.316
    dy = -23.148
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 63.301
    dy = -17.175
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 61.786
    dy = -12.006
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 59.763
    dy = -8.948
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 57.239
    dy = -6.739
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 54.457
    dy = -5.224
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 50.759
    dy = -4.294
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 48.240
    dy = -2.143
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 45.529
    dy = -0.904
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 43.220
    dy = -0.289
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.225
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.225
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

