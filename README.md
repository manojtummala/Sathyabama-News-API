# Sathyabama-News-API
```bash
A JSON API to scrap details of latest news and events from hhtps://sathyabama.ac.in
```

# Features

- Latest News and Updates:
         - Return JSONified link text, date and URL for all the latest updates displayed.
- Latest Events:
         - Return JSONified link text, date, venue and URL for all the latest events displayed.
  
# Schema

All API access is over ```HTTPS```, and accessed from the ```<https://sathyabama-api.herokuapp.com>```. All data is sent as JSON.
```bash
{
  "Project-Name":"Sathyabama-Event-API",
  "author":"Manoj T",
  "email":"tummmalamanoj2002@gmail.com",
  "website":"https://manojtummala.github.io"
}
```
# End Points

### ```GET: /```
Result:
```json
{
  "Project-Name":"Sathyabama-Event-API",
  "author":"Manoj T",
  "email":"tummmalamanoj2002@gmail.com",
  "website":"https://manojtummala.github.io"
}
```
### ```GET: news```
Result:
```json
{
  "list":[
    {
       "News": "Post Graduate - 2020 Batch - Regular - Timetable",
       "Time":"Tue, 11/17/2020 - 08:00",
       "URL":"https://sathyabama.ac.in/news/post-graduate-2020-batch-regular-timetable"
    },
    {
       "News": "Arrear Examination for the following batches will be conducted through ONLINE Mode from 18.11.2020 to 28.11.2020.",
       "Time":"Fri, 11/06/2020 - 14:21",
       "URL":"https://sathyabama.ac.in/news/arrear-examination-following-batches-will-be-conducted-through-online-mode-18112020-28112020"
    },
    {
       "News": "Sathyabama awarded with QS -  E Lead (E - Learning Excellence for Academic Digitisation)",
       "Time":"Fri, 10/23/2020 - 18:33",
       "URL":"https://sathyabama.ac.in/news/sathyabama-awarded-qs-e-lead-e-learning-excellence-academic-digitisation"
    },
  ]
}
```
### `GET: /events`  
Result:  
```json
{
  "list":[
    {
        "Event":"AICTE Sponsored STTP on Digital Twin Technology (Phase - III)",
        "Time":"Time: 08:00 AM",
        "Venue":"Venue: Sathyabama - Online",
        "URL":"https://sathyabama.ac.in//event/aicte-sponsored-sttp-digital-twin-technology-phase-iii"
    },
    {
        "Event":"Post Graduate Diploma Course in Computational Biology",
        "Time":"Time: 08:00 AM",
        "Venue":"Venue: Sathyabama - Online",
        "URL":"https://sathyabama.ac.in//event/post-graduate-diploma-course-computational-biology"
    },
  ]
}
```
