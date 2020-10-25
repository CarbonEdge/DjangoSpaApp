from rest_framework import serializers

from leads.models import Lead

#lead seriliser
class LeadSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        