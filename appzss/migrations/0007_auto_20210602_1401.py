# Generated by Django 3.2.3 on 2021-06-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appzss', '0006_auto_20210602_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(choices=[('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Afghanistan', 'Afghanistan'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Anguilla', 'Anguilla'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('Samoa (American)', 'Samoa (American)'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Åland Islands', 'Åland Islands'), ('Azerbaijan', 'Azerbaijan'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('St Barthelemy', 'St Barthelemy'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei'), ('Bolivia', 'Bolivia'), ('Caribbean NL', 'Caribbean NL'), ('Brazil', 'Brazil'), ('Bahamas', 'Bahamas'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Congo (Dem. Rep.)', 'Congo (Dem. Rep.)'), ('Central African Rep.', 'Central African Rep.'), ('Congo (Rep.)', 'Congo (Rep.)'), ('Switzerland', 'Switzerland'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Cook Islands', 'Cook Islands'), ('Chile', 'Chile'), ('Cameroon', 'Cameroon'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Cape Verde', 'Cape Verde'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('Western Sahara', 'Western Sahara'), ('Eritrea', 'Eritrea'), ('Spain', 'Spain'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands', 'Falkland Islands'), ('Micronesia', 'Micronesia'), ('Faroe Islands', 'Faroe Islands'), ('France', 'France'), ('Gabon', 'Gabon'), ('Britain (UK)', 'Britain (UK)'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('French Guiana', 'French Guiana'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greenland', 'Greenland'), ('Gambia', 'Gambia'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('South Georgia & the South Sandwich Islands', 'South Georgia & the South Sandwich Islands'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island & McDonald Islands', 'Heard Island & McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Iraq', 'Iraq'), ('Iran', 'Iran'), ('Iceland', 'Iceland'), ('Italy', 'Italy'), ('Jersey', 'Jersey'), ('Jamaica', 'Jamaica'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Comoros', 'Comoros'), ('St Kitts & Nevis', 'St Kitts & Nevis'), ('Korea (North)', 'Korea (North)'), ('Korea (South)', 'Korea (South)'), ('Kuwait', 'Kuwait'), ('Cayman Islands', 'Cayman Islands'), ('Kazakhstan', 'Kazakhstan'), ('Laos', 'Laos'), ('Lebanon', 'Lebanon'), ('St Lucia', 'St Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Libya', 'Libya'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova', 'Moldova'), ('Montenegro', 'Montenegro'), ('St Martin (French)', 'St Martin (French)'), ('Madagascar', 'Madagascar'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Myanmar (Burma)', 'Myanmar (Burma)'), ('Mongolia', 'Mongolia'), ('Macau', 'Macau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldives', 'Maldives'), ('Malawi', 'Malawi'), ('Mexico', 'Mexico'), ('Malaysia', 'Malaysia'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Philippines', 'Philippines'), ('Pakistan', 'Pakistan'), ('Poland', 'Poland'), ('St Pierre & Miquelon', 'St Pierre & Miquelon'), ('Pitcairn', 'Pitcairn'), ('Puerto Rico', 'Puerto Rico'), ('Palestine', 'Palestine'), ('Portugal', 'Portugal'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Solomon Islands', 'Solomon Islands'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Singapore', 'Singapore'), ('St Helena', 'St Helena'), ('Slovenia', 'Slovenia'), ('Svalbard & Jan Mayen', 'Svalbard & Jan Mayen'), ('Slovakia', 'Slovakia'), ('Sierra Leone', 'Sierra Leone'), ('San Marino', 'San Marino'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('South Sudan', 'South Sudan'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('El Salvador', 'El Salvador'), ('St Maarten (Dutch)', 'St Maarten (Dutch)'), ('Syria', 'Syria'), ('Eswatini (Swaziland)', 'Eswatini (Swaziland)'), ('Turks & Caicos Is', 'Turks & Caicos Is'), ('Chad', 'Chad'), ('French Southern & Antarctic Lands', 'French Southern & Antarctic Lands'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('East Timor', 'East Timor'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('Turkey', 'Turkey'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Ukraine', 'Ukraine'), ('Uganda', 'Uganda'), ('US minor outlying islands', 'US minor outlying islands'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City', 'Vatican City'), ('St Vincent', 'St Vincent'), ('Venezuela', 'Venezuela'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Vietnam', 'Vietnam'), ('Vanuatu', 'Vanuatu'), ('Wallis & Futuna', 'Wallis & Futuna'), ('Samoa (western)', 'Samoa (western)'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50),
        ),
    ]