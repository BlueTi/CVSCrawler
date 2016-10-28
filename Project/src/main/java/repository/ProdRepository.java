package repository;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import entity.prodEntity;

@Repository
public class ProdRepository {
	private JdbcTemplate temp;
	
	
	@Autowired
	public ProdRepository(DataSource ds){
		temp= new JdbcTemplate(ds);
	}
	
	public List<prodEntity> getList(String table){		
		List<prodEntity>list = new ArrayList<prodEntity>();
		String sql="select * from "+table;		
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),table,rs.getString(5))));
		sql="select * from GS";
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),"GS",rs.getString(5))));

		Collections.sort(list,new Comparator<prodEntity>() {
			public int compare(prodEntity p1,prodEntity p2){				
				return p1.getProdName().compareTo(p2.getProdName());				
			}
		});	
		return list;
	}
	public List<prodEntity> searchList(String word){
		List<prodEntity>list = new ArrayList<prodEntity>();
		String sql="select * from CU where prodName like '%"+word+"%'";		
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),"CU",rs.getString(5))));
		sql="select * from GS where prodName like '%"+word+"%'";	
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),rs.getString(3),rs.getString(4),"GS",rs.getString(5))));
		Collections.sort(list,new Comparator<prodEntity>() {
			public int compare(prodEntity p1,prodEntity p2){				
				return p1.getProdName().compareTo(p2.getProdName());				
			}
		});	
		return list;
	}
}
