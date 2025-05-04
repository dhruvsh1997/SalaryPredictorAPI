import os
import pickle
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import SalaryPredictionInputSerializer

@api_view(['POST'])
def predict_salary(request):
    serializer = SalaryPredictionInputSerializer(data=request.data)

    if serializer.is_valid():
        model_name = serializer.validated_data['model_name'].lower().strip()
        experience = serializer.validated_data['experience_year']

        model_path = os.path.join(settings.MEDIA_ROOT, 'Models', f'{model_name}.pkl')

        if not os.path.exists(model_path):
            return Response({"error": f"Model '{model_name}' not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            with open(model_path, 'rb') as file:
                model = pickle.load(file)

            salary_pred = model.predict(np.array([[experience]]))
            return Response({
                "model": model_name,
                "experience_year": experience,
                "predicted_salary": float(salary_pred[0])
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
