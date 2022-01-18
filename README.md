GitHub Link - https://github.com/sanjaychaurasiya/Xtream/tree/master
Heroku Deployed Link - https://xtream-intern.herokuapp.com/

API Endpoint - https://xtream-intern.herokuapp.com/
This Endpoint is used to get and post data. 
JSON Object - {
    "email": "<email>",
    "name_of_receiver": "<name>",
    "city": "<city>"
}
Whenever you send a POST request it automatically hit weather API to get current temperature 
according to the city name in the POST request (city) and send email to the receiver email address, 
which is in the post request (email).
