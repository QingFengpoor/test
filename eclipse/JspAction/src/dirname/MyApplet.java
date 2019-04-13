package dirname;
import java.applet.*;
import java.awt.*;
public class MyApplet extends Applet{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	double f(double x) {
		return(Math.cos(x/5)+Math.sin(x/7)+2)*getSize().height/4;
	}
	public void paint(Graphics g) {
		for(int x=0;x<getSize().width;x++) {
			g.setColor(Color.RED);
			g.drawLine(x, (int)f(x), x+1, (int)f(x+1));
		}
	}
	public String getAppletInfo() {
		return "Draw a sin graph.";
	}
}
