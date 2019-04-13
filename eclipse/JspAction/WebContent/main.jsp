<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
<title>在JSP使用JavaBeans示例</title>
</head>

<body>
    <div style="margin:auto;text-align:center;">
        <h2>在JSP使用JavaBeans示例</h2>
        <hr/>
        <jsp:useBean id="msg" class="com.yiibai.Message" />
        <p>获取默认设置的信息是：<jsp:getProperty name="msg" property="message" /></p>

        <jsp:setProperty name="msg" property="message" value="Hello JSP..." />
        <p>获取设置的信息是：<jsp:getProperty name="msg" property="message" /></p>

    </div>
    <h2>forward 动作实例</h2>
    <%--<jsp:forward page="date.jsp" /> --%>
    <jsp:plugin type = "applet" codebase = "dirname" code = "MyApplet.class" width = "60" height = "80">
	   <jsp:params>
	   		<jsp:param name = "fontcolor" value = "red" />
	  		<jsp:param name = "background" value = "black" />
		</jsp:params>
   		<jsp:fallback>
      		Unable to initialize Java Plugin
   		</jsp:fallback>
   	</jsp:plugin>
   	
</body>
</html>