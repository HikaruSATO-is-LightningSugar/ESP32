import pigpio
from pca9685 import pca9685
import time

PCA9685_ADDR = 0x40
pwm_freq = 50

grip_ch = 0
joint1_ch = 1
joint2_ch = 2
joint3_ch = 3
stand_ch = 4

GRIP_O_PIN = 26
GRIP_C_PIN = 19
JOINT1_U_PIN = 18
JOINT1_D_PIN = 25
JOINT2_U_PIN = 23
JOINT2_D_PIN = 24
JOINT3_U_PIN = 16
JOINT3_D_PIN = 20
STAND_R_PIN = 21
STAND_L_PIN = 12

grip_deg = 0
joint1_deg = 0
joint2_deg = 0
joint3_deg = -60
stand_deg = 0

grip_max_deg = 60
grip_min_deg = -60
joint1_max_deg = 60
joint1_min_deg = -60
joint2_max_deg = 60
joint2_min_deg = -60
joint3_max_deg = 60
joint3_min_deg = -60
stand_max_deg = 60
stand_min_deg = -60

pi = pigpio.pi()

pi.set_mode( GRIP_O_PIN, pigpio.INPUT )
pi.set_mode( GRIP_C_PIN, pigpio.INPUT )
pi.set_mode( JOINT1_U_PIN, pigpio.INPUT )
pi.set_mode( JOINT1_D_PIN, pigpio.INPUT )
pi.set_mode( JOINT2_U_PIN, pigpio.INPUT )
pi.set_mode( JOINT2_D_PIN, pigpio.INPUT )
pi.set_mode( JOINT3_U_PIN, pigpio.INPUT )
pi.set_mode( JOINT3_D_PIN, pigpio.INPUT )
pi.set_mode( STAND_R_PIN, pigpio.INPUT )
pi.set_mode( STAND_L_PIN, pigpio.INPUT )
pi.set_pull_up_down( GRIP_O_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( GRIP_C_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT1_U_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT1_D_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT2_U_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT2_D_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT3_U_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( JOINT3_D_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( STAND_R_PIN, pigpio.PUD_OFF )
pi.set_pull_up_down( STAND_L_PIN, pigpio.PUD_OFF )

servo_drv = pca9685( pi, PCA9685_ADDR )
servo_drv.set_freq( pwm_freq )

p_width = servo_drv.deg_to_pulse ( grip_deg )
servo_drv.set_pulse_t( grip_ch, p_width )
p_width = servo_drv.deg_to_pulse ( joint1_deg )
servo_drv.set_pulse_t( joint1_ch, p_width )
p_width = servo_drv.deg_to_pulse ( joint2_deg )
servo_drv.set_pulse_t( joint2_ch, p_width )
p_width = servo_drv.deg_to_pulse ( joint3_deg )
servo_drv.set_pulse_t( joint3_ch, p_width )
p_width = servo_drv.deg_to_pulse ( stand_deg )
servo_drv.set_pulse_t( stand_ch, p_width )

while True:
    if ( pi.read( GRIP_O_PIN ) == pigpio.LOW ):
        grip_deg = grip_deg - 2
        if ( grip_deg < grip_min_deg ):
            grip_deg = grip_min_deg
        p_width = servo_drv.deg_to_pulse ( grip_deg )
        servo_drv.set_pulse_t( grip_ch, p_width )
        print( grip_deg )

    if ( pi.read( GRIP_C_PIN ) == pigpio.LOW ):
        grip_deg = grip_deg + 2
        if ( grip_deg > grip_max_deg ):
            grip_deg = grip_max_deg
        p_width = servo_drv.deg_to_pulse ( grip_deg )
        servo_drv.set_pulse_t( grip_ch, p_width )

    if ( pi.read( JOINT1_D_PIN ) == pigpio.LOW ):
        joint1_deg = joint1_deg - 2
        if ( joint1_deg < joint1_min_deg ):
            joint1_deg = joint1_min_deg
        p_width = servo_drv.deg_to_pulse ( joint1_deg )
        servo_drv.set_pulse_t( joint1_ch, p_width )

    if ( pi.read( JOINT1_U_PIN ) == pigpio.LOW ):
        joint1_deg = joint1_deg + 2
        if ( joint1_deg > joint1_max_deg ):
            joint1_deg = joint1_max_deg
        p_width = servo_drv.deg_to_pulse ( joint1_deg )
        servo_drv.set_pulse_t( joint1_ch, p_width )

    if ( pi.read( JOINT2_U_PIN ) == pigpio.LOW ):
        joint2_deg = joint2_deg - 2
        if ( joint2_deg < joint2_min_deg ):
            joint2_deg = joint2_min_deg
        p_width = servo_drv.deg_to_pulse ( joint2_deg )
        servo_drv.set_pulse_t( joint2_ch, p_width )

    if ( pi.read( JOINT2_D_PIN ) == pigpio.LOW ):
        joint2_deg = joint2_deg + 2
        if ( joint2_deg > joint2_max_deg ):
            joint2_deg = joint2_max_deg
        p_width = servo_drv.deg_to_pulse ( joint2_deg )
        servo_drv.set_pulse_t( joint2_ch, p_width )

    if ( pi.read( JOINT3_D_PIN ) == pigpio.LOW ):
        joint3_deg = joint3_deg - 2
        if ( joint3_deg < joint3_min_deg ):
            joint3_deg = joint3_min_deg
        p_width = servo_drv.deg_to_pulse ( joint3_deg )
        servo_drv.set_pulse_t( joint3_ch, p_width )

    if ( pi.read( JOINT3_U_PIN ) == pigpio.LOW ):
        joint3_deg = joint3_deg + 2
        if ( joint3_deg > joint3_max_deg ):
            joint3_deg = joint3_max_deg
        p_width = servo_drv.deg_to_pulse ( joint3_deg )
        servo_drv.set_pulse_t( joint3_ch, p_width )

    if ( pi.read( STAND_L_PIN ) == pigpio.LOW ):
        stand_deg = stand_deg - 2
        if ( stand_deg < stand_min_deg ):
            stand_deg = stand_min_deg
        p_width = servo_drv.deg_to_pulse ( stand_deg )
        servo_drv.set_pulse_t( stand_ch, p_width )

    if ( pi.read( STAND_R_PIN ) == pigpio.LOW ):
        stand_deg = stand_deg + 2
        if ( stand_deg > stand_max_deg ):
            stand_deg = stand_max_deg
        p_width = servo_drv.deg_to_pulse ( stand_deg )
        servo_drv.set_pulse_t( stand_ch, p_width )

    time.sleep( 0.1 )



