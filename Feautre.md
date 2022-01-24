-Features and Brain Storming
----------------------------------
Anime Scape is a small app that scrapes data from different Anime websites and notifies you of the anime that you want to be reminded on.

-What it should do is make a Get request to list all the anime on the selected website. For now, lets use Animixplay.com. 
-Since the website used pagination, it has to scrape each page from A to Z so we need to figure out have to grab from each page. 
-When selecting each anime, we need to grab its URL and scrap the data from there. 
-Now, these anime must be ongoing in order for it to work so. The best idea would be to check their status and if they are ongoing, notify the person, else tell them that this anime is already completed. 
-If it is ongoing, then look for the <div id="playcounter"> and display the contents. 
This is the gist of what it should do.
-The database needs to save the name of the anime, the current number of episodes, and the status to make sure it is still ongoing, we can also have a Dub or Sub to filter anime from Dubbed and Subbed. So Dubbed is True, Subbed is False.

#React Native Portion
---------------------------------
-The React Native version is that this has to be a mobile app, so it must display a list and a search engine. This search engine has to hold the anime that you want to keep track of.  
-Extras
----------------------------------
-We can have it constantly check behind the seens and notify each day. If the Episode total increases, we can display that the anime has aired. 
-We can also have the list of anime be a link to the latest episode. So I.E: https://animixplay.to/v1/kimetsu-no-yaiba-yuukaku-hen/ep7 <-- It there should be a /${episode}. Its possible to add the Episode Number so that as that number increases, it goes to that new episode. 
-Animixplay also holds the anime you are currently watching, we can have the list keep track of the anime you are currently watching and increment it once the website increments for you 
