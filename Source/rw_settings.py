import json
"""
Modul zum schreiben und lesen von json formatierten Dateien z.B. für Settings
"""

def read(filename):
  try:
    return json.load(open(filename))
  except:
    return None

def write(filename,dict):
  try:
    json.dump(dict, open(filename,'w'),indent=2)  # ident=2 -> New line for each variable
    return None
  except Exception as e:
     return e 


# # Beispielaufruf:
# settings = read("settings.txt")
# if settings == None:
#   settings = {"ip":"192.168.0.41","usr":"pi","pwd":"raspberry"}
#   write("settings.txt", settings)
# else:
#   print (settings)