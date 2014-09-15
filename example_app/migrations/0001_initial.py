# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'example_app_userprofile', (
            ('user_auth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('born_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_connection', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
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

        # Adding model 'Supervisor'
        db.create_table(u'example_app_supervisor', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['example_app.UserProfile'], unique=True, primary_key=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'example_app', ['Supervisor'])

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
        ))
        db.send_create_signal(u'example_app', ['Task'])

        # Adding model 'DeveloperWorkTask'
        db.create_table(u'example_app_developerworktask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.Developer'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.Task'])),
            ('time_lapsed_dev', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'example_app', ['DeveloperWorkTask'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'example_app_userprofile')

        # Deleting model 'Project'
        db.delete_table(u'example_app_project')

        # Deleting model 'Supervisor'
        db.delete_table(u'example_app_supervisor')

        # Deleting model 'Developer'
        db.delete_table(u'example_app_developer')

        # Deleting model 'Task'
        db.delete_table(u'example_app_task')

        # Deleting model 'DeveloperWorkTask'
        db.delete_table(u'example_app_developerworktask')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'example_app.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'example_app.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['example_app.Supervisor']"}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['example_app.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'example_app.developerworktask': {
            'Meta': {'object_name': 'DeveloperWorkTask'},
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['example_app.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['example_app.Task']"}),
            'time_lapsed_dev': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'developers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['example_app.Developer']", 'through': u"orm['example_app.DeveloperWorkTask']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['example_app.Project']", 'null': 'True', 'blank': 'True'}),
            'time_lapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'example_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'last_connection': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_auth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['example_app']