# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Supervisor'
        db.create_table(u'example_app_supervisor', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['example_app.UserProfile'], unique=True, primary_key=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'example_app', ['Supervisor'])

        # Adding model 'UserProfile'
        db.create_table(u'example_app_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('born_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_connection', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('years_seniority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_created', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'example_app', ['UserProfile'])

        # Adding model 'Project'
        db.create_table(u'example_app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'example_app', ['Project'])

        # Adding model 'Developer'
        db.create_table(u'example_app_developer', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['example_app.UserProfile'], unique=True, primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.Supervisor'])),
        ))
        db.send_create_signal(u'example_app', ['Developer'])

        # Adding model 'Task'
        db.create_table(u'example_app_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('time_lapsed', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('importance', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['example_app.Project'], null=True, blank=True)),
            ('app_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.UserProfile'])),
        ))
        db.send_create_signal(u'example_app', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Supervisor'
        db.delete_table(u'example_app_supervisor')

        # Deleting model 'UserProfile'
        db.delete_table(u'example_app_userprofile')

        # Deleting model 'Project'
        db.delete_table(u'example_app_project')

        # Deleting model 'Developer'
        db.delete_table(u'example_app_developer')

        # Deleting model 'Task'
        db.delete_table(u'example_app_task')


    models = {
        u'example_app.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'example_app.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['example_app.Supervisor']"}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['example_app.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'example_app.project': {
            'Meta': {'object_name': 'Project'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'example_app.supervisor': {
            'Meta': {'object_name': 'Supervisor', '_ormbases': [u'example_app.UserProfile']},
            'specialisation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['example_app.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'example_app.task': {
            'Meta': {'object_name': 'Task'},
            'app_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['example_app.UserProfile']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['example_app.Project']", 'null': 'True', 'blank': 'True'}),
            'time_lapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'example_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_connection': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['example_app']