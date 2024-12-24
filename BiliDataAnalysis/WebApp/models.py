from django.db import models
class VideoData(models.Model):
    aid = models.BigIntegerField(primary_key=True, db_comment='主键')
    tid = models.IntegerField(blank=True, null=True, db_comment='视频类型Id')
    tname = models.CharField(max_length=40, blank=True, null=True, db_comment='视频类型')
    title = models.CharField(max_length=255, blank=True, null=True, db_comment='视频标题')
    view = models.BigIntegerField(blank=True, null=True, db_comment='视频播放量')
    short_link_v2 = models.CharField(max_length=255, blank=True, null=True, db_comment='视频链接')
    danmaku = models.BigIntegerField(blank=True, null=True, db_comment='弹幕数量')
    share = models.BigIntegerField(blank=True, null=True, db_comment='转发数量')
    coin = models.BigIntegerField(blank=True, null=True, db_comment='投币数量')
    like = models.BigIntegerField(blank=True, null=True, db_comment='点赞数量')
    favorite = models.BigIntegerField(blank=True, null=True, db_comment='收藏数量')
    reply = models.BigIntegerField(blank=True, null=True, db_comment='评论数量')
    number = models.IntegerField(blank=True, null=True, db_comment='期数')

    class Meta:
        managed = True
        db_table = 'video_data'