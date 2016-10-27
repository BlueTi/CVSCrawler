$(function(){
	var c=12;
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
		        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span></p></div></li>");
		       	});
		       	if($.parseJSON(data).length<20)$('#more').remove();
		       	$("#more").appendTo($('.prod_list ul'));
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		}); 
	});
	
	$('#searchBtn').click(function searchWord(){
		var word=$('#searchWord').serialize();
		$.ajax({
		    url : "/ajax/searchWord",
		    data: word,
		    datatype:"json",
		    type : "post",
		    contentType: 'application/x-www-form-urlencoded; charset=utf-8',
		    success: function(data) {
		    	if(data.length<3) {alert("결과가 없습니다"); return }
		    	$(".prod_list ul li").hide();
		    	$("#more").remove();
		    	$("#searchTag input[name='one']").attr('checked',false);
		    	$("#searchTag input[name='two']").attr('checked',false);
		        $.each($.parseJSON(data),function(index,item){
		        	$(".prod_list ul").append("<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
				        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span></p></div></li>");
		       	});
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		}); 
	});
	
	$("#searchTag").change(function(){
		var one=$("#searchTag input[name='one']").is(':checked');		
		var two=$("#searchTag input[name='two']").is(':checked');
		$(".prod_list ul li").remove();
    	$("#more").remove();
    	var word=$('#searchWord').serialize();
		$.ajax({
		    url : "/ajax/searchWord",
		    data: word,
		    datatype:"json",
		    type : "post",
		    contentType: 'application/x-www-form-urlencoded; charset=utf-8',
		    success: function(data) {
		    	if(data.length<3) {alert("결과가 없습니다"); return }
		    	$(".prod_list ul li").hide();
		    	$("#more").remove();
		        $.each($.parseJSON(data),function(index,item){
		        	if((one&&item.prodTag=='1+1')||(two&item.prodTag=='2+1'))
		        		$(".prod_list ul").append("<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
		    		        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span></p></div></li>");
		    		});
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		}); 	
	});	
	
	
})