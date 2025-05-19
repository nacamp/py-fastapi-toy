
## case: developping

- directory
https://fastapi.tiangolo.com/tutorial/bigger-applications/
- dependencies : router에서 path 접근전에 체크(jwt)
https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/#dependencies-for-groups-of-path-operations
- Lifespan Events
https://fastapi.tiangolo.com/advanced/events/
- di
https://fastapi.tiangolo.com/tutorial/dependencies/#declare-the-dependency-in-the-dependant

## install pyjwt
```
poetry add pyjwt
```

## install sqlmodel
```bash
poetry add sqlmodel
poetry add bcrypt
poetry add "pydantic[email]"
```
## run
```bash
uvicorn main:app --reload
or
fastapi dev main.py
```
## install fastapi
```bash
mkdir py-fastapi-toy
cd py-fastapi-toy
poetry init
poetry add "fastapi[standard]"
poetry add "uvicorn[standard]"
```