package controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import repository.ProdRepository;

@Service
public class ListService {
	@Autowired
	ProdRepository repository;
	
	public List getList(){
		return repository.getList("CU");
	}
	public List getSearchList(String word){
		return repository.searchList(word);
	}
}
