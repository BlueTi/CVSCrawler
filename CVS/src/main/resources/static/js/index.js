$(function(){
	var c=12;
	var prodlist;
	var index=0;	
	
	function searchWord(){
		index=0;
		var word=$('#searchWord').serialize();
		return $.ajax({
		    url : "/ajax/searchWord",
		    data: word,
		    datatype:"json",
		    type : "post",
		    contentType: 'application/x-www-form-urlencoded; charset=utf-8',
		    beforeSend:function(){
		    	
		    },
		    success: function(data) {
		    	if(data.length<3) {alert("결과가 없습니다"); return 0}
		    	$(".prod_list ul li").remove();
		    	$("#searchTag").css("visibility","visible");
		    	if($('#head').css('margin-top')!=null){		    		
		    		$('#head').animate({
		    			top:'1%',
		    			left:'-25%'
		    		},200,function(){		    			
		    		});
		    	};		    	 
		    },
		    error:function(request,status,error){
		        alert("code:"+request.status+"\n"+"error:"+error);
		    },
		    complete:function(){
		    	
		    }
		});
	};
	
	
	function printList(){
		var max=index+12; 
		if(max>=prodlist.length)max=prodlist.length;
		for(var i=index;i<max;i++,index++){
			var tag="<li><div><span><img src="+prodlist[i].prodImg+" style='width:180px; height:180px;'><img src="+prodlist[i].CVS+" class='CVS'></span><p class='prodName'>"
        	+prodlist[i].prodName+"</p><p class='prodPrice'>"+prodlist[i].prodPrice+"원</p><p class='prodTag "+prodlist[i].prodTag+"'><span>";
			if(prodlist[i].prodTag=='DUM') tag+="덤증정</span></p></div></li>"; else tag+=prodlist[i].prodTag+"</span></p></div></li>";
			$(".prod_list ul").append(tag);
		}
		if($('#mBtn').length){
			$("#more").appendTo($('.prod_list ul'));
			if(prodlist.length-index<13)$('#more').remove();
		}
		else
			$(".prod_list ul").append("<li id='more'><button id='mBtn'>더보기</button></li>");	
	};	
	
	
	$(document).on("click","#mBtn",function(){
		printList();
		$("#more").appendTo($('.prod_list ul'));
	});	
	
	$('#searchBtn').click(function(){
		searchWord().then(function(data){
			$("#searchTag input[name='one']").attr('checked',true);
	    	$("#searchTag input[name='two']").attr('checked',true);
	    	$("#searchTag input[name='dum']").attr('checked',true);
	    	$("#searchTag input[name='CU']").attr('checked',true);
	    	$("#searchTag input[name='GS']").attr('checked',true);	    	
	    	prodlist=$.parseJSON(data);
		    $('.prod_list ul').hide();
		    if(prodlist!=0)
		    	printList();
		    $('.prod_list ul').show('slow');	 
		});
	});	
	
	/*태그폼 분류 */
	$("#searchTag").change(function(){
		var one=$("#searchTag input[name='one']").is(':checked');		
		var two=$("#searchTag input[name='two']").is(':checked');
		var dum=$("#searchTag input[name='dum']").is(':checked');
		var CU=$("#searchTag input[name='CU']").is(':checked');
		var GS=$("#searchTag input[name='GS']").is(':checked');
		$(".prod_list ul li").remove();
    	$("#more").remove();    	
    	
    	$.each(prodlist,function(index,item){
    		var tag="<li><div><span><img src="+item.prodImg+" style='width:180px; height:180px;'><img src="+item.CVS+" class='CVS'></span><p class='prodName'>"
        	+item.prodName+"</p><p class='prodPrice'>"+item.prodPrice+"</p><p class='prodTag "+item.prodTag+"'><span>";
			if(item.prodTag=='DUM') tag+="덤증정</span></p></div></li>"; else tag+=item.prodTag+"</span></p></div></li>";
        	if(((one&&item.prodTag=='1+1')||(two&item.prodTag=='2+1')||(dum&&item.prodTag=='DUM'))&&((CU&&item.CVS=='image/CULogo.jpg')||(GS&&item.CVS=='image/GSLogo.gif')))
        		$(".prod_list ul").append(tag);
    	});
	});		
	
	$("input[name=word]").on("textchange",function(){
		if($("input[name=word]").val().length<1)
			$("#searchBtn").val("전체목록");			
		else
			$("#searchBtn").val("검색");
	});
})