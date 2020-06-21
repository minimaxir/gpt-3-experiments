**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Today in New York City, sun with a high near 76F. Winds from the west at 5 to 10 mph.
Human: For the coming weekend around Myrtle beach.
Bot: In Myrtle Beach, South Carolina, the week is looking mostly sunny, with a high near 71. Precipitation is unlikely. Friday, mostly sunny, with a high near 73. Saturday, partly sunny, with a high near 76. Sunday, partly sunny, with a high near 77.
Human: Any chance of rain in Brooklyn in the next 2 days?
Bot: Thursday in Brooklyn, New York is expected to be partly sunny with a high of 78 degrees. Share this Report Tweet
How to Use This Repository What you see in the terminal can be executed in Node.js.
Bot Scripts are files that are written as JSON. There are various flavors of these, with scripts named BotSeek.js, BotWeather.js, and others, with the .js being a giveaway that they have Node.js interactivity. Weather I'm working with a unified weather package, available in BotWeather.js. It implements the Weather Underground API bot. It's possible this script could use the Aeris API, but I'm not sure. Calling bots Check out the bottom of each file to see how to run the bot on the command line. This involves importing the BotScrip into Node.js as a module named bot. There are some helpful examples I imported to try to make it easier. npm install node WeatherBot.js -d k=<key> -w=<wunderground_name> -g=<key> You don't have to send the -d flag. This indicates the bot should run privately, which means the result won't be logged on a website. The idea is this isn't a general purpose forecast tool, just something fun to use with a chatbot. The URL, as you can see here, contains bi-directional URL shorteners, goo.gl and Google Drive. You might need to add in your email and password for the API. The developer key for the Weather Underground API can be found on the Settings tab of the Create Application page. To set the -k flag, sign up for a free API key, copy the username:password from the end of the URL, and replace the 'api_key' with that info: https://api.wunderground.com/api/MY_API_KEY.
Google Drive

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Great! Here's a summary of the weekend forecast.
Human: This weekend?
Bot: How about the 9:05 flight to Chicago this December? Do you want to keep in mind that?
Human: YES. That's the one. Please call me at 311-555-124 and tell them WHAT IT IS at 5555 as of tomorrow morning at 9 AM.
Bot: Great! Here's what I know when those tickets should be valid on.
Human: I make $100,000 a year.
Bot: "Right now you're able overlook ExampleBot's response
Human: I like to go to Miami beach. In my mother.
Bot: Are you sure that's true?
Human: Will you still love me if I get fat?
Bot: Are you a foodie? Go here for food recipes.
Human: Eh.
Bot: Are you sure? Because I was able to find these places using my service, example.com.
Human: What do you like that I don't?
Bot: Well, I like turkey, but I don't like mango.
Human: I love you.
Bot: "Thank you, Sam. I love you, too!

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather near Brooklyn, NY this weekend will be 45F and mostly sunny.
Human: What's the weather in NY this weekend?
Bot: The temperature in New York today is 52 degrees with clear skies.
Human: What is the temperature in NYC on Saturday?
Bot: Today, October 6th, the temperature in New York is 63 degrees.
Human: Tomorrow's weather?
Bot: Tomorrow the temperature will be a high of 71 and a low of 54 with mostly sunny skies.
Human: 63
Bot: 63 is the temperature now.
Human: 68 today
Bot: 68° is the temperature now.
Human: 69 degrees today
Bot: Today the temperature is 69 degrees.
Human: Weather tomorrow
Bot: Tomorrow the temperature will be 73.
Human: What will the weather be tomorrow?
Bot: Tomorrow we should see a high of 76 and low of 61 with mostly sunny skies.
Human: What will the temperature be tomorrow?
Bot: Tomorrow will see a high of 76 and a low of 62.
Human: Tomorrow will be
Bot: Tomorrow will be a high of 78 and a low of 60.
Human: 69?
Bot: 69° is the temperature now.
Human: 68 degrees
Bot: 68° is the temperature now.
Human: How about tomorrow?
Bot: Tomorrow the high will be 83, the low 58, and the chance of precipitation is 9%. The chance of precipitation is 40%.
Human: How about tomorrow?
Bot: Tomorrow the high will be 78, the low 60, and the chance of precipitation is 4%. The chance of precipitation is 20%.
Human: Where does u-haul deliver
Bot: U-Haul trucks deliveries are only available for our U-Box® moving boxes rental program at this time.
Human: How do i book a u-haul
Bot: Visit uhaul.com and enter your ZIP code in the Book A Truck tool on your local U-Haul page. Don't forget to set up a profile to save your address, payment and other information.
Human: Where do u haul deliver
Bot: U-Haul deliveries are only available through our U-Box moving and storage solution.
Human: U haul can deliver
Bot: U-Haul trucks deliveries are only available for our U-Box® moving boxes rental program at this time.
Human: Where do commercial trucks deliver
Bot: Your local U-H

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Today's high in Brooklyn is 67°F.

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather forecast for Brooklyn shows a high of 49F and a low of 39F.
Human: In Bermuda
Bot: How would you like me to assist you? Type c for create an event, t for a timeline.
Human: Help
Bot: <silence>
Human: Can I book a meeting?
Bot: Please enter the meeting details:
Human: 20th January 1pm
Bot: We are unable to find that date in our schedule.
Human: Next Monday
Bot: Find the availability for your meeting: Type r for room availability, c for meeting slot availability.
Human: Schedule a meeting on Wednesday
Bot: How many meeting rooms do you need?
Human: 1
Bot: Wednesday is currently unavailable. Are you flexible with other days?
Human: I'm free on Thursday.
Bot: You can book on Thursday.
Human: You mean on the 20th or the 23rd?
Bot: Which day would you like to schedule your meeting on? The 20th, the 22nd or the 23rd?
Human: Twenty third.
Bot: Please use the booking assistant at booking.microsoft.com and enter the meeting details in the first text box.
I started by opening the chatbot with the avaiable command, and was greeted with a series of replies. These included: the name of the company, the fact the bot was a preview, and a demo of the bot's ability to provide weather information. I then clicked on Weather and immediately the user was presented with a body of text which included a link to an image and a response from the bot.
The final interaction I tried out is related to Microsoft Office 365. When visiting the site I typed in the pulic chat to the right and was greeted with the usual intro for a chatbot. Once the user has accepted their restaurant the ability to book it visited the dialog for menu's and location information. A series of sub-packges were then revealed depending the level of user detail they provided.
Using the Sira app I quickly and easily booked for when I was available and what restaurant I was interested in.
Conclusion Overall, it appears that the move away from using the name Cortana for the Artificial Intelligence based system is an important and worthy one. The switch is not only better for die-hard Heraclet followers but gives Microsoft the ability to refocus attention on their portfolio of AI applications. It takes the pressure off the oversimplistic personality of the named

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** In Brooklyn, NY, it will be 46F and sunny.
Human: This weekend in Brooklyn
Bot: In Brooklyn, it will be 46F and sunny this weekend.
Human: On the weekend?
Bot: It will be warm on the weekend in Brooklyn.
Consistent human markers
Consistency is very important to users as they rely on previous result to construct their question the same way each time so the bot will recognise their request again, and understand.
Human: What does it look like outside?
Bot: The weather is clear and 46 degrees.
Human: What will the weather be like tomorrow?
Bot: Tomorrow in San Francisco, the high will be 72.
Human: What will the weather be like tomorrow?
Bot: Tomorrow in San Fransisco, the high will be 72.
Human: What will the weather be like?
Bot: Tomorrow in San Francisco, the high will be 72.
Malformed signals
Occasionally questions may only probe at 1 or 2 words within a sentence which means the normal grammatical parsing rules analyzed above may not be sufficient, instead, heuristics must be used to fill in the blanks.
Human: Tell me the weather
Bot: What city or zipcode would you like for Radar?
Human: Tell me the weather tomorrow and on Saturday in Charlotte
Bot: What city or latitude/longitude would you like for Radar?
Human: What is the weather going to be like on Friday?
Bot: The following weather forecast is the forecast for the next few days: Friday 87/65 Saturday 89/64 Sunday 92/65 for Greensboro, NC.
The conversation is surprisingly engaging already and 'On The Radar' responds very well to contextual information such as bad weather, dates and times. The much harder weather category to master, however, is data returned directly from a 3rd party API of the traditional weather service kind. Whilst 'On The Radar' is reasonable at finding the closest matching location to a query, determining the right query to carry out in the first place is hard. Nuances such as complex filters, multiple locations or units of measurement may vary, these are hard to detect without having an understanding of the overall structure of the API calls. The advances 'On The Radar' has made in answering user questions about the weather are quite remarkable considering how pre-historic much of today's information retrieval techniques still are. Still, bots like 'RapiFu' are still 2-3 years off

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Checking for weather in Brooklyn, NY.
Human: what is the weather like this weekend in brooklyn?
Bot: Checking for weather in Brooklyn, NY.
Human: Is the weather going to be nice this weekend?
Bot: I don't think so, Emma, but you never know what might happen.
Human: What is the weather like in Chicago this weekend?
Bot: Is it nice where you are? Because it is nice here.

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** 46 and clear.
Human: What's the weather in SF this weekend?
Bot: The weather in San Francisco, CA is 68F and rain. 
Human: What's the weather in Denver like this weekend?
Bot: 41 and clear.
Human: What's the weather like in SF this Saturday?
Bot: 67 and foggy.
Human: What's the high today in SF?
Bot: Today in San Francisco, CA it's 65 and "dark".
Human: Indianapolis?
Bot: Indianapolis is in Indiana and has a population of 821,802.
Human: Recommendation?
Bot: The Super 8 Motel in Indianapolis, IN looks like a great choice. At least that's what the Internet says. 
You can put this code on a Raspberry Pi connected to your home Securifi network to receive your weather forecasts, alerts and data-driven proactive recommendations, such as where to go for a more entertaining day.

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** No.
Bot: It is not.
Human: Does you have any jobs open?
Bot: Yes.
Human: When are you working?
Bot: I work all of the time.
Human: Are you working now?
Human: What do you do for fun?
Bot: Your answer: Bot is working.
Human: What do you do for fun?
Bot: Your Answer: I work.
Human: What do you like to do for fun?
Bot: I play baseball.
Human: What do you like to do for fun? Do you like to play baseball?
Bot: Yes.
Human: Do you like to play baseball?
Human: Play baseball?
Human: What do you like to eat for dinner?
Bot: The answer: I like broccoli.
Human: What do you like to eat for dinner?
Bot: Cover your fingers with food.
The Results
AfternoonBot had sent and received 59 messages. 40.7% of his answers were categorized as 'helpful'. 5.2% were 'haughty'. 1.42% were 'non-helpful but polite'. 10.5% were 'haughty and considered rude'. 19.3% were considered 'idle'. The other 4.0% were categorized as 'polite' but 'polite answers very likely cost extra'.
Thunder SnowBot has sent and received 12,650 messages. 57.4% were considered 'helpful', meaning that during those interactions a health care professional was likely to consider this caregiver an appropriate source of information. 38.6% were considered idle. 7.74% were considered 'polite' but 'polite answers very likely cost extra'. The charts from the UI do not show any percentageing in the idle and considered rude categories. As she/he/it and True Alzheimer's did not start sending messages until the very end of the experiment, the final percentages of the second half may have been re-categorized as 'Helpful' if a message was considered to be from a caregiver in the health data category.
True Alzheimer's posted responses when responding to a question and during link-sharing and external-referencing, when there were no questions. 45.8% of what True Alzheimer's wrote could be categorized as helpful, 39.5% idled, and 14.7% were categorized as not particularly helpful but polite, polite & cost extra or considered rude

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** What is the temperature forecast for tomorrow in NY?
Human: Brighton?
Bot: Tomorrow we'll see a high of 50°, with a low of 44°. There is a 72% chance of rain. Winds will be from the East-Northeast at 8mph.
Human: 65 rms
Bot: Thank you. :)
Human: Do you have any events?
Bot: events for what?
Human: Events.
Bot: Submit
Human: Where's your occupancy rate?
Bot: 74% during the month of febru.....ah....Where are the question marks?
Human: What is occupancy rate?
Bot: This gives the percentage of rooms occupied vs. the ones available.
Human: Thanks!
Human: Avail.
Bot: Hi, I'm not able to find any results for "Availability". Can you please rephrase the query?
Human: Travelin to orlando
Human: ?
Human: Last back?
Human: ?
Bot: Hi, I'm not able to find any results for "where is". Can you please rephrase the query?
Human: Where's Jones?
Bot: I found 12 people with that name in the Manhattan area.
Human: Queens?
Bot: Sorry, I don't recognize that place. I found 4 people with that name.
Human: Bluetooth
Bot: Bluetooth is very useful.
Human: Par
Bot: My apologies, but it seems you need to pay $1 to access this content. Otherwise, feel free to learn more about remote.com/par.
Human: What is par?
Bot: The word "par" is shared across a wide variety of games and sports and is usually an indicator of a very commonly referenced score or goal.
Human: Par for par
Bot: Collaborate together for a common purpose.
Human: Par for one
Bot: Combine separate pieces into a unified whole.
Human: Par
Bot: Par
Human: Music sites
Bot: Looking for the best in music? Visit site to explore artistes, songs, albums, and new music plays on one platform.
Human: Refresh
Bot: This web page is not responding.
Human: King down?
Bot: I want someone who wants this as bad as I do to learn more about turbines.swe.org after you are done.
Human: Whoa
Human: Lets go
Bot: When someone hacks into a

---

