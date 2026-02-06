from rest_framework import serializers
from .models import Campaign, Donation


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


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = [
            '__all__',
        ]
        read_only_fields = [
            'backer'
        ]
        
