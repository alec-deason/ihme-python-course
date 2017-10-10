# Testing your code

We're now going to flip the normal order of things and talk about how
you go about testing the code that you write.

It's worthwhile to stop a bit and think about what we're trying
to do with tests.  

## Verification & Validation
These two terms are very confusing for most people, who use 
them interchangeably. The following table highlights the 
differences between verification and validation.

| S.N. |	Verification	| Validation |
|---|---|---|
| 1 |	Verification addresses the concern: "Are you building it right?" |	Validation addresses the concern: "Are you building the right thing?"|
|2 |	Ensures that the software system meets all the functionality.	| Ensures that the functionalities meet the intended behavior.|
|3	| Verification takes place first and includes the checking for documentation, code, etc.	| Validation occurs after verification and mainly involves the checking of the overall product.
|4	| Done by developers.	| Done by testers.|
|5	|It has static activities, as it includes collecting reviews, walkthroughs, and inspections to verify a software.	|It has dynamic activities, as it includes executing the software against the requirements.|
|6	|It is an objective process and no subjective decision should be needed to verify a software.	|It is a subjective process and involves subjective decisions on how well a software works. |

## Writing Tests

Writing tests is either very easy or very difficult, depending 
on the structure of the code you're trying to test.  This is one of the 
reasons why decomposing your code into functions with concrete and limited
responsibilities is so helpful.  

## How to think about your code when testing

1. What is the "happy path" through your code.  I.E. what happens when you get normal inputs to your code.
2. How many branches are in my code?  How do I make sure they're all covered.
3. Are there any edge cases that might show up?  How does your code deal with them.
4. Are there any guarantees about the kinds of input my code will receive.  Do I need to make any guarantees about the output?
