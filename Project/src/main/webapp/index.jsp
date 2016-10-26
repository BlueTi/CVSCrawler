<%@page import="entity.prodEntity"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<link rel='stylesheet' type='text/css' href='index.css'/>
<% List<prodEntity> list=(List)request.getAttribute("list");  %>
<script type="text/javascript" src="jqueryScript.js">
	list=<%=list%>
</script>
<title>일단 만들어 그리고 부셔</title>
</head>

<body>
	<!-- 이름으로 검색 -->
	<form id='searchWord' method='post' onSubmit="return false;">
		<input name="word" type='text'/>
		<input id='searchBtn' value="검색" type='button'> 
	</form>
	
	<div id="head">
		<div class="logo"><img src="https://cu.bgfretail.com/images/common/logo.gif"/></div>
		<div class="logo"><img src="http://gs25.gsretail.com/_ui/desktop/common/images/gscvs/common/logo.gif"></div>
		<!--가격범위 range, 태그 checkbox  -->
	<form id='searchTag'>
		<input name="one" type="checkbox"/><label>1+1</label> 
		<input name="two" type="checkbox"/><label>2+1</label>		
	</form>
	</div>
	
	<div class='prod_list'>
		<ul>
		<%
		int c=5;		
		int i=0;
		for(;i<c;i++){
		%>		
			<li>
			<div>
			<img src="<%=list.get(i).getProdImg() %>" style="width:180px; height:180px;">
			<p class='prodName'><%=list.get(i).getProdName() %></p>
			<p class='prodPrice'><%=list.get(i).getProdPrice()%></p>
			<p class='prodTag'><span><%=list.get(i).getProdTag() %></span></p>
			</div>
			</li>
		<%}%>		
		</ul>		
	</div>
	<div id="more"><button id="moreBtn">더보기</button></div>
</body>
</html>