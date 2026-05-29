from datetime import datetime, timezone

# Programming aptitude questions
# 4 topics × 3 difficulties × 6 questions = 72 total
# Selected at runtime: 1 easy + 1 medium + 1 hard per topic = 12 per subject
# question_format: multiple_choice
# correct_answer: the label (A/B/C/D)
#
# Topics:
#   1. Fundamentals       — variables, data types, control flow, basic I/O
#   2. OOP & Design       — classes, objects, inheritance, encapsulation
#   3. Algorithms & DS    — sorting, searching, complexity, arrays, stacks
#   4. Web & Databases    — HTML/CSS basics, SQL, HTTP, client-server model

APTITUDE_PROGRAMMING_QUESTIONS = [

    # ════════════════════════════════════════
    # TOPIC: FUNDAMENTALS
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "Which of the following is a valid variable name in most programming languages?",
     "options": [{"label": "A", "value": "2myVar"}, {"label": "B", "value": "my-var"}, {"label": "C", "value": "myVar"}, {"label": "D", "value": "my var"}],
     "correct_answer": "C", "explanation": "Variable names cannot start with a digit, contain hyphens, or have spaces. 'myVar' follows standard naming rules.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "What is the output of: print(10 % 3)?",
     "options": [{"label": "A", "value": "3"}, {"label": "B", "value": "1"}, {"label": "C", "value": "0"}, {"label": "D", "value": "3.33"}],
     "correct_answer": "B", "explanation": "The % operator returns the remainder of division. 10 ÷ 3 = 3 remainder 1.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "Which data type would best store the value True or False?",
     "options": [{"label": "A", "value": "int"}, {"label": "B", "value": "float"}, {"label": "C", "value": "boolean"}, {"label": "D", "value": "string"}],
     "correct_answer": "C", "explanation": "A boolean (bool) data type stores only two values: True or False.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "What does an 'if' statement do in programming?",
     "options": [{"label": "A", "value": "Repeats a block of code"}, {"label": "B", "value": "Defines a function"}, {"label": "C", "value": "Executes code only when a condition is true"}, {"label": "D", "value": "Imports a library"}],
     "correct_answer": "C", "explanation": "An 'if' statement evaluates a condition; the code block inside only runs when that condition is true.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "Which of the following best describes a 'loop' in programming?",
     "options": [{"label": "A", "value": "A way to store data"}, {"label": "B", "value": "A structure that repeats a block of code"}, {"label": "C", "value": "A type of variable"}, {"label": "D", "value": "A way to define a class"}],
     "correct_answer": "B", "explanation": "A loop (for, while) repeats a block of code multiple times until a condition is met.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "easy",
     "text": "What symbol is commonly used for single-line comments in Python?",
     "options": [{"label": "A", "value": "//"}, {"label": "B", "value": "/*"}, {"label": "C", "value": "#"}, {"label": "D", "value": "--"}],
     "correct_answer": "C", "explanation": "In Python, the # symbol starts a single-line comment. (//) is used in JavaScript/C++.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "What is the output of the following code?\nx = 5\nif x > 3:\n    print('A')\nelif x > 1:\n    print('B')\nelse:\n    print('C')",
     "options": [{"label": "A", "value": "A"}, {"label": "B", "value": "B"}, {"label": "C", "value": "C"}, {"label": "D", "value": "A and B"}],
     "correct_answer": "A", "explanation": "x=5 satisfies 'x > 3' first. Once a condition is true, the rest of the elif/else chain is skipped.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "How many times does the following loop execute?\nfor i in range(2, 10, 3):",
     "options": [{"label": "A", "value": "2"}, {"label": "B", "value": "3"}, {"label": "C", "value": "4"}, {"label": "D", "value": "8"}],
     "correct_answer": "B", "explanation": "range(2, 10, 3) generates: 2, 5, 8 — three values. i=11 would exceed 10, so it stops.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "What is the difference between '==' and '=' in most programming languages?",
     "options": [{"label": "A", "value": "No difference"}, {"label": "B", "value": "'==' assigns a value; '=' compares values"}, {"label": "C", "value": "'=' assigns a value; '==' compares values"}, {"label": "D", "value": "'==' is only used in loops"}],
     "correct_answer": "C", "explanation": "'=' is the assignment operator (stores a value); '==' is the equality operator (checks if two values are equal).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "What does the following function return?\ndef add(a, b):\n    return a + b\nresult = add(3, 4)",
     "options": [{"label": "A", "value": "None"}, {"label": "B", "value": "34"}, {"label": "C", "value": "7"}, {"label": "D", "value": "add"}],
     "correct_answer": "C", "explanation": "The function adds its two parameters. add(3, 4) returns 3 + 4 = 7.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "What is a 'null' or 'None' value in programming?",
     "options": [{"label": "A", "value": "The value 0"}, {"label": "B", "value": "An empty string"}, {"label": "C", "value": "The absence of a value"}, {"label": "D", "value": "A boolean False"}],
     "correct_answer": "C", "explanation": "null/None represents the intentional absence of any value — it is not 0, False, or an empty string.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "medium",
     "text": "Which of the following correctly describes a 'stack overflow' error?",
     "options": [{"label": "A", "value": "Running out of hard disk space"}, {"label": "B", "value": "Infinite recursion exceeding the call stack limit"}, {"label": "C", "value": "Dividing a number by zero"}, {"label": "D", "value": "Accessing an index outside an array"}],
     "correct_answer": "B", "explanation": "A stack overflow occurs when a program's call stack exceeds its limit, typically due to infinite or deeply nested recursion.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What does the following Python code output?\nresult = [x**2 for x in range(5) if x % 2 == 0]\nprint(result)",
     "options": [{"label": "A", "value": "[0, 4, 16]"}, {"label": "B", "value": "[1, 9, 25]"}, {"label": "C", "value": "[0, 1, 4, 9, 16]"}, {"label": "D", "value": "[4, 16]"}],
     "correct_answer": "A", "explanation": "range(5) = 0,1,2,3,4. Filter even (% 2 == 0): 0, 2, 4. Square each: 0, 4, 16.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What is the output of this code?\ndef mystery(n):\n    if n <= 1:\n        return n\n    return mystery(n-1) + mystery(n-2)\nprint(mystery(6))",
     "options": [{"label": "A", "value": "6"}, {"label": "B", "value": "8"}, {"label": "C", "value": "13"}, {"label": "D", "value": "21"}],
     "correct_answer": "B", "explanation": "This is a Fibonacci function. mystery(6) = F(6) = 0,1,1,2,3,5,8 → 8.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What is the time complexity of accessing an element in a Python list by index?",
     "options": [{"label": "A", "value": "O(n)"}, {"label": "B", "value": "O(log n)"}, {"label": "C", "value": "O(1)"}, {"label": "D", "value": "O(n²)"}],
     "correct_answer": "C", "explanation": "Python lists are backed by arrays in memory. Index access is O(1) — constant time — regardless of list size.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What is the difference between pass-by-value and pass-by-reference?",
     "options": [{"label": "A", "value": "They are the same thing"}, {"label": "B", "value": "Pass-by-value sends a copy; pass-by-reference sends the actual memory address"}, {"label": "C", "value": "Pass-by-reference only works with integers"}, {"label": "D", "value": "Pass-by-value is faster but uses more memory"}],
     "correct_answer": "B", "explanation": "Pass-by-value gives the function a copy (changes don't affect the original). Pass-by-reference gives the function direct access to the original variable.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What does 'scope' mean in programming?",
     "options": [{"label": "A", "value": "The size of a variable in memory"}, {"label": "B", "value": "The region of code where a variable is accessible"}, {"label": "C", "value": "The speed at which code executes"}, {"label": "D", "value": "The number of times a loop runs"}],
     "correct_answer": "B", "explanation": "Scope defines where a variable can be accessed. A local variable only exists inside its function; a global variable is accessible throughout the program.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "fundamentals", "difficulty": "hard",
     "text": "What is the output?\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
     "options": [{"label": "A", "value": "[1, 2, 3]"}, {"label": "B", "value": "[1, 2, 3, 4]"}, {"label": "C", "value": "[4]"}, {"label": "D", "value": "Error"}],
     "correct_answer": "B", "explanation": "In Python, 'y = x' does not copy the list — both variables point to the same object. Appending to y also modifies x.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: OOP & DESIGN
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "In Object-Oriented Programming (OOP), what is a 'class'?",
     "options": [{"label": "A", "value": "A running instance of a program"}, {"label": "B", "value": "A blueprint for creating objects"}, {"label": "C", "value": "A type of loop"}, {"label": "D", "value": "A stored value"}],
     "correct_answer": "B", "explanation": "A class is a template or blueprint that defines the attributes and methods that objects of that class will have.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "What is an 'object' in OOP?",
     "options": [{"label": "A", "value": "A method inside a class"}, {"label": "B", "value": "A variable that holds a number"}, {"label": "C", "value": "An instance of a class"}, {"label": "D", "value": "A type of condition"}],
     "correct_answer": "C", "explanation": "An object is a specific instance created from a class, with its own set of attribute values.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "Which OOP principle means hiding the internal details of an object?",
     "options": [{"label": "A", "value": "Inheritance"}, {"label": "B", "value": "Polymorphism"}, {"label": "C", "value": "Encapsulation"}, {"label": "D", "value": "Abstraction"}],
     "correct_answer": "C", "explanation": "Encapsulation bundles data and methods together and restricts direct access to internal state.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "What does 'inheritance' mean in OOP?",
     "options": [{"label": "A", "value": "An object calling its own methods"}, {"label": "B", "value": "A child class acquiring properties of a parent class"}, {"label": "C", "value": "Hiding data from the user"}, {"label": "D", "value": "Two classes sharing the same name"}],
     "correct_answer": "B", "explanation": "Inheritance allows a subclass (child) to reuse and extend the attributes and methods of a superclass (parent).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "In a class, what is a 'method'?",
     "options": [{"label": "A", "value": "A stored value"}, {"label": "B", "value": "A function defined inside a class"}, {"label": "C", "value": "A class variable"}, {"label": "D", "value": "An imported module"}],
     "correct_answer": "B", "explanation": "A method is a function that belongs to a class and typically operates on the object's data.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "easy",
     "text": "What keyword is used to create an instance of a class in most OOP languages?",
     "options": [{"label": "A", "value": "create"}, {"label": "B", "value": "define"}, {"label": "C", "value": "new"}, {"label": "D", "value": "make"}],
     "correct_answer": "C", "explanation": "The 'new' keyword (in Java, JavaScript, C++) instantiates a class. Python uses the class name directly, e.g., Dog().", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "What is polymorphism in OOP?",
     "options": [{"label": "A", "value": "A class inheriting from multiple parents"}, {"label": "B", "value": "The ability of different objects to respond to the same method in different ways"}, {"label": "C", "value": "Restricting access to class attributes"}, {"label": "D", "value": "Defining a method inside a loop"}],
     "correct_answer": "B", "explanation": "Polymorphism allows objects of different classes to be treated through the same interface, each implementing the behaviour in its own way.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "What is method overriding?",
     "options": [{"label": "A", "value": "Defining two methods with the same name but different parameters in the same class"}, {"label": "B", "value": "A child class providing its own implementation of a method inherited from a parent"}, {"label": "C", "value": "Calling a method before the object is created"}, {"label": "D", "value": "Removing a method from a parent class"}],
     "correct_answer": "B", "explanation": "Method overriding lets a subclass replace the parent's implementation with its own version of the same method.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "What is the purpose of a constructor (__init__ in Python)?",
     "options": [{"label": "A", "value": "To delete an object"}, {"label": "B", "value": "To define class-level constants"}, {"label": "C", "value": "To initialize an object's attributes when it is created"}, {"label": "D", "value": "To inherit from a parent class"}],
     "correct_answer": "C", "explanation": "A constructor is called automatically when an object is created, setting up its initial state.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "What does the 'super()' keyword do in Python?",
     "options": [{"label": "A", "value": "Creates a new class"}, {"label": "B", "value": "Calls a method from the parent class"}, {"label": "C", "value": "Makes a variable global"}, {"label": "D", "value": "Deletes an object"}],
     "correct_answer": "B", "explanation": "'super()' gives access to methods of the parent (super) class, commonly used in constructors to run the parent's __init__.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "What is the difference between an abstract class and an interface?",
     "options": [{"label": "A", "value": "They are the same thing"}, {"label": "B", "value": "Abstract classes can have some implemented methods; interfaces only declare method signatures"}, {"label": "C", "value": "Interfaces can be instantiated; abstract classes cannot"}, {"label": "D", "value": "Abstract classes are used in Python; interfaces are used in Java only"}],
     "correct_answer": "B", "explanation": "Abstract classes can include both abstract (unimplemented) and concrete (implemented) methods. Interfaces (in languages like Java) declare only method signatures with no implementation.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "medium",
     "text": "Which design principle states that a class should have only one reason to change?",
     "options": [{"label": "A", "value": "Open/Closed Principle"}, {"label": "B", "value": "Liskov Substitution Principle"}, {"label": "C", "value": "Single Responsibility Principle"}, {"label": "D", "value": "Dependency Inversion Principle"}],
     "correct_answer": "C", "explanation": "The Single Responsibility Principle (SRP) states each class should do one thing and have only one reason to be modified.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "What is the output of the following Python code?\nclass Animal:\n    def speak(self): return 'generic'\nclass Dog(Animal):\n    def speak(self): return 'woof'\nclass Cat(Animal):\n    def speak(self): return 'meow'\nanimals = [Dog(), Cat(), Animal()]\nprint([a.speak() for a in animals])",
     "options": [{"label": "A", "value": "['generic', 'generic', 'generic']"}, {"label": "B", "value": "['woof', 'meow', 'generic']"}, {"label": "C", "value": "Error"}, {"label": "D", "value": "['woof', 'meow']"}],
     "correct_answer": "B", "explanation": "Each object calls its own overridden speak() method. This is runtime polymorphism.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "What is the Liskov Substitution Principle?",
     "options": [{"label": "A", "value": "A class should be open for extension but closed for modification"}, {"label": "B", "value": "Objects of a subclass should be replaceable for objects of the superclass without breaking the program"}, {"label": "C", "value": "High-level modules should not depend on low-level modules"}, {"label": "D", "value": "Each class should have only one responsibility"}],
     "correct_answer": "B", "explanation": "LSP states that wherever a parent class is used, a subclass object can be substituted without altering the correctness of the program.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "What design pattern is used when you want only one instance of a class to exist throughout the application?",
     "options": [{"label": "A", "value": "Factory"}, {"label": "B", "value": "Observer"}, {"label": "C", "value": "Singleton"}, {"label": "D", "value": "Decorator"}],
     "correct_answer": "C", "explanation": "The Singleton pattern ensures a class has only one instance and provides a global point of access to it.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "In Python, what is the difference between a class variable and an instance variable?",
     "options": [{"label": "A", "value": "There is no difference"}, {"label": "B", "value": "Class variables are shared across all instances; instance variables are unique to each object"}, {"label": "C", "value": "Instance variables are defined in __init__; class variables are defined outside all methods but cannot be accessed by instances"}, {"label": "D", "value": "Class variables are faster to access"}],
     "correct_answer": "B", "explanation": "Class variables are defined in the class body and shared by all instances. Instance variables (set in __init__ with self.) are unique to each object.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "What is composition over inheritance and why is it preferred?",
     "options": [{"label": "A", "value": "Using loops instead of functions for cleaner code"}, {"label": "B", "value": "Building complex classes by combining simpler objects rather than extending class hierarchies"}, {"label": "C", "value": "Replacing all methods with static functions"}, {"label": "D", "value": "Avoiding the use of classes entirely"}],
     "correct_answer": "B", "explanation": "Composition (has-a relationship) is often preferred over inheritance (is-a) because it leads to looser coupling, easier testing, and more flexible design.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "oop_and_design", "difficulty": "hard",
     "text": "What does the Observer design pattern do?",
     "options": [{"label": "A", "value": "Ensures only one instance of a class exists"}, {"label": "B", "value": "Lets a subject notify multiple observer objects automatically when its state changes"}, {"label": "C", "value": "Provides a simplified interface to a complex subsystem"}, {"label": "D", "value": "Creates objects without specifying the exact class"}],
     "correct_answer": "B", "explanation": "The Observer pattern defines a one-to-many dependency: when the subject changes state, all registered observers are notified and updated automatically.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: ALGORITHMS & DATA STRUCTURES
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "What data structure operates on a First-In, First-Out (FIFO) principle?",
     "options": [{"label": "A", "value": "Stack"}, {"label": "B", "value": "Queue"}, {"label": "C", "value": "Tree"}, {"label": "D", "value": "Graph"}],
     "correct_answer": "B", "explanation": "A queue is FIFO — the first element added is the first to be removed (like a line of people).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "What data structure operates on a Last-In, First-Out (LIFO) principle?",
     "options": [{"label": "A", "value": "Queue"}, {"label": "B", "value": "Array"}, {"label": "C", "value": "Stack"}, {"label": "D", "value": "Linked list"}],
     "correct_answer": "C", "explanation": "A stack is LIFO — the last element added is the first to be removed (like a stack of plates).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "In an array of 5 elements, what is the index of the last element?",
     "options": [{"label": "A", "value": "5"}, {"label": "B", "value": "4"}, {"label": "C", "value": "6"}, {"label": "D", "value": "0"}],
     "correct_answer": "B", "explanation": "Arrays use 0-based indexing. An array with 5 elements has indices 0, 1, 2, 3, 4. The last index is 4.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "What does O(1) time complexity mean?",
     "options": [{"label": "A", "value": "The algorithm never finishes"}, {"label": "B", "value": "The algorithm is the fastest possible"}, {"label": "C", "value": "The algorithm takes constant time regardless of input size"}, {"label": "D", "value": "The algorithm loops once"}],
     "correct_answer": "C", "explanation": "O(1) — constant time — means the operation takes the same time regardless of how large the input is.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "What is a 'key-value' data structure that provides fast lookup?",
     "options": [{"label": "A", "value": "Array"}, {"label": "B", "value": "Stack"}, {"label": "C", "value": "Dictionary / Hash map"}, {"label": "D", "value": "Queue"}],
     "correct_answer": "C", "explanation": "A dictionary (hash map) stores data as key-value pairs, enabling average O(1) lookups by key.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "easy",
     "text": "Which sorting algorithm repeatedly compares adjacent elements and swaps them if out of order?",
     "options": [{"label": "A", "value": "Merge sort"}, {"label": "B", "value": "Quick sort"}, {"label": "C", "value": "Bubble sort"}, {"label": "D", "value": "Binary search"}],
     "correct_answer": "C", "explanation": "Bubble sort compares adjacent pairs and bubbles the largest unsorted element to the end in each pass.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "What is the time complexity of binary search on a sorted array of n elements?",
     "options": [{"label": "A", "value": "O(n)"}, {"label": "B", "value": "O(n²)"}, {"label": "C", "value": "O(log n)"}, {"label": "D", "value": "O(1)"}],
     "correct_answer": "C", "explanation": "Binary search halves the search space each step, giving O(log n) time complexity.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "In a singly linked list, what does each node contain?",
     "options": [{"label": "A", "value": "Only data"}, {"label": "B", "value": "Data and a pointer to the next node"}, {"label": "C", "value": "A key and a value"}, {"label": "D", "value": "Two pointers: previous and next"}],
     "correct_answer": "B", "explanation": "Each node in a singly linked list stores its data and a pointer (reference) to the next node.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "What is a binary tree?",
     "options": [{"label": "A", "value": "A tree that stores only 0s and 1s"}, {"label": "B", "value": "A tree where each node has at most two children"}, {"label": "C", "value": "A tree with exactly two levels"}, {"label": "D", "value": "A sorted array represented as a tree"}],
     "correct_answer": "B", "explanation": "In a binary tree, each node has a maximum of two child nodes: left and right.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "Which traversal visits the root node first, then left, then right subtrees?",
     "options": [{"label": "A", "value": "In-order"}, {"label": "B", "value": "Post-order"}, {"label": "C", "value": "Level-order"}, {"label": "D", "value": "Pre-order"}],
     "correct_answer": "D", "explanation": "Pre-order traversal: Root → Left → Right. In-order: Left → Root → Right. Post-order: Left → Right → Root.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "What is the worst-case time complexity of bubble sort?",
     "options": [{"label": "A", "value": "O(n log n)"}, {"label": "B", "value": "O(n)"}, {"label": "C", "value": "O(n²)"}, {"label": "D", "value": "O(log n)"}],
     "correct_answer": "C", "explanation": "Bubble sort's worst case is O(n²) — for a reverse-sorted array, every pair needs to be compared and swapped.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "medium",
     "text": "What does a hash function do?",
     "options": [{"label": "A", "value": "Sorts data alphabetically"}, {"label": "B", "value": "Maps input data to a fixed-size output (hash code)"}, {"label": "C", "value": "Encrypts data using a password"}, {"label": "D", "value": "Compresses data to save space"}],
     "correct_answer": "B", "explanation": "A hash function maps input of any size to a fixed-size hash code, used for fast lookups in hash tables.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "What is the time complexity of merge sort in all cases?",
     "options": [{"label": "A", "value": "O(n)"}, {"label": "B", "value": "O(n²)"}, {"label": "C", "value": "O(n log n)"}, {"label": "D", "value": "O(log n)"}],
     "correct_answer": "C", "explanation": "Merge sort divides the array (log n levels) and merges n elements at each level — giving O(n log n) in best, average, and worst case.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "What problem does dynamic programming solve most efficiently?",
     "options": [{"label": "A", "value": "Sorting large arrays"}, {"label": "B", "value": "Searching through graphs"}, {"label": "C", "value": "Problems with overlapping subproblems and optimal substructure"}, {"label": "D", "value": "Memory allocation in real time"}],
     "correct_answer": "C", "explanation": "Dynamic programming stores solutions to subproblems (memoization/tabulation) to avoid redundant computation in problems like Fibonacci, knapsack, and shortest paths.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "In a min-heap, what is always true about the root node?",
     "options": [{"label": "A", "value": "It is the largest element"}, {"label": "B", "value": "It is the median element"}, {"label": "C", "value": "It is the smallest element"}, {"label": "D", "value": "It has no children"}],
     "correct_answer": "C", "explanation": "In a min-heap, every parent is smaller than or equal to its children. Therefore the root is always the minimum element.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "What is the space complexity of a recursive Fibonacci implementation without memoization?",
     "options": [{"label": "A", "value": "O(1)"}, {"label": "B", "value": "O(n)"}, {"label": "C", "value": "O(n²)"}, {"label": "D", "value": "O(log n)"}],
     "correct_answer": "B", "explanation": "The call stack depth reaches O(n) in the recursive Fibonacci function (the longest chain from root to leaf).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "Which graph traversal algorithm is best suited for finding the shortest path in an unweighted graph?",
     "options": [{"label": "A", "value": "Depth-First Search (DFS)"}, {"label": "B", "value": "Breadth-First Search (BFS)"}, {"label": "C", "value": "Dijkstra's algorithm"}, {"label": "D", "value": "Merge sort"}],
     "correct_answer": "B", "explanation": "BFS explores level by level, guaranteeing the first path found to any node is the shortest in an unweighted graph.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "algorithms_and_ds", "difficulty": "hard",
     "text": "What is a collision in a hash table and how is it commonly resolved?",
     "options": [{"label": "A", "value": "When two keys map to the same index; resolved by chaining or open addressing"}, {"label": "B", "value": "When an array is full; resolved by doubling its size"}, {"label": "C", "value": "When two values are equal; resolved by removing duplicates"}, {"label": "D", "value": "When a pointer is null; resolved by initializing it to 0"}],
     "correct_answer": "A", "explanation": "A hash collision occurs when two different keys produce the same hash index. Common resolutions: chaining (linked list at each slot) or open addressing (probing for the next empty slot).", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: WEB & DATABASES
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "What does HTML stand for?",
     "options": [{"label": "A", "value": "Hyper Transfer Markup Language"}, {"label": "B", "value": "HyperText Markup Language"}, {"label": "C", "value": "High Text Machine Language"}, {"label": "D", "value": "HyperText Modeling Language"}],
     "correct_answer": "B", "explanation": "HTML — HyperText Markup Language — is the standard language for creating web pages.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "Which SQL command retrieves data from a database table?",
     "options": [{"label": "A", "value": "INSERT"}, {"label": "B", "value": "UPDATE"}, {"label": "C", "value": "DELETE"}, {"label": "D", "value": "SELECT"}],
     "correct_answer": "D", "explanation": "SELECT is the SQL command used to query and retrieve data from one or more tables.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "What does CSS stand for and what is its purpose?",
     "options": [{"label": "A", "value": "Computer Style Sheet — formats databases"}, {"label": "B", "value": "Cascading Style Sheets — controls the visual styling of web pages"}, {"label": "C", "value": "Coding Style System — defines server logic"}, {"label": "D", "value": "Content Style Script — handles page interactions"}],
     "correct_answer": "B", "explanation": "CSS (Cascading Style Sheets) controls the layout, colors, fonts, and overall visual presentation of HTML documents.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "What HTTP status code indicates a successful request?",
     "options": [{"label": "A", "value": "404"}, {"label": "B", "value": "500"}, {"label": "C", "value": "200"}, {"label": "D", "value": "301"}],
     "correct_answer": "C", "explanation": "HTTP 200 OK means the request was successful and the server returned the requested resource.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "Which of the following is a NoSQL database?",
     "options": [{"label": "A", "value": "MySQL"}, {"label": "B", "value": "PostgreSQL"}, {"label": "C", "value": "MongoDB"}, {"label": "D", "value": "SQLite"}],
     "correct_answer": "C", "explanation": "MongoDB is a NoSQL document database. MySQL, PostgreSQL, and SQLite are relational (SQL) databases.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "easy",
     "text": "What does API stand for?",
     "options": [{"label": "A", "value": "Application Program Interface"}, {"label": "B", "value": "Automated Programming Instruction"}, {"label": "C", "value": "Application Programming Interface"}, {"label": "D", "value": "Applied Protocol Integration"}],
     "correct_answer": "C", "explanation": "API — Application Programming Interface — defines how software components communicate with each other.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What is the difference between GET and POST HTTP methods?",
     "options": [{"label": "A", "value": "GET deletes data; POST creates data"}, {"label": "B", "value": "GET retrieves data (visible in URL); POST sends data in the request body"}, {"label": "C", "value": "They are the same"}, {"label": "D", "value": "GET is for HTTPS only; POST is for HTTP only"}],
     "correct_answer": "B", "explanation": "GET appends parameters to the URL and is for retrieving data. POST sends data in the request body, typically for creating or submitting data.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What does this SQL query return?\nSELECT name FROM students WHERE grade > 85 ORDER BY name ASC;",
     "options": [{"label": "A", "value": "All columns for students with grade > 85, sorted by name"}, {"label": "B", "value": "The names of students with grade > 85, sorted alphabetically"}, {"label": "C", "value": "The count of students with grade > 85"}, {"label": "D", "value": "All students, sorted by grade"}],
     "correct_answer": "B", "explanation": "SELECT name retrieves only the name column. WHERE filters for grade > 85. ORDER BY name ASC sorts the results alphabetically.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What is a PRIMARY KEY in a relational database?",
     "options": [{"label": "A", "value": "A column that can have duplicate values"}, {"label": "B", "value": "A column that uniquely identifies each row in a table"}, {"label": "C", "value": "A foreign reference to another table"}, {"label": "D", "value": "The first column of every table"}],
     "correct_answer": "B", "explanation": "A PRIMARY KEY uniquely identifies each record in a table. It cannot be NULL and must be unique.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What is the purpose of an index in a database?",
     "options": [{"label": "A", "value": "To store backup copies of data"}, {"label": "B", "value": "To speed up data retrieval at the cost of additional storage"}, {"label": "C", "value": "To enforce data types on columns"}, {"label": "D", "value": "To link two tables together"}],
     "correct_answer": "B", "explanation": "A database index is a data structure that improves query speed on specific columns at the cost of extra storage and slower write operations.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What does JSON stand for and what is it used for?",
     "options": [{"label": "A", "value": "Java Standard Object Network — for Java programs only"}, {"label": "B", "value": "JavaScript Object Notation — a lightweight format for data exchange"}, {"label": "C", "value": "JavaScript Online Notation — for browser animations"}, {"label": "D", "value": "Java Serialized Object Node — for file storage"}],
     "correct_answer": "B", "explanation": "JSON (JavaScript Object Notation) is a text-based, language-agnostic data format widely used for transmitting data between servers and web clients.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "medium",
     "text": "What is the difference between SQL JOIN types: INNER JOIN vs LEFT JOIN?",
     "options": [{"label": "A", "value": "They are the same"}, {"label": "B", "value": "INNER JOIN returns only matching rows; LEFT JOIN returns all rows from the left table plus matching rows from the right"}, {"label": "C", "value": "LEFT JOIN returns only rows from the left table"}, {"label": "D", "value": "INNER JOIN is faster in all cases"}],
     "correct_answer": "B", "explanation": "INNER JOIN returns rows where there is a match in both tables. LEFT JOIN returns all rows from the left table, with NULLs where there is no match in the right table.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What is database normalization and what does 3NF (Third Normal Form) require?",
     "options": [{"label": "A", "value": "Copying data across tables; 3NF requires three tables minimum"}, {"label": "B", "value": "Organizing a database to reduce redundancy; 3NF requires no transitive dependencies on non-key attributes"}, {"label": "C", "value": "Encrypting database columns; 3NF requires three encryption keys"}, {"label": "D", "value": "Indexing all columns; 3NF requires three indexes per table"}],
     "correct_answer": "B", "explanation": "Normalization reduces data redundancy and improves integrity. 3NF requires the table be in 2NF and have no transitive functional dependencies (non-key attributes depending on other non-key attributes).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What do the ACID properties of a database transaction guarantee?",
     "options": [{"label": "A", "value": "Speed, security, availability, and compression"}, {"label": "B", "value": "Atomicity, Consistency, Isolation, Durability"}, {"label": "C", "value": "Authentication, Caching, Indexing, Distribution"}, {"label": "D", "value": "Auto-scaling, Compression, Integrity, and Decentralization"}],
     "correct_answer": "B", "explanation": "ACID: Atomicity (all or nothing), Consistency (valid state before and after), Isolation (transactions don't interfere), Durability (committed changes persist).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What is a RESTful API and which HTTP method is used to update an existing resource?",
     "options": [{"label": "A", "value": "A real-time API; uses PATCH only"}, {"label": "B", "value": "An architectural style for web APIs; uses PUT or PATCH to update"}, {"label": "C", "value": "A database API; uses UPDATE"}, {"label": "D", "value": "A GraphQL-based API; uses POST for everything"}],
     "correct_answer": "B", "explanation": "REST (Representational State Transfer) is an architectural style. PUT replaces the entire resource; PATCH applies a partial update.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What is SQL injection and how is it prevented?",
     "options": [{"label": "A", "value": "Inserting too many rows; prevented by pagination"}, {"label": "B", "value": "An attack where malicious SQL is inserted into input fields; prevented by parameterized queries / prepared statements"}, {"label": "C", "value": "Slow query performance; prevented by indexing"}, {"label": "D", "value": "Copying a database; prevented by encryption"}],
     "correct_answer": "B", "explanation": "SQL injection exploits unsanitized input to execute malicious queries. Parameterized queries (prepared statements) separate SQL code from user data, preventing this.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What is the N+1 query problem in web development?",
     "options": [{"label": "A", "value": "Running a query N+1 times longer than optimal"}, {"label": "B", "value": "Executing one query to fetch a list, then N additional queries to fetch related data for each item — instead of one JOIN"}, {"label": "C", "value": "Having one more table than needed in the database schema"}, {"label": "D", "value": "Using N+1 indexes on a single table"}],
     "correct_answer": "B", "explanation": "The N+1 problem occurs when code fetches a list (1 query), then loops through it making an extra query per item (N queries). It's solved by eager loading with JOINs.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "programming", "topic": "web_and_databases", "difficulty": "hard",
     "text": "What is the purpose of JWT (JSON Web Token) in web authentication?",
     "options": [{"label": "A", "value": "To encrypt the database connection"}, {"label": "B", "value": "To store user passwords securely"}, {"label": "C", "value": "To securely transmit claims between parties as a signed, self-contained token"}, {"label": "D", "value": "To compress HTTP responses"}],
     "correct_answer": "C", "explanation": "A JWT is a compact, self-contained token that encodes user claims (e.g., user ID, roles) and is signed so the server can verify its authenticity without a database lookup.", "active": True, "createdAt": datetime.now(timezone.utc)},
]