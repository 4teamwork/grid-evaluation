import random
from datetime import timedelta
from datetime import date
import json


NUM_RECORDS = 10000

EARLIEST_DATE = date(2010, 1, 1)

PUBLIC_TRIAL = [
    'Nicht gepr\xc3\xbcft',
    'Nicht \xc3\xb6ffentlich',
    'Eingeschr\xc3\xa4nkt \xc3\xb6ffentlich',
    '\xc3\x96ffentlich',
]

AUTHORS = [
    'David Erni',
    'Jonas Baumann',
    'Lukas Graf',
    'Matthias Leimgruber',
    'Pascal Habegger',
    'Philippe Gross',
]


PERSONS_FIRSTNAMES = [
    'Hans',
    'Stefan',
    'Tobias',
    'Patrick',
    'Franz',
    'Urs',
    'Jakob',
    'Christian',
    'Thomas',
]


PERSONS_LASTNAMES = [
    'Muster',
    'Frischknecht',
    'Maurer',
    'Meier',
    'Landholt',
    'Zimmermann',
    'Bossard']

TITLE_TEMPLATES = [
    'Antrag von {person} betreffend {obj} {location}',
    'Beschwerde von {person} betreffend {obj} {location}',
    'Interpellation von {person} bez\xc3\xbcglich {obj} {location}',
    'Motion von {person} betreffend {obj} {location}',
    'Anfrage von {person} betreffend {obj} {location}',
    'Stellungnahme von {person} bez\xc3\xbcglich {obj} {location}',
]

OBJS = [
    'Schulhaus',
    'Kirche',
    'Garage',
    'Restaurant',
    'Spielplatz',
    'Kreuzung',
    'Einfamilienhaus',
    'Br\xc3\xbccke',
]

STREETS = [
    'an der Murtenstr.',
    'an der Marktgasse',
    'an der Weissensteinstr.',
    'an der Bahnhofstr.',
    'an der Seftigenstr.',
    'an der Grabenstr.',
    'an der Spitalgasse',
    'an der Engehaldestr.',
]

PLACES = [
    'am Bahnhofplatz',
    'am Waisenhausplatz',
    'am Bundesplatz',
    'am B\xc3\xa4rengraben',
    'am C\xc3\xa4cilienplatz',
]


def random_public_trial():
    return random.choice(PUBLIC_TRIAL)


def random_location():
    place = random.choice((0, 1))
    if place:
        location = random.choice(PLACES)
    else:
        num = random.choice(range(1, 100))
        location = "%s %s" % (random.choice(STREETS), num)
    return location


def random_obj():
    return random.choice(OBJS)


def random_person():
    firstname = random.choice(PERSONS_FIRSTNAMES)
    lastname = random.choice(PERSONS_LASTNAMES)
    return "%s %s" % (firstname, lastname)


def random_author():
    return random.choice(AUTHORS)


def random_date():
    range_days = (date.today() - EARLIEST_DATE).days
    day_offset = random.randint(1, range_days)
    d = EARLIEST_DATE + timedelta(days=day_offset)
    return d.isoformat()


def random_title():
    person = random_person()
    obj = random_obj()
    location = random_location()
    template = random.choice(TITLE_TEMPLATES)
    title = template.format(person=person,
                            obj=obj,
                            location=location)
    return title


records = []
for i in range(1, NUM_RECORDS + 1):
    record = dict(
        sequence_number=i,
        title=random_title(),
        author=random_author(),
        document_date=random_date(),
        receipt_date=random_date(),
        delivery_date=random_date(),
        checked_out=random_author(),
        subdossier='',
        public_trial=random_public_trial(),
    )
    records.append(record)

print json.dumps(records,
                 sort_keys=True,
                 indent=4,
                 separators=(',', ': '))
