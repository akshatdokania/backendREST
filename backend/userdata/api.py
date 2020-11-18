from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import UserSerializer
from .models import Userdata
from django.views.decorators.csrf import csrf_exempt

class UserInput(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    def get(self, request):
        id = request.data.get('hospitalid')
        try:
            form = Userdata.objects.get(hospitalid = id)
            return Response('User Exists', 400)
        except:
            return Response(status = 200)



    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            epicount, labcount, vitalcount, count, message = checkparams(serializer.data)
            return Response({"epicount": epicount,"labcount": labcount, "vitalcount": vitalcount,"count": count, "message": message}, 200)
        return Response(serializer.errors, 400)

class UserDetail(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def get(self, request, id):
        try:
            model= Userdata.objects.get(hospitalid = id)
        except Userdata.DoesNotExist:
            return Response('User Details Not Found', 404)
        serializer = UserSerializer(model)
        return Response(serializer.data, 200)

    def put(self, request, id):
        try:
            model, created = Userdata.objects.get_or_create(hospitalid = id)
        except Userdata.DoesNotExist:
            return Response('User Detail Not Found', 404)
        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            epicount, labcount, vitalcount, count, message = checkparams(serializer.data)
            return Response({"epicount": epicount,"labcount": labcount, "vitalcount": vitalcount,"count": count, "message": message}, 200)
        return Response(serializer.errors, 400)

class UserTrial(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        epicount, labcount, vitalcount, count, message = checkparams(request.data)
        data = {"epicount": epicount,"labcount": labcount, "vitalcount": vitalcount,"count": count, "message": message}
        return Response(data, 200)

def checkparams(params):
        total = 0
        total_param = 1
        count_epi = 0
        count_vital = 0
        count_lab = 0
        riskMessage = "Risk returned null"
        if int(params['age']) > 55:
            counter += 1
        if 'drpdownValue' in params:
            if 'H/O DM/(HbA1c>7.6)' in params['drpdownValue']:
                count_epi += 1
                total_param += 1
            if 'H/O PULMONARY DISEASE' in params['drpdownValue']:
                count_epi += 1
                total_param += 1
            if 'H/O CKD' in params['drpdownValue']:
                count_epi += 1
                total_param += 1
            if 'H/O HCN' in params['drpdownValue']:
                count_epi += 1
                total_param += 1
            if 'H/O DM/(HbA1c>7.6)' in params['drpdownValue']:
                count_epi += 1
                total_param += 1
            if 'IMMUNOSUPRESSION' in params['drpdownValue']:
                count_epi +=  1
                total_param += 1
        if 'resrate' in params:
            if int(params['resrate']) > 24:
                count_vital += 1
                total_param += 1
        if 'heartrate' in params:
            if int(params['heartrate']) > 125:
                count_vital += 1
                total_param += 1
        if 'spo' in params:
            if int(params['spo']) < 90:
                count_vital += 1
                total_param += 1
        if 'ddimer' in params:
            if int(params['ddimer']) > 1000:
                count_lab += 1
                total_param += 1
        if 'cpk' in params:
            if int(params['cpk']) > 400:
                count_lab += 1
                total_param += 1
        if 'crp' in params:
            if int(params['crp']) > 100:
                count_lab += 1
                total_param += 1
        if 'ldh' in params:
            if int(params['ldh']) > 245:
                count_lab += 1
                total_param += 1
        if 'tropo' in params:
            if float(params['tropo']) > 0.1:
                count_lab += 1
                total_param += 1
        if 'ferr' in params:
            if int(params['ferr']) > 500:
                count_lab += 1
                total_param += 1
        if 'absolute' in params:
            if float(params['absolute']) < 0.8:
                count_lab += 1
                total_param += 1
        total = count_epi+count_lab+count_vital
        risk = (total/total_param) * 10
        risk = round(risk, 2)
        total_vl = count_lab+count_vital
        if(count_epi>0 and count_vital>0 and count_lab>0):
            riskMessage = "High Risk"
            return count_epi,count_lab,count_vital,risk,riskMessage
        elif(total_vl == 2 and count_lab != 0 and count_vital != 0):
            riskMessage = "Moderate Risk"
            return count_epi,count_lab,count_vital,risk,riskMessage
        elif(total_vl >= 2):
            riskMessage = "High Risk"
            return count_epi,count_lab,count_vital,risk,riskMessage
        elif(count_epi > 0 and (count_lab == 1 or count_vital == 1)):
            riskMessage = "Moderate Risk"
            return count_epi,count_lab,count_vital,risk,riskMessage
        elif(total < 2 or (count_epi > 0 and count_lab == 0 and count_vital == 0)):
            riskMessage = "Low Risk"
            return count_epi,count_lab,count_vital,risk,riskMessage
        return count_epi,count_lab,count_vital,risk,riskMessage
