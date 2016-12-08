package cvs.entity;

public class DumEntity {
	private String dumName,dumImg;
	private int dumPrice;
	

	public DumEntity(String dumName, int dumPrice, String dumImg) {
		this.dumName = dumName;
		this.dumImg = dumImg;
		this.dumPrice = dumPrice;
	}
	
	public String getDumName() {
		return dumName;
	}
	public void setDumName(String dumName) {
		this.dumName = dumName;
	}
	public String getDumImg() {
		return dumImg;
	}
	public void setDumImg(String dumImg) {
		this.dumImg = dumImg;
	}
	public int getDumPrice() {
		return dumPrice;
	}
	public void setDumPrice(int dumPrice) {
		this.dumPrice = dumPrice;
	}
	
	
}
