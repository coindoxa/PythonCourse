import subprocess
from time import sleep
from uiautomator import device as d


def swipe_up():
   cmd = (['adb', 'shell', 'input', 'swipe', '540', '679', '0', '0'])
   x = subprocess.call(cmd)


def unlock():
    d.screen.on()
    d.press.home()
    swipe_up()
    for i in range(5):
        d(text='0').click()



def main():
    unlock()
   # setup()
   # self_reporting_menu()
   # today_tab()
   # map_tab()
   # city_search('Anchorage food', 'Food Court', 'Alaska')
   #city_search('Boston', 'MA, USA', 'Massachusetts')
   #text_size()


if __name__ == '__main__':
   main()
