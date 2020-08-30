<h1 align="center">
  <br>
  <a href="https://github.com/elmoiv/DLSE"><img src="https://github.com/elmoiv/DLSE/blob/master/icon.png" alt="XSStrike"></a>
  <br>
  DLSE
  <br>
</h1>

<h4 align="center">One click skill editor for Dying Light Game</h4>

## Features
  - Super user-friendly, all the hard work done in one click.
  - Compatible with all versions.
  - Ability to save your skills profile and share it with others.
  - Reset any/all skill to its original value.
  - Edited skills can be sorted for fast access.
  - Search for any skill in no time.

## Download
Win64 Release: [Download](https://github.com/elmoiv/DLSE/releases/tag/1.0)
## Usage
To run the Editor from source:
 - `pip install -r requirements.txt`
 - `python DLSE.py`

## What Happens
  - When you launch DLSE for the first time, it will navigate you to choose DyingLight executable file.
  - DLSE will copy Data0.pak file to it's working folder existed in "Documents".
  - skills xml files will be extracted and backed up for safety.
  - Now you can select your desired skill and edit its value.
  - When you are done. Click apply to update the game with the new edits.
  - You can now launch the game.

## Requirements
  ```
PyQt5
qdarkstyle
  ```
## Screenshot
<p align="center">
  <img src="https://github.com/elmoiv/DLSE/blob/master/preview.png">
</p>

## Problems
Antivirus mark compiled exe as **Win64:Trojan-gen**.

To solve this problem:
  - Disable antivirus software.
  - Install the release.
  - Add application folder to exception list.
  - Enable antivirus again.

Virus Total Results:
  - DLSE: [Report](https://www.virustotal.com/gui/file/ba005ae9277bc7703247bf00b8156be2e5eaf014294ade188a8f726c9ae355e8/detection/f-ba005ae9277bc7703247bf00b8156be2e5eaf014294ade188a8f726c9ae355e8-1595172634)
  - DLSE [Full Libraries]: [Report](https://www.virustotal.com/gui/file/3dcbc45f2b8708aa0d52810344b8f64bc4f7fc00d7c451bc138cf0096a69cab7/detection/f-3dcbc45f2b8708aa0d52810344b8f64bc4f7fc00d7c451bc138cf0096a69cab7-1595172987)
  - DLSE v1.1 Setup: [Report](https://www.virustotal.com/gui/file/110bcca8e4087522ba5fee1852e2c0598d7008e64a7c6a6cc6b80c718a5ca1f1/detection/f-110bcca8e4087522ba5fee1852e2c0598d7008e64a7c6a6cc6b80c718a5ca1f1-1595619055)

If you have any concerns about the release, compile it yourself.

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/DLSE/issues) or send me a pull request.
