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
<script type="text/javascript" src="jqueryScript.js"></script>
<title>일단 만들어 그리고 부셔</title>
</head>

<body>
	<!-- 이름으로 검색 -->
	<form id='searchWord' method='post' onSubmit="return false;">
		<input name="word" type='text'/>
		<input id='searchBtn' value="검색" type='button'>
	</form>
	
	<div id="head">
		<div class="logo"><a href="#"><img src="https://cu.bgfretail.com/images/common/logo.gif"/></a></div>
		<div class="logo"><a href="#"><img src="image/GSlogo.gif"></a></div>
		<!--가격범위, 태그 checkbox  -->
	<form id='searchTag'>
		<input name="one" type="checkbox"/><label>1+1</label> 
		<input name="two" type="checkbox"/><label>2+1</label>
		<input name="dum" type="checkbox"/><label>덤증정</label>				
	</form>
	
	
	</div>
	
	<div class='prod_list'>
		<ul>
			<c:forEach var="item" items="${list}"  begin="0" varStatus="status" end="12" >
				<li>
				<div>
				<span><img src="${item.prodImg}" style="width:180px; height:180px;"><img class='CVS' src=${item.CVS}></span>
				<p class='prodName'>${item.prodName}</p>
				<p class='prodPrice'>${item.prodPrice}</p>				
				<p class='prodTag'><span>${item.prodTag}</span></p>
				</div>
				</li>
			</c:forEach>			
			<li id="more"><button id="moreBtn">더보기</button></li>
		</ul>		
	</div>	
</body>
</html>