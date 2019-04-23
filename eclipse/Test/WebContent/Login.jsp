<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>欢迎登录☺</title>
<%! 
	String pathusername,pathpassword,pathcss1;
	String URL="jdbc:sqlserver://127.0.0.1:1433;databaseName=test";
	Connection con=null;
	Statement stmt;
	ResultSet rs;
%>
<%
	try{
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		con=DriverManager.getConnection(URL,"sa","feng1204");
		stmt=con.createStatement();//Statement 对象可以把SQL语句发动到数据库
		String sqlpathusername="select imagepath from image where imagename='Login_username'";
		String sqlpathpassword="select imagepath from image where imagename='Login_password'";
		String sqlpathcss1="select imagepath form image where imagename='Login_css1'";
		System.out.println(sqlpathusername+"\n"+sqlpathpassword+"\n"+sqlpathcss1+"\n");
		try{
			rs=stmt.executeQuery(sqlpathusername);
			System.out.println("执行查询usernameimage成功"+"</br>");
			if(rs.next()){
				pathusername=rs.getString("imagepath");
				}
			else{
				System.out.println("查询结果为空");
			}
			rs=stmt.executeQuery(sqlpathpassword);
			System.out.println("执行查询passwordimage成功"+"</br>");
			if(rs.next()){
				pathpassword=rs.getString("imagepath");
				}
			else{
				System.out.println("查询结果为空");
			}
		}catch(Exception epath){
			System.out.println("执行查询失败"+"</br>");
		}
	}catch(Exception e){
		System.out.println("连接失败"+"</br>");
		e.printStackTrace();
	}
	
	try{
		con.close();
		out.println("关闭成功"+"</br>");
	}catch(Exception e2){
		out.println("关闭失败"+"</br>");
	}
%>
<link rel="stylesheet" href="css/2.css">
</head>
<body>
	<div class="header">
		<div class="zhishiku">
			<p class="zsk">知识库管理系统</p>
		</div>
		<div class="xhx">
		</div>
	</div>
	<div class="ban">
		<div class="logGet">
			<div class="logD logDtip">
				<p class="p1">登录</p>
			</div>
			<form method="POST">
				<div class="lgD">
					<img src="<%=pathusername %>" width="20" height="20" alt=""/>
					<input type="text" name="username" placeholder="输入用户名">
				</div>
				<div class="lgD">
					<img src="<%=pathpassword %>"  width="20" height="20" alt=""/>
					<input type="password" name="password" placeholder="输入密码">
				</div>
				<div class="logC">
					<input type="submit" value="登录">
				</div>
			</form>

		</div>
	</div>
<%
	try{
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		con=DriverManager.getConnection(URL,"sa","feng1204");
		stmt=con.createStatement();//Statement 对象可以把SQL语句发动到数据库
		String susername=request.getParameter("username");
		String spassword=request.getParameter("password");
		String sql="select password from T_User where username='"+susername+"'";
		try{
			rs=stmt.executeQuery(sql);
			System.out.println("执行查询成功"+"</br>");
			while(rs.next()){
				String gpassword=rs.getString("password");
				if(gpassword.equals(spassword)){
					System.out.println("密码正确"+"</br>");
					response.sendRedirect("Login.html");
				}
				else 
					System.out.println("密码不正确"+"</br>");
			}
		}catch(Exception exsql){
			System.out.println("执行查询失败"+"</br>");
		}
	}catch(Exception e){
		System.out.println("连接失败"+"</br>");
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