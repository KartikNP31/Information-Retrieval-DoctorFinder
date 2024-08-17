IR Mini Project - Understanding Text in Health Domain - (Find Doctor)




# Install required library
-    pip install django
-    pip install pandas
-    pip install matplotlib
-    pip install numpy
-    pip install bs4
 

## How to Run Application - follow the below steps
-    1.  Unzip P29-MiniProject-LETAP.zip 
-    2.  Open in terminal -> P29-MiniProject-LETAP
-    3.  Run following commands in the terminal one-by-one (Note that parent directory should be 'P29-MiniProject-LETAP'): 
            >- cd code 
            >- python manage.py runserver
-    4. search for the link in the Chrome :  http://127.0.0.1:8000/




## Try this Example : 
        City : Bangalore
        Speciality : general surgeon
        Locality : Whitefield




### About Project -
    1.  Understanding Text in Health Domain - (Find Doctor) is a Information Retrieval project 
    2.  It search for doctor as per user input preference.
    3.  3 input choice are given to user, namely - 
            City - City where user searching for doctor
            Specialty - Specialty of doctor, user searching for
            Locality - Locality in the mentioned city
    4.  On clicking 'Submit' - top 20 relevant list(document) of doctor's will be listed
    5.  Feedback - For each listed document, feedback option is provided to user, where user can like or dislike the result for his/her query.
    6.  At the Bottom of listed documents(list of doctors) , 'Show P-R Curve' button is provided 
    7.  By clicking on 'Show P-R Curve' button - a small window will pop-out showing P-R curve according to submitted feedback by the user
    8.  Like : relevant document
    9.  dislike : non-relevant document




## Dataset - 
    1. Dataset is collected by web-crawling of the website : Practo.com
    2. We have collected around oneLakh list of document containing following information of Doctor : 
        DoctorName,Experience,Speciality,Fees,Rating,Locality,City


