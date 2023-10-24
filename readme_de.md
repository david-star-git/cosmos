# Discord Bot Readme

## Sprachversionen
[![Englisch](https://img.shields.io/badge/Englisch-English-blue)](readme.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-German-blue)](readme_de.md)
[![Spanisch](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

Willkommen zur Dokumentation für **Cosmos**, ein vielseitiger und leistungsstarker Discord Bot, der entwickelt wurde, um die Erfahrung auf deinem Server zu verbessern. Diese Readme bietet einen Überblick über die Funktionen des Bots und wie man sie effektiv nutzt.

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Erste Schritte](#erste-schritte)
  - [Voraussetzungen](#voraussetzungen)
  - [Installation](#installation)
- [Konfiguration](#konfiguration)
- [Bot Befehle](#bot-befehle)
- [Mitwirken](#mitwirken)

## Einführung

**Cosmos** ist ein Discord Bot, der entwickelt wurde, um deinen Server interaktiver und unterhaltsamer zu gestalten. Er ist mit einer Reihe von Funktionen ausgestattet, die Moderation, Unterhaltung, Informationsabruf und mehr ermöglichen. Egal, ob du eine Gaming-Community, eine Lerngruppe oder einen anderen Typ von Server verwaltest, **Cosmos** hat etwas zu bieten.

## Erste Schritte

### Voraussetzungen

- Ein Konto bei [Discord](https://discord.com/)
- Zugang zu einem Discord Server, in dem du Administratorberechtigungen hast

### Installation

#### Schritt 1: Discord Developer Portal

1. Gehe auf das [Discord Developer Portal](https://discord.com/developers/applications/).
2. Melde dich mit deinem Discord-Konto an.

#### Schritt 2: Neue Anwendung erstellen

1. Klicke auf den Button "New Application" (Neue Anwendung erstellen).
2. Gib einen Namen für deine Anwendung ein (dies wird der Name deines Bots sein).
3. Klicke auf "Create" (Erstellen).

#### Schritt 3: Bot erstellen

1. Wähle im linken Menü "Bot" aus.
2. Klicke auf "Add Bot" (Bot hinzufügen).
3. Bestätige die Aktion mit "Yes, do it!" (Ja, bestätigen).

#### Schritt 4: Bot-Token kopieren

1. Unter dem Abschnitt "TOKEN" findest du deinen Bot-Token. Klicke auf "Copy" (Kopieren), um den Token in die Zwischenablage zu kopieren. Hinweis: Halte diesen Token geheim, da er Zugriff auf deinen Bot ermöglicht.

#### Schritt 5: Bot zu einem Server einladen

1. Kehre zur Seite deiner Anwendung zurück, indem du auf den Anwendungsnamen oben links klickst.
2. Wähle im linken Menü "OAuth2" aus.
Unter "OAuth2 URL Generator" wähle "bot" und "applications.commands" aus den Scopes aus.
Wähle die Berechtigungen aus, die dein Bot haben soll (z.B. "Read Messages", "Send Messages" usw.) der bot sollte Administrator berechtigungen haben.
Kopiere den generierten OAuth2-Link und füge ihn in deinen Webbrowser ein.
Wähle einen Server aus, zu dem du deinen Bot einladen möchtest, und bestätige die Einladung.

#### Schritt 6: Konfiguriere den bot

# Konfiguration

Die `config.json` Datei ermöglicht es dir, verschiedene Aspekte des Bots **Cosmos** anzupassen, um ihn an die Bedürfnisse Ihres Servers anzupassen. Hier ist eine Aufschlüsselung der Konfigurationsoptionen:

- **name:** Der Anzeigename des Bots im Server.
- **id:** Die ID des Bots.
- **activity:** Der Aktivitätsstatus, der für den Bot angezeigt wird (z. B. "Schaut über das Universum.").
- **owner:** Die ID des Bot-Eigentümers, der besondere Privilegien hat.

### Kanäle

- **log_channel:** Der Kanal, in dem Aktivitätsprotokolle und Benachrichtigungen des Bots gesendet werden.
- **announcement_channel:** Der Kanal für wichtige Ankündigungen des Teams an den server.
- **suggestion_channel:** Der Kanal, in dem Benutzer Vorschläge einreichen können.
- **ticket_category:** Die Kategorie zum Erstellen von Support-Ticket-Kanälen.
- **closed_category:** Die Kategorie, in die geschlossene oder erledigte Ticket-Kanäle verschoben werden.

### Rollen

- **verify_role:** Die Rolle, die Benutzern zugewiesen wird, nachdem sie verifiziert wurden.
- **ticket_role:** Die Rolle, die Benutzern gewährt wird, die Zugriff auf das Moderieren von Support-Tickets haben.
- **double_xp_role:** Die Rolle, die Benutzern doppelte Erfahrungspunkte im Server gibt.

Zusätzlich ermöglicht die Hauptbot-Datei das Zuordnen von Rollen zu bestimmten Stufen für ein Stufensystem. Das `roles`-Wörterbuch ordnet Stufen den entsprechenden Rollen-IDs zu. Benutzern werden diese Rollen zugewiesen, wenn sie die angegebenen Stufen erreichen. Um Rollen und Stufen hinzuzufügen oder zu entfernen, können Sie dieses Wörterbuch bearbeiten.

```python
roles = {
    0:   1127584577683202148,
    5:   1127584523702521916,
    10:  1127584455456981002,
    15:  1127584401342091314,
    20:  1127584356777599047,
    25:  1127584304713695323,
    30:  1127584248652627999,
    35:  1127584186715353098,
    40:  1127584121418416178,
    45:  1127584069883019375,
    50:  1127583980565299273,
    60:  1127583919001313450,
    70:  1127583602851446814,
    80:  1127583573856239627,
    90:  1127583535272820737,
    115: 1127583507514929294,
    130: 1127583471947235338,
    160: 1127583438690603079,
    200: 1127579753663172608
}
```

### Token

1. Erstelle eine Datei namens `.env` im selben Ordner wo sich `index.py` befindet.
2. Schreibe da folgende Zeile rein: `TOKEN = "DeinToken"` ersetze dabei `DeinToken` mit dem tatsächlichem Token vom Bot.

#### Schritt 7: Code ausführen

1. Stelle sicher, dass du Python installiert hast. Falls nicht kannst du sie [hier](https://www.python.org/downloads/) herunterlade.
2. Installiere die Python Pakete. `pip install -r requirements.txt`
3. Führe deinen Code aus.
Dein Bot sollte sich nun im Discord anmelden und auf Befehle oder Ereignisse reagieren können.

## Bot Befehle

Hier sind einige der wichtigsten Befehle, die von **Cosmos** unterstützt werden:

### Ban

- **Beschreibung:** Verbannt einen Benutzer vom Server.
- **Verwendung:** `/ban [benutzer] [grund]`

### Kick

- **Beschreibung:** Schmeißt einen Benutzer vom Server.
- **Verwendung:** `/kick [benutzer] [grund]`

### Mute

- **Beschreibung:** Schaltet einen Benutzer stumm (Er kann danach nicht schreiben).
- **Verwendung:** `/mute [benutzer] [grund]`

### Unmute

- **Beschreibung:** Entstummt einen Benutzer.
- **Verwendung:** `/unmute [benutzer] [grund]`

### Clear

- **Beschreibung:** Löscht eine anzahl von Nachrichten in einem Kanahl.
- **Verwendung:** `/clear [anzahl]`

### Info

- **Beschreibung:** Zaigt den Strafverlauf von einem Benutzer an der in `users.db` gespeichert wird.
- **Verwendung:** `/info [benutzer]`

### Warn

- **Beschreibung:** Warnt einen Benutzer.
- **Verwendung:** `/warn [benutzer] [grund]`

### Reset

- **Beschreibung:** Setzt die information ( Strafverlauf, Level ) von einem Benutzer zurück. Alternativ kann er auch benutzt werden um Benutzer zur Datenbank hinzuzufügen.
- **Verwendung:** `/unmute [benutzer] [grund]`

### Server info

- **Beschreibung:** Zeigt Informationen über dem Server an.
- **Verwendung:** `/serverinfo`

### Avatar

- **Beschreibung:** Gibt dir den Avatar ( profilbild ) eines Benutzers.
- **Verwendung:** `/avatar [benutzer]`

### Suggest

- **Beschreibung:** Benutzer können es benutzen damit sie Vorschläge an das team schicken können.
- **Verwendung:** `/suggest [nachricht]`

### Announce

- **Beschreibung:** Das Team kann es benutzen um uniforme Ankündigungen an die Benutzer zu schicken.
- **Verwendung:** `/announce [nachricht]`

### Ping

- **Beschreibung:** Gibt den Ping des Bots wider.
- **Verwendung:** `/ping`

### Rank

- **Beschreibung:** Zeigt dir dein level an.
- **Verwendung:** `/rank`

### Set level

- **Beschreibung:** Setzt das Level von einem Benutzer.
- **Verwendung:** `/level [benutzer] [level]`

### Verify

- **Beschreibung:** Erlaubt Benutzern sich zu verifizieren.
- **Verwendung:** `/verify`

### Rules

- **Beschreibung:** Sendet die Server-regeln ( diese müssen in `index.py` auf Zeile 526-536 manuell geändert werden ).
- **Verwendung:** `/rules`

### Ticket

- **Beschreibung:** Erlaubt es Benutzern einen Ticket zu erstellen.
- **Verwendung:** `/ticket`

## Mitwirken

Wir begrüßen Beiträge aus der Community! Wenn du zu **Cosmos** beitragen möchtest, befolge bitte diese Schritte:

1. Fork das Repository.
2. Erstelle einen neuen Branch.
3. Füge deine Verbesserungen oder Fehlerkorrekturen hinzu.
4. Reiche einen Pull Request ein.

Vielen Dank, dass du **Cosmos** gewählt hast! Wir hoffen, dass dieser Bot deinem Discord Server viel Wert und Freude bringt. Wenn du Vorschläge oder Feature-Anfragen hast, zögere nicht, uns wissen zu lassen!

## Lizenz

Dieses Projekt steht unter der [GNU General Public License, Version 3.0](LICENSE). Den vollständigen Lizenztext finden Sie [hier](https://www.gnu.org/licenses/gpl-3.0.html).
