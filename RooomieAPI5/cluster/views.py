from django.http import HttpResponse, JsonResponse
from django.db.models.query import QuerySet

# import rpy2
# import rpy2.robjects as robjects

from .models import MemInfo, MemMchInfo, PreDistAnalysis, AfterDistAnalysis, WantnessAnalysis, MchResult
from .defactorize import *

'''
들어오는 유형에 따라 json reponse를 변경해주는 클래스
'''
class TypeManager():
    type=""
    def getType(self):
        return self.type
    def setType(self, type):
        self.type=type
    def compType(self, this_type):
        if self.type == this_type: return True
        else: return False

tm = TypeManager()


'''
RooomieAPI Server 첫화면
'''
def index(request):
    return HttpResponse('This is RooomieAPI Server')


'''
회원 5명 불러오는 메소드
'''
def getMemInfo(request):
    tm.setType("getMemInfo")
    return MemInfo.objects.all()[:5]


'''
추천 리스트 불러오는 메소드: NAME, MAJOR, PHONE,  
'''
def getRecoList(request):
    op = MchResult.objects.filter(STUD_ID=request.GET["STUD_ID"])
    op_stud_id_list=[]
    recoList = []
    for instance in op:
        op_STUD_ID = instance.OP_STUD_ID # 이부분 최종적으로는 STUD_ID->OP_SUTD_ID
        op_info = MemInfo.objects.filter(STUD_ID = op_STUD_ID).get()
        op_mch = MemMchInfo.objects.filter(STUD_ID = op_STUD_ID).get()
        op_stud_id_list.append(op_STUD_ID)
        recoList.append({
            "STUD_ID": request.GET["STUD_ID"],
            "OP_STUD_ID": op_STUD_ID,
            "OP_NAME": op_info.NAME,
            "OP_AGE": op_mch.MY_AGE,
            "OP_MAJOR": op_info.MAJOR,
            "OP_PHONE": op_info.PHONE,
            "OP_GRADE": op_mch.MY_GRADE,
            "OP_CLEAN": df_CLEAN(op_mch.MY_CLEAN),
            "OP_YASIK": df_YASIK(op_mch.MY_YASIK),
            "OP_CHARACTER": df_CHARACTER(op_mch.MY_CHARACTER),
            "OP_OUTSIDE_ACTIVITY": df_OUTACT(op_mch.MY_OUTSIDE_ACTIVITY),
            "OP_FREQ_DRINK": df_FREQ_DRINK(op_mch.MY_FREQ_DRINK),
            "OP_DRINK": df_DRINK(op_mch.MY_DRINK),
            "OP_SMOKE": df_SMOKE(op_mch.MY_SMOKE)
        })
    print(op_stud_id_list)
    print(recoList)
    return JsonResponse(recoList, safe=False)


'''
회원가입 예제 메소드
'''
def postMemberExample(request):
    new_ID = request.POST["ID"]
    new_PWD = request.POST["PWD"]
    new_STUD_ID =    request.POST["STUD_ID"]
    new_NAME =      request.POST["NAME"]
    new_GENDER =    request.POST["GENDER"]
    new_PHONE =     request.POST["PHONE"]
    new_EMAIL =     request.POST["EMAIL"]
    MemInfo.objects.create(ID=new_ID, PWD=new_PWD, STU_ID=new_STUD_ID, NAME=new_NAME, GENDER=new_GENDER, PHONE=new_PHONE, EMAIL=new_EMAIL)
    MemInfo.objects.filter(STU_ID=new_STUD_ID).register()

    return JsonResponse([{"ID":"", "PWD":""}])

def listAllUserIDs(request):
    tm.setType("listAllUserIDs")
    return MemInfo.objects.all()

# def signup(request):
#     if request.method == "POST":
#         form = MemInfoForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(request, new_user)
#             return redirect('index')
#     else:
#         form = UserForm()
#         return render(request, 'memo_app/adduser.html', {'form': form})

'''
회원가입 예제 메소드 : ID, PWD
'''
def postMember(request):
    new_ID = request.GET["ID"]
    new_PWD = request.GET["PWD"]
    print("ID: ", new_ID, "PWD: ", new_PWD)
    # MemInfo.objects.create(ID=new_ID)
    return JsonResponse([{"ID":"Good", "PWD":"Good"}], safe=False)


'''
회원가입 메소드 : ID, PWD, NAME, PHONE, EMAIL, STUD_ID
'''
def postMemberAll(request):
    new_ID = request.GET["ID"]
    new_PWD = request.GET["PWD"]
    new_NAME = request.GET["NAME"]
    new_PHONE = request.GET["PHONE"]
    new_EMAIL = request.GET["EMAIL"]
    new_STUD_ID = request.GET["STUD_ID"]
    print("ID: ", new_ID, "PWD: ", new_PWD)

    new_member = MemInfo.objects.create(STUD_ID=new_STUD_ID, ID=new_ID, PWD=new_PWD, NAME=new_NAME, PHONE=new_PHONE, EMAIL=new_EMAIL)
    new_member.register()
    print("Successfully register!")
    return JsonResponse([{"STUD_ID":"Good", "ID":"Good", "PWD":"Good", "NAME":"Good", "PHONE":"Good", "EMAIL":"Good"}], safe=False)


