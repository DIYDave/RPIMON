from paramiko import SSHClient
from paramiko import AutoAddPolicy
import PySimpleGUI as sg
from sys import exit         # DW ansonsten Fehler beim schlieesen
import time

import rw_settings            # Read / write settings

VERSION = "1.00"
# GUI
def make_window():
  sg.theme("DarkBlue14")  #DarkGrey11
  menu_def = [['&Raspberry Pi', ['&Shutdown / Reboot', "Connect SSH"]], ['&Application', ['&Exit','&About']]]
  layout =  [ [sg.Menu(menu_def, key='-MENU-')],
              [sg.Text('CPU:'), sg.Text(k="-CPUTEMP-", text_color="LIGHTGREY",  size=(5,1), justification="right"),sg.Checkbox('KoT', default=True, k='-KOT-',tooltip='Keep On Top')]], 
  return sg.Window('RPIMON', layout,  finalize=True, grab_anywhere=True, no_titlebar=True)  #no_titlebar=True

def my_popup(window):
    layout = [[sg.Text("Are you shure to shutdown \nor restart the raspberry pi ??")],
              [sg.Button("Shut down",size = (8,1)), sg.Button("Reboot", size = (8,1)), sg.Button("Cancel", size = (8,1))]]
    win = sg.Window("Shure?", layout, modal=True, grab_anywhere=True, keep_on_top=True, no_titlebar=True)
    event, value= win.read()
    win.close()
    window.write_event_value(event,None)

def main():
  ssh = SSHClient()
  ssh_cycle = 5                                 # Temp reading every n seconds
  settings = handle_settings()                  # Load settings                        
  ssh_connect(ssh,settings)                     # Try to connect
  lasttime = time.time() - ssh_cycle            # Set time to make a temperature query
  window = make_window() 
  while True:                                   # This is the Event Loop for the GUI      
    event, values = window.read(timeout=1)            
    if event == sg.WIN_CLOSED or event == 'Exit':
      break
    elif event == 'Shutdown / Reboot': 
      my_popup(window)
    elif event in ("Shut down", "Reboot", "Cancel"):
      if event == "Shut down":
        ssh_send(ssh, 'sudo shutdown -h now')
      elif event == "Reboot":
         ssh_send(ssh, 'sudo reboot')
    elif event == "Connect SSH":
      ssh_connect(ssh,settings)                     # Try to connect
      lasttime = time.time() - ssh_cycle            # Set time to make a temperature query
    elif event == 'About':
      sg.popup_no_titlebar("Version:" + VERSION + "\nRPI monitor by Dave's DIY", keep_on_top=True)
    elif time.time() - lasttime > ssh_cycle:
      temp = ssh_send(ssh, 'cat /sys/class/thermal/thermal_zone0/temp')
      if temp != None:
        temp = round(temp/1000,1)
        if temp < 67.0:
          window['-CPUTEMP-'].update(text_color="LIGHTGREEN")
        elif temp <= 77.0:
          window['-CPUTEMP-'].update(text_color="ORANGE")
        elif temp > 77.0:
          window['-CPUTEMP-'].update(text_color="RED")
        window['-CPUTEMP-'].update(str(temp) + '°C')
      else:
        window['-CPUTEMP-'].update(text_color="RED")
        window['-CPUTEMP-'].update("Offline")
      lasttime = time.time()
    if values["-KOT-"] == True:
      window.TKroot.wm_attributes("-topmost", 1)          # Muss so, da "keep_on_top" nicht dynamisch funktioniert
    else:
      window.TKroot.wm_attributes("-topmost", 0)
  ssh.close()    
  window.close()
  exit(0)

def ssh_connect(ssh,settings):
  try:
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(settings.get("ip"), port=settings.get("port"), username = settings.get("usr"), password = settings.get("pwd"), timeout = 2, auth_timeout = 3)
  except:
    ssh.close()

def ssh_send(ssh, command):
  if ssh.get_transport() is not None and ssh.get_transport().is_active():
      try:
        stdin, stdout, stderr = ssh.exec_command(command,timeout=2)
        return int(stdout.read())
      except:
        ssh.close()  
        return None
  else:
    ssh.close()  
    return None

def handle_settings():
  settings = rw_settings.read(".\settings.txt")           # Read settings from file
  if settings == None:                                    # File not found
    settings = {"ip":"192.168.0.41", "port":"22", "usr":"pi", "pwd":"raspberry"}  # Default settings to make new file
    rw_settings.write(".\settings.txt", settings)         # Make new file
    sg.popup_no_titlebar("No settings file found!\nA new one was created with default values.\nPlease edit \"settings.txt\" for your own values.\nAnd restart the application",keep_on_top=True)
  return settings

if __name__ == '__main__':
  main()
