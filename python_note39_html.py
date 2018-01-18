python_note39_html.py

通过一系列tag组成<html>...</html>，包含<head></head>,<body></body>
表达链接，图片，表格，表单

CSS:
	层叠样式表，用来控制HTML里的元素如何展示
JavaScript:
	为了让HTML具有交互性，作为脚本语言添加的
<script></script>


<html>
<head>
	<title>Hello</title>
	<style type="text/css">
		h1 {
			color:#333333;
			font-size: 48px;
			text-shadow: 3px 3px 3px #666666;
		}
	</style>
------>层叠样式表(Cascading Style Sheets)
	<script type="text/javascript">
		function change(){
			document.getElementsByTagName('h1')[0].style.color = '#ff0000';
		}
------>JavaScript
	</script>
</head>
<body>
	<h1 onclick="change()">Hello,world</h1>
</body>
</html>

