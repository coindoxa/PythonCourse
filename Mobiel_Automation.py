from uiautomator import device as d
import time

#d.(text='Camera').clickF()
d.screen.on()

d.press.home()
d(text='Camera').click()