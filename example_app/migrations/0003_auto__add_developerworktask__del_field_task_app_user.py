# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeveloperWorkTask'
        db.create_table(u'example_app_developerworktask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.Developer'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.Task'])),
            ('time_lapsed_dev', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'example_app', ['DeveloperWorkTask'])

        # Deleting field 'Task.app_user'
        db.delete_column(u'example_app_task', 'app_user_id')


    def backwards(self, orm):
        # Deleting model 'DeveloperWorkTask'
        db.delete_table(u'example_app_developerworktask')


        # User chose to not deal with backwards NULL issues for 'Task.app_user'
        raise RuntimeError("Cannot reverse this migration. 'Task.app_user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Task.app_user'
        db.add_column(u'example_app_task', 'app_user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example_app.UserProfile']),
                      keep_default=False)


    models = {
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