package cvs.service;

import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.stereotype.Service;

import cvs.entity.prodEntity;
import cvs.repository.repository;

@Service
@AutoConfigurationPackage
public class SearchService {
	@Autowired
	repository repo;
	
	public JSONArray searchWord(String word){
		List<prodEntity> list = new ArrayList<prodEntity>();
		list=repo.getWordList(word);
		JSONArray jar = new JSONArray();
		for(prodEntity p :list){
			JSONObject ob = new JSONObject();			
			ob.put("prodImg",p.getProdImg());
			ob.put("prodName",p.getProdName());
			ob.put("prodPrice",p.getProdPrice());
			ob.put("prodTag",p.getProdTag());
			
			if(p.getCVS().equals("CU"))	ob.put("CVS", "image/CULogo.jpg");
			else if(p.getCVS().equals("GS")) ob.put("CVS", "image/GSLogo.gif");
			
			jar.add(ob);
		}
		return jar;
	}
	
}
