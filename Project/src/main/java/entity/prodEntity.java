package entity;

public class prodEntity {
	private String prodName,prodTag,prodImg;
	private int prodPrice;
	
	public prodEntity(){}	
	
	public prodEntity(String prodName, int prodPrice, String prodTag, String prodImg) {
		super();
		this.prodName = prodName;
		this.prodTag = prodTag;
		this.prodImg = prodImg;
		this.prodPrice = prodPrice;
	}


	public String getProdName() {
		return prodName;
	}
	public void setProdName(String prodName) {
		this.prodName = prodName;
	}
	public String getProdTag() {
		return prodTag;
	}
	public void setProdTag(String prodTag) {
		this.prodTag = prodTag;
	}
	public String getProdImg() {
		return prodImg;
	}
	public void setProdImg(String prodImg) {
		this.prodImg = prodImg;
	}
	public int getProdPrice() {
		return prodPrice;
	}
	public void setProdPrice(int prodPrice) {
		this.prodPrice = prodPrice;
	}
}
