import RPi.GPIO as GPIO
from time import sleep

servoPin = 12 
SERVO_MAX_DUTY = 12 # 최대 주기 (180도)
SERVO_MIN_DUTY = 3 # 최소 주기 (0도)

GPIO.setmode(GPIO.BOARD) # GPIO 설정
GPIO.setup(servoPin, GPIO.OUT) # 서보핀 출력 설정

servo = GPIO.PWM(servoPin, 50) # 서보핀을 PWM 모드 50Hz로 사용
servo.start(0)

def setServoPos(degree):
    # 180도가 최대 각도임
    if degree > 180:
        degree = 180

    # 각도(degree)를 duty로 변경
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    
    #각도와 duty 값 출력 (디버깅 용도)
    print("각도 (degree) : {} to {}(duty)".format(degree, duty))

    servo.ChangeDutyCycle(duty)


setServoPos(45) # 45도 모터 회전


servo.stop() # 서보 모터 정지
GPIO.cleanup() # GPIO 초기화하여 다음 모터 작동을 준비함
    
