import RPi.GPIO as GPIO
import time

# 핀 설정
in1 = 17
in2 = 27
ena = 22

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

# PWM 설정
pwm = GPIO.PWM(ena, 1000)  # PWM 주파수 설정
pwm.start(25)  # 초기 듀티 사이클 설정 (25%)

def motor_forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

def motor_backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

def motor_stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

try:
    while True:
        print("Motor Forward")
        motor_forward()
        time.sleep(5)
        
        print("Motor Stop")
        motor_stop()
        time.sleep(2)
        
        print("Motor Backward")
        motor_backward()
        time.sleep(5)
        
        print("Motor Stop")
        motor_stop()
        time.sleep(2)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()


servo.stop() # 서보 모터 정지
GPIO.cleanup() # GPIO 초기화하여 다음 모터 작동을 준비함
    
