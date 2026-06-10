import random


questions = {
    "What keyword defines a function?": "def",
    "What keyword returns a value from a function?": "return",
    "What keyword creates an anonymous function?": "lambda",
    "What special method acts as a constructor?": "__init__",
    "What variable refers to the current object?": "self",

    "Which data type stores text?": "str",
    "Which data type stores whole numbers?": "int",
    "Which data type stores decimal numbers?": "float",
    "Which data type stores True or False values?": "bool",
    "Which data type stores key-value pairs?": "dict",

    "Which data type stores unique values?": "set",
    "Which data type stores ordered mutable values?": "list",
    "Which data type stores ordered immutable values?": "tuple",
    "Which value represents nothing?": "None",
    "Which function returns an object's type?": "type",

    "What keyword starts a conditional statement?": "if",
    "What keyword provides another condition?": "elif",
    "What keyword handles all remaining cases?": "else",
    "Which operator checks equality?": "==",
    "Which operator checks inequality?": "!=",

    "What keyword starts a counted loop?": "for",
    "What keyword starts a conditional loop?": "while",
    "What keyword exits a loop immediately?": "break",
    "What keyword skips an iteration?": "continue",
    "Which function creates a sequence of numbers?": "range",
    "What is the first 2 words we write when we start learning any programming language?": "hello world",

    "What keyword begins exception handling?": "try",
    "What keyword catches exceptions?": "except",
    "What keyword always executes?": "finally",
    "What keyword raises an exception?": "raise",
    "What keyword does nothing?": "pass",

    "Which function displays output?": "print",
    "Which function takes user input?": "input",
    "Which function returns length?": "len",
    "Which function converts to integer?": "int",
    "Which function converts to string?": "str",

    "Which module provides math functions?": "math",
    "Which module generates random values?": "random",
    "Which module works with operating systems?": "os",
    "Which module handles JSON data?": "json",
    "Which module works with dates?": "datetime",

    "Which keyword imports a module?": "import",
    "Which keyword imports specific names?": "from",
    "Which keyword creates a class?": "class",
    "Which decorator creates a static method?": "staticmethod",
    "Which decorator creates a class method?": "classmethod",

    "Which list method adds an item?": "append",
    "Which list method removes the last item?": "pop",
    "Which list method sorts a list?": "sort",
    "Which list method reverses a list?": "reverse",
    "Which list method inserts at an index?": "insert",

    "Which string method converts text to lowercase?": "lower",
    "Which string method converts text to uppercase?": "upper",
    "Which string method removes surrounding spaces?": "strip",
    "Which string method splits a string?": "split",
    "Which string method joins strings?": "join",

    "Which dictionary method returns all keys?": "keys",
    "Which dictionary method returns all values?": "values",
    "Which dictionary method returns key-value pairs?": "items",
    "Which dictionary method safely retrieves a value?": "get",
    "Which dictionary method removes a key?": "pop",

    "Which operator performs exponentiation?": "**",
    "Which operator returns remainder?": "%",
    "Which operator performs floor division?": "//",
    "Which operator performs logical AND?": "and",
    "Which operator performs logical OR?": "or",

    "Which operator performs logical NOT?": "not",
    "Which keyword checks membership?": "in",
    "Which keyword checks identity?": "is",
    "Which symbol starts a comment?": "#",
    "Which operator assigns a value?": "=",

    "Which function opens a file?": "open",
    "Which file mode reads a file?": "r",
    "Which file mode writes a file?": "w",
    "Which file mode appends to a file?": "a",
    "Which method closes a file?": "close",

    "Which built-in function finds the largest value?": "max",
    "Which built-in function finds the smallest value?": "min",
    "Which built-in function calculates absolute value?": "abs",
    "Which built-in function rounds a number?": "round",
    "Which built-in function combines iterables?": "zip",

    "Which built-in function returns object identity?": "id",
    "Which built-in function returns ASCII code?": "ord",
    "Which built-in function returns a character?": "chr",
    "Which built-in function sorts an iterable?": "sorted",
    "Which built-in function enumerates items?": "enumerate"
}


def python_quiz_game() :
    questions_list = list(questions.keys())
    total_questions = 10
    score = 0
    selected_questions = random.sample(questions, total_questions)

    for question in selected_questions:
        print(questions)
        user_input = input("Your Answers: ").lower().strip()
        correct_answers = questions[questions]
        if correct_answers == user_input.lower():
            print("Correct answer!!\n")
            score +=1
        else:
            print(f"Wrong answer!!\nThe correct answer is {correct_answers}.\n")
    print(f"Game over!!Your total score is: {score}")   

python_quiz_game()   

