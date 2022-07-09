import pandas as pd
df1 = pd.DataFrame({
    "Countries": ["Brazil", 'USA', 'Denmark', 'Russia', 'France', 'Poland', 'Sweden', 'International'],
    "Amount": [2, 1, 4, 2, 2, 1, 4, 1],
    "Tournament": ['MLG and ESL', 'Eleague', 'IEM, Starladder, Eleague and FACEit', 'PGL', 'Dreamhack', 'ESl',
                   'ESL and Dreamhack', 'PGL']})
df2 = pd.DataFrame({
    "Prize": [2000000, 1000000, 250000],
    "Amount": [2, 10, 7],
    "Year": ['2020 and 2022', '2015 to 2020', '2013 to 2015']

})
df3 = pd.DataFrame({
    "Rating": [1.25, 1.22, 1.15, 1.15, 1.12, 1.11, 1.10, 1.09, 1.08, 1.07],
    "Player": ['s1mple', 'ZywOO', 'device', 'NiKo', 'coldzera', 'oskar',
               'ropz', 'XANTARES', 'Twistzzz', 'kennyS'],
    "Country": ['Ukraine', 'France', 'Denmark', 'Bosnia', 'Brazil', 'Czechia',
                'Estonia', 'Turkiye', 'Canada', 'France']
})
df4 = pd.DataFrame({
    "Weapons": ['ak47', 'm4a1', 'awp', 'm4a1_silencer', 'usp', 'glock', 'deagle',
                'famas', 'other'],
    "Percentage": [34.36, 13.33, 12.19, 7.05, 4.8, 3.54, 3.47, 2.12, 19.3]
})
df5 = pd.DataFrame({
    "Teams": ['Astralis', 'NaVi', 'SK / LG', 'Faze Clan', 'Team Liquid', 'Fnatic', 'Gambit',
              'Big', 'Heroic'],
    "Time": [584, 410, 318, 216, 149, 123, 119, 71, 66]

})
df6 = pd.DataFrame({
    "Weapons": ['ak47', 'm4a1', 'awp', 'm4a1_silencer', 'usp', 'glock', 'deagle',
                'famas'],
    "Damage": [36, 33, 115, 38, 35, 30, 53, 30],
    "Type": ['Automatic Rifle', 'Automatic Rifle', 'Sniper Rifle',
             'Automatic Rifle', 'Pistol', 'Pistol', 'Pistol', 'Automatic Rifle']

})
df7 = pd.DataFrame({
    "Weapons": ['P200, Glock and USP', 'P250', 'Tec-9, CZ75 and 57',
                'Desert Eagle', 'Mac-10 and Nova', 'UMP45', 'MP9', 'P90', 'GALIL', 'FAMAS',
                'AK47', 'M4A1', 'M4A4', 'AUG and SG300', 'AWP', 'M249'],
    "Price": [200, 300, 500, 700, 1050, 1200, 1250, 2350, 1800, 2250, 2700, 2900, 3100, 3300,
              4750, 5200]
})
df8 = pd.DataFrame({
    "Teams": ['Navi', 'Cloud 9', 'Spirit', 'Outsiders', 'ForZe', 'Entropiq', '1WIN', 'K23',
              'FURIA', 'Imperial', 'MIBR', '9Z', '00NATION', 'Pain', 'HUMMER', 'Arctic',
              'FaZe', 'ENCE', 'Vitality', 'G2', 'NIP', 'BIG', 'Heroic', 'Astralis',
              'Team Liquid', 'Complexity', 'Gaimin', 'EG', 'Strife', 'EG.PA',
              'BNB', 'Brazen'],
    "Placement": [8, 7, 6, 5, 4, 3, 2, 1,
                  8, 7, 6, 5, 4, 3, 2, 1,
                  8, 7, 6, 5, 4, 3, 2, 1,
                  8, 7, 6, 5, 4, 3, 2, 1],
    "Region": ['ASIA', 'ASIA', 'ASIA', 'ASIA', 'ASIA', 'ASIA', 'ASIA', 'ASIA',
               'BRAZIL', 'BRAZIL', 'BRAZIL', 'BRAZIL', 'BRAZIL', 'BRAZIL', 'BRAZIL', 'BRAZIL',
               'EUROPE', 'EUROPE', 'EUROPE', 'EUROPE', 'EUROPE', 'EUROPE', 'EUROPE', 'EUROPE',
               'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']
})
df9 = pd.DataFrame({
    "Money": [1400, 1900, 2400, 2900, 3400, 3250, 3250, 3500, 1400, 1900, 2400, 2900, 3400, 3250, 0, 3500],
    "Team": ['CT', 'CT', 'CT', 'CT', 'CT', 'CT', 'CT', 'CT',
             'TR', 'TR', 'TR', 'TR', 'TR', 'TR', 'TR', 'TR'],
    "Status": ['1st Loss', '2nd Loss', '3rd Loss', '4th Loss', '5th Loss +',
               'Win via elimination', 'Win via time', 'Defuse', '1st Loss', '2nd Loss', '3rd Loss',
               '4th Loss', '5th Loss +', 'Win via elimination', 'Time runs out', 'Bomb Detonation']
})
