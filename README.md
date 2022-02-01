This program has the intention of aiding a user in the creation of a Boolean String
It does that by holding a variety of values that can be used in the search of one single concept,
holding it in a list with many other strings that have the same use but for other values,
then looking into the list of user demands and creating a boolean search string based on that.

It is quite a simple program, but it can be upgraded into something even more useful.

How it works:
 To create our boolean string, we separate our phrase into different segments, each with a different function:
 (technologies) AND (work) AND (location) AND (platform) AND (spoken language)
 each of these segments will have many useful words to our search, separated ("just" OR "like" OR "so")
 every item in our search will be associated with these words, like:
 python : "pyt*" OR "Pyt*" OR "pithon" OR "Paithon"
 So, when we choose our technology, we can go ahead and choose the work of our candidate(backend,frontend,etc)
 The process will continue until we have our options selected
 then we will go after the values exemplified in line 18, and append them in our string
 Until we have completed the string
 In the end we will have a Boolean string search created on our terms!