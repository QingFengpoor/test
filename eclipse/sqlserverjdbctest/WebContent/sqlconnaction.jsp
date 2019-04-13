<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<% 
	String URL="jdbc:sqlserver://127.0.0.1:1433;databaseName=test";
	Connection con=null;
	try{
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		con=DriverManager.getConnection(URL,"sa","feng1204");
		out.print("连接成功");
	}catch(Exception e){
		e.printStackTrace();
	}finally{
		try{
			con.close();
		}catch(Exception e2){
			
		}
	}
%>
</body>
</html>