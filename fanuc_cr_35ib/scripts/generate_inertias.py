import numpy as np

# Codice per generare file xacro per parametri di massa, centro di massa, inerzia rispetto al centro
# di massa, Da terna cad a Terna DH

# CAD Parameters

    # Sensor
s_mass_cad = 124
s_mass_real = s_mass_cad
s_cm_x_cad = 0.1556e-3
s_cm_y_cad = -0.0218e-3
s_cm_z_cad = 127.2444e-3
s_xx_cad = 1940807.25e-6
s_xy_cad = 1454.1876e-6
s_xz_cad = 1845.6964e-6
s_yy_cad = 1867988.353e-6
s_yz_cad = -263.9106e-6
s_zz_cad = 2707963.372e-6
s_dx_cad = 0e-3
s_dy_cad = 0e-3
s_dz_cad = 0e-3
s_rx_cad = np.deg2rad(0)
s_ry_cad = np.deg2rad(0)
s_rz_cad = np.deg2rad(0)

    # Base
b_mass_cad = 38.4558
b_mass_real = b_mass_cad
b_cm_x_cad = -22.1188e-3
b_cm_y_cad = 3.8776e-3
b_cm_z_cad = 97.3027e-3
b_xx_cad = 453153.0558e-6
b_xy_cad = -6259.5067e-6
b_xz_cad = -21560.4658e-6
b_yy_cad = 598759.2442e-6
b_yz_cad = -4527.0636e-6
b_zz_cad = 838728.7083e-6
b_dx_cad = 0e-3
b_dy_cad = 0e-3
b_dz_cad = -243.00e-3
b_rx_cad = np.deg2rad(0)
b_ry_cad = np.deg2rad(0)
b_rz_cad = np.deg2rad(0)

    # Link 1
l1_mass_cad = 111.4512
l1_mass_real = l1_mass_cad
l1_cm_x_cad = 10.1989e-3
l1_cm_y_cad = 20.8502e-3
l1_cm_z_cad = -97.9719e-3
l1_xx_cad = 1996641.51e-6
l1_xy_cad = -163274.737e-6
l1_xz_cad = 96167.3114e-6
l1_yy_cad = 2021184.2e-6
l1_yz_cad = 249519.015e-6
l1_zz_cad = 1784754.62e-6
l1_dx_cad = 0.00e-3
l1_dy_cad = 0.00e-3
l1_dz_cad = 0.00e-3
l1_rx_cad = np.deg2rad(0)
l1_ry_cad = np.deg2rad(0)
l1_rz_cad = np.deg2rad(0)

    # Cover Joint 1
c1_mass_cad = 0.4958
c1_mass_real = c1_mass_cad
c1_cm_x_cad = 53.4939e-3
c1_cm_y_cad = 119.8277e-3
c1_cm_z_cad = 489.6408e-3
c1_xx_cad = 5763.057e-6
c1_xy_cad = -488.0196e-6
c1_xz_cad = -1826.8501e-6
c1_yy_cad = 8563.0712e-6
c1_yz_cad = -793.7218e-6
c1_zz_cad = 9726.5366e-6
c1_dx_cad = 0.0265e-3
c1_dy_cad = 0.3e-3
c1_dz_cad = 425.00e-3
c1_rx_cad = np.deg2rad(0)
c1_ry_cad = np.deg2rad(0)
c1_rz_cad = np.deg2rad(0)

    # Rear Cover Joint 1
rc1_mass_cad = 0.3844
rc1_mass_real = rc1_mass_cad
rc1_cm_x_cad = -80.5061e-3
rc1_cm_y_cad = 39.1483e-3
rc1_cm_z_cad = 480.8188e-3
rc1_xx_cad = 7036.5023e-6
rc1_xy_cad = 2264.8748e-6
rc1_xz_cad = -1118.1009e-6
rc1_yy_cad = 5525.327e-6
rc1_yz_cad = -1473.3148e-6
rc1_zz_cad = 8598.3654e-6
rc1_dx_cad = -0.0353e-3
rc1_dy_cad = 0.00e-3
rc1_dz_cad = 520.2942e-3
rc1_rx_cad = np.deg2rad(0)
rc1_ry_cad = np.deg2rad(0)
rc1_rz_cad = np.deg2rad(0)

    # Link 2
