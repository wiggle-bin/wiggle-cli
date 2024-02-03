# Wiggle-cli

Control the [WiggleR](https://github.com/wiggle-bin/wiggle-r) via the command line. Wiggle-cli allows you do things like change the light and control the camera of the WiggleR via the command line.

## Installation

```
pip3 install wiggler_studiorabota
```

## Documentation

```
wiggler -h
```

## Enable recording service

In the terminal run `wiggle_record_install`. This will install and start a service which runs `wiggler --record` to take pictures every couple of seconds.

```
wiggle_record_install
```


You can check the status with:

```
systemctl --user status wiggle_record.service
```

To stop the service run:

```
systemctl --user stop wiggle_record.service
```

To start the service run:

```
systemctl --user start wiggle_record.service
```

## Installation for development

Updating packages on Raspberry Pi
```
pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
```

Installing package
```
pip3 install -e .
```

For installation without dev dependencies
```
pip install --no-dev -r requirements.txt
```