# |Twitter app|
---------------------------------------------------------------
This program generates a map with locations of Twitter friends.
---------------------------------------------------------------
Warning ! 
For using this app you should have Twitter bearer token.
# |Functions:| 
Module includes 5 different functions:
1. get_info
|Sends request to Twitter with the help of bearer token.
Returns json with the information about first 50 friends of user with given username.|
2. get_friends_coordinates
|Function gets a dictionary and returns a list
of tuples with each friend's coordinates.|
3. create_map
|Function creates an html map with markers as friends' locations.|
4. index
|Function creates the main page of the app.|
5. final_map
|Function creates a final map about friends.|

# |Example of usage|
When user runs the program, he/she gets the local server ip, then (after clicking on it) the page in browser loads. On that stage user can write a nickname on Twitter, for which he/she wants to get followers map. The user also has to input a bearer token (it is used to get friends list from Twitter).The waiting time is usually 1-2 minutes, depending on the Internet connection and the work of geopy.
Here is an example of an output in console:
![Photo](images/consoleexample.png?raw=true "text")
Here is an example of site:
![Photo](images/siteexample.png?raw=true "An example of user's input and the terminals output")

# |Result|
The result is a map with a layer of Twitter friends' locations. You can add and remove layers on the map using the layer control.
Note: there are 4 different styles of map.
Here is a generated map:
![Photo](images/mapexample.png?raw=true "text")

