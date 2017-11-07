python_note22常用內建模块datetime.py

- datetime:python 处理日期时间的标准库
- 获取当前日期和时间
	from datetime import datetime
	now = datetime.now()
	print(now)

- 获取指定时间和日期
	直接用参数构造一个datatime：
	from datatime import datatime
	dt = datatime(2017, 4, 19, 12, 20)
	print(dt)

- datatime转换为timestamp
	计算机中的时间用数字表示，把1970年1月1日 00:00:00称为epoch time，当前时间是相对于epoch time的秒数
	----称为time stamp
	from datatime import datatime
	dt = datatime(2017,11,1,2,9,51)
	dt.timestamp()
	----得到的是一个浮点数

- timestamp转换为datatime
	from datatime import datatime
	t = 1429417200.0
	print(datatime.fromtimestamp(t))
	注，因为datatime是有时区的，这个转换是timestamp和本地时间做转换
- timestamp 转换到UTC标准时区的时间
	print(datatime.utcfromtimestamp(t))

- str转换为datatime
	from datetime import datetime
	cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')#%....规定日期和时间部分的格式
	print(cday)
	*转换后的datetime没有时区信息

- datetime转换为str
	有了datetime的对象，要把它格式化为字符串显示给用户
	from datetime import datetime
	now = datetime.now()
	print(now.strftime('%a,%b %d %H:%M'))
	#detail of %...
	# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

- datetime 加减
	from datetime import datetime, timedelta
	now = datetime.now()
	now + timedelta(hours = 10)
	now - timedelta(days = 1)
	now + timedelta(days = 2, hours = 12)

- 本地时间转换为UTC时间
	本地时间：系统设定时区的时间,SGT是UTC+8:00,
	datetime类型有一个时区属性，默认为none，需要设置
	from datetime import datetime, timedelta, timezone
	tz_utz_8 = timezone(timedelta(hours=8)) # 创建时间UTC+8:00
	now = datetime.now()
	dt = now.replace(tzinfo = tz_utz_8)

- 时区转换
	#拿到UTC时间，并强制设置时区为UTC+0：00
	utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
	print(utc_dt)
	#用astimezone()将时区转为北京时间
	bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
	#设置为东京时间
	tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
	tokyo_dt1 = bj_dt.astimezone(timezone(timedelta(hours=9)))
	tolyo_dt和tokyo_dt1的时间是相等的，任何带时区的datetime都可以在正确转换

例，把用户输入日期2017-1-21 9:01:30, 时区信息UTC+5:00，转换为timestamp
	import re
	from datetime import datetime, timezone, timedelta
	def to_timestamp(dt_str, tz_str):
		a = re.split(r'[\+\:]',tz_str)
		tz = int(a[1])
		#上面两句可以改成
		int(re.match(r'^(\D+)([+-]\d+)\:(\d+)$',tz_str).group(2))
		#利用group提取分组
		cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
		print(cday)#UTC+5:00的datetime
		#cday的值：	datetime.datetime(2015, 6, 1, 8, 10, 30)
		tz_utc_5 = timezone(timedelta(hours=tz))
		print(tz_utc_5)
		cday1 = cday.replace(tzinfo=tz_utc_5)#想把时区强制设为UTC+8:00
		return cday1.timestamp()
