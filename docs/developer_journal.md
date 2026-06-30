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


