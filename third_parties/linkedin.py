import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """ "
    Scrape information from Linkedin profiles, Manually scrape the information
    from the Linkedin profile.
    """

    response = requests.get(linkedin_profile_url, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Failed to get response from {linkedin_profile_url}")

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    print(scrape_linkedin_profile(linkedin_profile_url))
