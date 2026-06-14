import azure.functions as func

import logging
 
# Initialize the Function App

app = func.FunctionApp(auth_level=func.AuthLevel.ANONYMOUS)
 
# Define the HTTP Trigger

@app.route(route="HttpExample")

def HttpExample(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
 
    # Try to get 'name' from the URL query string

    name = req.params.get('name')

    # If not in URL, try to get 'name' from the JSON request body

    if not name:

        try:

            req_body = req.get_json()

        except ValueError:

            req_body = None

        if req_body:

            name = req_body.get('name')
 
    # Return the response

    if name:

        return func.HttpResponse(f"Hello, {name}. This Azure Function executed successfully.")

    else:

        return func.HttpResponse(

             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",

             status_code=200

        )

 
