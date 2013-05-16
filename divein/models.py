from django.db import models

# Create your models here.
class Federation(models.Model):
    federation = models.CharField('Federation name'    , max_length=50)
    website    = models.URLField('Federation website'  , blank=True)

    def __unicode__(self):
        return self.federation

class Level(models.Model):
    level      = models.CharField('The level name'      , max_length=50)
    federation = models.ForeignKey(Federation)

    def __unicode__(self):
        return '{}({})'.format(self.level, self.federation)

class Club(models.Model):
    club      = models.CharField('The club name' , max_length=50)
    website   = models.URLField('Club website'  , blank=True)
    city      = models.CharField('Club city', max_length=50  , blank=True)

    def __unicode__(self):
        return self.club

class Diver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField()
    birth_date = models.DateField('birth_date')
    levels     = models.ManyToManyField(Level, through='Graduate')

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Graduate(models.Model):
    user          = models.ForeignKey(Diver)
    level         = models.ForeignKey(Level)
    date          = models.DateField('The graduate date')
    club          = models.ForeignKey(Club, blank=True)

    def __unicode__(self):
        return '{} => {}'.format(self.user, self.level)

class Site(models.Model):
    name     = models.CharField('The site name'     ,max_length=200)
    city     = models.CharField('The site city'     ,max_length=200)
    country  = models.CharField('The site country'  ,max_length=200)
    max_depth = models.IntegerField('Maximum site depth', blank = True)

    def __unicode__(self):
        return self.name

class Dive(models.Model):
    date     = models.DateTimeField('Dive date')
    duration = models.IntegerField('Dive duration in minutes')
    depth    = models.IntegerField('Dive max deep in meters')
    club     = models.ForeignKey(Club, blank=True)
    site     = models.ForeignKey(Site)

    def __unicode__(self):
        return '{} = {}'.format(self.site, self.date)