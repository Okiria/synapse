from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models

# author - emmanuel okiria
# email - emmaokiria@gmail.com
# phone - +256790790184
# date - 2/01/2016 - 12:00pm ***


class Opportunity(models.Model):
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
    opportunity_name = models.CharField('Opportunity Name', max_length=50)
    opportunity_owner = models.CharField('Opportunity Owner', max_length=50)
    account_name = models.CharField('Account Name', max_length=50)
    close_date = models.DateField('Close Date', auto_now=False, auto_now_add=False)
    type = models.CharField('Type', max_length=50, choices=TYPE)
    stage = models.CharField('Stage', max_length=50, choices=STAGE)
    primary_campaign_source = models.CharField('Primary Campaign Source', max_length=100)
    amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
    loss_reason = models.CharField('Loss Reason', max_length=50, choices=REASON)
    next_step = models.CharField('Next Step', max_length=50)
    lead_source = models.CharField('Lead Source', max_length=20, choices=SOURCE)
    description = models.CharField('Opportunity Description', max_length=200)


class Lead(models.Model):
    STATUS = (
        ('--None--', '--None--'),
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('Unqualified', 'Unqualified'),
        ('Working', 'Working'),
        ('Nurturing', 'Nurturing'),
    )

    SALUTATION = (
        ('--None--', '--None--'),
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Prof', 'Prof'),
        ('Dr', 'Dr'),
    )

    INDUSTRY = (
        ('--None--', '--None--'),
        ('Telecom', 'Telecom'),
        ('Engineering', 'Engineering'),
        ('Banking', 'Banking'),
    )

    SOURCE = (
        ('--None--', '--None--'),
        ('Advertisement', 'Advertisement'),
        ('Webinar', 'Webinar'),
        ('Trade Show', 'Trade Show'),
        ('Customer Referral', 'Customer Referral'),
        ('Employee Referral', 'Employee Referral'),
        ('Partner', 'Partner'),
    )

    RATING = (
        ('--None--', '--None--'),
        ('Hot', 'Hot'),
        ('Warm', 'Warm'),
        ('Cold', 'Cold'),
    )

    lead_status = models.CharField('Lead Status', max_length=20, choices=STATUS)
    lead_owner = models.CharField('Lead Owner', max_length=50)
    name = models.CharField('Name of Lead', max_length=100)
    salutation = models.CharField('Salutation', max_length=50, choices=SALUTATION)
    first_name = models.CharField('First Name', max_length=100)
    middle_name = models.CharField('Middle Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    website = models.URLField('Website', null=True, blank=True, verify_exists=False)
    title = models.CharField('Title', max_length=100)
    company = models.CharField('Company', max_length=100)
    email = models.EmailField('email', max_length=150, )
    industry = models.CharField('Industry', max_length=100, choices=INDUSTRY)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                    "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Phone Number', validators=[phone_regex], blank=True) # validators should be a list
    number_of_employees = models.IntegerField('Number of Employees')
    mobile = models.CharField('Mobile Number', validators=[mobile_regex], blank=True)
    lead_source = models.CharField('Lead Source', max_length=100, choices=SOURCE)
    rating = models.CharField('Rating', max_length=50, choices=RATING)
    country = models.CharField('Country', max_length=50)
    address = models.CharField('Address', max_length=50)
    street = models.CharField('Street', max_length=50)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50, blank=True, null=True)
    postal_code = models.CharField('Postal Code', max_length=50)

class Account(models.Model):
    ACCOUNT_TYPE = (
        ('--None--', 'None'),
        ('Competitor', 'Competitor'),
        ('Customer', 'Customer'),
        ('Analyst', 'Analyst'),
        ('Press', 'Press'),
        ('Integrator', 'Integrator'),
        ('Investor', 'Investor'),
    )

    INDUSTRY = (
        ('--None--', '--None--'),
        ('Telecom', 'Telecom'),
        ('Engineering', 'Engineering'),
        ('Banking', 'Banking'),
    )

    COUNTRY = (
        ('--None--', '--None--'),
        ('Algeria', 'Algeria'),
        ('Uganda', 'Uganda'),
    )

    account_name = models.CharField('Account Name', max_length=100)
    account_owner = models.CharField('Account Owner', max_length=150)
    type = models.CharField('Account Type', max_length=50, choices=ACCOUNT_TYPE)
    parent_account = models.CharField('Parent Account', max_length=100)
    website = models.URLField('Website', null=True, blank=True, verify_exists=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                    "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Phone Number', validators=[phone_regex], blank=True) # validators should be a list
    description = models.CharField('Description', max_length=200)
    industry = models.CharField('Industry', max_length=50, choices=INDUSTRY)
    employees = models.IntegerField('Employees')
    billing_address = models.CharField('Billing Address', max_length=100)
    street = models.CharField('Street', max_length=50)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50,null=True, blank=True)
    postal_code = models.CharField('Postal Code', max_length=50)
    country = models.CharField('Country', max_length=100, choices=COUNTRY)
    shipping_address = models.CharField('Shipping Address', max_length=50)


