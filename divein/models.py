from django.db import models

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
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField()
    birth_date = models.DateField('birth_date')
    levels     = models.ManyToManyField(Level, through='Graduate')
    friends    = models.ManyToManyField('self') # self refer to Diver class, not current instance

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

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
        return u'{}({})'.format(self.name, self.city)

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
    divers       = models.ManyToManyField(Diver, through='DivePart', related_name='+')
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