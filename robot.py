
import wpilib
import wpilib.drive
from navx import AHRS


import wpimath

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        pass


    def teleopInit(self):
        pass 


    def teleopPeriodic(self):
        #pega a rotação do robô pela valores da navX
        yaw = self.navx.getAngle()

        pitch = self.navx.getPitch()
        #conjumina os valores da navx e dos encoders (não adicionados) dentro do P
        r = wpimath.geometry.Rotation2d(yaw, pitch)
        p = wpimath.geometry._geometry.Pose2d(2.0, 2.0, r)
        #mostra o valor do p
        print(p)




if __name__ == "__main__":
    wpilib.run(MyRobot)
