<%@page import="java.util.Date,java.text.DateFormat"%>
<%@page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page buffer="16kb" autoFlush="true" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Study 菜鸟教程</title>
</head>
<body>
<%
out.println("你的IP是： " + request.getRemoteAddr());
%>
<%--变量声明 --%>
<%!
	int i=0;
	int a,b,c;
	DateFormat ddtf=DateFormat.getDateTimeInstance();
%>
<%-- 表达式 --%>
<p>
	今天的日期是：<% out.println(ddtf.format(new Date())); %>
	<%!int day=3; %>
	<%
		if(day==1|day==7){
	%>
	<p>今天是周末 ，不上班</p>
	<% 		
		}else{
	%>
	<p>今天工作日，还能上班</p>
	<%		
		}
	%>
	<h2>for 循环</h2>
		<%!int fontSize; %>
		<%
			for(fontSize=1;fontSize<=5;fontSize++){
		%>
		<font color="green" size="<%=fontSize %>">JSP教程</font>
		<br/>
		<%
			}
		%>
	<%-- out.println(getAttributeNames()); --%>
	
</body>
</html>