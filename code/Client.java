/***********************************************************************
 * Module:  Client.java

 ***********************************************************************/
public class Client {

	public static void main(String[] args) {
		SceneBuilder sb;
		sb = (SceneBuilder)XMLUtil.getBean();		
		SceneController sc = new SceneController();
		Scene scene;
		scene=sc.construct(sb);
		System.out.println("Scene1:");
		System.out.println("��ͼΪ"+scene.getMap());
		System.out.println("����Ϊ"+scene.getWeather());
		System.out.println("��������Ϊ"+scene.getSound());

	}

}
