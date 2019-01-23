{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\froman\fcharset0 Times-Roman;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 To run my code type either of the 2 commands:\
1. 
\f1\fs22 \cf0 \kerning1\expnd0\expndtw0 \CocoaLigature0 \outl0\strokewidth0 python MATHUR_RAVEENA_HW6.py -source=local\
          or\
2. python MATHUR_RAVEENA_HW6.py -source=remote\
\

\f0\fs24 The following happens when you run the code:\
1) newsfinal.db is created in the same directory as the .py file above\
2) if source =local:\
Then the code displays the following:\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf0 a) Distribution of section of news amongst headlines for LA Times\
b)  Distribution of section of news amongst headlines for New York Times\
c) Distribution of news sources in google news \
d) usage of keywords in headlines of New York Times \
e) the no.of headlines in google news, LA times and New York times featuring President Trump\
\
3) if source=remote\
Then the code displays the following:\
a) how much news from different countries reported in New York Times US version\
\cf2 \expnd0\expndtw0\kerning0
\CocoaLigature1 \outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 1. For this code to work successfully please install\
1) nltk library ({\field{\*\fldinst{HYPERLINK "https://www.nltk.org/install.html"}}{\fldrslt https://www.nltk.org/install.html}})\
2) geocoder ({\field{\*\fldinst{HYPERLINK "http://geocoder.readthedocs.io/index.html"}}{\fldrslt http://geocoder.readthedocs.io/index.html}})\
3) SQLalchemy\
4) SQLite\
5) Matplotlib\
6) Pandas\
7) Numpy\
You may use the commands given in the documentation.\
(the others are more standard so not included)\
The whole code works but please be patient.\
if source =remote\
1) The plot takes time to display, so be patient\
if source=local\
1) There are 5 plots that need to be displayed.\
2) They are not viewed all at once, rather the 1st one will be shown, then to see the 2nd one, close the first one. Please keep closing the plots to view next ones. If you would not close the plot window you will not see the next plot.\
This could have been improved but when I tried to fit a lot of the plots in one page they lost meaning because their attributes got jumbled.\
\
The project works fine on my system and is designed to be with minimum errors. Please contact raveenam@usc.edu in case of issues.}