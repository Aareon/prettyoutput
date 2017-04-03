[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org/)
PrettyOutput allows you to print pretty colors with ease. What more do you want?

## Installation
Options:
1. Clone this repository (you probably know what you're doing)
2. `pip install prettyoutput` (for the everyday pleb)
   * Alternatively, you can use `py(thon)3 -m pip install prettyoutput`
3. Download the archive from releases

# Usage
```py
import prettyoutput

prettyoutput.info('Well, isn\'t this neat?')
prettyoutput.success('Yes! Yes it is.')
prettyoutput.error('Oh noes!')
prettyoutput.warning('Get outta here!')
```

### PrettyOutput also supports printing without args!
```py
import prettyoutput

prettyoutput.info()
prettyoutput.success()
prettyoutput.error()
prettyoutput.warning()
```
Notice when executed, everything is aligned perfectly!

## Got the time? We do!
Here's how to use the time option. All times are UTC.
```py
import prettyoutput

prettyoutput.error(time=True)
```


### Python interpreter acting funny?
You're probably seeing a really confusing string of characters, right?
```py
>>> import prettyoutput
>>> prettyoutput.error()
[ERROR]   | An error has occured!
'\x1b[0;31;40m[ERROR]   | \x1b[1;37;40mAn error has occured!'
>>>
```
Not to worry!
### Try this;
```py
>>> import prettyoutput
>>> print(prettyoutput.error(prn_out=False))
[ERROR]   | An error has occured!```
```
> PrettyOutput returns the message created so that it may be re-used.
> Save the returned string to a variable, and you may never have to call
> PrettyOutput again!

License
----

[![DUB](https://img.shields.io/dub/l/vibe-d.svg)](https://github.com/Aareon/Tipsy/blob/master/LICENSE)