l2_mass_cad = 52.129
l2_mass_real = l2_mass_cad
l2_cm_x_cad = 10.2655e-3
l2_cm_y_cad = 325.2433e-3
l2_cm_z_cad = 350.6632e-3
l2_xx_cad = 4865699.995e-6
l2_xy_cad = 51187.5694e-6
l2_xz_cad = -128457.1259e-6
l2_yy_cad = 4978356.461e-6
l2_yz_cad = 78649.1115e-6
l2_zz_cad = 316331.8153e-6
l2_dx_cad = 55.1499e-3
l2_dy_cad = 504.49e-3
l2_dz_cad = 0.00e-3
l2_rx_cad = np.deg2rad(-90)
l2_ry_cad = np.deg2rad(0)
l2_rz_cad = np.deg2rad(0)

    # Link 3
l3_mass_cad = 35.0853
l3_mass_real = l3_mass_cad
l3_cm_x_cad = 144.5105e-3
l3_cm_y_cad = 439.5909e-3
l3_cm_z_cad = 116.614e-3
l3_xx_cad = 620491.024e-6
l3_xy_cad = 38191.3749e-6
l3_xz_cad = 254912.9436e-6
l3_yy_cad = 747780.2771e-6
l3_yz_cad = 4501.5848e-6
l3_zz_cad = 596090.7964e-6
l3_dx_cad = 0.00e-3
l3_dy_cad = 406.1534e-3
l3_dz_cad = 0.00e-3
l3_rx_cad = np.deg2rad(0)
l3_ry_cad = np.deg2rad(-90)
l3_rz_cad = np.deg2rad(90)

    # Cover Joint 3
c3_mass_cad = 0.2852
c3_mass_real = c3_mass_cad
c3_cm_x_cad = 12.9961e-3
c3_cm_y_cad = 496.9879e-3
c3_cm_z_cad = -0.5544e-3
c3_xx_cad = 1683.6229e-6
c3_xy_cad = 142.4192e-6
c3_xz_cad = -0.0312e-6
c3_yy_cad = 2210.1318e-6
c3_yz_cad = -39.0087e-6
c3_zz_cad = 2301.8635e-6
c3_dx_cad = 0.0016e-3
c3_dy_cad = 408.1534e-3
c3_dz_cad = 0.0248e-3
c3_rx_cad = np.deg2rad(0)
c3_ry_cad = np.deg2rad(-90)
c3_rz_cad = np.deg2rad(90)

    # Link 4
l4_mass_cad = 21.7498
l4_mass_real = l4_mass_cad
l4_cm_x_cad = 282.3453e-3
l4_cm_y_cad = -62.9394e-3
l4_cm_z_cad = -0.2993e-3
l4_xx_cad = 78138.8112e-6
l4_xy_cad = -76651.2033e-6
l4_xz_cad = 674.2049e-6
l4_yy_cad = 765641.749e-6
l4_yz_cad = -60.7571e-6
l4_zz_cad = 774914.081e-6
l4_dx_cad = -286.2e-3
l4_dy_cad = 0.1661e-3
l4_dz_cad = 0.00e-3
l4_rx_cad = np.deg2rad(0)
l4_ry_cad = np.deg2rad(-90)
l4_rz_cad = np.deg2rad(0)

    # Link 5
l5_mass_cad = 1.2716
l5_mass_real = l5_mass_cad
l5_cm_x_cad = 30.1773e-3
l5_cm_y_cad = -19.814e-3
l5_cm_z_cad = 0.0027e-3
l5_xx_cad = 3362.7807e-6
l5_xy_cad = 846.7754e-6
l5_xz_cad = -0.0007e-6
l5_yy_cad = 3805.3704e-6
l5_yz_cad = 0.0206e-6
l5_zz_cad = 3260.462e-6
l5_dx_cad = 0.00e-3
l5_dy_cad = 0.00e-3
l5_dz_cad = 0.00e-3
l5_rx_cad = np.deg2rad(90)
l5_ry_cad = np.deg2rad(-90)
l5_rz_cad = np.deg2rad(0)

    # Link 6
