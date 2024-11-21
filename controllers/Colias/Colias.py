from controller import Robot


class Colias(Robot):
    def __init__(self):
        super().__init__()
        self.time_step = int(self.getBasicTimeStep())
        print(self.time_step)
        self.sensors = {}
        self.camera = self.getDevice('camera')
        print(self.camera)
        self.camera.enable(self.time_step)
        self.motor_left = self.getDevice('MotorLeft')
        self.motor_right = self.getDevice('MotorRight')

    def move(self):
        self.motor_left.setPosition(float('inf'))
        self.motor_right.setPosition(float('inf'))
        self.motor_left.setVelocity(2)
        self.motor_right.setVelocity(2)
        while self.step(self.time_step) != -1:
            pass
    
    
robot = Colias()
robot.move()