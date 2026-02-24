# RCON_CS
Simple Python script to run RCON command for Counter-Strike 1.6 dedicated server.

## Compile from source (Windows)
`pip install pyinstaller`

`pyinstaller --onefile rcon_cs.py`

## How to use
### Using raw .py script
`python rcon_cs.py -i IP -p PORT -a PASSWORD status`
### Using compiled binary
`rcon_cs -i IP -p PORT -a PASSWORD status`