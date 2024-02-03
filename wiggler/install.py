import os
from pathlib import Path

def install():
    scriptFile = Path(__file__).parent / f"service/wiggle_record_boot.sh"
    serviceFile = Path(__file__).parent / f"service/wiggle_record.service"
    os.system(f'sudo cp {scriptFile} /usr/bin/wiggle_record_boot.sh')
    os.system(f'sudo cp {serviceFile} /etc/systemd/user/wiggle_record.service')
    os.system('systemctl --user enable wiggle_record.service')
    os.system('systemctl --user start wiggle_record.service')