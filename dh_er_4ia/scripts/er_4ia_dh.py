import numpy as np

n = 6
d = np.array([0, 0, 0, -290, 0, -70])
a = np.array([0, 260, 20, 0, 0, 0])
alpha = np.array([np.deg2rad(90), 0, np.deg2rad(-90),
                  np.deg2rad(90), np.deg2rad(90), np.deg2rad(180)])
theta = np.array([0, np.deg2rad(90), 0, 0, 0, 0])
m = np.array([2.305, 5.338, 2.391, 3.575, 1.380, 0])
com_x = np.array([6.049, -189.204, -5.543, -0.209, 0.096, 0])
com_y = np.array([-72.681, 12.598, 16.001, 148.510, 2.212, 0])
com_z =np.array([6.749, -17.164, -28.758, -2.019, -23.858, 0])
ix = np.array([16393.500, 17180.500, 5024.855, 21552.150, 1711.018, 0])
iy = np.array([11838.810, 51234.801, 4562.809, 4253.950, 1649.590, 0])
iz = np.array([10608.650, 43298.789, 5240.497, 21529.539, 939.970, 0])
lower_limit = np.array([-170, -110, -122.29, -190, -120, -360 ])
upper_limit = np.array([170, 120, 280, 190, 120, 360]) #°
vel_lim = np.array([460, 360, 520, 560, 560, 900]) #°/s


T = []

def dh_matrix(a, alpha, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0,              np.sin(alpha),               np.cos(alpha),               d],
        [0,              0,                           0,                           1]
    ])

def rot_to_rpy(R):

    pitch = np.arctan2(-R[2,0], np.sqrt(R[0,0]**2 + R[1,0]**2))
    
    if np.cos(pitch) != 0:
        roll  = np.arctan2(R[2,1], R[2,2])
        yaw   = np.arctan2(R[1,0], R[0,0])
    else:
        
        roll  = 0
        yaw   = np.arctan2(-R[0,1], R[1,1])

    return roll, pitch, yaw

pose = []

for i in range(n):
    Ti = dh_matrix(a[i], alpha[i], d[i], theta[i])
    
    # posizione relativa
    x, y, z = Ti[0:3, 3]
    
    # rotazione relativa
    R = Ti[0:3, 0:3]
    roll, pitch, yaw = rot_to_rpy(R)
    
    pose.append([
        x*0.001,
        y*0.001,
        z*0.001,
        roll,
        pitch,
        yaw
    ])

pose = np.array(pose)

print(pose)
with open("urdf/dh_er_4ia.xacro", "w") as f:
    
    f.write('<?xml version="1.0"?>\n')
    f.write('<robot xmlns:xacro="http://wiki.ros.org/xacro">\n\n')
    f.write(f'  <!-- J1 -->\n')
    f.write(f'  <xacro:property name="J1_xyz" '
                f'value="0.0 0.0 0.0"/>\n')
        
    f.write(f'  <xacro:property name="J1_rpy" '
                f'value="0.0 0.0 0.0"/>\n')
    f.write(f'  <xacro:property name="J1_ll" value="{np.deg2rad(lower_limit[i])}"/>\n')
    f.write(f'  <xacro:property name="J1_ul" value="{np.deg2rad(upper_limit[i])}"/>\n')
    f.write(f'  <xacro:property name="J1_vl" value="{np.deg2rad(vel_lim[i])}"/>\n')
    f.write(f'  <xacro:property name="J1_e" value="{100}"/>\n\n')
    
    
    for i in range(n):
        
        j = i + 1
        jj = j+1

        # f.write(f'  <!-- J{j} -->\n')
        # f.write(f'  <xacro:property name="J{j}_xyz" '
        #         f'value="{pose[i,0]} {pose[i,1]} {pose[i,2]}"/>\n')
        # f.write(f'  <xacro:property name="J{j}_rpy" '
        #         f'value="{pose[i,3]} {pose[i,4]} {pose[i,5]}"/>\n')
        # f.write(f'  <xacro:property name="J{j}_ll" value="{np.deg2rad(lower_limit[i])}"/>\n')
        # f.write(f'  <xacro:property name="J{j}_ul" value="{np.deg2rad(upper_limit[i])}"/>\n')
        # f.write(f'  <xacro:property name="J{j}_vl" value="{np.deg2rad(vel_lim[i])}"/>\n')
        # f.write(f'  <xacro:property name="J{j}_e" value="{100}"/>\n\n')
        
        f.write(f'  <!-- L{j} -->\n')
        
        f.write(f'  <xacro:property name="L{j}_mass" value="{m[i]}"/>\n')
        f.write(f'  <xacro:property name="L{j}_x_com" value="{com_x[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_y_com" value="{com_y[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_z_com" value="{com_z[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_xx" value="{ix[i]*1e-6}"/>\n')
        f.write(f'  <xacro:property name="L{j}_yy" value="{iy[i]*1e-6}"/>\n')
        f.write(f'  <xacro:property name="L{j}_zz" value="{iz[i]*1e-6}"/>\n\n')

        f.write(f'  <!-- J{jj} -->\n')
        f.write(f'  <xacro:property name="J{jj}_xyz" '
                f'value="{pose[i,0]} {pose[i,1]} {pose[i,2]}"/>\n')
        f.write(f'  <xacro:property name="J{jj}_rpy" '
                f'value="{pose[i,3]} {pose[i,4]} {pose[i,5]}"/>\n')
        f.write(f'  <xacro:property name="J{jj}_ll" value="{np.deg2rad(lower_limit[i])}"/>\n')
        f.write(f'  <xacro:property name="J{jj}_ul" value="{np.deg2rad(upper_limit[i])}"/>\n')
        f.write(f'  <xacro:property name="J{jj}_vl" value="{np.deg2rad(vel_lim[i])}"/>\n')
        f.write(f'  <xacro:property name="J{jj}_e" value="{100}"/>\n\n')

    f.write('</robot>\n')