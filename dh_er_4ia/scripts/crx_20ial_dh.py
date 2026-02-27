import numpy as np

n = 6
d = np.array([0, 0, 0, -540, 150, -160])
a = np.array([0, 710, 0, 0, 0, 0])
alpha = np.array([np.deg2rad(90), 0, np.deg2rad(-90),
                  np.deg2rad(90), np.deg2rad(-90), np.deg2rad(180)])
theta = np.array([0, np.deg2rad(90), 0, 0, 0, 0])
m = np.array([10.799, 11.773, 4.703, 4.409, 2.577, 1.362])
com_x = np.array([-0.58, -379.49, 0.060, -0.030, 1.280, 0.110])
com_y = np.array([-37.02, 0.05, -9.68, 183.3, 32.61, -0.042])
com_z =np.array([45.65, 185.22, -41.26, 1.39, -22.52, -45.44])
ix = np.array([106721.703, 62306.961, 20659.381, 95116.398, 7818.762, 1450.347])
iy = np.array([75747.82, 1257636.0, 22006.051, 5355.183, 4530.349, 1398.7260])
iz = np.array([65877.281, 1228300.00, 9088.77, 94348.117, 6158.803, 1476.059])
lower_limit = np.array([-180, -180, -270, -190, -180, -225])
upper_limit = np.array([180, 180, 270, 190, 180, 225]) #°
vel_lim = np.array([80, 80, 120, 112.5, 90, 112.5]) #°/s


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
with open("urdf/dh_crx_20ial.xacro", "w") as f:
    
    f.write('<?xml version="1.0"?>\n')
    f.write('<robot xmlns:xacro="http://wiki.ros.org/xacro">\n\n')
    
    for i in range(n):
        
        j = i + 1

        f.write(f'  <!-- J{j} -->\n')
        f.write(f'  <xacro:property name="J{j}_xyz" '
                f'value="{pose[i,0]} {pose[i,1]} {pose[i,2]}"/>\n')
        f.write(f'  <xacro:property name="J{j}_rpy" '
                f'value="{pose[i,3]} {pose[i,4]} {pose[i,5]}"/>\n')
        f.write(f'  <xacro:property name="J{j}_ll" value="{np.deg2rad(lower_limit[i])}"/>\n')
        f.write(f'  <xacro:property name="J{j}_ul" value="{np.deg2rad(upper_limit[i])}"/>\n')
        f.write(f'  <xacro:property name="J{j}_vl" value="{np.deg2rad(vel_lim[i])}"/>\n')
        f.write(f'  <xacro:property name="J{j}_e" value="{100}"/>\n\n')
        
        f.write(f'  <!-- L{j} -->\n')
        
        f.write(f'  <xacro:property name="L{j}_mass" value="{m[i]}"/>\n')
        f.write(f'  <xacro:property name="L{j}_x_com" value="{com_x[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_y_com" value="{com_y[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_z_com" value="{com_z[i]*0.001}"/>\n')
        f.write(f'  <xacro:property name="L{j}_xx" value="{ix[i]*1e-6}"/>\n')
        f.write(f'  <xacro:property name="L{j}_yy" value="{iy[i]*1e-6}"/>\n')
        f.write(f'  <xacro:property name="L{j}_zz" value="{iz[i]*1e-6}"/>\n\n')

    f.write('</robot>\n')