l6_mass_cad = 0.7536
l6_mass_real = l6_mass_cad
l6_cm_x_cad = 0.00e-3
l6_cm_y_cad = 0.00e-3
l6_cm_z_cad = -33.9197e-3
l6_xx_cad = 688.4945e-6
l6_xy_cad = 0.00e-6
l6_xz_cad = 0.00e-6
l6_yy_cad = 688.6907e-6
l6_yz_cad = 0.00e-6
l6_zz_cad = 1045.4319e-6
l6_dx_cad = 0.00e-3
l6_dy_cad = 0.00e-3
l6_dz_cad = -90.00e-3
l6_rx_cad = np.deg2rad(180)
l6_ry_cad = np.deg2rad(0)
l6_rz_cad = np.deg2rad(0)

# codice

def transform(mass_cad, mass_real, x, y, z, ixx, ixy, ixz, iyy, iyz, izz, dx, dy, dz, rx, ry, rz):
    
    I = np.array([[ixx, ixy, ixz], 
                  [ixy, iyy, iyz], 
                  [ixz, iyz, izz]])*mass_real/mass_cad
    
    Rx = np.array([[1, 0, 0], 
                  [0, np.cos(rx), -np.sin(rx)], 
                  [0, np.sin(rx), np.cos(rx)]])
    
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)],
                  [0, 1, 0], 
                  [-np.sin(ry), 0, np.cos(ry)]])
    
    Rz = np.array([[np.cos(rz), -np.sin(rz), 0],
                  [np.sin(rz), np.cos(rz), 0],
                  [0, 0, 1]])
    
    R = Rz @ Ry @ Rx

    Inew = R.T @ I @ R

    ixx_n = Inew[0, 0]
    ixy_n = Inew[0, 1]
    ixz_n = Inew[0, 2]
    iyy_n = Inew[1, 1]
    iyz_n = Inew[1, 2]
    izz_n = Inew[2, 2]

    rpy = [0.0, 0.0, 0.0]

    xyz = np.array([x, y, z])
    d = np.array([dx, dy, dz])

    xyz_n = R.T @ (xyz - d)

    return mass_real, xyz_n, rpy, ixx_n, ixy_n, ixz_n, iyy_n, iyz_n, izz_n

# calcoli
s_mass, s_xyz, s_rpy, s_xx, s_xy, s_xz, s_yy, s_yz, s_zz = transform(s_mass_cad, s_mass_real, s_cm_x_cad, s_cm_y_cad, s_cm_z_cad, 
                                                                              s_xx_cad, s_xy_cad, s_xz_cad,
                                                                              s_yy_cad, s_yz_cad, s_zz_cad,
                                                                              s_dx_cad, s_dy_cad, s_dz_cad, 
                                                                              s_rx_cad, s_ry_cad, s_rz_cad)

b_mass, b_xyz, b_rpy, b_xx, b_xy, b_xz, b_yy, b_yz, b_zz = transform(b_mass_cad, b_mass_real, b_cm_x_cad, b_cm_y_cad, b_cm_z_cad, 
                                                                              b_xx_cad, b_xy_cad, b_xz_cad,
                                                                              b_yy_cad, b_yz_cad, b_zz_cad,
                                                                              b_dx_cad, b_dy_cad, b_dz_cad, 
                                                                              b_rx_cad, b_ry_cad, b_rz_cad)

