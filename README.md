# RPIMON
Simple monitor and control for Raspberry Pi over SSH
<br />
![alt tag](https://github.com/DIYDave/RPIMON/blob/main/Ansicht.jpg)

## German (English version below)
Dieses Tool wurde aus der Not gebohren, einen Raspberry Pi runterzufahren bevor die Speisung ausgeschaltet wird.
In meinem Fall läuft der RPI in einer Laserschneidmaschine mit [LaserWeb](https://https://github.com/LaserWeb/LaserWeb4). Dieses geniale Tool bietet aber keine Möglichkeit den RPI runterzufahren.

### Funktion:
Das Tool stellt eine Verbindung zu einem Raspberry Pi über SSH her.
Dazu muss SSH auf dem RPI natürlich freigeschaltet sein.
Während dem Betrieb wird die aktuelle CPU Temperatur angezeigt.
Über das Menü kann der RPI dan neu gestartet oder heruntergefahren werden.

### Realisierung
Das Tool ist in Python 3.10.x geschrieben und ist erst mein zweites Programm in dieser Sprache.
Es dürfte also einiges geben, was nicht perfekt gelöst ist..
Es werden die Module [pysimplegui](https://https://pysimplegui.readthedocs.io/en/latest/) und 
Die .exe Datei ist für den Betrieb ohne installiertem Python auf jedem Windowsrechner gedacht.
Obwohl diese Version recht gross ist, wird zur Laufzeit sehr wenig Ressourcen verwendet.

### Settings
Beim ersten Start wird die Datei "settings.txt" erzeugt.
Diese Datei im JSON Format muss mit einem Texteditor an die Einstellungen des verwendeten RPI angepasst werden .
Das Format darf dabei nicht geändert werden. (Z.B. Anführungszeichen)
<br />
Inhalt:
```
{
  "ip": "192.168.0.41",
  "port": "22",
  "usr": "pi",
  "pwd": "raspberry"
}
```

## English
This tool was born out of necessity to shut down / reboot a Raspberry Pi before the power is switched off.
In my case the RPI is running in a laser cutting machine using [LaserWeb](https://https://github.com/LaserWeb/LaserWeb4). However, this ingenious tool does not offer the possibility of shutting down the RPI.

### Function:
The tool connects to a Raspberry Pi via SSH.
To do this, SSH must of course be activated on the RPI.
The current CPU temperature is displayed during operation.
The RPI can then be restarted or shut down via the menu.

### Realization
The tool is written in Python 3.10.x and is only my second program in this language.
So there might be some things that haven't been solved perfectly.
The .exe file is intended for use on any Windows computer without Python installed.
Although this version is quite large, very few resources are used at runtime.

### Settings
The "settings.txt" file is created when you start it for the first time.
This file in JSON format must be adapted to the settings of the RPI used using a text editor.
The format must not be changed. (e.g. quotation marks)
<br />
Contents:
```
{
  "ip": "192.168.0.41",
  "port": "22",
  "usr": "pi",
  "pwd": "raspberry"
}
```
