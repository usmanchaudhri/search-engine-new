Steps to start the Sanic server:
- python3 main.py

Excute curl command:
- curl -X GET 'http://0.0.0.0:8080/usersearch?_id=1'
- curl -X GET 'http://0.0.0.0:8080/ticketsearch?_id=436bf9b0-1147-4c0a-8439-6f79833bff5b'
- curl -X GET 'http://0.0.0.0:8080/organizationsearch?external_id=9270ed79-35eb-4a38-a46f-35725197ea8d&shared_tickets=false'

If had more time: 
- more testing around corner cases
- exception handler
- implement ability to search across documents which i was implementing under /search API
- validation layer which will test the input REST request for any error before doing the search



