from rest_framework import serializers

class SalaryPredictionInputSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    experience_year = serializers.FloatField()
