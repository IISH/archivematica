# -*- coding: utf-8 -*-
"""Migration to add a 7-zip method to the Archivematica AIP compression
methods that does not use compression. 7-zip copy mode.
"""
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):
    """Entry point for the migration."""
    dependencies = [('main', '0056_transfer_access_system_id')]
    operations = [
        migrations.RunPython(data_migration_up, data_migration_down),
    ]
