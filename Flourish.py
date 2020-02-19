import subprocess

import time
from uiautomator import device as d



def swipe_up():
   cmd = (['adb', 'shell', 'input', 'swipe', '540', '679', '0', '0'])
   x = subprocess.call(cmd)

def setup():
   ###subprocess.run('adb shell am force-stop com.google.android.apps.cerebra.dunlin', shell=True)
   ### d.screen.on()
   ###d.press.home()
   ##clear cache
   subprocess.call('adb shell pm clear com.google.android.apps.cerebra.dunlin', shell=True)
   time.sleep(3)
   # Launch app with activity doesnt work for now
   ##subprocess.call('adb shell am start -n com.google.android.apps.cerebra.dunlin/com.google.android.apps.cerebra.dunlin.contribute.ContributeFlowActivity', shell=True)
   d(text='Flourish').click()
   d(text='Continue').click()
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/account_toggle').click()
   d(text='Continue').click()
   for i in range(4):
       d(scrollable=True).fling()
   """ LINKS NOT AVAILABLE YET 
   d(scrollable=True).scroll.to(text='go/employee-privacy-policy')
   d(text='go/employee-privacy-policy').click()
   """
  ###swipe_up()
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/flu_pilot_contribute_consent_alabama_resident_radio_button').click()
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/text_input_end_icon').click()
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/query_data_item').click()
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/contribute_button_consent').click()
   d(text='Continue').click()
   d(text='Allow all the time').click()
   ### d(text='Finish').click()

def self_reporting_menu():
    ##Click Today Tab
    print('SET UP TEST')
    d(text='Today').click()
    time.sleep(2)
    if d(text='Got your flu shot?').exists:
       print('Today Tab PASS')
    else:
       print("Today Tab FAIL")
    ##Click Map tab
    time.sleep(2)
    d(text='Map').click()
    if d(text='Flu activity is minimal in Washington this week.').exists:
       print('Map tab PASS')
    else:
       print("Map Tab FAIL")
    ##Click About tab
    time.sleep(2)
    d(text='About').click()
    if d(text='Status reports').exists:
       print('About tab PASS')
    else:
       print("About Tab FAIL")
    print('Self reporting Menu Test PASS')

def today_tab():
   print('TODAY TAB TEST')
   d(text='Today').click()
   time.sleep(2)
   if d(text='Flu activity is minimal in Washington.').exists:
       print('Flu activity text PASS')
   else:
       print('Flu activity text FAIL')
   d(text='Got your flu shot?').click()
   time.sleep(2)
   if d(text='Did you get the flu shot this season?').exists:
       print('Get your flu shot button PASS')
   else:
       print('Get your flu shot button FAIL')
   d.press.back()
   d(text='How are you feeling?').click()
   time.sleep(2)
   if d(text='How are you feeling today?').exists:
       print('How are you feeling button PASS')
   else:
       print('How are you feeling button FAIL')
   d.press.back()

def map_tab():
   print('MAP TAB TEST')
   ###Use search feature
   d(text='Map').click()
   d(text='Search').click()
   d(text='Search').set_text('Florida')
   time.sleep(3)
   if d(text='Florida City').exists:
       d(text='Florida City').click()
   time.sleep(3)
   if d(text='Flu activity is minimal in Florida this week.').exists:
       print('Use search feature PASS')
   else:
       print('Use search feature FAIL')
    ###Expand the key menu
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/map_legend_close').click()
   if d(text='View Key').exists:
       print('Expand the key menu PASS')
   else:
       print('Expand the key menu FAIL')
    ###Current-Location button
   d(resourceId='com.google.android.apps.cerebra.dunlin:id/my_location').click()
   if d(text='Flu activity is minimal in Washington this week.').exists:
       print('Current-Location button PASS')
   ##Map can be panned/zoomed
   for i in range(2):
       d(resourceId='com.google.android.apps.cerebra.dunlin:id/experimentdetails_viewpager').pinch.Out()
       time.sleep(2)
       d(resourceId='com.google.android.apps.cerebra.dunlin:id/experimentdetails_viewpager').pinch.In(percent=100, steps=10)
   d.swipe(500, 800, 0, 0)
   # d.swipe(52, 1368, 0, 0)
   d.swipe(500, 1192, 0, 0)
   d.swipe(54, 1185, 0, 0)

## Text status shown when selecting different state. Testing Alaska and Massachusetts
def city_search(city, place, verify):
   d(text='Search').click()
   d(text='Search').set_text(city)
   time.sleep(3)
   if d(text=place).exists:
       d(text=place).click()
   time.sleep(3)
   if d(text='Flu activity is minimal in ' +verify+ ' this week.').exists:
       print(verify+' Use search feature PASS')
   else:
       print(verify+' Use search feature FAIL')
   d.press.home()
   d(text='Flourish').click()
   d(text='Map').click()

def text_size():
    subprocess.call('adb shell am start -n com.android.settings/com.android.settings.SubSettings', shell=True)
    d(scrollable=True).fling()
    d(text='Accessibility').click()
    d(text='Font size').click()
    for i in range(2):
        d(resourceId='com.android.settings:id/larger').click()
    d.press.home()
    d(text='Flourish').click()
    d(text='Map').click()
    if d(text='Flu activity is minimal in Washington this week.').exists:
       print('Map tab PASS')
    else:
       print("Map Tab FAIL")
    subprocess.call('adb shell am start -n com.android.settings/com.android.settings.SubSettings', shell=True)
    d(scrollable=True).fling()
    d(text='Accessibility').click()
    d(text='Font size').click()
    for i in range(3):
        d(resourceId='com.android.settings:id/smaller').click()
    d.press.home()
    d(text='Flourish').click()
    d(text='Map').click()
    if d(text='Flu activity is minimal in Washington this week.').exists:
       print('Map tab PASS')
    else:
       print("Map Tab FAIL")

def no_outside_us(29):
    d.press.home()
    d(text='Flourish').click()
    d(text='Map').click()
### Search doesn't support outside US 29

def main():
   # setup()
   # self_reporting_menu()
   # today_tab()
   # map_tab()
   # city_search('Anchorage food', 'Food Court', 'Alaska')
   #city_search('Boston', 'MA, USA', 'Massachusetts')
   text_size()


if __name__ == '__main__':
   main()

