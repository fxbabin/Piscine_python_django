#! /usr/bin/python3

def main():
    d = {
        'Hendrix'   :   '1942',
        'Allman'    :   '1946',
        'King'      :   '1925',
        'Clapton'   :   '1945',
        'Johnson'   :   '1911',
        'Berry'     :   '1926',
        'Vaughan'   :   '1954',
        'Cooder'    :   '1947',
        'Page'      :   '1944',
        'Richards'  :   '1943',
        'Hammett'   :   '1962',
        'Cobain'    :   '1967',
        'Garcia'    :   '1942',
        'Beck'      :   '1944',
        'Santana'   :   '1947',
        'Ramone'    :   '1948',
        'White'     :   '1975',
        'Frusciante':   '1970',
        'Thompson'  :   '1949',
        'Burton'    :   '1939',
    }
    year_musician = {}
    for musician, year in d.items():
        if year not in year_musician:
            year_musician[year] = []
        year_musician[year].append(musician)
    
    for year, musicians in sorted(year_musician.items()):
        for musician in sorted(musicians):
            print(year, musician)


if __name__ == '__main__':
    main()