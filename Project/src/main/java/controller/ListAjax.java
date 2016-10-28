package controller;

import java.io.PrintWriter;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import entity.CUprodEntity;


@Controller
@ComponentScan({"controller","repository"})
public class ListAjax {
	
	@Autowired
	ListService service;
	
	@ResponseBody
	@RequestMapping(value="/ajax/Morelist", method= RequestMethod.POST)
	public void loadList(HttpServletResponse resp,@RequestParam(value="count") int count) throws Exception{
		resp.setCharacterEncoding("utf-8");
		List<CUprodEntity> list=service.getList();		
		JSONArray jar = new JSONArray();
		int max=count+20;
		if(max>list.size()) max=list.size();			
		for(int i=count;i<max;i++){
			CUprodEntity p = list.get(i);
			JSONObject ob = new JSONObject();			
	        ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());
			ob.put("prodTag",p.getProdTag());
			if(p.getCVS().equals("CU"))
				ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS"))
				ob.put("CVS", "image/GSLogo.gif");
			jar.add(ob);
		}        
        PrintWriter out = resp.getWriter();
        out.print(jar);
	}
	
	@ResponseBody
	@RequestMapping(value="/ajax/searchWord",method=RequestMethod.POST)
	public void searchWordList(HttpServletResponse resp,@RequestParam(value="word")String word)throws Exception{
		resp.setCharacterEncoding("utf-8");
		List<CUprodEntity>list=service.getSearchList(word);
		JSONArray jar = new JSONArray();
		for(CUprodEntity p :list){
			JSONObject ob = new JSONObject();			
	        ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());
			ob.put("prodTag",p.getProdTag());	
			if(p.getCVS().equals("CU"))
				ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS"))
				ob.put("CVS", "image/GSLogo.gif");
			jar.add(ob);
		}
		PrintWriter out = resp.getWriter();
        out.print(jar);
	}
	
}
