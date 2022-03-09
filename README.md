# RPIMON
Simple monitor and control for Raspberry Pi over SSH
<br />
![alt tag](https://github.com/DIYDave/RPIMON/blob/main/Ansicht.jpg)

## German (English version below)
Dieses Tool wurde aus der Not gebohren, einen Raspberry Pi runterzufahren bevor die Speisung ausgeschaltet wird.
In meinem Fall läuft der RPI in einer Laserschneidmaschine mit LaserWeb. Dieses geniale Tool bietet aber keine Möglichkeit den RPI runterzufahren.

### Funktion:
Das Tool stellt eine Verbindung zu einem Raspberry Pi über SSH her.
Dazu muss SSH auf dem RPI natürlich freigeschaltet sein.
Während dem Betrieb wird die aktuelle CPU Temperatur angezeigt.
Über das Menü kann der RPI dan neu gestartet oder heruntergefahren werden.

### Realisierung
Das Tool ist in Python 3.10.x geschrieben und ist erst mein zweites Programm in dieser Sprache.
Es dürfte also einiges geben, was nicht perfekt gelöst ist..
Die .exe Datei ist für den Betrieb ohne installiertem Python auf jedem Windowsrechner gedacht.
Obwohl diese Version sehr gross ist, wird zur Laufzeit sehr wenig Ressourcen verwendet.

### Settings
Beim ersten Start wird die Datei "settings.txt" erzeugt.
Diese Datei im JSON Format muss an die Einstellungen des verwendeten RPI angepasst werden .
Das Format darf dabei nicht geändert werden. (Z.B. Anführungszeichen)
Inhalt:
```
{
  "ip": "192.168.0.41",
  "port": "22",
  "usr": "pi",
  "pwd": "raspberry"
}
```
