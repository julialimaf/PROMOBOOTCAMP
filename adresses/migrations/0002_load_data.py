from django.db import migrations
import os


def load_cep(apps, schema_editor):
    base_dir = os.path.dirname(__file__)
    sql_path = os.path.join(base_dir, "sql", "insert_addresses_ceps.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read().replace("addresses_ceps", "adresses_ceps")
        schema_editor.execute(sql)


def load_city(apps, schema_editor):
    base_dir = os.path.dirname(__file__)
    sql_path = os.path.join(base_dir, "sql", "insert_addresses_cities.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read().replace("addresses_cities", "adresses_cities")
        schema_editor.execute(sql)


def load_states(apps, schema_editor):
    base_dir = os.path.dirname(__file__)
    sql_path = os.path.join(base_dir, "sql", "insert_addresses_states.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read().replace("addresses_states", "adresses_states")
        schema_editor.execute(sql)


class Migration(migrations.Migration):

    dependencies = [
        ("adresses", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_cep),
        migrations.RunPython(load_city),
        migrations.RunPython(load_states),
    ]
