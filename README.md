# empatica_assigment_app
Empatica &lt;3 Assigment app.

This is my assigment app for the Empatica <3 people team.
You can see a working sample at http://panzerfausten.pythonanywhere.com
#Instructions:
  

##Installing:
grab the code  
Just clone the code from this repository!  
>git clone git@github.com:panzerfausten/empatica_assigment_app.git

##libs
First make sure have flask installed. This is the only extra library needed.
To install flask you can use your package manager
>*linux: sudo apt-get instal python-flask in ubuntu or sudo zypper install python-flask in openSuSE   
>*macOS:	sudo pip install Flask (sometimes you get linking troubles in mac after installation. You can use ln for this)

##deploying  
*On your PC:  
If you decide to run it on yout PC just do:  
>python  main.py  

This will start the server at:  http://127.0.0.1:5000/. Just open your browser and head that direction :)

*On pythonanywhere:  
If you want to run in on the cloud  (THE CLOUD! https://www.youtube.com/watch?v=8cp_uwr-7lY)  
*Create an account at pythonanywhere.com  
*Create a new app on your domain by going to web tab -> add a new web app, d select "flask" with python 2.7 and hit next.  
*Create a zip file with the cloned repository   
*Go back to the files tab in  your dashboard at pythonanywhere.com and upload your file. This step may take some time so go with your family and have some quality time.  
*After some minutes come back (you still have to work) and select "open bash console here"  
*Unpress your files with the command 'unzip [file]'.  
*Let's asume you named your folder 'mysite' (if the folder already existed just delete everything in there)  
*Move the 'data' folder one hierarchy mysite with "mv data/ ../" (pythonanywhere treats the paths a little different)  
*Go to the 'web' tab and select your app. Then click on 'WSGI configuration file' in the 'Code' seccion and change the last line to:

    from main import app as application  
This will allow pythonanywhere to load the app.  
*Save the file and click "reload appname.pythonanywhere.com".  

That's it. Your app should be running at appname.pythonanywhere.com
If not, please check the Error log file at the Log files section


##using
This app does not uses any DBMS. Instead uses a dummy authentication method (I did this to avoid extra configuration :P)  

the available users, passwords and roles are:
| Username        | Password           | role  |
| ------------- |:-------------:| -----:|
| dmiranda@empatica.com      | pwd123 | patient |
| aboj@empatica.com     | bojo      |   patient|
| mike@empatica.com | rodri      |    support |
| god@empatica.com | dioeilmiopastore      |    god |
|gfreeman@empatica.com|wololo|doctor|

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

Webpages are not protected so you can see them if you have the links. 


And that's all. Hope you like it :)

