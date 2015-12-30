from __future__ import unicode_literals

from django.db import models

# author - emmanuel okiria
# email - emmaokiria@gmail.com
# phone - +256790790184


class opportunity(models.Model):
    TYPE = (
        ('Existing Business', 'Existing Business'),
        ('New Business', 'New Business'),
    )

    STAGE = (
        ('Qualification', 'Qualification'),
        ('Needs Analysis', 'Needs Analysis'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Closed Won', 'Closed Won'),
        ('Closed Lost', 'Closed Lost'),
    )

    REASON = (
        ('Lost to Competitor', 'Lost to Competitor'),
        ('No Budget/Lost Funding', 'No Budget/Lost Funding'),
        ('No Decision/ Non-Responsive', 'No Decision/ Non-Responsive'),
        ('Price', 'Price'),
        ('Others', 'Others'),
    )

    SOURCE = (
        ('Advertisement', 'Advertisement'),
        ('Customer Event', 'Customer Event'),
        ('Employee Referral', 'Employee Referral'),
        ('Google AdWords', 'Google AdWords'),
    )
    opportunity_name = models.CharField('Opportunity Name', max_length= 50)
    opportunity_owner = models.CharField('Opportunity Owner', max_length= 50)
    account_name = models.CharField('Account Name', max_length= 50)
    close_date = models.DateField('Close Date', auto_now=False, auto_now_add=False)
    type = models.CharField('Type', max_length= 50, choices= TYPE)
    stage = models.CharField('Stage', max_length= 50, choices= STAGE)
    primary_campaign_source = models.CharField('Primary Campaign Source', max_length= 100)
    amount = models.DecimalField('Amount', max_digits= 10, decimal_places= 2)
    loss_reason = models.CharField('Loss Reason', max_length= 50, choices= REASON)
    next_step = models.CharField('Next Step', max_length= 50)
    lead_source = models.CharField('Lead Source', max_length=20, choices=SOURCE)
    description = models.CharField('Opportunity Description', max_length=200)