**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather in Brooklyn, New York is 65F and clear this weekend. I hope you got your umbrella.
Here we're able to introduce responsiveness into our interactions. Previously if the bot did not exist, a user would be given a simple response. Now they are automatically routed to either the default response provided by Microsoft or potentially another provider such as Weather Underground. We also receive a more concise and understandable language parsing by building a template system from the responses.
Another interesting implementation is the conversation system. Here we use the library to have a two way conversation with a user.
Imagine a command or query that brings across information. This information could be passed to the system, the user, or in the case of a conversation could be communicated in a conversation format.
In a two-way conversation, each line responds to the previous line and they have the ability to end the conversation. Our conversation responder is basically a parser that is breaking down the input and displaying relevant information.
For instance, if a user inputs the command, "weather," we send a get weather request to our weather provider. After parsing the data, we display varied data on the console. Again, we want to display relevant data to the user. In most cases this is just the current location and current conditions. However, if a user inputs, "what is the weather in Sydney, Australia," we ask them to confirm that they want to view temperature data for Sydney, Australia. They confirm and we send them a request with the location in place. After receiving the data, we display it. Note that we are again, applying our theme of relevance
This concept can be applied to the base system later when we implement commands such as, "ask about sports news."
Temperature in Sydney, Australia is 50ªF
The following is the data structure that our conversation scaffold uses to display information.
Sales
Another bot, sales demo, is used to illustrate the financial, B2B bot system that our company offers.

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Saturday: 64F with a high of 66F and a 93% chance of rain.  Sunday: 49F with a high of 59F and  a  36% chance of rain.
Human: For the weekend?
Bot: Hard to say.  On 5/16/2018 the weather in Brooklyn, New York  will be Sunny, with an high of 64.  There is a 14% chance of precipitation and a low of 53.  I would advise you wear pants with the chance of precipitations that you will get while your there.   It will be much warmer on 5/17/2018.  This day the weather will be Sunny, with a high of 72.  Probability of precipitations will be 0%.  I would suggest wearing more sunny and rainbow pants on that day as well.
Note: The bot was deliberately programmed to make errors of this nature.
Human: Do you have an umbrella?
Bot: Why would I have an umbrella?
There are more examples on the blog post for  Dreadful Philly Weather Bot: Part II .
Now I want people to build on/and improve this without copying from it.  I've open sourced the code for the deep learning samples here: https://github.com/wilsonmar/WeatherBot and it has instructions and datasets here: https://github.com/wilsonmar/WeatherBot/tree/master/Data
My next destination from here isn't a kitchen sink bot yet.  I want to use the raspberry pi for something new.  I'll be posting my next robot endeavor soon!

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Seattle, WA is 46F and clear. Current Conditions: Mostly Cloudy.
Human: This weekend
Bot: The weather in Oakland, CA is 42F and clear. Current Conditions: Fog.
Human: What is the weather in Oakland like Nov 1 2015
Bot: The weather in Oakland, CA is 42F and clear. Current Conditions: Fog.
Human: What is the weather like in oakland califonia this weekdays?
Bot: The weather in Oakland, CA is 42F and clear. Current Conditions: Fog.
Human: What's the weather like in New York in December?
Bot: New York, NY is 39F and clear. Current Conditions: Snow.
Human: What's the weather like in Boston?
Bot: Boston, MA is 42F and clear. Current Conditions: Partly Cloudy.
Human: What's the weather like in in Oklahoma?
Bot: Oklahoma City, OK is 36F and clear.
Human: What's the weather like in Austin, TX
Bot: Austin, TX is 55F and partially cloudy. Current Conditions: Overcast.
Human: What's the weather for new york tomorrow
Bot: New York, NY is 52F and clear. Current Conditions: Partly Cloudy.
Human: Can you tell me the weather
Bot: Colorado Springs, CO is 58F and clear. Current Conditions: Fog.
Human: What is the weather like in (scranton)
Bot: Scranton, PA is 50F and clear. Current Conditions: Clear.
Human: What is the weather like in manhattan
Bot: Manhattan, NY is 48F and clear. Current Conditions: Clear.
Human: Do you give me the current weather in nv?
Bot: Las Vegas, NV is 57F and clear. Current Conditions: Clear.
Human: What is the current weather in san diego ?
Bot: San Diego, CA is 61F and clear. Current Conditions: Fog.
Human: What time does this go off line
Bot: This chat bot will go offline in approximately 15 minutes.
Until next post, Happy Chatting!

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** It's Saturday and partly cloudy in Chicago, 70F. Today is Saturday and partly cloudy in Chicago, IL, 70F.
Human: This weekend.
Bot: I don't appear to have a location. Tell me a location.
Human: San Francisco, CA.
Bot: It's currently 72 degrees in San Francisco, CA and mostly cloudy.
Human: My city.
Bot: It's currently 69 in your city.
Human: Weather tomorrow.
Bot: It's Monday at 9:54 AM and it is mainly the rainy in Philadelphia, PA, 59F.
Human: My zipcode
Bot: It's rainy in 55246
Human: My zipcode
Bot: The local time in 55246 is 5:40 PM
Human: Weather in tampa tomorrow
Bot: Tomorrow is Tuesday at 1:50 AM.
Human: What is the capital of texas
Bot: Here are 3 things I found for 'What is the capital of texas'.Will that do? https://www.google.com/search?q=What+is+the+capital+of+Texas.&oq=What+is+the+capital+of+Texa.&aqs=chrome..69i57.7288j0j7&sourceid=chrome&ie=UTF-8
Human: Yes 2009 microsoft
Bot: Will that do? http://news.cnet.com/8301-10784_3-20069475-83.html https://www.google.com/search?q=2009+microsoft+sting+bot&oq=2009+micros.&aqs=chrome..69i57j69i61j0l2.3263j0j7&sourceid=chrome&ie=UTF-8
Human: Yes i use eventhelper
Bot: Will that do? https://www.eventhelper.com/free/g.aspx https://socialchorus.com/
Human: What is it i use it to
Bot: Will that do? https://www.eventhelper.com/free/g.aspx https://socialchorus.com/
Human: Are you online
Bot: Are you talking to me?
Human: Any good pictures on your site
Bot: Will that do? https://www.eventhelper.com/free/g.aspx https://socialchorus.com

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** Today is Sat Sep 29, 2017. The date is today. It is Saturday. Today's high is 46. Tomorrow's high is 50. Humidity is 93%. The condition is Cloudy and Chance of Rain. Sunrise is at 6:49 AM and sunset is at 6:32 PM.
Human: Please schedule an appointment for Saturday this weekend.
Bot: Sure. When are you available?
Human: This weekend?
Bot: How about October 30, 2017 at 10 AM?
Human: This weekend on Friday?
Bot: No appointments this weekend on Friday are available. You might try a different date or a different time slot.
Human: Thank you.
Bot: You're welcome. Thanks for visiting the Google Store Converse!

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather in Brooklyn, NY is Cloudy today. The high will be 56F and the low will be 39F. The UV index is Low, and the windchill is 43F. The dewpoint is 35F.
Human: This weekend?
Bot: The weather forecast in Brooklyn, New York for the next few days is windy. Rain is not expected during the next 10 days.
Human: This weekend?
Bot: The weather in Brooklyn, NY for the next week is forecasted to be very windy. The highest temperature will be 59°F and the lowest temperature will be 22°F. The wind speed will be 10 mph, which is about the same as a gentle breeze. It looks like it will be mostly cloudy for the next 2 days. Why?
Human: Where is a fancy restaurant in core Manhattan?
Bot: Results for "romeo's pizza in manhattan" Just 2 miles, +185 results for "restaurants in manhattan" Just 1 miles, +95 results.
Human: Can you tell me about chef basia verya?
Bot: I already told you everything I know about chef Basia Verya! Why?
Human: Tell me again.
Bot: Who do you study with?
Human: Who do you work for?
Bot: Where do you work?
Human: Are you rich?
Bot: What rivers make up the Amazon?
Human: What river is the Amazon?
Bot: What's your friend George Bush?
Human: What's Trump like.
Bot: President Donald Trump's counselor and communications director, Hope Hicks, will resign on March 29, the White House says. Reagan, 35th president of the United States (1981-89).
Human: Who is Thomas Jefferson.
Bot: Thomas Jefferson was the 3rd President of USA, and as such was behind the Louisiana Purchase and the Lewis and Clark expedition. He conducted a famous test of a lightning rod. Why?
Human: Tell me about paul gayetty.
Bot: Mon cancer du poumon "laniegavelon cel-lula" a leo vei fre-au taca mult mais e asocia a si sicomasculinin continua con sa mi-ue tal la.
Human: Tell me about rasputin.
Bot: Rasputin "svetla din grad pana in cer"-doamna chir

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** 46 degrees and clear.
Human: Sorry I didn't know it was that's percent
Bot: Little colder and cloudy.
Human: Through the weekend?
Bot: 36 degrees and clear.
Human: The weekend? I'm in Union
Bot: The weekend forecast for Union, NJ is 45 degrees and mostly sunny.
Human: Look it up for Philly
Bot: The weather in Philadelphia, PA is 36F and clear.
Human: What's the WEather like in philidelphia this weekend
Bot: 45 degrees and sunny.
Human: 65f and sunny
Bot: 36 degrees and sunny.
Human: 45 and sunny
Bot: 36 degrees and sunny.
Human: What's the weather like on the weekend
Bot: 37 degrees, sunny.
Human: What's the High temps the weekend
Bot: 44 degrees and clear.
Human: Hello, a donde esta caliente y con sol en NY ?
Bot: En Echo Park, NY hace un calor del 60F. Human: One degree Celsius
Bot: Renos, CA. it is 86F.
Human: 76F in Orlando FL
Bot: Ocala, FL is 76F and partly cloudy.
Human: What's the weather in Orlando this weekend
Bot: 44 degrees and sunny.
Human: Estimated high for Ambler,PA this weekend?
Bot: 46 degrees and clear.
This is just a taste of what's possible today ... a little bot that's "just enough" to answer the question. To help with that we've brought in an smart service from Revelytix that allows for easy storage and querying of data using standard SQL without the hassle of a traditional database administrator role. More on this next post. Need help? Let us know and we'd be happy to find the right mix of people and technologies to help bring you your bot.
Bots. We do a lot of them. Have a look at our Bots page or visit CoinTent to look at a dozen plus bots we've already built. We also build bots with many partners with our Pocket Bot technology. You need Excel? We've got a platform that makes that easy too. Check out our Award winning Excel as a Service

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** I'm not able to find any results for that location?
Human: This weekend in Brooklyn.
Bot: The weather in Brooklyn, NY is 58F Friday and 56F Saturday.
Human: Sacramento, ca.
Bot: Overcast. Low around 46F. High around 68F.
Human: Where in Augsburg?
Bot: I can answer that. There are no vacancies in Augsburg?
Human: Um I'd like to know what the weather is like Tuesday in Augsburg. (via SMS, iPhone app)
Bot: The one thing I love most about Augsburg is the wife of William and Elisabeth (mayor).
Human: Weather?
Bot: I can tell a joke about Augsburg. There are no vacancies in Augsburg.
Human: What is the weather on a Monday in Hillerstrasse, Augsburg in February?
Bot: The weather in Augsburg, Bayern, Germany is not good today but will be partly cloudy tomorrow. Today - Friday, the temperature will be around 46 degrees. Tonight it will fall to around 32 degrees. The low for Augsburg tomorrow will be 41 degrees.
Human: Tell me the weather in Augsburg today and tomorrow please
Bot: In June Augsburg had nice weather 79.3 F. Mostly sunny during the day and clear at night. Very windy.



