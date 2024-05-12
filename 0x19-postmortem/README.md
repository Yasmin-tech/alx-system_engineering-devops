*

# ***MyWeatherForecast Post-mortem incident report***



## About The App:

  

This service offers registered users daily email updates with comprehensive weather insights and helpful advice to make the most of their day. These messages are delivered promptly at 6:00 am and catered to every user of the platform. An HTML file will be attached to the email sent so that the user can view it in their browser. Although the app runs locally for only two hours a day due to limited resources, it is a convenient tool that is exclusively accessible within the local network. As a result, my users are limited to my family members.

## The workflow:

The service is available for two hours a day, from 5:00 am to 7:00 am EAT. During this time, users can visit the website and register to start receiving weather information emails the following day. If a user is already registered, they will receive the weather information email by 6:00 am EAT.

The entire process is automated, with a Linux system scheduling a script to run at 5:00 am EAT. This script starts an application that uses port 9393 to service the website, access the database for user information, and generate custom HTML pages. These HTML pages are then returned to the initial script that started the app.

**See the full report [here](https://docs.google.com/document/d/1s05v_0tLQ-PCbWzJUcApKUqbsComza8H-hT5H5bxDVQ/edit?usp=sharing)**#
