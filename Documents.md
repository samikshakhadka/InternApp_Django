# Request Response Cycle

1. Recieve request from client
2. Web Server handles the recived request from client and forwards it to Django application
3. When client request is recieved, WSGI handler is created.
4. Import settings.py
5. Load middleware . Each request goes through middleware.
6. Django URL dispatcher recievers request and examines URL. URL dispatcher maps requested URL to a specific view based on URL patterns defined in the Django URL configuration.
7. Associated view fucntion is called . Views are function or classes with logic to generate response
8. View function or class processes the request to generate desired output.
9. If template rendering is required view passes necessay data to the appropriate template.
10. View finally generates HTTP response object. This object encapsulates the response content, status code, and additional headers or metadata. The response can be a simple HTML page, JSON data, a file download, or any other form of data.
11. Finally the client receives the response from the Django application and sends it back to the client that made the initial request.
12. The cycle is repeated

# Concurrency

- execution of several tasks or process simultaneously.
- enable program to work in several tasks simultaneously.
- concurrency allows programmes to effectively utilize system resources .

## Concurrency vs parallelism

- parallelism refers to carryion out numerous tasks concurrently or parallelly.
- concurrency refers to system capacity to carry tasks in interleaved. Even when they run on a single processing unit, coordinating several tasks concurrently is the main goal.

# Copy

- Assignment statements in Python do not copy objects, they create bindings between a target and an object.

## Shallow copy

- creates a new object which stores the reference of the original elements. it doesn't create a copy of nested objects, instead it just copies the reference of nested objects

## Deep Copy

- A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
