# Alpha Apparel Developer Journal

---

## Day 1

Repository created.

Established project vision.

Defined MVP.

Created roadmap.

Next:

Design project architecture.

## Day 2
Development Notes

Python Version

3.13.3

Virtual Environment

.\.venv\Scripts\Activate.ps1

## Day 3
What did we build?
SQLAlchemy configuration
Declarative Base
First database model
SQLite database
Database inspection tool

What did we learn?
Difference between working directory and script location.
python script.py behaves differently than python -m package.module.
sys.path determines how imports are resolved.
SQLAlchemy builds tables from metadata.
__repr__ makes debugging dramatically easier.

What should Future Us remember?
When writing developer tools inside the project, prefer running them as modules (python -m ...) instead of directly executing the script.

I think today's journal entry is going to be one of our strongest.

What did we build?
add_ticker.py
automatic timestamps
database persistence
querying with SQLAlchemy
enhanced inspection tool
What did we learn?


The difference between defining a schema and storing data.
Why model defaults belong in the model.
The difference between default=function and default=function().
Why python -m matters for package execution.
The distinction between:
current working directory
script location
sys.path

Those are lessons that will keep paying dividends.

What should Future Us remember?
Developer utilities belong in backend/tools/ and should be run as modules (python -m tools.<tool_name>).

## Day 4
What did we build?
First REST API endpoint
Database dependency injection
Automatic session management
Querying through HTTP

What did we learn?
yield pauses a function instead of ending it.
finally always executes, even if an exception occurs.
FastAPI dependency injection keeps endpoint code clean.
Models represent database tables.
Schemas represent API contracts.

What should Future Us remember?
Endpoints should focus on business logic. Resource management (database sessions, authentication, etc.) belongs in reusable dependencies.

What did we build?
API routers
Cleaner application structure
Automatic OpenAPI documentation
Better separation of responsibilities

What did we learn?
APIRouter represents one area of the application.
main.py should compose the application, not implement it.
FastAPI generates documentation from our type hints and schemas.
Refactoring should preserve behavior while improving structure.

Future Us
If a file begins accumulating unrelated responsibilities, ask whether it deserves its own module rather than continuing to grow.
That's essentially what we did today.

