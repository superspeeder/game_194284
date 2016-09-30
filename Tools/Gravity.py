from BaseForces import SimpleDirectionalForce
from ForceDecorators import *
from ForceConstant import G_FORCE_UNIT_RATE, DIRECTION_DOWN
from ForceFunctions import increase


class GravityForce(SimpleDirectionalForce):
  def __init__(self, sgs):
    super(GravityForce, self).__init__(self, DIRECTION_DOWN)
    self.gs = sgs
    self.incg = G_FORCE_UNIT_RATE
  
  @CollisionDetect.down
  def isOnGround(self):
    x = bool()
    return x
