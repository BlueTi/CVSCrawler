package cvs.service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Service;

import cvs.entity.prodEntity;
import cvs.repository.DumEntity;
import cvs.repository.repository;

@Service
@AutoConfigurationPackage
public class SearchService {
	@Autowired
	repository repository;
	
	@SuppressWarnings("unchecked")
	public JSONArray searchWord(String word){
		List<prodEntity> list = new ArrayList<prodEntity>();
		list=repository.getWordList(word);
		

		Collections.sort(list,new Comparator<prodEntity>(){
			public int compare(prodEntity p1,prodEntity p2){				
				return p1.getProdName().compareTo(p2.getProdName());
			}
		});
		
		JSONArray jar = new JSONArray();
		for(prodEntity p :list){
			JSONObject ob = new JSONObject();			
			ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());
			ob.put("prodTag",p.getProdTag());
			
			if(p.getCVS().equals("CU"))	ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS")) ob.put("CVS", "image/GSLogo.gif");
			
			if(p.getDum()!=null)
				for(DumEntity d :repository.getDumList(p.getDum())){
					ob.put("dumName", d.getDumName());
					ob.put("dumPrice", d.getDumPrice());
					ob.put("dumImg", d.getDumImg());
				}
			jar.add(ob);
		}
		return jar;
	}
	
}
