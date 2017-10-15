# HackNY Fall 2017

Our Project: OceanCache - a website where users can take pictures of the trash they find and it will automatically be input into a database to save ocean cleanup volunteers from having to manually keep track of the trash they find

cache-em-all.com

# todo

- [x] domain name at domain.com
- [ ] finish devpost
- [x] add more data visualizations for the rest of the beaches
- [ ] add facebook post integration
- [ ] take screenshots and add them to devpost
- [x] add map coordinates
- [x] map option on firebase
- [ ] fix submit buttons
- [x] change wording to "thank you for submitting a" can

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


# Presentation

**Natalie: Why**

Raise your hand if you like going to the beach

Keep your hand raised and raise your hand if you like marine life and want ocean animals to be happy and healthy

Me too!

I'm from California and have been volunteering with an organization Heal the Bay since I was little

At beach cleanups, each volunteer has a piece of paper and a trash bag that they walk around with and they write down evey item of trash they pick up, keeping a tally of the total number of bottles, cans, and everything they find.

At the end of the cleanup, one volunteer collects all the slips of paper and manually inputs this data into Heal the Bay's trash collection database.

With this information, Heal the Bay targets their efforts towards limiting the amount of trash found at the beach. Recently LA banned plastic bags - this was in part due to efforts led by beach cleanup organizations after they found that one of the most found items at beach cleanups were plastic bags. 

With this app, instead of spending valuable volunteer hours on inputting data, volunteers can spend their time evaluating the data found, working on pushing new laws like this one, and making real changes.

**Someone: How/Clarifai API/GoogleMaps API**

walk through use of app:

imput a picture, this image goes through a Clarifai Model we made and classifies the image as a type of trash, this is automatically added to our Firebase Database with the location found using the GoogleMaps API

imput a different picture and see how our model identifies it as a different type of trash and ups the number in the Firebase Database

**Someone: Social media posting to game-ify cleaning up and get more users and to build awareness**

to get more awareness about ocean cleanups and game-ify ocean cleanups, we added capability to compete with your facebook friends on who can pick up the most trash and added a share button that posts a status to your wall sharing how to get more involved with beach cleanups!

Through this button you can post to your wall about how you are picking up trash though OceanCache!

**Kevin: Firebase**

our database collects information as said before and keeps track of it like so

we chose to use firebase because

with this data, we are then able to display the data so that users can best understand the data and share it with others so that they can understand it too.

We also have a donate button and an about us section!
