import tensorflow as tf
from tensorflow.python.client import device_lib

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Physical Devices: ", tf.config.experimental.list_physical_devices())
print(device_lib.list_local_devices())