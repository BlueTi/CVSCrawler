$(function(){
	var c=12;
	var prodlist;
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
		        	$(".prod_list ul").append("<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
		        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag "+item.prodTag+"'><span>"+item.prodTag+"</span></p></div></li>");
		       	});
		       	if($.parseJSON(data).length<20)$('#more').remove();
		       	$("#more").appendTo($('.prod_list ul'));
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		}); 
	});
	
	function searchWord(){
		index=0;
		var word=$('#searchWord').serialize();
		return $.ajax({
		    url : "/ajax/searchWord",
		    data: word,
		    datatype:"json",
		    type : "post",
		    contentType: 'application/x-www-form-urlencoded; charset=utf-8',
		    success: function(data) {
		    	if(data.length<3) {alert("결과가 없습니다"); return }
		    	$(".prod_list ul li").hide();
		    	$("#more").remove();
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		});
	};
	
	
	var index=0;
	
	function printList(index){
		var max=index+12; 
		if(max>=prodlist.length)max=prodlist.length;
		for(var i=index;i<max;i++){
			var tag="<li><div><span><img src="+prodlist[i].prodImg+" style='width:180px; height:180px;'><img src="+prodlist[i].CVS+" class='CVS'></span><p class='prodName'>"
        	+prodlist[i].prodName+"</p><p class='prodPrice'>"+prodlist[i].prodPrice+"</p><p class='prodTag "+prodlist[i].prodTag+"'><span>";
			if(prodlist[i].prodTag=='DUM') tag+="덤증정</span></p></div></li>"; else tag+=prodlist[i].prodTag+"</span></p></div></li>";
			$(".prod_list ul").append(tag);
		}
		if($('#mBtn').length){
			$("#more").appendTo($('.prod_list ul'));
			if(prodlist.length-index<13)$('#more').remove();
		}
		else
			$(".prod_list ul").append("<li id='more'><button id='mBtn'>더보기</button></li>");	

		if(prodlist.length-index<12)$('#more').remove();
	};	
	
	
	$(document).on("click","#mBtn",function(){
		printList(index+12);
		$("#more").appendTo($('.prod_list ul'));
		index+=12;
	});
	
	
	
	
	
	$('#searchBtn').click(function(){
		searchWord().then(function(data){
	    	$("#searchTag input[name='one']").attr('checked',true);
	    	$("#searchTag input[name='two']").attr('checked',true);
	    	$("#searchTag input[name='dum']").attr('checked',true);
	    	$("#searchTag input[name='CU']").attr('checked',true);
	    	$("#searchTag input[name='GS']").attr('checked',true);		    	
	    	prodlist=$.parseJSON(data);
	    	printList(index);	   
		});
	});
	
	
	
	
	$("#searchTag").change(function(){
		var one=$("#searchTag input[name='one']").is(':checked');		
		var two=$("#searchTag input[name='two']").is(':checked');
		var dum=$("#searchTag input[name='dum']").is(':checked');
		var CU=$("#searchTag input[name='CU']").is(':checked');
		var GS=$("#searchTag input[name='GS']").is(':checked');
		$(".prod_list ul li").remove();
    	$("#more").remove();    	
    	searchWord().then(function(data){
    		$.each($.parseJSON(data),function(index,item){
    			var tag="<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
	        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag "+item.prodTag+"'><span>";
    			if(item.prodTag=='DUM') tag+="덤증정</span></p></div></li>"; else tag+=item.prodTag+"</span></p></div></li>";
	        	if(((one&&item.prodTag=='1+1')||(two&item.prodTag=='2+1')||(dum&&item.prodTag=='DUM'))&&((CU&&item.CVS=='image/CULogo.jpg')||(GS&&item.CVS=='image/GSLogo.gif')))
	        		$(".prod_list ul").append(tag);
	    	});
		});
	});	
})