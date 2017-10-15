# HackNYFall2017

# todo

- [ ] domain name at domain.com
- [ ] finish devpost
- [ ] add more data visualizations
- [ ] add facebook post integration

## Inspiration

Wanting to keep our beaches and parks clean and help keep track of our efforts so we can best create laws and make lifestyfle changes to better the planet, we created OceanCleanup. As a frequent volunteer for beach cleanups, I know the flawed system that is used. Volunteers must carry around a piece of paper and write down the names of the items they find and keep a tally of the totals of each different trash category. At the end of the beach cleanup, the paper slips are collected and a voluneer manually inputs this data into the trash collection database. With this data, organizations like Heal the Bay can target efforts towards reducing trash found on beaches with real data. This will permit Heal the Bay's volunteers to spend time evaluating the data found and how to best reduce trash found at the beach!

## What it does

Our webapp allows users to upload a photo of the trash they find and using the Clarifai API, the trash will be labeled and put into the trash database with the location the trash was found which we used the the GoogleMaps API with.

## How I built it

We built this using Python, JavaScript, HTML and CSS. We are using flask and ngrok to share this webapp online.

## Challenges I ran into

We found the general Clarifai model was not giving us the labels we were looking for, so we created our own dataset. We also ran into challenges parsing the JSON file of how Clarifai identified the images, but thanks Kunal for helping us debug!

## Accomplishments that I'm proud of

First Hackathon!!! (not for Natalie) and made a really dope site!!

## What I learned

SO MUCH!!

We learned about how to make Flask templates and make PULL requests and made an awesome and super helpful site.

How to pronounce "La Jolla", the mutual friend game is really fun, sweet potato, quinoa and curry chicken are a GREAT combo.

## What's next for OceanCleanup

Bring it to Heal The Bay!!!

Get better data analysis views so that people can better identify trash according to quantity or location

Game-ify OceanCleanup so that users can compete with their facebook friends to see who can pick up the most trash

This can also be used in cities like New York to keep NYC's parks clean :)

