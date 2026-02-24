# RCON_CS
A simple CLI created in Python to run RCON commands for Counter-Strike 1.6 dedicated servers.

## How to Use
Download the [latest release](https://github.com/raffysucilan/rcon-cs/releases).  
### Sample Batch File
```
@echo off

set IP=0.0.0.0 
set PORT=0
set PASSWORD=

rem Using Binary
rcon_cs -i %IP% -p %PORT% -a %PASSWORD% status

rem Using Script
python rcon_cs.py -i %IP% -p %PORT% -a %PASSWORD% status

pause
```
## Compile from Source (Windows)
### Using [PYInstaller](https://pypi.org/project/pyinstaller)
`pyinstaller --onefile rcon_cs.py`