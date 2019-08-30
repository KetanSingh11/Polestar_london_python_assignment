#### Internal APIs (backend utilities):
Here are some internal API's as well, for more control and simplicity sake. Read more about them [here](README_more.md).

- **init_db** `/api/init_db/`    
    Initializes the database - reads this [csv](../positions.csv) and writes to the local database (sqlite).
    - Methods: _GET, DELETE_
    
    Example:
    ```bash
    curl -X GET "http://localhost:5010/api/init_db/"
    curl -X DELETE "http://localhost:5010/api/init_db/"
    ```

- **test** `/api/shipsdata/`     
    Returns the data from the shipdata table (csv data)
    - Methods: _GET, DELETE_
    
    Examples:
    ```bash
    curl -X GET "http://localhost:5010/api/shipsdata/"
    curl -X DELETE "http://localhost:5010/api/shipsdata/"
    ```
     