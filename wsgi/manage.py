#!/usr/bin/env python
import os, sys

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
if __name__ == "__main__":
    settings = "{{ project_name }}.settings"
    if ON_OPENSHIFT:
        settings = "{{ project_name }}.settings.openshift"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
    # Add the lib/ directory to the system path
    sys.path.append("lib")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
