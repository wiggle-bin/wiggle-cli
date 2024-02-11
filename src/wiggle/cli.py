import argparse
import os
from wiggle.tag import tag as tagControl
from wiggle_settings.main import update_setting, Status

def main():

    parser = argparse.ArgumentParser(prog='wiggler', description='WiggleR API')

    parser.add_argument('-i', '--install', action='store_true',
                        help='first time setup')

    parser.add_argument('-s', '--server', action='store_true',
                        help='start api server')

    light = parser.add_argument_group("light")
    light.add_argument('--light', nargs='?',
                       const=0.1, help='light intensity from 0.01 to 1', type=float)
    light.add_argument('--light-off', action='store_true',
                       help='turn light off')

    recording = parser.add_argument_group("recording")
    recording.add_argument('--recording',
                         const='status',
                         nargs='?',
                         choices=['stop', 'start'],
                         help='control wiggler recording')
    
    tag = parser.add_argument_group("tag")
    tag.add_argument('--tag',
                        action='store_true',
                        help='start or stop experiment')

    args = parser.parse_args()

    if args.install:
        os.system(f"mkdir WiggleR")
        os.system(f"mkdir WiggleR/Videos WiggleR/Pictures WiggleR/Recording WiggleR/Zip WiggleR/Data WiggleR/Settings")
    elif args.light:
        update_setting("light", Status.ON)
    elif args.light_off:
        update_setting("light", Status.OFF)
    elif args.recording:
        if args.recording == 'start':
            update_setting("recording", Status.ON)
        elif args.recording == 'stop':
            update_setting("recording", Status.OFF)
    elif args.tag:
        tagControl.tag()
    else:
        print("run wiggler -h for options")


if __name__ == '__main__':
    main()
