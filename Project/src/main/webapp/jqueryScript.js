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
	
	function searchWord(){
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
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    }		 
		});
	};
	
	$('#searchBtn').click(function(){
		searchWord().then(function(data){
	    	$("#searchTag input[name='one']").attr('checked',true);
	    	$("#searchTag input[name='two']").attr('checked',true);
	    	$("#searchTag input[name='dum']").attr('checked',true);
	    	$("#searchTag input[name='CU']").attr('checked',true);
	    	$("#searchTag input[name='GS']").attr('checked',true);	
	    	
			/*$.each($.parseJSON(data),function(index,item){
	        	$(".prod_list ul").append("<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
			        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span></p></div></li>");
	       	});*/
	    	var list=$.parseJSON(data);
	    	for(var i=0;i<4;i++){
	    		$(".prod_list ul").append("<li><div><span><img src="+list[i].prodImg+" style='width:180px; height:180px;'><img src="+list[i].CVS+" class='CVS'></span><p class='prodName'>"
			        	+list[i].prodName+"</p><p class='prodPrice'>"+list[i].prodPrice+"</p><p class='prodTag'><span>"+list[i].prodTag+"</span></p></div></li>");
	    	}
			$("#more").appendTo($('.prod_list ul'));
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
	        	if(((one&&item.prodTag=='1+1')||(two&item.prodTag=='2+1')||(dum&&item.prodTag=='DUM'))&&((CU&&item.CVS=='image/CULogo.jpg')||(GS&&item.CVS=='image/GSLogo.gif')))
	        		$(".prod_list ul").append("<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
	    		        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag'><span>"+item.prodTag+"</span></p></div></li>");
	    	});
		});
	});	
	
	
})