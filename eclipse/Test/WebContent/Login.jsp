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
	Statement stmt;
	ResultSet rs;
	try{
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		con=DriverManager.getConnection(URL,"sa","feng1204");
		out.print("连接成功"+"</br>");
		stmt=con.createStatement();//Statement 对象可以把SQL语句发动到数据库
		String susername=request.getParameter("username");
		String spassword=request.getParameter("password");
		out.print("用户名："+susername+"</br>");
		out.println("密码："+spassword+"</br>");
		String sql="select password from T_User where username='"+susername+"'";
		out.println(sql+"</br>");
		try{
			rs=stmt.executeQuery(sql);
			out.println("执行查询成功"+"</br>");
			while(rs.next()){
				String gpassword=rs.getString("password");
				out.println("查询到的密码:"+gpassword+"</br>");
				out.println("spassword的长度:"+spassword.length()+"</br>");
				out.println("gpassword的长度:"+gpassword.length()+"</br>");
				if(gpassword.equals(spassword))
					out.println("密码正确"+"</br>");
				else 
					out.println("密码不正确"+"</br>");
			}
		}catch(Exception exsql){
			out.println("执行查询失败"+"</br>");
		}
	}catch(Exception e){
		out.println("连接失败"+"</br>");
		e.printStackTrace();
	}
	
	try{
		con.close();
		out.println("关闭成功"+"</br>");
	}catch(Exception e2){
		out.println("关闭失败"+"</br>");
	}
	
%>
</body>
</html>