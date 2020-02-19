import subprocess

import time
from uiautomator import device as d



def swipe_up():
   cmd = (['adb', 'shell', 'input', 'swipe', '540', '679', '0', '0'])
   x = subprocess.call(cmd)
#swipe_up()

#d.swipe.right()
#d.swipe.up(steps=10)


text ="With your consent, we may collect and process personally identifiable information in accordance with this agreement and Google Employee Privacy Policy available at . For example, we may ask for your name, email address, and other information that may identify you."
if d(text='Personally identifiable information').exists:
    print ('Good')
else:
    print ('Bad')