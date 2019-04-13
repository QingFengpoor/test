<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%!int pageCount = 0;

    void addCount() {
        pageCount++;
    }%>

<%
    addCount();
%>
<center>
    <p>Copyright © 2018 | 备案号：琼ICP备13001417号-3 |  联系我们：769728683@qq.com | 访问次数：<%=pageCount%></p>
</center>