Human: How's sturgeon fishing in Michigan?
Bot: (via SMS, iPhone app) Missouri - Charles Sturgeon you can contact at strugf1@missouri.edu, 239-150-7988.
Human: What is the average temperature this month in Adelaide South Australia?
Bot: The average temperature this month in Adelaide is 49 degrees.

The first live tv-interview from the event was shown in December 2012 in an Austrian television show named "nova anthologica" and was attended by Ian Hutchings as a representative of all the participants. The resulting episode was commented in online magazines and talk shows. In May 2012 the project Leisure Expert & Climate Change: Using chat algorithms to keep up with climate change. was nominated for the second Face2Face, a major conference of interaction with computers, taking place in June 2012 in Brighton, UK. Many further nominations as well as invitations for university lectures and special showcases on climate change and Engagement/Nudging were shown on conferences and web magazines and also in a press release of eu project of future and emerging technologies. Accordingly messages were sent

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather in Brooklyn, NY this weekend is 46F and clear.
Human: When is the best time to go jogging if I want to avoid the cold?
Bot: According to the weather, the best time to go jogging is today.
Human: What is the date and time of a first- come, first-served useless meeting next Thursday?
Bot: What is the date and time of a first- come, first-served useless meeting next week on 18 Mar?
Human: No, no, no, Thursday.
Bot: What is the date and time of a first- come, first- served useless meeting on 01 Mar?
Human: What are you wearing today?
Bot: I am wearing white shirt and black shorts.
These were not always conceived of as a bunch of questions but as revealing a specific piece of information. I played and hacked at this bot for six days before opening it up for others to test. My aim over the next six weeks is for her to reply to more intuitive questions as she has been trained to reply to the structured information questions I do list above.
The game is afoot. Join the hunt, contribute to my experiment at github and upvote my bot's questions at dormroomai.com

---

**Human: What's the weather like this weekend?**
**Bot: Are you on a boat? Because I was not able to find any results for that location?**
**Human: What's the weather like in Brooklyn this weekend?**
**Bot: The weather in Brooklyn, NY is 46F and clear.**
**Human: This weekend?**
**Bot:** The weather forecast for this weekend in Brooklyn, NY is 69F and sunny.

---

