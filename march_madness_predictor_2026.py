import requests                                                                            #Import libraries
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
#import html5lib


url1 = "https://www.sports-reference.com/cbb/seasons/men/2026-school-stats.html"                                        # Basic school stats (3PT%)
url2 = "https://www.sports-reference.com/cbb/seasons/men/2026-advanced-school-stats.html"                               # Advanced School stats (Pace)
url3 = "https://www.sports-reference.com/cbb/seasons/men/2026.html"                                                     # Season summary (regular season and conf champs)
url4 = "https://kenpom.com/"                                                                                            # KenPom stats (Net Rtg, OffRtg, DefRtg, Rank)


"""Scrape website data to local files"""

data1 = requests.get(url1)
with open("basic_stats.html", "w+") as f1:
    f1.write(data1.text)

data2 = requests.get(url2)
with open("advanced_stats.html", "w+") as f2:
    f2.write(data2.text)

""" data3 = requests.get(url3)                                                                                          # Keeps returning UnicodeEncodeError: 'charmap codec can't encode character '\x87'
with open("summary_stats.html", "w+") as f3:
    f3.write(data3.text) """

data4 = requests.get(url4)
with open("kenpom_stats.html", "w+") as f4:
    f4.write(data4.text)

"""Clean and format tables"""

'''Basic stats cleaning'''

with open("basic_stats.html") as f1:                                                                                    #Opens html
    page1 = f1.read()
soup1 = BeautifulSoup(page1, "html.parser") 
soup1.find('tr', class_= "over_header").decompose()                                                                     # Removes over header
soup1.find('tr', class_= "thead").decompose()                                                                           # Removes extra headers within table
stats_html1 = soup1.find_all(id = "basic_school_stats")                                                                 # Returns just the table from the html
basic_stats = pd.read_html(str(stats_html1))[0]                                                                         # Reads html table into pandas as a string, [0] returns first element in list which is the table

simple_bs = basic_stats.iloc[:, [1, 27]]                                                                                # Creates new variable containing school name & 3PT%

'''Advanced stats cleaning'''

with open("advanced_stats.html") as f2:
    page2 = f2.read()
soup2 = BeautifulSoup(page2, "html.parser")
soup2.find('tr', class_= "over_header").decompose()                                                                     #Cleans table of extra rows
soup2.find('tr', class_= "over_header thead").decompose()
soup2.find('tr', class_= "thead").decompose()
stats_html2 = soup2.find_all(id = "adv_school_stats")
adv_stats = pd.read_html(str(stats_html2))[0]
simple_as = adv_stats.loc[:, ['School', 'Pace']]                                                                        # Creates new list of schools and pace

'''KenPom stats cleaning'''

