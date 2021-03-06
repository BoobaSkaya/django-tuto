from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


import urllib, hashlib

class Federation(models.Model):
    federation = models.CharField('Federation name'    , max_length=50)
    website    = models.URLField('Federation website'  , blank=True)

    def __unicode__(self):
        return self.federation

class Level(models.Model):
    level      = models.CharField('The level name'      , max_length=50)
    federation = models.ForeignKey(Federation)

    def __unicode__(self):
        return u'{}({})'.format(self.level, self.federation)

class Club(models.Model):
    club      = models.CharField('The club name' , max_length=50)
    website   = models.URLField('Club website'  , blank=True)
    city      = models.CharField('Club city', max_length=50  , blank=True)

    def __unicode__(self):
        return self.club

class Diver(models.Model):
    #Do not refer directly User since it can change
    #User settings.AUTH_USER_MODEL instead
    user       = models.OneToOneField(settings.AUTH_USER_MODEL) 
    birth_date = models.DateField('birth_date')
    levels     = models.ManyToManyField(Level, through='Graduate')
    # self refer to Diver class, not current instance
    friends    = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return u'{}'.format(self.user.username)

    def getGravatar(self, size=40):
        default = "http://www.example.com/default.jpg"
        gravatar_url = "http://www.gravatar.com/avatar/"
        gravatar_url += hashlib.md5(self.user.email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        return gravatar_url

class Graduate(models.Model):
    diver         = models.ForeignKey(Diver)
    level         = models.ForeignKey(Level)
    date          = models.DateField('The graduate date')
    club          = models.ForeignKey(Club, blank=True)

    def __unicode__(self):
        return u'{} => {}'.format(self.diver, self.level)

class Spot(models.Model):
    name     = models.CharField('The site name'     ,max_length=200)
    city     = models.CharField('The site city'     ,max_length=200)
    country  = models.CharField('The site country'  ,max_length=200)
    max_depth = models.IntegerField('Maximum site depth', blank = True)
    gps      = models.CharField('GPS location'     ,max_length=200, blank = True)
    
    def __unicode__(self):
        return u'{}'.format(self.name)

class SpotComment(models.Model):
    text    = models.CharField('Comment', max_length=1000)
    diver   = models.ForeignKey(Diver)
    date    = models.DateTimeField('Comment posted date')
    
    def __unicode__(self):
        return u'{} says {}'.format(self.diver, self.text)



class DiveTag(models.Model):
    tag          = models.CharField('The dive tag'     ,max_length=30)

    def __unicode__(self):
        return self.tag

class Dive(models.Model):
    date         = models.DateTimeField('Dive date')
    duration     = models.IntegerField('Dive duration in minutes')
    depth        = models.IntegerField('Dive max deep in meters')
    club         = models.ForeignKey(Club, blank=True)
    spot         = models.ForeignKey(Spot)
    created_by   = models.ForeignKey(Diver, related_name='+')
    created_date = models.DateField('Creation date')
    divers       = models.ManyToManyField(Diver, through='DivePart', related_name='+', blank=True)
    tags         = models.ManyToManyField(DiveTag, blank=True)

    def __unicode__(self):
        return u'{} [{}]'.format(self.spot, self.date)


class DivePart(models.Model):
    dive    = models.ForeignKey(Dive)
    diver   = models.ForeignKey(Diver)
    note    = models.IntegerField('The dive note')
    leader  = models.BooleanField('Was the dive leader')

    def __unicode__(self):
        return u'{} was in {}'.format(self.diver, self.dive)