<%@ page import="java.util.Date,java.text.DateFormat" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! DateFormat dtfm=DateFormat.getDateTimeInstance(); %>
<p>今天是: <%= dtfm.format(new Date()) %></p>