# GENDER, AGE, GRADE, PERSONALITY, CLEANNESS, NIGHTFOOD, OUTSIDEACTIVITY, MAXALCOHOL, ALCOHOLFREQ, SMOKING
def postMatchAll(request):
    new_STUD_ID =               request.GET["STUD_ID"]
    new_MY_GENDER =             f_GENDER(request.GET["MY_GENDER"])
    new_MY_AGE =                request.GET["MY_AGE"]
    new_MY_GRADE =              request.GET["MY_GRADE"]
    new_MY_CLEAN =              f_CLEAN(request.GET["MY_CLEAN"])
    new_MY_YASIK =              f_YASIK(request.GET["MY_YASIK"])
    new_MY_CHARACTER =          f_CHARACTER(request.GET["MY_CHARACTER"])
    new_MY_OUTSIDE_ACTIVITY =   f_OUTACT(request.GET["MY_OUTSIDE_ACTIVITY"])
    new_MY_FREQ_DRINK =         f_FREQ_DRINK(request.GET["MY_FREQ_DRINK"])
    new_MY_DRINK =              request.GET["MY_DRINK"]
    new_MY_SMOKE =              f_SMOKE(request.GET["MY_SMOKE"])
    new_OP_AGE =                request.GET["OP_AGE"]
    new_OP_GRADE =              request.GET["OP_GRADE"]
    new_OP_CLEAN =              f_CLEAN(request.GET["OP_CLEAN"])
    new_OP_YASIK =              f_YASIK(request.GET["OP_YASIK"])
    new_OP_OUTSIDE_ACTIVITY =   f_YASIK(request.GET["OP_OUTSIDE_ACTIVITY"])
    new_OP_FREQ_DRINK =         f_FREQ_DRINK(request.GET["OP_FREQ_DRINK"])
    new_OP_DRINK =              request.GET["OP_DRINK"]
    new_OP_SMOKE =              f_OP_SMOKE(request.GET["OP_SMOKE"])
    new_AGREE_WITH =            f_AGREE_WITH(request.GET["AGREE_WITH"])

    print("성격 : ", new_MY_CHARACTER)
    print("흡연 여부 : ", new_MY_SMOKE)

    new_member=MemInfo.objects.filter(STUD_ID=new_STUD_ID).get()
    print("new member's NAME is ", new_member.NAME, "STUD_ID is ", new_member.STUD_ID)
    new_member_obj = MemMchInfo.objects.create(STUD_ID=MemInfo.objects.filter(STUD_ID=new_STUD_ID).get(),
                                                MY_GENDER=new_MY_GENDER,
                                                MY_AGE=new_MY_AGE,
                                                MY_GRADE=new_MY_GRADE,
                                                MY_CLEAN=new_MY_CLEAN,
                                                MY_YASIK=new_MY_YASIK,
                                                MY_CHARACTER=new_MY_CHARACTER,
                                                MY_OUTSIDE_ACTIVITY=new_MY_OUTSIDE_ACTIVITY,
                                                MY_FREQ_DRINK=new_MY_FREQ_DRINK,
                                                MY_DRINK=new_MY_DRINK,
                                                MY_SMOKE=new_MY_SMOKE,
                                                OP_AGE=new_OP_AGE,
                                                OP_GRADE=new_OP_GRADE,
                                                OP_CLEAN=new_OP_CLEAN,
                                                OP_YASIK=new_OP_YASIK,
                                                OP_OUTSIDE_ACTIVITY=new_OP_OUTSIDE_ACTIVITY,
                                                OP_FREQ_DRINK=new_OP_FREQ_DRINK,
                                                OP_DRINK=new_OP_DRINK,
                                                OP_SMOKE=new_OP_SMOKE,
                                                AGREE_WITH=new_AGREE_WITH)
    new_member_obj.register()

    #추천 알고리즘 작동
    # robjects.r("""
    #     source("00.Load_Data.R")            #DB에서 데이터 load
    #     source("01.Clustering.R")           #insert data into cluster_predistanalysis table & K-modes Clustering
    #     source("02.Calculate_Distance.R")   #Calculate Similarity & extract top 5 & insert data into cluster_afterdistanalysis
    #     source("03.Wantness_Analysis.R")    #Calculate Wantness and Scoring & insert data into cluster_wantnessanalysis and cluster_mchresult
    # """)

    return JsonResponse([{"STUD_ID": "Good",
                            "MY_GENDER": "Good",
                            "MY_AGE": "Good",
                            "MY_GRADE": "Good",
                            "MY_CLEAN": "Good",
                            "MY_YASIK": "Good",
                            "MY_CHARACTER": "Good",
                            "MY_OUTSIDE_ACTIVITY": "Good",
                            "MY_FREQ_DRINK": "Good",
                            "MY_DRINK": "Good",
                            "MY_SMOKE": "Good",
                            "OP_AGE": "Good",
                            "OP_GRADE": "Good",
                            "OP_CLEAN": "Good",
                            "OP_YASIK": "Good",
                            "OP_OUTSIDE_ACTIVITY": "Good",
                            "OP_FREQ_DRINK": "Good",
                            "OP_DRINK": "Good",
                            "OP_SMOKE": "Good",
                            "AGREE_WITH": "Good"
                          }], safe=False)



