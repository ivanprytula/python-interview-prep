<!--
.. title: Knowledge Scope
.. slug: knowledge-scope
.. date: 2022-04-18 15:22:12 UTC+03:00
.. description: Scopes of desired knowledge
.. type: text
-->

**Scopes of desired knowledge**  
 - [x] OpenEDG Python Institute certification exams  _[[Syllabus](#section1)]_  
```python
certifications_levels_desc: dict[str, dict] = {
    "PCEP": {
        "full_name": "Certified Entry-Level Python Programmer",
        "codes": ["PCEP-30-01", "PCEP-30-02"],
    },
    "PCAP": {
        "full_name": "Certified Associate in Python Programming",
        "codes": ["PCAP-31-02", "PCAP-31-03"],
    },
    "PCPP1": {
        "full_name": "Certified Professional in Python Programming 1",
        "codes": ["PCPP-32-101"],
    },
    "PCPP2": {
        "full_name": "Certified Professional in Python Programming 2",
        "codes": ["PCPP-32-201"],
    },
}
```
 - [ ] some book1... 

---

<div id="#section1"></div>

# PCAP – Certified Associate in Python Programming PCAP-31-0x
## Objectives
1. Objectives of Entry-Level plus...
2. Objectives of Entry-Level plus...
3. Objectives of Entry-Level plus...
4. Objectives of Entry-Level plus...
5. Python modules: their rationale, function, how to import them in different ways,
   and present the content of some standard modules provided by Python;
   the way in which modules are coupled together to make packages;
   the concept of an exception and Python’s implementation of exceptions,
   including the _try-except_ instruction, with its applications, and the _raise_ instruction;
   strings and their specific methods, together with their similarities and differences compared to the lists;

6. The fundamentals of OOP and the way they are adopted in Python,
   showing the difference between OOP and the classical, procedural approach;
   the standard objective features: inheritance, abstraction, encapsulation, and polymorphism,
   along with Python-specific issues like instance vs. class variables, and Python’s implementation of inheritance;
   objective nature of exceptions; Python’s generators (the _yield_ instruction) and closures (the _lambda_ keyword);
   the means Python developers can use to process (create, read, and write) files.

### Syllabus PCAP-31-02 (PVTCs)
#### Block 1: Control and Evaluations
- basic concepts: interpreting and the interpreter, compilation and the compiler, language elements, lexis, syntax and semantics, Python keywords, instructions, indenting
- literals: Boolean, integer, floating-point numbers, scientific notation, strings
- operators: unary and binary, priorities and binding
- numeric operators: ** * / % // + –
- bitwise operators: ~ & ^ | << >>
- string operators: * +
- Boolean operators: **not and or**
- relational operators ( == != > >= < <= ), building complex Boolean expressions
- assignments and shortcut operators
- accuracy of floating-point numbers
- basic input and output: **input(), print(), int(), float(), str()** functions
- formatting **print()** output with **end=** and **sep=** arguments
- conditional statements: **if, if-else, if-elif, if-elif-else**
- the **pass** instruction
- simple lists: constructing vectors, indexing and slicing, the **len()** function
- simple strings: constructing, assigning, indexing, slicing comparing, immutability
- building loops: **while, for, range(), in**, iterating through sequences
- expanding loops: **while-else, for-else**, nesting loops and conditional statements
- controlling loop execution: **break, continue**

#### Block 2: Data Aggregates
- strings in detail: ASCII, UNICODE, UTF-8, immutability, escaping using the "\" character,
  quotes and apostrophes inside strings, multiline strings, copying vs. cloning, advanced slicing,
  string vs. string, string vs. non-string,
  basic string methods (**upper(), lower(), isxxx(), capitalize(), split(), join()**, etc.)
  and functions (len(), chr(), ord()), escape characters
- lists in detail: indexing, slicing, basic methods (**append(), insert(), index()**)
  and functions (**len(), sorted()**, etc.), **del** instruction, iterating lists with the **for** loop,
  initializing, **in** and **not in** operators, list comprehension, copying and cloning
- lists in lists: matrices and cubes
- tuples: indexing, slicing, building, immutability
- tuples vs. lists: similarities and differences, lists inside tuples and tuples inside lists
- dictionaries: building, indexing, adding and removing keys,
  iterating through dictionaries as well as their keys and values,
  checking key existence, **keys(), items()** and **values()** methods

#### Block 3: Functions and Modules
- defining and invoking your own functions and generators
- **return** and **yield** keywords, returning results, the **None** keyword, recursion
- parameters vs. arguments, positional keyword and mixed argument passing, default parameter values
- converting generator objects into lists using the **list()** function
- name scopes, name hiding (shadowing), the **global** keyword
- **lambda** functions, defining and using **map(), filter(), reduce(), reversed(), sorted()** functions, and the **sort()** method
- the **if** operator
- import directives, qualifying entities with module names, initializing modules
- writing and using modules, the **\__name\__** variable
- **pyc** file creation and usage
- constructing and distributing packages, packages vs. directories, the role of the **\__init\__.py** file
- hiding module entities
- Python hashbang, using multiline strings as module documentation

#### Block 4: Classes, Objects, and Exceptions
- defining your own classes, superclasses, subclasses, inheritance,
  searching for missing class components, creating objects
- class attributes: class variables and instance variables, defining,
  adding and removing attributes, explicit constructor invocation
- class methods: defining and using, the **self** parameter meaning and usage
- inheritance and overriding, finding class/object components
- single inheritance vs. multiple inheritance
- name mangling
- invoking methods, passing and using the **self** argument/parameter
- the **\__init\__** method
- the role of the **\__str\__** method
- introspection: **\__dict\__**, **\__name\__**, **\__module\__**, **\__bases\__** properties,
  examining class/object structure
- writing and using constructors
- **hasattr(), type(), issubclass(), isinstance(), super()** functions
- using predefined exceptions and defining your own ones
- the **try-except-else-finally** block, the **raise** statement, the **except-as** variant
- exceptions hierarchy, assigning more than one exception to one **except** branch
- adding your own exceptions to an existing hierarchy
- assertions
- the anatomy of an exception object
- input/output basics: opening files with the **open()** function, stream objects, binary vs. text files,
  newline character translation, reading and writing files, **bytearray** objects
- **read(), readinto(), readline(), write(), close()** methods

### Syllabus PCAP-31-03 (PVTCs, OnVUE)
#### Block 1: Modules and Packages
- import variants; advanced qualifying for nested modules
- dir(); sys.path variable
- math: ceil(), floor(), trunc(), factorial(), hypot(), sqrt(); random: random(), seed(), choice(), sample()
- platform: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()
- idea, __pycache__, __name__, public variables, __init__.py
- searching for modules/packages; nested packages vs directory tree

#### Block 2: Exceptions
- except, except:-except; except:-else:, except (e1,e2)
- the hierarchy of exceptions
- raise, raise ex, assert
- event classes, except E as e, arg property
- self-defined exceptions, defining and using

#### Block 3: Strings
- ASCII, UNICODE, UTF-8, codepoints, escape sequences
- ord(), chr(), literals
- indexing, slicing, immutability
- iterating through,
- concatenating, multiplying, comparing (against strings and numbers)
- in, not in
- .isxxx(), .join(), .split()
- .sort(), sorted(), .index(), .find(), .rfind()

#### Block 4: Object-Oriented Programming
- ideas: class, object, property, method, encapsulation, inheritance, grammar vs class, superclass, subclass
- instance vs class variables: declaring, initializing
- __dict__ property (objects vs classes)
- private components (instance vs classes), name mangling
- methods: declaring, using, self parameter
- instrospection: hasattr() (objects vs classes), __name__, __module__, __bases__ properties
- inheritance: single, multiple, isinstance(), overriding, not is and is operators
- inheritance: single, multiple, isinstance(), overriding, not is and is operators
- constructors: declaring and invoking
- polymorphism
- __name__, __module__, __bases__ properties, __str__() method
- multiple inheritance, diamonds

#### Block 5: Miscellaneous (List Comprehensions, Lambdas, Closures, and I/O Operations)
- list comprehension: if operator, using list comprehensions
- lambdas: defining and using lambdas, self-defined functions taking lambda as as arguments; map(), filter();
- closures: meaning, defining, and using closures
- I/O Operations: I/O modes, predefined streams, handles; text/binary modes
- open(), errno and its values; close()
- .read(), .write(), .readline(); readlines() (along with bytearray())

---

# PCPP1 – Certified Professional in Python Programming 1 PCPP-32-10x
### Syllabus PCPP-32-101
#### Block 1: Advanced Perspective of Classes and OOP in Python
- Classes, Instances, Attributes, Methods;
- Working with class and instance data;
- Copying object data using _shallow_ and _deep_ operations;
- Inheritance and Polymorphism;
- Different faces of Python methods: _static_ and _class_ methods;
- Abstract classes vs. method overloading;
- Composition vs. Inheritance – two ways to the same destination;
- Implementing Core Syntax;
- Subclassing built-ins;
- Attribute Encapsulation;
- Advanced techniques of creating and serving exceptions;
- Serialization of Python objects using the _pickle_ module;
- Making Python object persistent using the _shelve_ module;
- Metaprogramming (function decorators, class decorators, metaclasses.)

#### Block 2: Python Enhancement Proposals (PEP)
- What is PEP?
- Coding conventions – not only style and naming;
- _PEP 20_ – The Zen of Python: a collection of principles that influences the design of Python code;
- _PEP 8_ – Style Guide for Python Code: coding conventions for code comprising the STL in the main Python distribution;
- _PEP 257_ – Docstring Conventions: what is _docstring_, and some semantics as well as conventions associated with them;
- A tour of other important PEPs.

#### Block 3: GUI Programming
- What is GUI and where it comes from;
- Constructing a GUI – basic blocks and conventions;
- Event-driven programming;
- Popular GUI environments and toolkits;
- _tkinter_  Python interface to Tcl/Tk ( tkinter’s application life cycle; widgets, windows and events; sample applications)
- _pygame_ – a simple way of developing multimedia applications.

#### Block 4: The Elements of Network Programming: Working with RESTful APIs
- the basic concepts of network programming, REST, network sockets, and client-server communication;
- How to use and create sockets in Python;
- how to establish and close the connection with a server;
- JSON and XML files, and how they can be used in network communication;
- HTTP methods, and how to say anything in HTTP;
- How to build a sample testing environment;
- CRUD;
- How to build a simple REST client;
- how to fetch and remove data from servers;
- how to add new data to servers and update the already-existing data.

#### Block 5: File Processing and Communicating with a Program’s Environment
- Processing files:
    - _sqlite3_ – interacting with SQLite databases;
    - _xml_ – creating and processing XML files;
    - _csv_ – CSV file reading and writing;
    - _logging_ – basics logging facility for Python;
    - _configparser_ – configuration file parser.
- Communicating with a program’s environment:
    - _os_ – interacting with the operating system;
    - _datetime_ – manipulating with dates and time;
    - _io_ – working with streams;
    - _time_ – time access and conversions.

---

# PCPP2 – Certified Professional in Python Programming 2 PCPP-32-20x
### Syllabus PCPP-32-201
#### Block 1: Creating and Distributing Packages
- Using _pip_
- Basic directory structure
- The _setup.py_ file
- Sharing, storing, and installing packages
- Documentation
- License
- Testing principles and techniques
    - **unittest** – Unit testing framework
    - **Pytest** – framework to write tests

#### Block 2: Design Patterns
- Object-oriented design principles and the concept of design patterns
- The _Singleton_ Design Pattern
- The _Factory_ Pattern
- The _Façade_ Pattern
- The _Proxy_ Pattern
- The _Observer_ Pattern
- The _Command_ Pattern
- The _Template Method_ Pattern
- Model-View-Controller
- The _State Design_ Pattern

#### Block 3: Interprocess Communication
- multiprocessing — Process-based parallelism
- threading — Thread-based parallelism
- subprocess — Subprocess management
- Multiprocess synchronisation
    - **queue** — A synchronized queue class
    - **socket** — Low-level networking interface
    - **mmap** — Memory-mapped file support

#### Block 4: Python Network Programming
- Python Socket Module
    - Introduction to sockets
    - Server Socket Methods
    - Client socket methods
    - General socket methods
    - Client-Server vs. Peer-to-peer
    - Other Internet modules

#### Block 5: Python-MySQL Database Access
- Relational databases – fundamental principles and how to work with them
- MySQL vs. rest of the world
- **CRUD** Application
    - db connection
    - db create
    - db insert
    - db read
    - db update
    - db delete
