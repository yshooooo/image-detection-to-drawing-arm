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

    dx = 14.652
    dy = -6.825
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.652
    dy = -6.825
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.862
    dy = -8.538
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.990
    dy = -10.047
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.990
    dy = -10.047
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.844
    dy = -11.663
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.844
    dy = -11.663
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.813
    dy = -13.154
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.562
    dy = -12.834
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.988
    dy = -10.988
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.103
    dy = -10.336
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.059
    dy = -9.681
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.172
    dy = -9.925
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.922
    dy = -11.547
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.240
    dy = -11.354
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.110
    dy = -9.848
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.348
    dy = -9.361
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.871
    dy = -8.188
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.772
    dy = -6.490
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.643
    dy = -5.839
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.798
    dy = -5.437
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.654
    dy = -1.360
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.793
    dy = -0.124
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.793
    dy = -0.124
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.668
    dy = -0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.668
    dy = -0.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.985
    dy = -1.736
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.037
    dy = -1.742
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.447
    dy = -0.240
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.235
    dy = -2.324
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.758
    dy = -5.436
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.524
    dy = -6.334
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.641
    dy = -8.131
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.131
    dy = -10.143
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.747
    dy = -13.257
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.134
    dy = -13.892
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.024
    dy = -16.061
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.610
    dy = -17.127
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.855
    dy = -14.756
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.588
    dy = -15.372
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.851
    dy = -15.143
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.303
    dy = -16.379
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.054
    dy = -19.652
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.301
    dy = -21.367
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.172
    dy = -22.211
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.333
    dy = -22.018
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.102
    dy = -20.720
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.596
    dy = -18.301
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.719
    dy = -15.384
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.719
    dy = -15.384
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.655
    dy = -14.593
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.655
    dy = -14.593
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.882
    dy = -13.220
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.882
    dy = -13.220
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.376
    dy = -17.121
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.376
    dy = -17.121
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.838
    dy = -20.083
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.613
    dy = -21.096
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.741
    dy = -21.372
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.865
    dy = -22.659
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.871
    dy = -23.219
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.194
    dy = -25.401
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.004
    dy = -25.432
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.445
    dy = -26.429
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.398
    dy = -26.310
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.829
    dy = -24.599
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.426
    dy = -24.187
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.038
    dy = -26.309
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.994
    dy = -26.432
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.306
    dy = -25.186
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.720
    dy = -18.780
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.688
    dy = -17.746
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.636
    dy = -15.785
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.305
    dy = -14.633
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.274
    dy = -13.523
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.274
    dy = -13.523
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.899
    dy = -13.768
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.899
    dy = -13.768
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.223
    dy = -14.696
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.893
    dy = -14.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.893
    dy = -14.891
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.303
    dy = -15.011
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.303
    dy = -15.011
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.636
    dy = -14.771
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.485
    dy = -13.115
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.184
    dy = -9.887
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.351
    dy = -8.417
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.886
    dy = -6.575
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.886
    dy = -6.575
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.147
    dy = -9.682
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.147
    dy = -9.682
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.542
    dy = -10.909
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.695
    dy = -12.654
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.393
    dy = -12.582
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.806
    dy = -11.411
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.806
    dy = -11.411
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.811
    dy = -11.477
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.811
    dy = -11.477
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.920
    dy = -12.294
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.424
    dy = -12.827
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.120
    dy = -12.416
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.978
    dy = -11.636
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.978
    dy = -11.636
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.683
    dy = -7.942
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.683
    dy = -7.942
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.305
    dy = -7.697
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.305
    dy = -7.697
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.969
    dy = -18.131
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.969
    dy = -18.131
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.740
    dy = -19.518
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.870
    dy = -21.245
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.870
    dy = -21.245
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.839
    dy = -23.086
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.839
    dy = -23.086
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.109
    dy = -25.309
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.109
    dy = -25.309
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.260
    dy = -23.817
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.260
    dy = -23.817
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.272
    dy = -23.196
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.272
    dy = -23.196
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.276
    dy = -25.806
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.276
    dy = -25.806
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.327
    dy = -27.367
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.348
    dy = -33.213
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.338
    dy = -39.109
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.330
    dy = -45.085
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.404
    dy = -52.692
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.066
    dy = -56.472
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.184
    dy = -60.800
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.836
    dy = -60.912
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.839
    dy = -61.428
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.430
    dy = -61.043
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.430
    dy = -61.043
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.801
    dy = -60.794
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.801
    dy = -60.794
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.055
    dy = -54.510
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.798
    dy = -48.900
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.542
    dy = -49.097
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.666
    dy = -47.934
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.686
    dy = -48.621
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.307
    dy = -48.338
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.257
    dy = -47.136
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.057
    dy = -46.767
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.979
    dy = -47.016
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.063
    dy = -45.282
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.337
    dy = -45.501
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.596
    dy = -42.798
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.471
    dy = -40.570
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.471
    dy = -40.570
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.853
    dy = -41.936
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.853
    dy = -41.936
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.460
    dy = -44.649
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.932
    dy = -47.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.196
    dy = -47.715
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.739
    dy = -47.658
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.725
    dy = -44.543
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.725
    dy = -44.543
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.476
    dy = -47.875
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.476
    dy = -47.875
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.083
    dy = -48.116
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.083
    dy = -48.116
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.472
    dy = -48.136
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.472
    dy = -48.136
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.599
    dy = -48.755
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.599
    dy = -48.755
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.465
    dy = -47.891
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.465
    dy = -47.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.959
    dy = -43.916
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.584
    dy = -38.373
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.180
    dy = -35.202
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.547
    dy = -32.668
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.011
    dy = -30.577
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.078
    dy = -28.412
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.078
    dy = -28.412
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.473
    dy = -28.413
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.473
    dy = -28.413
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.127
    dy = -29.668
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.476
    dy = -31.419
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.358
    dy = -33.410
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.103
    dy = -38.004
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.492
    dy = -40.201
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.492
    dy = -40.201
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.242
    dy = -36.475
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.242
    dy = -36.475
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.504
    dy = -37.736
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.132
    dy = -42.072
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.881
    dy = -44.815
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.126
    dy = -45.249
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.146
    dy = -46.641
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.650
    dy = -43.387
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.135
    dy = -39.207
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.888
    dy = -37.383
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.998
    dy = -35.112
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.998
    dy = -35.112
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.355
    dy = -34.237
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.355
    dy = -34.237
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.040
    dy = -31.025
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.227
    dy = -28.910
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.227
    dy = -28.910
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.743
    dy = -28.164
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.743
    dy = -28.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.750
    dy = -28.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.750
    dy = -28.164
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.758
    dy = -28.659
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.758
    dy = -28.659
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.585
    dy = -30.283
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.146
    dy = -32.195
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.637
    dy = -36.690
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.770
    dy = -39.727
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.647
    dy = -41.801
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.678
    dy = -41.811
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.678
    dy = -41.811
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.336
    dy = -41.321
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.336
    dy = -41.321
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 7.407
    dy = -44.627
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.679
    dy = -47.273
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.679
    dy = -47.273
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.809
    dy = -47.888
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.809
    dy = -47.888
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.941
    dy = -48.629
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.941
    dy = -48.629
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.671
    dy = -49.256
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.671
    dy = -49.256
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.925
    dy = -50.129
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.925
    dy = -50.129
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.536
    dy = -49.136
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.536
    dy = -49.136
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.302
    dy = -48.648
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.302
    dy = -48.648
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.272
    dy = -47.013
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.272
    dy = -47.013
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.268
    dy = -46.773
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.268
    dy = -46.773
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.765
    dy = -47.657
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.765
    dy = -47.657
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.446
    dy = -44.642
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.446
    dy = -44.642
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.372
    dy = -47.140
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.372
    dy = -47.140
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.011
    dy = -47.414
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.562
    dy = -46.227
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.481
    dy = -45.672
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.481
    dy = -45.672
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.523
    dy = -45.918
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.523
    dy = -45.918
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.245
    dy = -47.394
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.245
    dy = -47.394
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.251
    dy = -47.608
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.251
    dy = -47.608
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.001
    dy = -47.633
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.001
    dy = -47.633
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.135
    dy = -51.007
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.135
    dy = -51.007
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.873
    dy = -51.189
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.776
    dy = -52.104
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.776
    dy = -52.104
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.039
    dy = -53.458
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.039
    dy = -53.458
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.623
    dy = -54.292
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 15.623
    dy = -54.292
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.882
    dy = -52.248
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.882
    dy = -52.248
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.251
    dy = -51.746
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.251
    dy = -51.746
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.192
    dy = -51.343
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.192
    dy = -51.343
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.195
    dy = -51.885
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.195
    dy = -51.885
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.585
    dy = -53.452
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.585
    dy = -53.452
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.929
    dy = -54.340
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.929
    dy = -54.340
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.927
    dy = -61.538
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.927
    dy = -61.538
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.528
    dy = -69.757
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.018
    dy = -73.070
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.399
    dy = -80.271
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -88.709
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = -88.709
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.343
    dy = -91.811
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 4.343
    dy = -91.811
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 5.323
    dy = -90.284
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.113
    dy = -87.227
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.175
    dy = -85.236
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.175
    dy = -85.236
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.421
    dy = -83.993
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.421
    dy = -83.993
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.161
    dy = -84.616
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.565
    dy = -85.100
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.590
    dy = -84.513
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.143
    dy = -81.506
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 12.143
    dy = -81.506
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.400
    dy = -80.769
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.400
    dy = -80.769
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.674
    dy = -88.092
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.742
    dy = -99.504
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.742
    dy = -99.504
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.141
    dy = -99.505
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 14.141
    dy = -99.505
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.974
    dy = -93.051
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.540
    dy = -84.863
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.540
    dy = -84.863
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.435
    dy = -87.223
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 9.435
    dy = -87.223
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.577
    dy = -100.000
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 6.577
    dy = -100.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.584
    dy = -89.830
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.584
    dy = -89.830
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.016
    dy = -88.545
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.863
    dy = -85.479
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.863
    dy = -85.479
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.951
    dy = -72.357
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 21.951
    dy = -72.357
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.683
    dy = -72.847
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.683
    dy = -72.847
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.064
    dy = -69.850
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.064
    dy = -69.850
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.733
    dy = -70.707
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.603
    dy = -70.093
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.603
    dy = -70.093
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.604
    dy = -68.362
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.604
    dy = -68.362
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.983
    dy = -68.362
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.983
    dy = -68.362
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.871
    dy = -67.746
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.871
    dy = -67.746
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.290
    dy = -66.368
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.290
    dy = -66.368
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.972
    dy = -65.998
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.972
    dy = -65.998
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.099
    dy = -66.379
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.382
    dy = -66.008
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.684
    dy = -67.493
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.684
    dy = -67.493
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.046
    dy = -68.614
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.046
    dy = -68.614
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.538
    dy = -68.001
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.599
    dy = -67.976
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.599
    dy = -67.976
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.072
    dy = -65.405
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.072
    dy = -65.405
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.704
    dy = -65.134
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.577
    dy = -63.422
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.577
    dy = -63.422
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.710
    dy = -62.422
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.710
    dy = -62.422
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.917
    dy = -60.799
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.314
    dy = -58.809
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.314
    dy = -58.809
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.079
    dy = -61.187
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.079
    dy = -61.187
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.416
    dy = -62.169
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.344
    dy = -61.294
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.344
    dy = -61.294
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.466
    dy = -62.172
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.466
    dy = -62.172
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 18.627
    dy = -61.162
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.010
    dy = -59.069
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.010
    dy = -59.069
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.871
    dy = -60.920
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 17.871
    dy = -60.920
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.479
    dy = -64.134
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.479
    dy = -64.134
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.354
    dy = -57.198
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.354
    dy = -57.198
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.719
    dy = -52.158
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.213
    dy = -50.128
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 20.213
    dy = -50.128
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.452
    dy = -49.006
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.452
    dy = -49.006
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.335
    dy = -48.259
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.335
    dy = -48.259
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.700
    dy = -47.898
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.700
    dy = -47.898
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 24.299
    dy = -49.660
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.831
    dy = -52.466
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.831
    dy = -52.466
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.684
    dy = -51.728
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.684
    dy = -51.728
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.351
    dy = -50.733
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.351
    dy = -50.733
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.800
    dy = -50.490
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.800
    dy = -50.490
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.054
    dy = -50.816
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.774
    dy = -50.461
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.774
    dy = -50.461
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.778
    dy = -50.373
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.778
    dy = -50.373
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.235
    dy = -51.268
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.235
    dy = -51.268
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.286
    dy = -51.002
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.286
    dy = -51.002
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.663
    dy = -51.626
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.663
    dy = -51.626
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.427
    dy = -53.607
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.427
    dy = -53.607
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.972
    dy = -52.837
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.972
    dy = -52.837
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.563
    dy = -46.157
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.563
    dy = -46.157
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.860
    dy = -45.577
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.314
    dy = -45.829
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.297
    dy = -46.351
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.085
    dy = -47.018
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.845
    dy = -46.155
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.152
    dy = -44.534
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.190
    dy = -44.793
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.665
    dy = -41.053
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.301
    dy = -38.459
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.301
    dy = -38.459
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.178
    dy = -41.065
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.178
    dy = -41.065
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.989
    dy = -43.008
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.340
    dy = -48.121
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 22.589
    dy = -45.851
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.077
    dy = -41.813
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.077
    dy = -41.813
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.066
    dy = -43.164
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.066
    dy = -43.164
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.091
    dy = -45.214
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.031
    dy = -44.915
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.031
    dy = -44.915
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.957
    dy = -44.389
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.957
    dy = -44.389
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.855
    dy = -41.651
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.855
    dy = -41.651
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.405
    dy = -44.422
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 29.405
    dy = -44.422
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.686
    dy = -45.256
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.518
    dy = -42.926
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.518
    dy = -42.926
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.861
    dy = -45.243
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.861
    dy = -45.243
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.110
    dy = -45.810
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.639
    dy = -45.369
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.639
    dy = -45.369
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.265
    dy = -45.908
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.265
    dy = -45.908
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.893
    dy = -46.810
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.009
    dy = -47.643
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.009
    dy = -47.643
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.271
    dy = -47.386
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.271
    dy = -47.386
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.121
    dy = -46.720
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.793
    dy = -46.829
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.469
    dy = -47.957
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.120
    dy = -47.887
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.994
    dy = -46.279
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.994
    dy = -46.279
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.107
    dy = -48.008
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.107
    dy = -48.008
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.616
    dy = -48.133
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.616
    dy = -48.133
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.512
    dy = -47.988
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.512
    dy = -47.988
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.390
    dy = -49.744
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.738
    dy = -53.224
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.738
    dy = -53.224
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.973
    dy = -53.846
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.973
    dy = -53.846
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.308
    dy = -55.623
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.849
    dy = -55.347
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.890
    dy = -53.300
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.338
    dy = -51.601
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.838
    dy = -41.228
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.330
    dy = -35.417
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.191
    dy = -32.468
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.669
    dy = -30.396
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.525
    dy = -28.529
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.893
    dy = -26.194
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.909
    dy = -25.558
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.909
    dy = -25.558
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.296
    dy = -28.784
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 27.296
    dy = -28.784
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.898
    dy = -29.443
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.259
    dy = -30.918
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.010
    dy = -32.725
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 31.628
    dy = -37.263
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.772
    dy = -39.611
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.144
    dy = -40.928
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.601
    dy = -40.943
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.601
    dy = -40.943
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.014
    dy = -40.891
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.014
    dy = -40.891
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.913
    dy = -39.964
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.185
    dy = -38.200
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.185
    dy = -38.200
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.842
    dy = -35.983
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.842
    dy = -35.983
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.969
    dy = -38.354
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.472
    dy = -40.986
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 38.206
    dy = -43.720
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.970
    dy = -46.400
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.970
    dy = -46.400
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.642
    dy = -46.288
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.642
    dy = -46.288
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.022
    dy = -46.161
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.022
    dy = -46.161
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.097
    dy = -52.730
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.097
    dy = -52.730
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 37.597
    dy = -55.104
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.766
    dy = -61.177
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.829
    dy = -62.658
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.290
    dy = -62.770
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.116
    dy = -62.140
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.348
    dy = -60.322
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.880
    dy = -60.187
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.368
    dy = -59.125
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.286
    dy = -56.605
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.862
    dy = -56.972
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.485
    dy = -60.050
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.485
    dy = -60.050
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.990
    dy = -62.905
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 34.990
    dy = -62.905
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.972
    dy = -68.636
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.714
    dy = -72.330
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 28.822
    dy = -77.610
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 26.795
    dy = -79.509
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 23.799
    dy = -80.272
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 19.118
    dy = -79.781
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 16.340
    dy = -77.273
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.276
    dy = -73.449
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.276
    dy = -73.449
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.879
    dy = -72.456
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 32.879
    dy = -72.456
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.176
    dy = -79.661
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.043
    dy = -80.709
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.235
    dy = -82.194
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 39.179
    dy = -83.495
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.665
    dy = -88.089
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 44.665
    dy = -88.089
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.104
    dy = -82.382
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.104
    dy = -82.382
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 36.103
    dy = -85.808
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 35.201
    dy = -90.229
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.059
    dy = -95.622
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.398
    dy = -99.876
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.398
    dy = -99.876
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.808
    dy = -99.504
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 25.808
    dy = -99.504
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 30.764
    dy = -92.006
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.234
    dy = -86.609
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.626
    dy = -82.562
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.126
    dy = -79.778
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 33.126
    dy = -79.778
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.313
    dy = -37.220
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 8.313
    dy = -37.220
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 10.188
    dy = -35.726
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 11.285
    dy = -30.620
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.279
    dy = -27.911
    base_z = 0.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 13.279
    dy = -27.911
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

    dx = 0.000
    dy = 0.000
    base_z = 10.000
    movel(posx(cx + dx, cy + dy, cz + base_z + calc_z_offset(dy), *PEN_RPY), vel=vel, acc=acc, r=1)

