# Router-Reboot
Python 3 script for the automation of rebooting a router


<ins>Why I started this project:</ins>

The internet at my house is abysmal. Our provider isn't great, and the router/gateway we have gets slow on a nearly weekly basis requiring the need to reboot. I got tired of getting up each time to unplug it when it slowed down, and I also hated having to log into the router's admin page. Also, the router doesn't have it's own scheduling abilities to automate reboots through the router. So I decided I would write a script to do the work for me that I could run whenever I need to.

<ins>What is missing from the file:</ins>

This project uses Selenium to control the browser. You will need to go to Selenium's website and find the appropiate WebDriver for your purposes. I am using chromedriver.exe, and I have it in the same directory as my python program.
Also, shouldn't have to be said, but just in case, you will need to pip install selenium to get the selenium package.
This particular program is written for Windows, so if you are on Linux/Mac, you will need to change a few parts of the code.

<ins>Future additions:</ins>

I have this set up on a personal server at my house, so I will be using the server to run the program at a set time during the week so I won't have to worry about manually rebooting during the day. I can just have it run at night when no one is using it.
I plan on adding the ability to text or email me when it runs and finishes so I know it is working, and so I'll know if there is a problem (like the internet never came back on).
