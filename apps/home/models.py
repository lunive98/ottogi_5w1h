# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Df1(models.Model):
    pid = models.IntegerField(primary_key=True)
    자치구 = models.CharField(max_length=50)
    topic1 = models.CharField(db_column='Topic1', max_length=50)  # Field name made lowercase.
    topic2 = models.CharField(db_column='Topic2', max_length=10)  # Field name made lowercase.
    topic3 = models.CharField(db_column='Topic3', max_length=10)  # Field name made lowercase.
    topic4 = models.CharField(db_column='Topic4', max_length=10)  # Field name made lowercase.
    score = models.DecimalField(max_digits=25, decimal_places=20)
    new_label = models.DecimalField(max_digits=25, decimal_places=20)

    class Meta:
        managed = False
        db_table = 'df1'


class Df3(models.Model):
    pid = models.IntegerField()
    score_review = models.DecimalField(max_digits=7, decimal_places=2)
    new_label_review = models.DecimalField(max_digits=7, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'df3'


class Info(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=50)
    uphpareatitle = models.CharField(db_column='upHpAreaTitle', max_length=10)  # Field name made lowercase.
    hpareatitle = models.CharField(db_column='hpAreaTitle', max_length=20)  # Field name made lowercase.
    hpschcatenm = models.CharField(db_column='hpSchCateNm', max_length=20)  # Field name made lowercase.
    mcatenm = models.CharField(db_column='mcateNm', max_length=20)  # Field name made lowercase.
    cmt = models.CharField(max_length=30, blank=True, null=True)
    lat = models.DecimalField(max_digits=11, decimal_places=7)
    lng = models.DecimalField(max_digits=11, decimal_places=7)
    addr = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100, blank=True, null=True)
    hundredyn = models.CharField(db_column='hundredYn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    likecnt = models.IntegerField(db_column='likeCnt', blank=True, null=True)  # Field name made lowercase.
    bookmarkcnt = models.IntegerField(db_column='bookmarkCnt', blank=True, null=True)  # Field name made lowercase.
    viewcnt = models.IntegerField(db_column='viewCnt', blank=True, null=True)  # Field name made lowercase.
    callcnt = models.IntegerField(db_column='callCnt', blank=True, null=True)  # Field name made lowercase.
    sharecnt = models.IntegerField(db_column='shareCnt', blank=True, null=True)  # Field name made lowercase.
    chkincnt = models.IntegerField(db_column='chkinCnt', blank=True, null=True)  # Field name made lowercase.
    rpcnt = models.IntegerField(db_column='rpCnt', blank=True, null=True)  # Field name made lowercase.
    parkingyn = models.CharField(db_column='parkingYn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valletyn = models.CharField(db_column='valletYn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(max_length=100, blank=True, null=True)
    menu = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'info'


class Keyword(models.Model):
    pid = models.ForeignKey(Info, models.DO_NOTHING, db_column='pid')
    keyword_1 = models.CharField(max_length=20)
    keyword_2 = models.CharField(max_length=20, blank=True, null=True)
    keyword_3 = models.CharField(max_length=20, blank=True, null=True)
    keyword_4 = models.CharField(max_length=20, blank=True, null=True)
    keyword_5 = models.CharField(max_length=20, blank=True, null=True)
    keyword_6 = models.CharField(max_length=20, blank=True, null=True)
    keyword_7 = models.CharField(max_length=20, blank=True, null=True)
    keyword_8 = models.CharField(max_length=20, blank=True, null=True)
    keyword_9 = models.CharField(max_length=20, blank=True, null=True)
    keyword_10 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class SiksinInfo(models.Model):
    place_name = models.TextField(blank=True, null=True)
    place_tag1 = models.TextField(blank=True, null=True)
    place_tag2 = models.TextField(blank=True, null=True)
    place_tag3 = models.TextField(blank=True, null=True)
    place_tag4 = models.TextField(blank=True, null=True)
    place_tag5 = models.TextField(blank=True, null=True)
    place_location = models.TextField(blank=True, null=True)
    place_category = models.TextField(blank=True, null=True)
    place_near_station = models.TextField(blank=True, null=True)
    place_contents_info = models.TextField(blank=True, null=True)
    place_address = models.TextField(blank=True, null=True)
    place_convenience = models.TextField(blank=True, null=True)
    place_telephone = models.TextField(blank=True, null=True)
    place_route = models.TextField(blank=True, null=True)
    place_homepage = models.TextField(blank=True, null=True)
    place_drink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siksin_info'


class SiksinReview(models.Model):
    siksin_review_id = models.AutoField(primary_key=True)
    place_name = models.TextField(blank=True, null=True)
    place_review_content = models.TextField(blank=True, null=True)
    place_reviewer = models.TextField(blank=True, null=True)
    place_review_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siksin_review'
