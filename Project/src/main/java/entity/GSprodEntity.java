package entity;

public class GSprodEntity {
	private String prodName,prodTag,prodImg,CVS,dum;
	private int prodPrice;
	
	public GSprodEntity(){}	
	
	public GSprodEntity(String prodName, int prodPrice, String prodTag, String prodImg,String dum) {
		super();
		this.prodName = prodName;
		this.prodTag = prodTag;
		this.prodImg = prodImg;
		this.prodPrice = prodPrice;
		this.dum=dum;
	}


	public String getDum() {
		return dum;
	}

	public void setDum(String dum) {
		this.dum = dum;
	}

	public String getCVS() {
		return CVS;
	}

	public void setCVS(String cVS) {
		CVS = cVS;
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
