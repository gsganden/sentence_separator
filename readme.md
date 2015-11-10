This Python script puts each sentence of a LaTeX document on a separate line, which is helpful for tracking changes with Git and other version-control systems.

It prompts you for the filepath of the document you would like to change, reprompting as long as the file is not found. It then asks for the desired output filepath, reprompting once if the output and input filepaths are the same (which is not recommended). Finally, it copies the text from the input file into the output file, with the appropriate newline characters inserted.

It is a bit susceptible to false positives, e.g. separating on "et al." in the middle of a sentence. However, it is not fooled by "i.e.," "e.g.," ellipses, decimal numbers, or upper-case initials. I would be surprised if it is not also susceptible to false negatives, but I have not seen any yet.

The usual caveats apply: Bug reports are welcome, but this is unsupported software. It works for my purposes, but I make no warranties or guarantees that it will work for yours.