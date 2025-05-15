import pandas as pd
from projects.models import Country, OrgUnit, Theme, Project
from django.utils.dateparse import parse_date
import os
import django


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unhabitat_project.settings')
django.setup()

from projects.models import Country, Project, FocalArea, SubCounty

# Load the Excel file
df = pd.read_excel("/workspaces/unhabitat-web-intern/projects/Application Development - Exam Data.xlsx")  

# Iterate through each row and populate the database
for _, row in df.iterrows():
    country_name = row["Country(ies)"].strip()
    country, _ = Country.objects.get_or_create(name=country_name)

    focal_area_name = row["Focal Area"].strip()
    focal_area, _ = FocalArea.objects.get_or_create(name=focal_area_name)

    sub_county_name = row["Sub County"].strip()
    sub_county, _ = SubCounty.objects.get_or_create(name=sub_county_name)

    Project.objects.get_or_create(
        title=row["Project Title"].strip(),
        year=row["Year"],
        country=country,
        focal_area=focal_area,
        sub_county=sub_county,
        implementing_partner=row["Implementing Partner"].strip(),
        donor=row["Donor"].strip(),
        budget=row["Budget (USD)"],
       )

print("Data import complete.")


# Import Countries
for country_name in df['Country(ies)'].dropna().unique():
    Country.objects.get_or_create(name=country_name.strip())

    # Import Org Units
for org_unit_name in df['Org Unit'].dropna().unique():
    OrgUnit.objects.get_or_create(name=org_unit_name.strip())

        # Import Themes
for theme_name in df['Theme'].dropna().unique():
    Theme.objects.get_or_create(name=theme_name.strip())

            # Import Projects
for _, row in df.iterrows():
    country, _ = Country.objects.get_or_create(name=row['Country'].strip())
    org_unit, _ = OrgUnit.objects.get_or_create(name=row['Org Unit'].strip())
    theme, _ = Theme.objects.get_or_create(name=row['Theme'].strip())
                            
    Project.objects.get_or_create(
        name=row['Project Title'].strip(),
        location=row['Location'].strip(),
        budget=row['Budget'],
        start_date=parse_date(str(row['Start Date'])),
        end_date=parse_date(str(row['End Date'])),
        status=row['Approval Status'].strip(),
        country=country,
        org_unit=org_unit,
        theme=theme
          )
                