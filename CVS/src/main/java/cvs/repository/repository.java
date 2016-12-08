package cvs.repository;

import java.util.ArrayList;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import cvs.entity.DumEntity;
import cvs.entity.prodEntity;

@Repository
@AutoConfigurationPackage
public class repository {
	private JdbcTemplate temp;
	
	@Autowired
	public repository(DataSource ds){
		temp= new JdbcTemplate(ds);
	}
	public List<prodEntity> getWordList(String word){
		List<prodEntity>list = new ArrayList<prodEntity>();
		String sql="select * from prodList where prodName like '%"+word+"%'";
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),
				rs.getString(3),rs.getString(4),rs.getString(6),rs.getString(5))));	
		return list;
	}
	
	public List<DumEntity> getDumList(String name){
		List<DumEntity>list = new ArrayList<DumEntity>();
		String sql="select * from dumList where prodName like '%"+name+"%'";
		list.addAll(temp.query(sql, (rs,no)->new DumEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replace(",","")),rs.getString(3))));
		return list;
	}
	public List<prodEntity> getMenuFoodList(){
		List<prodEntity>list = new ArrayList<prodEntity>();
		String sql="select * from prodList,menu where prodList.prodName in( menu.prodName where menu ='과자') ";
		list.addAll(temp.query(sql, (rs,no)->new prodEntity(rs.getString(1),Integer.parseInt(rs.getString(2).replaceAll(",", "")),
				rs.getString(3),rs.getString(4),rs.getString(6),rs.getString(5))));	
		return list;
	}
}
