[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org/)
PrettyOutput allows you to print pretty colors with ease. What more do you want?

## Usage
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

### Got the time? We do!
```py
import prettyoutput

prettyoutput.error(time=True)
```

### Python interpreter acting funny?
```py
>>> import prettyoutput
>>> prettyoutput.error()
[ERROR]   | An error has occured!
'\x1b[0;31;40m[ERROR]   | \x1b[1;37;40mAn error has occured!'
>>>
```
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
