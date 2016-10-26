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
<script type="text/javascript">
$(function(){
	var c=5;
	$("#moreBtn").click(function(){
		$.ajax({
		    url : "/ajax/Morelist",
		    data: {"count":c},
		    datatype:"json",
		    type : "post",
		    contentType: 'application/x-www-form-urlencoded; charset=utf-8',
		    success: function(data) {
		       	c+=12;
		        $.each($.parseJSON(data),function(index,item){
		        	$(".prod_list ul").append("<li><div><img src="+item.prodImg+" style='width:180px; height:180px;'><p class='prodName'>"
		        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span><p></div></li>");
		       	});
		        //$("#more").insertAfter($('.prod_list ul li').last());
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		}); 
	});
})

</script>
<title>일단 만들어 그리고 부셔</title>
</head>

<body>
	<!-- 이름으로 검색 -->
	<form class='search' method='post' action="">
		<input name="word" type='text'/>
		<input value="검색" type='button' onclick="/ajax/search"> 
	</form>
	
	<div id="head">
		<div class="logo"><img src="https://cu.bgfretail.com/images/common/logo.gif"/></div>
		<div class="logo"><img src="http://gs25.gsretail.com/_ui/desktop/common/images/gscvs/common/logo.gif"></div>
		<!--가격범위 range, 태그 checkbox  -->
	<form>
		<input type="checkbox"/><label>1+1</label> 
		<input type="checkbox"/><label>2+1</label>		
	</form>
	</div>
	
	<div class='prod_list'>
		<ul>
		<%
		List<prodEntity> list=(List)request.getAttribute("list"); 
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