First-Association-Automater
===========================

This is a project for automating first associations using the Edinburgh Associative Thesaurus in xml, using the Python xml tools.

The idea will be to create a custom vocabulary curriculum for a student applying techniques from spaced-repetition and novel applications of abstract algebras. 

Projects:
---------


First Letter Association Automater:

An automated generator with single word context.  Aimed to reduce ambiguity of follow-up word for letter.

Basically the algorithm will look for the word that has the highest association to the previous word and starts with the target letter.

Actual Example Output:

```
a - apple (seed word)
e - eat
i - intake
o - output
u - use
```

The above is an actual output sample, the program will simple automate the process.

Some uncommon words would not churn out enough responses, if we somehow built a comprehensive associative thesaurus via irc it would make this really powerful.