l1_mass, l1_xyz, l1_rpy, l1_xx, l1_xy, l1_xz, l1_yy, l1_yz, l1_zz = transform(l1_mass_cad, l1_mass_real, l1_cm_x_cad, l1_cm_y_cad, l1_cm_z_cad, 
                                                                              l1_xx_cad, l1_xy_cad, l1_xz_cad,
                                                                              l1_yy_cad, l1_yz_cad, l1_zz_cad,
                                                                              l1_dx_cad, l1_dy_cad, l1_dz_cad, 
                                                                              l1_rx_cad, l1_ry_cad, l1_rz_cad)

c1_mass, c1_xyz, c1_rpy, c1_xx, c1_xy, c1_xz, c1_yy, c1_yz, c1_zz = transform(c1_mass_cad, c1_mass_real, c1_cm_x_cad, c1_cm_y_cad, c1_cm_z_cad, 
                                                                              c1_xx_cad, c1_xy_cad, c1_xz_cad,
                                                                              c1_yy_cad, c1_yz_cad, c1_zz_cad,
                                                                              c1_dx_cad, c1_dy_cad, c1_dz_cad, 
                                                                              c1_rx_cad, c1_ry_cad, c1_rz_cad)

rc1_mass, rc1_xyz, rc1_rpy, rc1_xx, rc1_xy, rc1_xz, rc1_yy, rc1_yz, rc1_zz = transform(rc1_mass_cad, rc1_mass_real, rc1_cm_x_cad, rc1_cm_y_cad, rc1_cm_z_cad, 
                                                                              rc1_xx_cad, rc1_xy_cad, rc1_xz_cad,
                                                                              rc1_yy_cad, rc1_yz_cad, rc1_zz_cad,
                                                                              rc1_dx_cad, rc1_dy_cad, rc1_dz_cad, 
                                                                              rc1_rx_cad, rc1_ry_cad, rc1_rz_cad)

l2_mass, l2_xyz, l2_rpy, l2_xx, l2_xy, l2_xz, l2_yy, l2_yz, l2_zz = transform(l2_mass_cad, l2_mass_real, l2_cm_x_cad, l2_cm_y_cad, l2_cm_z_cad, 
                                                                              l2_xx_cad, l2_xy_cad, l2_xz_cad,
                                                                              l2_yy_cad, l2_yz_cad, l2_zz_cad,
                                                                              l2_dx_cad, l2_dy_cad, l2_dz_cad, 
                                                                              l2_rx_cad, l2_ry_cad, l2_rz_cad)

l3_mass, l3_xyz, l3_rpy, l3_xx, l3_xy, l3_xz, l3_yy, l3_yz, l3_zz = transform(l3_mass_cad, l3_mass_real, l3_cm_x_cad, l3_cm_y_cad, l3_cm_z_cad, 
                                                                              l3_xx_cad, l3_xy_cad, l3_xz_cad,
                                                                              l3_yy_cad, l3_yz_cad, l3_zz_cad,
                                                                              l3_dx_cad, l3_dy_cad, l3_dz_cad, 
                                                                              l3_rx_cad, l3_ry_cad, l3_rz_cad)

c3_mass, c3_xyz, c3_rpy, c3_xx, c3_xy, c3_xz, c3_yy, c3_yz, c3_zz = transform(c3_mass_cad, c3_mass_real, c3_cm_x_cad, c3_cm_y_cad, c3_cm_z_cad, 
                                                                              c3_xx_cad, c3_xy_cad, c3_xz_cad,
                                                                              c3_yy_cad, c3_yz_cad, c3_zz_cad,
                                                                              c3_dx_cad, c3_dy_cad, c3_dz_cad, 
                                                                              c3_rx_cad, c3_ry_cad, c3_rz_cad)

l4_mass, l4_xyz, l4_rpy, l4_xx, l4_xy, l4_xz, l4_yy, l4_yz, l4_zz = transform(l4_mass_cad, l4_mass_real, l4_cm_x_cad, l4_cm_y_cad, l4_cm_z_cad, 
                                                                              l4_xx_cad, l4_xy_cad, l4_xz_cad,
                                                                              l4_yy_cad, l4_yz_cad, l4_zz_cad,
                                                                              l4_dx_cad, l4_dy_cad, l4_dz_cad, 
                                                                              l4_rx_cad, l4_ry_cad, l4_rz_cad)

