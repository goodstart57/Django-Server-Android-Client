from django.utils import timezone

from django.db import models

# 회원 개인 정보 테이블
class MemInfo(models.Model):
    STUD_ID =               models.CharField(max_length=9, primary_key=True, unique=True)  # PK
    ID =                    models.CharField(max_length=24, default="0", unique=True)
    PWD =                   models.CharField(max_length=24, default="0")
    NAME =                  models.CharField(max_length=32, null=True)
    GENDER =                models.CharField(max_length=4, null=True)
    PHONE =                 models.CharField(max_length=11, null=True)
    EMAIL =                 models.EmailField(max_length=256, null=True)
    MAJOR =                 models.CharField(max_length=48, null=True, default="통계학과")
    TS_CREATED =            models.DateTimeField(auto_now_add=True)
    TS_UPDATED =            models.DateTimeField(auto_now=True)
    def register(self):
        self.TS_CREATED = timezone.now()
        self.TS_UPDATED = timezone.now()
        self.save()


# 회원 매칭 정보(원본)
class MemMchInfo(models.Model):
    STUD_ID =               models.OneToOneField(MemInfo, on_delete=models.CASCADE, primary_key=True, unique=True, db_column="STUD_ID")  # PK, FK
    #STU_ID =                models.CharField(max_length=9, unique=True, primary_key=True)
    MY_GENDER =             models.CharField(max_length=2)
    MY_AGE =                models.IntegerField()
    MY_GRADE =              models.IntegerField()
    MY_CLEAN =              models.CharField(max_length=48)
    MY_YASIK =              models.CharField(max_length=48)
    MY_CHARACTER =          models.CharField(max_length=256)
    MY_OUTSIDE_ACTIVITY =   models.IntegerField()
    MY_FREQ_DRINK =         models.CharField(max_length=32)
    MY_DRINK =              models.IntegerField()
    MY_SMOKE =              models.CharField(max_length=8)
    OP_AGE =                models.IntegerField()
    OP_GRADE =              models.IntegerField()
    OP_CLEAN =              models.CharField(max_length=48)
    OP_YASIK =              models.CharField(max_length=48)
    OP_OUTSIDE_ACTIVITY =   models.IntegerField()
    OP_FREQ_DRINK =         models.CharField(max_length=32)
    OP_DRINK =              models.IntegerField()
    OP_SMOKE =              models.CharField(max_length=8)
    AGREE_WITH =            models.CharField(max_length=32)
    # TS_UPDATED =            models.DateTimeField(auto_now=True)
    def register(self):
        # self.TS_UPDATED = timezone.now()
        self.save()


# K-mins 알고리즘 군집화 전 데이터
class PreDistAnalysis(models.Model):
    STUD_ID =               models.OneToOneField(MemInfo, on_delete=models.CASCADE, primary_key=True, unique=True, db_column="STUD_ID")  # PK, FK
    #STU_ID =                models.CharField(max_length=9, unique=True, primary_key=True)
    MY_GENDER =             models.IntegerField()
    MY_CHARACTER_F =        models.IntegerField()
    MY_NEW_CLEAN_F =        models.IntegerField()
    MY_YASIK_F =            models.IntegerField()
    MY_OUTSIDE_ACTIVITY_F = models.IntegerField()
    MY_FREQ_DRINK_F =       models.IntegerField()
    MY_DRINK_F =            models.IntegerField()


# K-mins 알고리즘 군집화 후 데이터
class AfterDistAnalysis(models.Model):
    STUD_ID =               models.OneToOneField(MemInfo, on_delete=models.CASCADE, primary_key=True, unique=True, db_column="STUD_ID")  # PK, FK
    OP_STUD_ID =             models.CharField(max_length=9)
    DISTANCE =              models.DecimalField(max_digits=4, decimal_places=4)
    DIST_RNK =              models.IntegerField()


# 상대방 정보 테이블
class WantnessAnalysis(models.Model):
    STUD_ID =               models.OneToOneField(MemInfo, on_delete=models.CASCADE, primary_key=True, unique=True, db_column="STUD_ID")  # PK, FK
    GENDER =                models.IntegerField()
    AGE_SCORE =             models.IntegerField()
    GRADE_SCORE =           models.IntegerField()
    CLEAN_SCORE =           models.IntegerField()
    YASIK_SCORE =           models.IntegerField()
    FREQ_DRINK_SCORE =      models.IntegerField()
    SMOKE_SCORE =           models.IntegerField()
    AGREE_SCORE =           models.IntegerField()
    WANT_RNK =              models.DecimalField(max_digits=4, decimal_places=4)


# 매칭 결과 테이블
class MchResult(models.Model):
    STUD_ID =               models.OneToOneField(MemInfo, on_delete=models.CASCADE, primary_key=True, unique=True, db_column="STUD_ID")  # PK, FK
    OP_STUD_ID =            models.CharField(max_length=9)  # PK, FK
    GROUP =                 models.IntegerField()
    FINAL_RANK =            models.IntegerField()
    TS_UPDATED =            models.DateTimeField(auto_now=True)
