# Python API Poster
Simple python script to post contents of a JSON file to a RESTful API

### Table of Contents
1. [Installation](#Installation)
2. [Necessary Components](#Necessary-Components)
2. [Connecting to a Different Database](#Connecting-to-a-Different-Database)


### **Installation**
Clone the repository.
```bash
$ git clone https://github.com/connellboyce/Python-API-Poster.git
```

Open the program in your IDE and run.


### **Necessary Components**
* Python 3
* POST Permissions in a web API


### **Connecting to a Different Database**
This program is specialized to write to the database for [my Pepper Garden app](https://github.com/connellboyce/pepper-garden), but this can be changed.
There are a few things you will need to have set up first, however.
1. You must have an API allowing POST requests
2. You must have a JSON file containing an array of objects
3. The JSON objects must be valid in the eyes of the desired API
    * Do not try to use a JSON object lacking required fields or having information the API will reject
4. Replace the variables at the top of the Python script to match the API you would like to post to
    * url: This should be the API URL which allows POST requests
    * headers: This should include any HTTP headers that the API requires. Authorization headers, like the one in the variable currently, will usually expire. Make sure your headers are valid.
    * fileName: Put the name of the JSON file you would like to iterate through and POST in the directory here. The [pepperList.json](pepperList.json) file is in the correct location for reference.
    * arrayName: This should be the name of the array contained inside the JSON file.
5. Run the program

