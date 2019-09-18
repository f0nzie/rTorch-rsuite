
import os

if (os.getenv('KERAS_IMPLEMENTATION', 'tensorflow') == 'keras'):
  from keras.constraints import Constraint
else:
  from tensorflow.python.keras.constraints import Constraint

class RConstraint(Constraint):

  def __init__(self, r_call, r_get_config):
    self.r_call = r_call
    self.r_get_config = r_get_config
    
  def __call__(self, w):
    return self.r_call(w)

  def get_config(self):
    return self.r_get_config()
      


