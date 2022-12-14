# Generated by Django 3.2.13 on 2022-09-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Df1',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('자치구', models.CharField(max_length=50)),
                ('topic1', models.CharField(db_column='Topic1', max_length=50)),
                ('topic2', models.CharField(db_column='Topic2', max_length=10)),
                ('topic3', models.CharField(db_column='Topic3', max_length=10)),
                ('topic4', models.CharField(db_column='Topic4', max_length=10)),
                ('score', models.DecimalField(decimal_places=20, max_digits=25)),
                ('new_label', models.DecimalField(decimal_places=20, max_digits=25)),
            ],
            options={
                'db_table': 'df1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Df3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('score_review', models.DecimalField(decimal_places=2, max_digits=7)),
                ('new_label_review', models.DecimalField(decimal_places=5, max_digits=7)),
            ],
            options={
                'db_table': 'df3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('uphpareatitle', models.CharField(db_column='upHpAreaTitle', max_length=10)),
                ('hpareatitle', models.CharField(db_column='hpAreaTitle', max_length=20)),
                ('hpschcatenm', models.CharField(db_column='hpSchCateNm', max_length=20)),
                ('mcatenm', models.CharField(db_column='mcateNm', max_length=20)),
                ('cmt', models.CharField(blank=True, max_length=30, null=True)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=11)),
                ('lng', models.DecimalField(decimal_places=7, max_digits=11)),
                ('addr', models.CharField(max_length=100)),
                ('addr2', models.CharField(blank=True, max_length=100, null=True)),
                ('hundredyn', models.CharField(blank=True, db_column='hundredYn', max_length=2, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('likecnt', models.IntegerField(blank=True, db_column='likeCnt', null=True)),
                ('bookmarkcnt', models.IntegerField(blank=True, db_column='bookmarkCnt', null=True)),
                ('viewcnt', models.IntegerField(blank=True, db_column='viewCnt', null=True)),
                ('callcnt', models.IntegerField(blank=True, db_column='callCnt', null=True)),
                ('sharecnt', models.IntegerField(blank=True, db_column='shareCnt', null=True)),
                ('chkincnt', models.IntegerField(blank=True, db_column='chkinCnt', null=True)),
                ('rpcnt', models.IntegerField(blank=True, db_column='rpCnt', null=True)),
                ('parkingyn', models.CharField(blank=True, db_column='parkingYn', max_length=2, null=True)),
                ('valletyn', models.CharField(blank=True, db_column='valletYn', max_length=2, null=True)),
                ('photo', models.CharField(blank=True, max_length=100, null=True)),
                ('menu', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_1', models.CharField(max_length=20)),
                ('keyword_2', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_3', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_4', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_5', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_6', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_7', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_8', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_9', models.CharField(blank=True, max_length=20, null=True)),
                ('keyword_10', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiksinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.TextField(blank=True, null=True)),
                ('place_tag1', models.TextField(blank=True, null=True)),
                ('place_tag2', models.TextField(blank=True, null=True)),
                ('place_tag3', models.TextField(blank=True, null=True)),
                ('place_tag4', models.TextField(blank=True, null=True)),
                ('place_tag5', models.TextField(blank=True, null=True)),
                ('place_location', models.TextField(blank=True, null=True)),
                ('place_category', models.TextField(blank=True, null=True)),
                ('place_near_station', models.TextField(blank=True, null=True)),
                ('place_contents_info', models.TextField(blank=True, null=True)),
                ('place_address', models.TextField(blank=True, null=True)),
                ('place_convenience', models.TextField(blank=True, null=True)),
                ('place_telephone', models.TextField(blank=True, null=True)),
                ('place_route', models.TextField(blank=True, null=True)),
                ('place_homepage', models.TextField(blank=True, null=True)),
                ('place_drink', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'siksin_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiksinReview',
            fields=[
                ('siksin_review_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.TextField(blank=True, null=True)),
                ('place_review_content', models.TextField(blank=True, null=True)),
                ('place_reviewer', models.TextField(blank=True, null=True)),
                ('place_review_score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'siksin_review',
                'managed': False,
            },
        ),
    ]
