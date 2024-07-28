from serpapi import GoogleSearch

params = {
    "engine": "google_jobs",
    "q": "barista new york",
    "hl": "en",
    "api_key": "92c25ee62c44d72638b2d2667b2d7f09365033349cff919e774eed8305a4f1e8"
}

search = GoogleSearch(params)
results = search.get_dict()
jobs_results = results["jobs_results"]