l5_mass, l5_xyz, l5_rpy, l5_xx, l5_xy, l5_xz, l5_yy, l5_yz, l5_zz = transform(l5_mass_cad, l5_mass_real, l5_cm_x_cad, l5_cm_y_cad, l5_cm_z_cad, 
                                                                              l5_xx_cad, l5_xy_cad, l5_xz_cad,
                                                                              l5_yy_cad, l5_yz_cad, l5_zz_cad,
                                                                              l5_dx_cad, l5_dy_cad, l5_dz_cad, 
                                                                              l5_rx_cad, l5_ry_cad, l5_rz_cad)

l6_mass, l6_xyz, l6_rpy, l6_xx, l6_xy, l6_xz, l6_yy, l6_yz, l6_zz = transform(l6_mass_cad, l6_mass_real, l6_cm_x_cad, l6_cm_y_cad, l6_cm_z_cad, 
                                                                              l6_xx_cad, l6_xy_cad, l6_xz_cad,
                                                                              l6_yy_cad, l6_yz_cad, l6_zz_cad,
                                                                              l6_dx_cad, l6_dy_cad, l6_dz_cad, 
                                                                              l6_rx_cad, l6_ry_cad, l6_rz_cad)

#  file xacro
with open("urdf/inertias_generated.xacro", "w") as f:
    
    f.write('<?xml version="1.0"?>\n')
    f.write('<robot xmlns:xacro="http://wiki.ros.org/xacro">\n\n')
    
    f.write(f'  <!-- Sensor -->\n')
    f.write(f'  <xacro:property name="s_mass" value="{s_mass}"/>\n')
    f.write(f'  <xacro:property name="s_xyz" value="{s_xyz[0]} {s_xyz[1]} {s_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="s_rpy" value="{s_rpy[0]} {s_rpy[1]} {s_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="s_ixx" value="{s_xx}"/>\n')
    f.write(f'  <xacro:property name="s_ixy" value="{s_xy}"/>\n')
    f.write(f'  <xacro:property name="s_ixz" value="{s_xz}"/>\n')
    f.write(f'  <xacro:property name="s_iyy" value="{s_yy}"/>\n')
    f.write(f'  <xacro:property name="s_iyz" value="{s_yz}"/>\n')
    f.write(f'  <xacro:property name="s_izz" value="{s_zz}"/>\n\n')

    f.write(f'  <!-- Base -->\n')
    f.write(f'  <xacro:property name="b_mass" value="{b_mass}"/>\n')
    f.write(f'  <xacro:property name="b_xyz" value="{b_xyz[0]} {b_xyz[1]} {b_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="b_rpy" value="{b_rpy[0]} {b_rpy[1]} {b_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="b_ixx" value="{b_xx}"/>\n')
    f.write(f'  <xacro:property name="b_ixy" value="{b_xy}"/>\n')
    f.write(f'  <xacro:property name="b_ixz" value="{b_xz}"/>\n')
    f.write(f'  <xacro:property name="b_iyy" value="{b_yy}"/>\n')
    f.write(f'  <xacro:property name="b_iyz" value="{b_yz}"/>\n')
    f.write(f'  <xacro:property name="b_izz" value="{b_zz}"/>\n\n')

    f.write(f'  <!-- Link 1 -->\n')
    f.write(f'  <xacro:property name="l1_mass" value="{l1_mass}"/>\n')
    f.write(f'  <xacro:property name="l1_xyz" value="{l1_xyz[0]} {l1_xyz[1]} {l1_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l1_rpy" value="{l1_rpy[0]} {l1_rpy[1]} {l1_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l1_ixx" value="{l1_xx}"/>\n')
    f.write(f'  <xacro:property name="l1_ixy" value="{l1_xy}"/>\n')
    f.write(f'  <xacro:property name="l1_ixz" value="{l1_xz}"/>\n')
    f.write(f'  <xacro:property name="l1_iyy" value="{l1_yy}"/>\n')
    f.write(f'  <xacro:property name="l1_iyz" value="{l1_yz}"/>\n')
    f.write(f'  <xacro:property name="l1_izz" value="{l1_zz}"/>\n\n')

    f.write(f'  <!-- Cover 1 -->\n')
    f.write(f'  <xacro:property name="c1_mass" value="{c1_mass}"/>\n')
    f.write(f'  <xacro:property name="c1_xyz" value="{c1_xyz[0]} {c1_xyz[1]} {c1_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="c1_rpy" value="{c1_rpy[0]} {c1_rpy[1]} {c1_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="c1_ixx" value="{c1_xx}"/>\n')
    f.write(f'  <xacro:property name="c1_ixy" value="{c1_xy}"/>\n')
    f.write(f'  <xacro:property name="c1_ixz" value="{c1_xz}"/>\n')
    f.write(f'  <xacro:property name="c1_iyy" value="{c1_yy}"/>\n')
    f.write(f'  <xacro:property name="c1_iyz" value="{c1_yz}"/>\n')
    f.write(f'  <xacro:property name="c1_izz" value="{c1_zz}"/>\n\n')

    f.write(f'  <!-- Rear Cover 1 -->\n')
    f.write(f'  <xacro:property name="rc1_mass" value="{rc1_mass}"/>\n')
    f.write(f'  <xacro:property name="rc1_xyz" value="{rc1_xyz[0]} {rc1_xyz[1]} {rc1_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="rc1_rpy" value="{rc1_rpy[0]} {rc1_rpy[1]} {rc1_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="rc1_ixx" value="{rc1_xx}"/>\n')
    f.write(f'  <xacro:property name="rc1_ixy" value="{rc1_xy}"/>\n')
    f.write(f'  <xacro:property name="rc1_ixz" value="{rc1_xz}"/>\n')
    f.write(f'  <xacro:property name="rc1_iyy" value="{rc1_yy}"/>\n')
    f.write(f'  <xacro:property name="rc1_iyz" value="{rc1_yz}"/>\n')
    f.write(f'  <xacro:property name="rc1_izz" value="{rc1_zz}"/>\n\n')

    f.write(f'  <!-- Link 2 -->\n')
    f.write(f'  <xacro:property name="l2_mass" value="{l2_mass}"/>\n')
    f.write(f'  <xacro:property name="l2_xyz" value="{l2_xyz[0]} {l2_xyz[1]} {l2_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l2_rpy" value="{l2_rpy[0]} {l2_rpy[1]} {l2_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l2_ixx" value="{l2_xx}"/>\n')
    f.write(f'  <xacro:property name="l2_ixy" value="{l2_xy}"/>\n')
    f.write(f'  <xacro:property name="l2_ixz" value="{l2_xz}"/>\n')
    f.write(f'  <xacro:property name="l2_iyy" value="{l2_yy}"/>\n')
    f.write(f'  <xacro:property name="l2_iyz" value="{l2_yz}"/>\n')
    f.write(f'  <xacro:property name="l2_izz" value="{l2_zz}"/>\n\n')

    f.write(f'  <!-- Link 3 -->\n')
    f.write(f'  <xacro:property name="l3_mass" value="{l3_mass}"/>\n')
    f.write(f'  <xacro:property name="l3_xyz" value="{l3_xyz[0]} {l3_xyz[1]} {l3_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l3_rpy" value="{l3_rpy[0]} {l3_rpy[1]} {l3_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l3_ixx" value="{l3_xx}"/>\n')
    f.write(f'  <xacro:property name="l3_ixy" value="{l3_xy}"/>\n')
    f.write(f'  <xacro:property name="l3_ixz" value="{l3_xz}"/>\n')
    f.write(f'  <xacro:property name="l3_iyy" value="{l3_yy}"/>\n')
    f.write(f'  <xacro:property name="l3_iyz" value="{l3_yz}"/>\n')
    f.write(f'  <xacro:property name="l3_izz" value="{l3_zz}"/>\n\n')

    f.write(f'  <!-- Cover 3 -->\n')
    f.write(f'  <xacro:property name="c3_mass" value="{c3_mass}"/>\n')
    f.write(f'  <xacro:property name="c3_xyz" value="{c3_xyz[0]} {c3_xyz[1]} {c3_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="c3_rpy" value="{c3_rpy[0]} {c3_rpy[1]} {c3_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="c3_ixx" value="{c3_xx}"/>\n')
    f.write(f'  <xacro:property name="c3_ixy" value="{c3_xy}"/>\n')
    f.write(f'  <xacro:property name="c3_ixz" value="{c3_xz}"/>\n')
    f.write(f'  <xacro:property name="c3_iyy" value="{c3_yy}"/>\n')
    f.write(f'  <xacro:property name="c3_iyz" value="{c3_yz}"/>\n')
    f.write(f'  <xacro:property name="c3_izz" value="{c3_zz}"/>\n\n')

    f.write(f'  <!-- Link 4 -->\n')
    f.write(f'  <xacro:property name="l4_mass" value="{l4_mass}"/>\n')
    f.write(f'  <xacro:property name="l4_xyz" value="{l4_xyz[0]} {l4_xyz[1]} {l4_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l4_rpy" value="{l4_rpy[0]} {l4_rpy[1]} {l4_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l4_ixx" value="{l4_xx}"/>\n')
    f.write(f'  <xacro:property name="l4_ixy" value="{l4_xy}"/>\n')
    f.write(f'  <xacro:property name="l4_ixz" value="{l4_xz}"/>\n')
    f.write(f'  <xacro:property name="l4_iyy" value="{l4_yy}"/>\n')
    f.write(f'  <xacro:property name="l4_iyz" value="{l4_yz}"/>\n')
    f.write(f'  <xacro:property name="l4_izz" value="{l4_zz}"/>\n\n')

    f.write(f'  <!-- Link 5 -->\n')
    f.write(f'  <xacro:property name="l5_mass" value="{l5_mass}"/>\n')
    f.write(f'  <xacro:property name="l5_xyz" value="{l5_xyz[0]} {l5_xyz[1]} {l5_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l5_rpy" value="{l5_rpy[0]} {l5_rpy[1]} {l5_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l5_ixx" value="{l5_xx}"/>\n')
    f.write(f'  <xacro:property name="l5_ixy" value="{l5_xy}"/>\n')
    f.write(f'  <xacro:property name="l5_ixz" value="{l5_xz}"/>\n')
    f.write(f'  <xacro:property name="l5_iyy" value="{l5_yy}"/>\n')
    f.write(f'  <xacro:property name="l5_iyz" value="{l5_yz}"/>\n')
    f.write(f'  <xacro:property name="l5_izz" value="{l5_zz}"/>\n\n')

    f.write(f'  <!-- Link 6 -->\n')
    f.write(f'  <xacro:property name="l6_mass" value="{l6_mass}"/>\n')
    f.write(f'  <xacro:property name="l6_xyz" value="{l6_xyz[0]} {l6_xyz[1]} {l6_xyz[2]}"/>\n')
    f.write(f'  <xacro:property name="l6_rpy" value="{l6_rpy[0]} {l6_rpy[1]} {l6_rpy[2]}"/>\n')
    f.write(f'  <xacro:property name="l6_ixx" value="{l6_xx}"/>\n')
    f.write(f'  <xacro:property name="l6_ixy" value="{l6_xy}"/>\n')
    f.write(f'  <xacro:property name="l6_ixz" value="{l6_xz}"/>\n')
    f.write(f'  <xacro:property name="l6_iyy" value="{l6_yy}"/>\n')
    f.write(f'  <xacro:property name="l6_iyz" value="{l6_yz}"/>\n')
    f.write(f'  <xacro:property name="l6_izz" value="{l6_zz}"/>\n\n')
    
    f.write('</robot>\n')