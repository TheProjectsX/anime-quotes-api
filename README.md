# Anime Quotes API

Get Anime quotes by using this API! This is an Unofficial Implementation of Official [Anime Character Database](https://www.animecharactersdatabase.com/api_series_characters.php) API

## Story:

I wan working on my [Anime Kingdom](https://) website Project. But I could not find any Free Anime Character Quotes API / Module. So what? We created one by Ourselves! We are Programmers After all!

## Methods Available:

-   getAnimeByQuery
-   getCharactersByAnimeId
-   getCharactersByQuery
-   getCharacterById
-   getCharacterQuotesById

## Usages:

```python
import anime_quotes as api

anime = api.getAnimeByQuery("naruto shippuden")

characters = api.getCharactersByAnimeId("100053")

characters = api.getCharactersByQuery("naruto")

character = api.getCharacterById("7861")

quotes = api.getCharacterQuotesById("7861")
```

## Parameters:

The main `getCharacterQuotesById` Function has 3 parameters:

-   id : Character ID
-   skip : How many Quotes to Skip (Numeric, Default = 0) [Unofficial - Not included in the Official API]
-   limit : How many Quotes to Get (Numeric, Default = 20). You can use `None` as value to get all the Quotes available [Unofficial - Not included in the Official API]
