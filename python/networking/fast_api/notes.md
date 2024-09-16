# FastAPI

## Setup Notes
- `pip install "fastapi[standard]` to install the FastAPI.
- To run the application in development mode you should use `fastapi dev main.py` assuming your code is main.py.
    - By default, FastAPI would run on the `127.0.0.1:8000`, `localhost` port `8000` in he development mode.
- To run the application in production mode you should use `fastapi run main.py` assuming your code is main.py.
    - By default, FastAPI would run on the `0.0.0.0:8000`, in `HTTP` mode

## Paths Parameters
- You would get a error if the type does not match with the required type.
    - Error code is `422` which means `unprocessable entitiy`
- Also, it is possible to use EnumClass to accept some specific values. 

## After Deployment
- `http://127.0.0.1:8000/openapi.json` to get the API schema.


## Deployment for Production
> It is a common practice to have one program/HTTP server running on the server (the machine, host, etc.) and managing all the HTTPS parts: receiving the encrypted HTTPS requests, sending the decrypted HTTP requests to the actual HTTP application running in the same server (the FastAPI application, in this case), take the HTTP response from the application, encrypt it using the appropriate HTTPS certificate and sending it back to the client using HTTPS. This server is often called a TLS Termination Proxy.
> Some of the options you could use as a TLS Termination Proxy are:
> - Traefik (that can also handle certificate renewals)
> - Caddy (that can also handle certificate renewals)
> - Nginx
> - HAProxy\
> --<cite>[FastAPI Documentation](https://fastapi.tiangolo.com/deployment/)</cite>
