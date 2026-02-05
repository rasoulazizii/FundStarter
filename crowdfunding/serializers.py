from rest_framework import serializers
from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id', 'owner', 'title', 'description', 
            'target_amount', 'current_amount', 'deadline', 'created_at'
        ]
        
        read_only_fields = [
            'owner', 'created_at'
        ]

