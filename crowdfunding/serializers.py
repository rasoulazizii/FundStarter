from rest_framework import serializers
from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'title', 'description', 'target_amount',
            'current_amount', 'deadline',
        ]
        
        read_only_fields = [
            'owner', 'created_at'
        ]

