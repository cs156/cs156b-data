# International data

## Getting started
If you are beginning international data analysis, an excellent place to start is `aggregated_our_world_in_data.csv`, which includes COVID-19 data per country and helpful related variables (demographics, health, etc.) all cleaned and organized with ISO variables.


Summary:
* `aggregated_our_world_in_data.csv` collects all relevant data from Our World in Data (compiled by quantummind and thohoff).
* `countries_regional_codes.csv` gives a mapping between country names and their respective alpha and numeric country codes. Standard protocol is to use `alpha-3` as the key (i.e United States of America -> USA). Source: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes. 


## `covid`

### `our_world_in_data`

`full_data.csv` contains data from the ECDC scraped from https://ourworldindata.org/coronavirus.

Compiled by thohoff


## `demographics`

Country-level 1960-now demographic data on age.

Source: UN Population Division, scraped from https://ourworldindata.org/age-structure.
Summary:
* `age-dependency-ratio-old.csv`: ratio of people over 64 to people 15-64 years
* `age-dependency-ratio-young-of-working-age-population.csv`: ratio of people under 15 to people 15-64 years
* `median-age.csv`: median age
* `share-of-the-population-that-is-70-years-and-older.csv`: population >=70 years old

Compiled by quantummind


## `health`

Country-level 1960-now data of conditions related to COVID-19 deaths and hospitals.

Source: World Bank, Global Burden of Disease Study 2017.
Summary:
* `hospital-beds-per-1000-people.csv`: hospital beds per 1000 people. https://ourworldindata.org/coronavirus
* `physicians-per-1000-people.csv`: physicians per 1000 people. https://ourworldindata.org/coronavirus
* `pneumonia-death-rates-age-standardized.csv`: pneumonia death rates per 100,000 individuals. https://ourworldindata.org/pneumonia
* `share-deaths-heart-disease.csv`: share of deaths caused by heart disease. https://ourworldindata.org/grapher/share-deaths-heart-disease
* `share-of-adults-who-smoke.csv`: share of adults who smoke. https://ourworldindata.org/smoking

Compiled by quantummind
