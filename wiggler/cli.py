import argparse
import os
from pathlib import Path
from wiggler.light import pixels
from wiggler.camera import camera as cameraControl

def main():

    parser = argparse.ArgumentParser(prog='wiggler', description='WiggleR API')

    parser.add_argument('-i', '--install', action='store_true',
                        help='first time setup')

    parser.add_argument('-s', '--server', action='store_true',
                        help='start api server')

    light = parser.add_argument_group("light")
    light.add_argument('--light-install', action='store_true',
                       help='install NeoPixel led ring')
    light.add_argument('--light', nargs='?',
                       const=0.1, help='light intensity from 0.01 to 1', type=float)
    light.add_argument('--light-off', action='store_true',
                       help='turn light off')

    camera = parser.add_argument_group("camera")
    camera.add_argument('--picture', action='store_true',
                       help='take one picture')

    recording = parser.add_argument_group("recording")
    recording.add_argument('--recording',
                         const='status',
                         nargs='?',
                         choices=['stop', 'start'],
                         help='control wiggler recording')

    service = parser.add_argument_group("service")
    service.add_argument('--service-install',
                         action='store_true',
                         help='install wiggler service to start api server on boot')
    service.add_argument('--service',
                         const='status',
                         nargs='?',
                         choices=['stop', 'start',
                                  'status', 'disable', 'enable'],
                         help='control wiggler service')

    args = parser.parse_args()

    if args.install:
        os.system(f"mkdir WiggleR")
        os.system(f"mkdir WiggleR/Videos WiggleR/Pictures WiggleR/Zip")
    elif args.server:
        os.system(f"uvicorn wiggler.main:app --reload --host 0.0.0.0")
    elif args.service_install:
        scriptFile = Path(__file__).parent / f"service/wiggler_boot.sh"
        serviceFile = Path(__file__).parent / f"service/wiggler.service"
        os.system(f'sudo cp {scriptFile} /usr/bin/wiggler_boot.sh')
        os.system(f'sudo cp {serviceFile} /etc/systemd/user/wiggler.service')
        os.system('systemctl --user enable wiggler.service')
        os.system('systemctl --user start wiggler.service')
    elif args.service:
        os.system(f'systemctl --user {args.service} wiggler.service')
    elif args.light_install:
        # /boot/config.txt by changing "dtparam=audio=on" to "dtparam=audio=off"
        # message to connect to ports
        print('...')
    elif args.light:
        pixels.on(args.light)
    elif args.light_off:
        pixels.off()
    elif args.camera_picture:
        cameraControl.picture()
    elif args.recording:
        if args.recording == 'start':
            cameraControl.start_recording()
        elif args.recording == 'stop':
            cameraControl.stop_recording()
    else:
        print("run wiggler -h for options")


if __name__ == '__main__':
    main()
