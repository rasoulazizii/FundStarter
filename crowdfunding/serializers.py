from rest_framework import serializers
from .models import Campaign, Donation
from django.utils import timezone


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
        fields = '__all__'
        read_only_fields = [
            'backer'
        ]
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('amount most be greater than zero')
        return value

    def validate(self, attrs):
        campaign = attrs['campaign']
        user = self.context['request'].user

        if campaign.owner == user:
            raise serializers.ValidationError('you can not donta your own campaign')
        
        if campaign.deadline < timezone.now():
            raise serializers.ValidationError('this campaign has ended.')
        
        return attrs