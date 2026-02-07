from rest_framework import serializers
from .models import Campaign, Donation
from django.utils import timezone


class CampaignSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Campaign
        fields = [
            'id', 'owner', 'title', 'description', 'image',
            'target_amount', 'current_amount', 'progress_percentage', 
            'deadline', 'created_at'
        ]
        read_only_fields = ['owner', 'current_amount', 'created_at']

    def get_progress_percentage(self, obj):
        if obj.target_amount > 0:
            percentage = (obj.current_amount / obj.target_amount) * 100
            return round(percentage, 2)
        return 0


class DonationSerializer(serializers.ModelSerializer):
    campaign_title = serializers.ReadOnlyField(source='campaign.title')
    backer_email = serializers.ReadOnlyField(source='backer.email')

    class Meta:
        model = Donation
        fields = [
            'id', 'campaign', 'campaign_title', 
            'backer', 'backer_email', 'amount', 'created_at'
        ]
        read_only_fields = ['backer']
    
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