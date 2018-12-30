# Abschlussarbeiten-Interface (WIP)
 https://img.shields.io/badge/django%20version-2.1-green.svg https://img.shields.io/badge/WIP-yes-red.svg https://img.shields.io/badge/awesome-hell%20yeah!-blue.svg

## Info 
Dieses Projekt (Work in Progress!) soll es Mitarbeitern einer Bildungseinrichtung ermöglichen, Ausschreibungen für Abschlussarbeiten
in einem zentralen Portal hochzuladen, wo sie von interessierten Studika betrachtet werden können und bei Bedarf auf Knopdruck eine Mail
an die entsprechende Kontaktperson senden können.

## Features
- Setzen von Tags pro Abschlussarbeit, welche in einer Tagcloud weiter gefiltert werden können 
- Alle verfügbaren Abschlussarbeiten können nach Aktualität, Lehrstuhl, Art der Arbeit etc. sortiert werden
- Neben zwei Freitextfeldern für Informationen kann zusätzlich pro Ausschreibung eine PDF mit weiteren Informationen hochgeladen werden 
- Durch Zuordnung jedes Backend-Nutzers zu einem Lehrstuhl ist übersichlicheres Nutzer- und Rechtemanagement möglich

## Installation
Das Abschlussarbeiten-Interface wurde erstellt mit Django v.2.1. Die Anbindung an beliebte Datenbank-Systeme wie MySQL und PostgeSQL ist problemlos möglich,
standardmäßig wird jedoch die interne sqlite-Datenbank verwendet. Zur Umstellung auf eine Produktions-Datenbank siehe [Django-Dokumentation](https://docs.djangoproject.com/en/2.1/ref/databases/).

Die Anwendung startet im Debug-Modus! Zur Migration auf den Produktivbetrieb wird die Verwendung von WSGI empfohlen. Wichtig ist, dass `STATIC_ROOT` und `MEDIA_ROOT` richtig geroutet werden,
da sonst CSS nicht ausgeliefert wird und kein Upload von PDF-Files möglich ist. Weitere Details sowie Anleitungen zur Migration siehe [hier](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/).

### Voraussetzungen 
### Schnellstart
Das beiliegende Shell-Skript übernimmt folgende Aufgaben:
- Installation der abhängigen Pakete (mittels pip)
- Migration der Datenbankstruktur
- Anlegen der Lehrstühle
- Anlegen der Nutzergruppen
- Anlegen eines Superusers für Django

Auf Linux/MacOS geht dies recht simpel mittels des beigefügten Shell-Skriptes.

```bash
cd <checkout-dir>/fsiaai
sh setup_and_run.sh

```
### manueller Start
Alle Voraussetzungen für Python-Pakete sind in der Datei `requirements.txt` hinterlegt. Sie können einfach per pip installiert werden:
```bash
cd <checkout-dir>/fsiaai
pip3 install -r requirements.txt
```

Alles weitere passiert über Management-Befehle von Django, welche in der hier gezeigten Reihenfolge ausgeführt werden sollten:
```bash 
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py makeusergroups
python3 manage.py makeworkgroups
python3 manage.py createsuperuser
python3 manage.py runserver
``` 
Der letzte Befehl startet den Debug-Server, welcher unter [localhost:8000] erreichbar ist.
