<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>index</title>
</head>
<body>
	<div style="margin:auto;text-align:center;">
	<h2>第一个JSP应用程序</h2>
	<% 
		String str="JSP Hello World ~";
		out.print(str);
	%>
	</div>
</body>
</html>