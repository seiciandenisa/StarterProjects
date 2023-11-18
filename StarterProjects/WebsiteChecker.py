import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:  # opening the csv file in read mode
        reader = csv.reader(file)  # to use the csv we create a reader object
        for row in reader:  # looping through the reader to get values back
            if 'https://' not in row[1] or 'http://' in row[1]:
                websites.append(f'https://{row[1]}')  # adding https if the list of websites don't have it
            else:
                websites.append(row[1])
        return websites


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


print(get_user_agent())


def get_status_description(status_code: int) -> str:  # getting status description
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value}{value.name}) {value.description}'  # creating the description
    return "Unknown status code"


print(HTTPStatus.BAD_REQUEST.name)
print(HTTPStatus.BAD_REQUEST.value)


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_websites(code))
    except Exception:
        print(f'**Could not get information for this website: "{website}"')


def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agent()

    # looping trough website
    for site in sites:
        check_website(site, user_agent)


if __name__ == '__main__':
    main()


