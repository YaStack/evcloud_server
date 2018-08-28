# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('snap', models.CharField(help_text='系统会通过该字段判断snap是否存在，不存在则自动创建snap并做protect操作。修改或新增snap时请确保镜像没有被任何虚拟机所占用！', max_length=200)),
                ('desc', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('enable', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0, help_text='用于在页面中的显示顺序，数值越小越靠前。', verbose_name='排序')),
                ('cephpool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.CephPool')),
            ],
            options={
                'verbose_name': '镜像',
                'verbose_name_plural': '1_镜像',
            },
        ),
        migrations.CreateModel(
            name='ImageType',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, verbose_name='类型编号')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='类型名称')),
                ('order', models.IntegerField(default=0, help_text='用于在页面中的显示顺序，数值越小越靠前。', verbose_name='排序')),
            ],
            options={
                'verbose_name': '镜像类型',
                'verbose_name_plural': '2_镜像类型',
            },
        ),
        migrations.CreateModel(
            name='Xml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('xml', models.TextField()),
                ('desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '虚拟机XML模板',
                'verbose_name_plural': '3_虚拟机XML模板',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.ImageType'),
        ),
        migrations.AddField(
            model_name='image',
            name='xml',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.Xml'),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('cephpool', 'name', 'version')]),
        ),
    ]