kenpom_stats = pd.read_csv("kenpom_stats.csv")
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Alabama St.', 'Alabama State')                                     # Start changing names to match BBReference
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Albany', 'Albany (NY)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Alcorn St.', 'Alcorn State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Appalachian St.', 'Appalachian State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Arizona St.', 'Arizona State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Arkansas Pine Bluff', 'Arkansas-Pine Bluff')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Arkansas St.', 'Arkansas State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Ball St.', 'Ball State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Bethune Cookman', 'Bethune-Cookman')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Boise St.', 'Boise State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('BYU', 'Brigham Young')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Cal Baptist', 'California Baptist')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Cal St. Bakersfield', 'Cal State Bakersfield')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Cal St. Fullerton', 'Cal State Fullerton')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Central Connecticut', 'Central Connecticut State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Charleston', 'College of Charleston')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Chicago St.', 'Chicago State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Cleveland St.', 'Cleveland State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Colorado St.', 'Colorado State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Coppin St.', 'Coppin State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('CSUN', 'Cal State Northridge')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Delaware St.', 'Delaware State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('East Tennessee St.', 'East Tennessee State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Fairleigh Dickinson', 'FDU')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('FIU', 'Florida International')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Florida St.', 'Florida State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Fresno St.', 'Fresno State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Gardner Webb', 'Gardner-Webb')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Georgia St.', 'Georgia State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Grambling St.', 'Grambling')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Idaho St.', 'Idaho State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Illinois Chicago', 'Illinois-Chicago')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Illinois St.', 'Illinois State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Indiana St.', 'Indiana State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Iowa St.', 'Iowa State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Jackson St.', 'Jackson State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Jacksonville St.', 'Jacksonville State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Kansas St.', 'Kansas State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Kennesaw St.', 'Kennesaw State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Kent St.', 'Kent State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('LIU', 'Long Island University')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Long Beach St.', 'Long Beach State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Louisiana Monroe', 'Louisiana-Monroe')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Loyola Chicago', 'Loyola (IL)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Loyola MD', 'Loyola (MD)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('LSU', 'Louisiana State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Maryland Eastern Shore', 'Maryland-Eastern Shore')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('McNeese', 'McNeese State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Miami FL', 'Miami (FL)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Miami OH', 'Miami (OH)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Michigan St.', 'Michigan State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Mississippi St.', 'Mississippi State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Mississippi Valley St.', 'Mississippi Valley State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Missouri St.', 'Missouri State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Montana St.', 'Montana State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Morehead St.', 'Morehead State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Morgan St.', 'Morgan State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Murray St.', 'Murray State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('N.C. State', 'NC State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Nebraska Omaha', 'Omaha')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('New Mexico St.', 'New Mexico State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Nicholls', 'Nicholls State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Norfolk St.', 'Norfolk State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('North Dakota St.', 'North Dakota State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Northwestern St.', 'Northwestern State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Ohio St.', 'Ohio State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Oklahoma St.', 'Oklahoma State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Oregon St.', 'Oregon State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Penn', 'Pennsylvania')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Penn St.', 'Penn State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Portland St.', 'Portland State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Prairie View A&M', 'Prairie View')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Queens', 'Queens (NC)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Sacramento St.', 'Sacramento State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Saint Francis', 'Saint Francis (PA)')
kenpom_stats['Team'] = kenpom_stats['Team'].replace("Saint Mary's", "Saint Mary's (CA)")
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Sam Houston St.', 'Sam Houston')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('San Diego St.', 'San Diego State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('San Jose St.', 'San Jose State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('SIUE', 'SIU Edwardsville')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('SMU', 'Southern Methodist')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('South Carolina St.', 'South Carolina State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('South Dakota St.', 'South Dakota State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Southeast Missouri', 'Southeast Missouri State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Southern Miss', 'Southern Mississippi')
kenpom_stats['Team'] = kenpom_stats['Team'].replace("St. John's", "St. John's (NY)")
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Tarleton St.', 'Tarleton State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Tennessee Martin', 'Tennessee-Martin')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Tennessee St.', 'Tennessee State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Texas A&M Corpus Chris', 'Texas A&M-Corpus Christi')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Texas St.', 'Texas State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('UMass Lowell', 'Massachusetts-Lowell')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('UMBC', 'Maryland-Baltimore County')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('UNLV', 'Nevada-Las Vegas')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('USC', 'Southern California')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('USC Upstate', 'South Carolina Upstate')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('UT Rio Grande Valley', 'Texas-Rio Grande Valley')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Utah St.', 'Utah State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('VCU', 'Virginia Commonwealth')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Washington St.', 'Washington State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Weber St.', 'Weber State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Wichita St.', 'Wichita State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Wright St.', 'Wright State')
kenpom_stats['Team'] = kenpom_stats['Team'].replace('Youngstown St.', 'Youngstown State')
kenpom_clean = kenpom_stats.dropna()
simple_kp = kenpom_clean.loc[:, ['Rk', 'Team', 'NetRtg', 'ORtg', 'DRtg']]
simple_kp = simple_kp.rename(columns={'Team': 'School'})
simple_kp.to_csv("kenpom_cleaned.csv")


"""Combine Lists"""

combined_stats = pd.merge(simple_bs, simple_as, on='School', how='inner')
school_drop = combined_stats[combined_stats['School'] == 'School'].index                                                   # Cleans extra 'school' value from school name column
combined_stats.drop(school_drop, inplace = True)
totals_drop = combined_stats[combined_stats['3P%'] == 'Totals'].index
combined_stats.drop(totals_drop, inplace = True)
combined_stats.to_csv("combined_stats.csv")
all_stats = pd.merge(combined_stats, simple_kp, on='School', how='outer')
all_stats.to_csv("NCAA_stats_2026.csv")