# smartconf
Smart cofiguration can let people access configuration items in this way like 'x.y' 

# Feature

- Easy to use
- No dependency
- Access configuration items more nature

# Python
  \> 2.7

# Usage
> cat test.ini

    [section1]
	option1 = value1
	optoin2 = value2
	
	[section2]
	foo = bar

> import smartconf

> sc = smartconf.SmartConf()   # smartconf instance

> r = smartconf.load('test.ini')  # load configuration file

> print(r.section1.option1, r.section2.foo)  # access configuration items

> \# remove option1 in section1

> r.section1.pop('option1')   

> sc.save()

> \# add section
> 
> r.section3 = dict()

> r.section3.item = 'value'

> sc.save()  # add section3

> \# remove section

> r.pop['section3']

> sc.save()


# Email
pengxj#outlook.com
