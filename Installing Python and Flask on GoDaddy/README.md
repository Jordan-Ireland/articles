# Installing Python and Flask On GoDaddy

## Description
These are the files for the Flask app that you will need ot put inside public_html to test if Python was successfully installed.
[Link To Article](https://medium.com/@jordan.b.ireland/installing-python-3-and-flask-on-godaddy-1635fe6f24bc)

## Contents

**public_html/** *Main folder to place in your website* <br />
├── **.htaccess** *Redirects all traffic to your app.cgi folder. Make sure to change to your username* <br />
└── **cgi-bin/** *Houses any and all python/cgi files* <br />
&nbsp;&nbsp;&nbsp;&nbsp;├── **app.cgi** *Starts the app.py Flask app and sets up environment variables* <br />
&nbsp;&nbsp;&nbsp;&nbsp;├── **app.py** *The main file for your Flask app. This tells the app which pages to point to based on URL (www.you.com/home)* <br />
&nbsp;&nbsp;&nbsp;&nbsp;└── **templates/** *Place all HTML files in here which you want to call from your app.cgi. If it isn't in here `render_template` won't display it* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── home.html

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.