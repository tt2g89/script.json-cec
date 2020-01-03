import xbmc
import urlparse
import sys
import time

try:
        params = urlparse.parse_qs('&'.join(sys.argv[1:]))
        command = params.get('command',None)
except:
        command = None

if command and command[0] == 'starten':
        xbmc.executebuiltin('CECActivateSource')

elif command and command[0] == 'wechseln':
        xbmc.executebuiltin('CECToggleState')

elif command and command[0] == 'standby':
        xbmc.executebuiltin('CECStandby')

elif command and command[0] == 'stop_und_standby':
        if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
                time.sleep(3)
        xbmc.executebuiltin('CECStandby')
