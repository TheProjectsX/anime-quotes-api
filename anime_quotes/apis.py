import requests, json, re
from fake_useragent import UserAgent

## GLOBAL Variables ##

# Base Path
BASE_PATH = "https://www.animecharactersdatabase.com/api_series_characters.php"

# User Agents
userAgent = UserAgent()


# Request Sending Function
def sendRequest(query={}):
    if len(query.keys()) < 1:
        {"success": False, "message": "No Query provided"}

    headers = {"user-agent": userAgent.random}

    response, error = None, None

    try:
        response = requests.get(BASE_PATH, params=query, headers=headers)
    except Exception as e:
        error = str(e)

    if response is None:
        return {"success": False, "message": "Some error occurred", "error": error}

    elif response.text == "-1":
        return {"success": False, "message": "Item not Found"}

    try:
        response = response.json()
    except Exception as e:
        return {
            "success": False,
            "message": "Failed to get Data",
            "serverResponse": response.text,
        }

    returnResponse = {"success": True, "data": response}

    return returnResponse


# Get Anime by Name (Query)
def getAnimeByQuery(query=""):
    """
    Search for Anime using their Name. Try to use Full Name.

    ### Returns in Success:
    ``` json
    {
        "success": true,
        "data": [
            {
                "characters_url": "https://www.animecharactersdatabase.com/api_series_characters.php?anime_id=100053",
                "anime_id": 100053,
                "anime_image": "https://ami.animecharactersdatabase.com/productimages/100053.jpg",
                "anime_name": "Naruto Shippuden"
            },
            {
                "characters_url": "https://www.animecharactersdatabase.com/api_series_characters.php?anime_id=101737",
                "anime_id": 101737,
                "anime_image": "https://ami.animecharactersdatabase.com/productimages/u/5688-1835879050.jpg",
                "anime_name": "Naruto Shippuden: the Movie"
            }
        ]
    }
    ```

    ### Returns in Error:
    ``` json
    {
        "success": false,
        "message": "Item not Found"
    }
    ```

    """

    params = {"anime_q": query}

    returnResponse = sendRequest(params)
    if not returnResponse["success"]:
        return returnResponse

    returnResponse["data"] = returnResponse["data"].get("search_results", [])
    return returnResponse


# Get all Characters of an Anime by ID
def getCharactersByAnimeId(id):
    """
    Get Characters list of an Anime using Anime ID.

    ### Returns in Success:
    ``` json
    {
        "success": true,
        "data": {
            "anime_name": "Naruto",
            "anime_image": "https://ami.animecharactersdatabase.com/productimages/1122.jpg",
            "anime_id": "1122",
            "characters": [
                {
                    "anime_id": 1122,
                    "anime_name": "Naruto",
                    "anime_image": "https://ami.animecharactersdatabase.com/productimages/1122.jpg",
                    "character_image": "https://ami.animecharactersdatabase.com/uploads/chars/thumbs/200/5688-1674579212.jpg",
                    "id": 10905,
                    "gender": "Male",
                    "name": "Naruto Uzumaki",
                    "desc": "Naruto Uzumaki is a character from the Anime Naruto."
                },
            ]
        }
    }
    ```

    ### Returns in Error:
    ``` json
    {
        "success": false,
        "message": "Item not Found"
    }
    ```

    """

    params = {"anime_id": id}

    returnResponse = sendRequest(params)
    if not returnResponse["success"]:
        return returnResponse

    # We don't need any preprocessing fro Character Data
    return returnResponse


# Search Character by Name (Query)
def getCharactersByQuery(query=""):
    """
    Search for Characters using their Name. Try to use Full Name.

    ### Returns in Success:
    ``` json
    {
        "success": true,
        "data": [
            {
                "anime_id": 1122,
                "anime_name": "Naruto",
                "anime_image": "https://ami.animecharactersdatabase.com/productimages/1122.jpg",
                "character_image": "https://ami.animecharactersdatabase.com/uploads/chars/thumbs/200/5688-1674579212.jpg",
                "id": 10905,
                "gender": "Male",
                "name": "Naruto Uzumaki",
                "desc": "Naruto Uzumaki is a character from the Anime Naruto."
            },
        ]
    }
    ```

    ### Returns in Error:
    ``` json
    {
        "success": false,
        "message": "Item not Found"
    }
    ```

    """

    params = {"character_q": query}

    returnResponse = sendRequest(params)
    if not returnResponse["success"]:
        return returnResponse

    returnResponse["data"] = returnResponse["data"].get("search_results", [])
    return returnResponse


# Get Character by ID
def getCharacterById(id):
    """
    Get Character data using Character ID.

    ### Returns in Success:
    ``` json
    {
        "success": true,
        "data": {
            "id": 10905,
            "anime_id": 1122,
            "anime_image": "https://ami.animecharactersdatabase.com/productimages/1122.jpg",
            "character_image": "https://ami.animecharactersdatabase.com/uploads/chars/thumbs/200/5688-1674579212.jpg",
            "origin": "Naruto",
            "gender": "Male",
            "name": "Naruto Uzumaki",
            "desc": "Naruto Uzumaki is a character from the Anime Naruto."
        }
    }
    ```

    ### Returns in Error:
    ``` json
    {
        "success": false,
        "message": "Item not Found"
    }
    ```

    """

    params = {"character_id": id}

    returnResponse = sendRequest(params)
    if not returnResponse["success"]:
        return returnResponse

    # We don't need any preprocessing fro Character Data
    return returnResponse


# Get Anime Character Quotes by Character ID
# Clean Invalid JSON String
def cleanJson(text):
    return re.sub(
        r'\\[^"\\/bfnrtu]|\\u(?![0-9a-fA-F]{4})', "", text.strip().replace('\r\n"', '"')
    )


# Actual Function
def getCharacterQuotesById(id, skip=0, limit=20):
    """
    Get Character Quotes by Id. You can use `skip` to skip some number and `limit` to limit the amount, you can use `None` as limit value to get all the Quotes (These features are unofficial).

    ### Returns in Success:
    ``` json
    {
        "success": true,
        "data": {
            "id": 7861,
            "anime_id": 100053,
            "anime_image": "https://ami.animecharactersdatabase.com/productimages/100053.jpg",
            "character_image": "https://ami.animecharactersdatabase.com/uploads/chars/thumbs/200/5688-1946301974.jpg",
            "origin": "Naruto Shippuden",
            "gender": "Male",
            "name": "Naruto Uzumaki",
            "desc": "Naruto Uzumaki is a character from the Anime Naruto Shippuden.",
            "quotes": [
                {
                    "series": "Naruto Shippuden",
                    "episode": 60,
                    "quote": "Whoa, I was about to get flattened..."
                }
            ],
            "quotes_count": 339
        }
    }
    ```

    ### Returns in Error:
    ``` json
    {
        "success": false,
        "message": "Item not Found"
    }
    ```

    """

    params = {"character_quotes": id}

    returnResponse = sendRequest(params)
    if returnResponse["success"]:
        return returnResponse

    try:
        serverResponse = returnResponse["serverResponse"]
        serverData = json.loads(cleanJson(serverResponse))
    except Exception as e:
        return {"success": False, "message": "Failed to get Data", "error": ""}

    cleanedData = []
    for quote in serverData["quotes"]:
        data = {
            "series": quote.get("SERIES"),
            "episode": quote.get("EPID"),
            "quote": quote.get("SUB_LINE"),
        }
        cleanedData.append(data)

    serverData["quotes_count"] = len(cleanedData)
    serverData["quotes"] = cleanedData[
        skip : limit + skip if limit is not None else None
    ]

    return {"success": True, "data": serverData}
