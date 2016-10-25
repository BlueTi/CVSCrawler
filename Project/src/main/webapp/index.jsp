<%@page import="entity.prodEntity"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script="jquery-3.1.1.min.js"/>
<link rel='stylesheet' type='text/css' href='index.css'/>
<script type="text/javascript">
	<%List<prodEntity> list=(List)request.getAttribute("list"); %>
	var list=<%=list%>;
	$(document).ready(function(){
		function nextPage(){
			$(".prod_list").(ul).append("TEST");
		}		
	});
</script>
<title>편의점 정보 찾기</title>
</head>
<body>
	<form class='search' method='post'>
		<input name="word" type='text'/>
		<input value="검색" type='submit'> 
	</form>
	<div id="head">
		<div class="logo"><img src="https://cu.bgfretail.com/images/common/logo.gif"/></div>
		<div class="logo"><img src="http://gs25.gsretail.com/_ui/desktop/common/images/gscvs/common/logo.gif"></div>
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
			<p><%=list.get(i).getProdName() %></p>
			<p><%=list.get(i).getProdPrice()%></p>
			</div>
			</li>
		<%}%>
		</ul>
	</div>
	<div><a href="javascript:nextPage();">더보기</a></div>
</body>
</html>