class Task(models.Model):

    PRIORITY = (
        ('--None--', '--None--'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    STATUS = (
        ('--None--', '--None--'),
        ('Open', 'Open'),
        ('Completed', 'Completed')
    )
    subject = models.CharField('Subject', max_length=50)
    assigned_to = models.CharField('Assigned To', max_length=100)
    due_date = models.DateField('Due Date')
    name = models.CharField('Name', max_length=50)
    related_to = models.CharField('Related To', max_length=50)
    comment = models.CharField('Comments', max_length=200)
    priority = models.CharField('Priority', max_length=50, choices=PRIORITY)
    status = models.CharField('Status', max_length=50, choices=STATUS)

class Contact(models.Model):
    SALUTATION = (
        ('--None--', '--None--'),
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Prof', 'Prof'),
        ('Dr', 'Dr'),
    )

    COUNTRY = (
        ('--None--', '--None--'),
        ('Algeria', 'Algeria'),
        ('Uganda', 'Uganda'),
    )

    first_name = models.CharField('First Name', max_length=100, blank=False, null=False)
    middle_name = models.CharField('Middle Name', max_length=100, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=100, blank=False, null=False)
    account_name = models.CharField('Account Name', max_length=100)
    contact_owner = models.CharField('Contact Owner', max_length=100)
    report_to = models.CharField('Reports To', max_length=100)
    title = models.CharField('Title', max_length=50)
    department = models.CharField('Department', max_length=50)
    email = models.EmailField('Email Address')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                    "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Phone Number', validators=[phone_regex], blank=True) # validators should be a list
    mobile = models.CharField('Mobile Number', validators=[mobile_regex], blank=True)
    street = models.CharField('Street', max_length=50)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50,null=True, blank=True)
    postal_code = models.CharField('Postal Code', max_length=50)
    country = models.CharField('Country', max_length=100, choices=COUNTRY)

class case(models.Model):
    STATUS = (
        ('--None--', '--None--'),
        ('New', 'New'),
        ('Closed', 'Closed'),
        ('On Hold', 'On Hold'),
        ('Escalated', 'Escalated'),
    )

    TYPE = (
        ('--None', 'None'),
        ('Problem', 'Problem'),
        ('Question', 'Question'),
        ('Feature Request', 'Feature Request'),
    )

    ORIGIN = (
        ('--None--', '--None--'),
        ('Email', 'Email'),
        ('Phone Call', 'Phone Call'),
        ('Web', 'Web'),
    )

    REASON = (
        ('--None--', '--None--'),
        ('User Did not attend training', 'User Did not attend training'),
        ('Complex Functionality', 'Complex Functionality'),
        ('New Problem', 'New Problem'),
        ('Existing Problem', 'Existing Problem'),
        ('Instructions Not Clear', 'Instructions Not Clear'),
    )

    PRIORITY = (
        ('--None--', '--None--'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )
    case_owner = models.CharField('Case Owner', max_length=100)
    contact_name = models.CharField('Contact Name', max_length=100)
    account_name = models.CharField('Account Name', max_length=100)
    status = models.CharField('Case Status', max_length=50, choices=STATUS)
    type = models.CharField('Case Type', max_length=50, choices=TYPE)
    case_origin = models.CharField('Case Origin', max_length=50, choices=ORIGIN)
    case_reason = models.CharField('Case Reason', max_length=50, choices=REASON)
    priority = models.CharField('Priority', max_length=50, choices=PRIORITY)
    subject = models.CharField('Subject', max_length=100)
    description = models.CharField('Description', max_length=200)
    email = models.EmailField('Email Address')
    company = models.CharField('Company', max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Phone Number', validators=[phone_regex], blank=True)