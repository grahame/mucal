import argparse
import requests
import icalendar


def get_ical(url):
    response = requests.get(url)
    assert response.status_code == 200
    return response.text


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("outfile")
    args = parser.parse_args()

    def same_day(c):
        ds = c["DTSTART"].dt
        de = c["DTEND"].dt
        return (de - ds).days == 0

    cal = icalendar.Calendar.from_ical(get_ical(args.url))
    cal.subcomponents = [c for c in cal.subcomponents if same_day(c)]

    with open(args.outfile, "wb") as fd:
        fd.write(cal.to_ical())
