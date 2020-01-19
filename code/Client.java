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
		System.out.println("地图为"+scene.getMap());
		System.out.println("天气为"+scene.getWeather());
		System.out.println("背景音乐为"+scene.getSound());

	}

}
