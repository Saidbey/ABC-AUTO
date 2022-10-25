import subprocess

import os
from django.core.management import BaseCommand
from django.conf import settings


def get_command_path(command: str):
    output, err = subprocess.Popen(['which', command], stdout=subprocess.PIPE).communicate()
    return str(output)[2:-3]


gc = get_command_path


class Command(BaseCommand):
    help = 'setting cron jobs'
    list_of_cron_jobs = [
        f"00 03 * * * {settings.BASE_DIR}/cron_jobs/dump.sh {settings.DATABASES['default']['NAME']} "
        f"{settings.BACKUP_ROOT}",
    ]

    def handle(self, *args, **options):
        subprocess.call(['crontab', '-r'])
        file = open('cron_job_list', 'w+')
        for job in self.list_of_cron_jobs:
            file.write(job + '\n')
        file.close()
        abs_path = os.path.abspath('cron_job_list')
        subprocess.call(['crontab', abs_path])
        os.remove(abs_path)
