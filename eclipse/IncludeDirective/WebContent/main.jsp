<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>主页(Main.jsp)</title>
</head>
<body>
    <%@ include file="header.jsp"%>

    <center>
        <p>这是Main.jsp页面的内容~</p>
        <p>include指令用于在编译阶段包括一个文件。这个指令告诉容器在编译阶段将其他外部文件的内容合并到当前JSP文件中。可在JSP页面的任何位置使用 include指令进行编码。</p>
    </center>
    <%@ include file="footer.jsp"%>
</body>
</html>