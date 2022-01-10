#
# one of the criteria on which computer languages are compared, is in how they group things
# to build larger things, that -syntatically- appear to be -one- thing,

# Some languages use { and } to enclose many statements, and just outside the {, they appear
# to the interpreter to be one thing, so you can do things like
#
# if (count(lines) > 250)
# {
#    and inside the braces, you can put as much stuff as you want, and they will all be controlled
#    by the if.
# indentation doesn't matter! as long as they're between the { and }, the if will run these lines if the
#                   condition inside the () evaluates to true (whatever that means in that language).
# }
#
# in -python-, the interpreter will look at indentation to determine what's in this "block", and therefore
# what is controlled by the if.
#
# so, an if looks like:
# if len(lines) > 250:
#   this line is indented, so it's controlled by the if. Notice the : at the end of the line, it means:
#   "here comes a block", and so all the indented lines will be in the "block" controlled by the if.
#
# there are other things about indentation...
# 1, you can't see an indentation, because it's just white space.
# 2, even though you cannot actually "see" white space, the interpreter
#    can, and as long as the indentation uses the same characters (spaces or tabs),
#    it will see there is an indentation. -but!!- if you have something like:
#
#    if bozo_the_clown_is_next_door:
#            the indentation is -spaces-, so if there is another indented line,
#            it must also use spaces, and so, the other case:
#
#    if barnum_and_bailey_circus_is_here:
#            the indentation here, is a tab, so, if there is another line, like:
#            this, then it must match the indentation characters, so here, it must be a tab.
#    else:
#            print("barnum and bailey circus is not here")
#
# Questions? Here is a running example:

# what will happen if you change the True to False in the next line?
bozo_the_clown_is_next_door = True # we're just looking at the ifs, not how to calculate the conditions

if bozo_the_clown_is_next_door: # notice the colon, it's part of the syntax for a "block"
    print("bozo is next door!")
else: # there's that : again
    print("bozo isn't next door")


